/* 文章頁的朗讀按鈕。規則見 SPEC.md「朗讀按鈕」。
   只用裝置本機的語音（localService 為 true），找不到符合頁面語系的本機語音就不顯示按鈕，
   文章內容不會送到語音服務的伺服器。不發出網路請求。
   瀏覽器儲存只用 localStorage 的一個鍵（STORE_KEY），存讀者選的語音與速度，不讀寫其他鍵，也不碰 cookie 與 IndexedDB。
   按鈕在 HTML 裡預設是 hidden，沒有 JavaScript 或瀏覽器不支援時，頁面跟沒有這支檔案一樣。 */
(function () {
  "use strict";

  var box = document.querySelector("[data-read-aloud]");
  var synth = window.speechSynthesis;
  if (!box || !synth || typeof window.SpeechSynthesisUtterance !== "function") return;
  var button = box.querySelector("button");
  var label = box.querySelector("[data-label]");
  var voiceField = box.querySelector("[data-voice-field]");
  var voiceSelect = box.querySelector("[data-voice]");
  var rateSelect = box.querySelector("[data-rate]");
  var pageLang = (document.documentElement.lang || "").toLowerCase();
  var pageEnglish = pageLang.indexOf("en") === 0;
  var pageHans = /hans|-cn\b/.test(pageLang);

  // 讀者選的語音與速度，換頁之後沿用。只存在讀者自己的瀏覽器，不會送出
  var STORE_KEY = "anoni-news-listen";
  function load() {
    try {
      var saved = JSON.parse(window.localStorage.getItem(STORE_KEY));
      return saved && typeof saved === "object" ? saved : {};
    } catch (err) {
      // 無痕模式或關掉儲存時讀不到，照預設值
      return {};
    }
  }
  function save() {
    try {
      window.localStorage.setItem(STORE_KEY, JSON.stringify({ voice: voice ? voiceId(voice) : null, rate: rateSelect.value }));
    } catch (err) {
      // 存不進去就只在這一頁有效
    }
  }
  var saved = load();

  // 速度的選項寫在 HTML 裡，存下來的值不在選項裡就維持預設
  for (var r = 0; r < rateSelect.options.length; r++) {
    if (rateSelect.options[r].value === String(saved.rate)) rateSelect.value = saved.rate;
  }

  // 語音的語言代碼各家寫法不同：zh-TW、zh_TW、cmn-Hant-TW、yue-HK。回傳選單上的分組與排序，
  // rank 越小越優先，null 是不能用。中文頁先列同一種字的普通話語音，再列另一種字的普通話，粵語排最後
  function classify(lang) {
    var tag = String(lang || "").toLowerCase().replace(/_/g, "-");
    var main = tag.split("-")[0];
    if (pageEnglish) return main === "en" ? { rank: 0, group: tag } : null;
    if (main === "yue" || /-(hk|mo)\b/.test(tag)) return { rank: 3, group: "yue" };
    if (main !== "zh" && main !== "cmn") return null;
    var hans = /-(hans|cn|sg)\b/.test(tag);
    var hant = /-(hant|tw)\b/.test(tag);
    var group = hant ? "tw" : hans ? "cn" : "zh";
    var order = pageHans ? { cn: 0, tw: 1, zh: 2 } : { tw: 0, cn: 1, zh: 2 };
    return { rank: order[group], group: group };
  }

  // 語音的名稱多半是人名，看不出是哪一種語言，選單依語言分組。中文的組名寫在 HTML 的 data-group-*，
  // 英文用瀏覽器內建的語言名稱，例如 American English、British English
  var englishNames = null;
  try {
    englishNames = new Intl.DisplayNames(["en"], { type: "language" });
  } catch (err) {
    // 舊瀏覽器沒有 Intl.DisplayNames，組名改用語言代碼
  }
  function groupLabel(group) {
    if (!pageEnglish) return voiceSelect.getAttribute("data-group-" + group) || group;
    try {
      return (englishNames && englishNames.of(group)) || group;
    } catch (err) {
      return group;
    }
  }

  function voiceId(v) {
    return v.voiceURI || v.name;
  }

  // Apple 的同一個語音會依音質分成好幾個版本，名稱相同，只有 voiceURI 不同，
  // 例如 iOS 的 com.apple.voice.compact.zh-TW.Meijia 與 com.apple.voice.super-compact.zh-TW.Meijia。
  // 同名的只留音質最好的那一個
  function quality(v) {
    var uri = String(v.voiceURI || "").toLowerCase();
    if (uri.indexOf(".premium.") >= 0) return 3;
    if (uri.indexOf(".enhanced.") >= 0) return 2;
    if (uri.indexOf(".super-compact.") >= 0) return 0;
    return 1;
  }

  var voices = [];
  var listed = "";
  var voice = null;
  var state = "idle";

  // 可選的語音：本機、語言符合頁面，依 rank 排序。同一級裡系統預設的排前面，
  // Apple 的 Eloquence 語音（Eddy、Flo 這一組）是舊式的合成音，排在同一組的最後
  function pickVoice() {
    var list = synth.getVoices() || [];
    var found = [];
    var byName = {};
    for (var i = 0; i < list.length; i++) {
      var v = list[i];
      // 線上語音（Chrome 的 Google 語音、Edge 的 Natural 語音）會把全文送到廠商的伺服器，一律不用
      if (v.localService !== true) continue;
      var c = classify(v.lang);
      if (!c) continue;
      // 同一個語音重複回報、或同名的不同音質版本，依名稱與語言合併成一項。
      // ids 記下合併掉的 voiceURI，讀者存過其中任何一個，都對應到留下來的這一項
      var key = v.name + "\n" + v.lang;
      var same = byName[key];
      if (same) {
        same.ids.push(voiceId(v));
        if (quality(v) > quality(same.v)) same.v = v;
        continue;
      }
      byName[key] = { v: v, c: c, i: i, ids: [voiceId(v)], old: /eloquence/i.test(v.voiceURI || "") ? 1 : 0 };
      found.push(byName[key]);
    }
    // 英文的各組 rank 相同，系統預設語音所在的那一組排第一，其餘依組名。
    // iOS 把每個語音都標成預設，預設分散在好幾組時不採用
    var home = null;
    var homes = {};
    for (var d = 0; d < found.length; d++) {
      if (found[d].v["default"]) homes[found[d].c.group] = true;
    }
    var homeList = Object.keys(homes);
    if (homeList.length === 1) home = homeList[0];
    found.sort(function (a, b) {
      return a.c.rank - b.c.rank || (b.c.group === home ? 1 : 0) - (a.c.group === home ? 1 : 0) ||
        (a.c.group < b.c.group ? -1 : a.c.group > b.c.group ? 1 : 0) ||
        a.old - b.old || (b.v["default"] ? 1 : 0) - (a.v["default"] ? 1 : 0) || a.i - b.i;
    });
    var signature = found.map(function (f) { return voiceId(f.v) + "\n" + f.v.lang; }).join("\n");
    // 清單沒變就不重填選單，讀者正打開選單時不會被關掉
    if (signature === listed) return;
    listed = signature;
    voices = found.map(function (f) { return f.v; });

    var keep = voice ? voiceId(voice) : saved.voice;
    voice = null;
    for (var j = 0; j < found.length; j++) {
      if (!voice && found[j].ids.indexOf(keep) >= 0) voice = found[j].v;
    }
    if (!voice) voice = voices[0] || null;

    voiceSelect.textContent = "";
    var optgroup = null;
    for (var k = 0; k < found.length; k++) {
      if (!optgroup || optgroup.getAttribute("data-group") !== found[k].c.group) {
        optgroup = document.createElement("optgroup");
        optgroup.setAttribute("data-group", found[k].c.group);
        optgroup.label = groupLabel(found[k].c.group);
        voiceSelect.appendChild(optgroup);
      }
      var option = document.createElement("option");
      option.value = String(k);
      option.textContent = voices[k].name;
      option.selected = voices[k] === voice;
      optgroup.appendChild(option);
    }
    // 只有一個可選時不顯示語音選單
    voiceField.hidden = voices.length < 2;
    if (state === "idle") box.hidden = !voice;
  }

  // 要朗讀的段落：標題、副標，接著是內文的每一個區塊。程式碼區塊逐字念出來沒有意義，跳過
  var BLOCKS = "h2, h3, h4, p, li, blockquote, figcaption, tr";
  function collect() {
    var items = [];
    function add(el, text) {
      text = (text || "").replace(/\s+/g, " ").trim();
      if (text) items.push({ el: el, text: text });
    }
    var title = document.querySelector(".story__title");
    var dek = document.querySelector(".story__dek");
    if (title) add(title, title.textContent);
    if (dek) add(dek, dek.textContent);
    var body = document.querySelector(".story__body");
    if (!body) return items;
    var nodes = body.querySelectorAll(BLOCKS);
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      if (el.closest("pre")) continue;
      // 清單項目裡的段落、引文裡的段落，由外層一起念，不重複
      var outer = el.parentElement && el.parentElement.closest("li, blockquote, figcaption, tr");
      if (outer && body.contains(outer)) continue;
      if (el.tagName === "TR") {
        var cells = [];
        for (var j = 0; j < el.cells.length; j++) cells.push(el.cells[j].textContent.trim());
        add(el, cells.join(pageEnglish ? ", " : "，"));
      } else {
        add(el, el.textContent);
      }
    }
    return items;
  }

  var items = null;
  var index = 0;
  // 每次開始或暫停都換一個編號，被 cancel() 打斷的舊語句回呼時編號對不上，直接略過
  var run = 0;
  var current = null;

  function mark(el) {
    if (current) current.classList.remove("is-reading");
    current = el;
    if (current) current.classList.add("is-reading");
  }

  function setState(next) {
    state = next;
    button.setAttribute("data-state", next);
    label.textContent = button.getAttribute("data-label-" + next);
  }

  function reset() {
    run += 1;
    index = 0;
    mark(null);
    setState("idle");
  }

  // 所有段落在點擊當下一次排進佇列。iOS 只允許使用者操作觸發的朗讀，等上一段念完再排下一段會被擋
  function start(from) {
    run += 1;
    var mine = run;
    var rate = parseFloat(rateSelect.value) || 1;
    synth.cancel();
    for (var i = from; i < items.length; i++) {
      (function (i) {
        var u = new window.SpeechSynthesisUtterance(items[i].text);
        u.voice = voice;
        u.lang = voice.lang;
        u.rate = rate;
        u.onstart = function () {
          if (mine !== run) return;
          index = i;
          mark(items[i].el);
        };
        u.onend = function () {
          if (mine === run && i === items.length - 1) reset();
        };
        u.onerror = function () {
          if (mine === run) reset();
        };
        synth.speak(u);
      })(i);
    }
    setState("playing");
  }

  // 暫停用 cancel() 再從同一段重新開始。各家的 pause() 行為不一致，Android 上等於停止
  function pause() {
    run += 1;
    synth.cancel();
    setState("paused");
  }

  button.addEventListener("click", function () {
    // 流量統計只記第一次點擊，暫停與繼續不重複計算
    button.removeAttribute("data-anoni-event");
    if (!voice) return;
    if (state === "playing") {
      pause();
      return;
    }
    if (!items) items = collect();
    if (!items.length) return;
    start(state === "paused" ? index : 0);
  });

  // 念到一半換語音或速度，從正在念的那一段用新的設定重念
  function changed() {
    save();
    if (state === "playing") start(index);
  }
  voiceSelect.addEventListener("change", function () {
    voice = voices[+voiceSelect.value] || voice;
    changed();
  });
  rateSelect.addEventListener("change", changed);

  // 離開頁面時停止，避免換頁之後還在念上一篇
  window.addEventListener("pagehide", function () {
    if (state !== "idle") {
      synth.cancel();
      reset();
    }
  });

  pickVoice();
  if (typeof synth.addEventListener === "function") {
    synth.addEventListener("voiceschanged", pickVoice);
  } else {
    synth.onvoiceschanged = pickVoice;
  }
  // 語音清單多半要等一下才載入完，Safari 不一定送出 voiceschanged
  window.setTimeout(pickVoice, 500);
  window.setTimeout(pickVoice, 2000);
})();
