/* 文章頁的朗讀按鈕。規則見 SPEC.md「朗讀按鈕」。
   只用裝置本機的語音（localService 為 true），找不到符合頁面語系的本機語音就不顯示按鈕，
   文章內容不會送到語音服務的伺服器。不讀寫 cookie、localStorage 與 IndexedDB，也不發出網路請求。
   按鈕在 HTML 裡預設是 hidden，沒有 JavaScript 或瀏覽器不支援時，頁面跟沒有這支檔案一樣。 */
(function () {
  "use strict";

  var box = document.querySelector("[data-read-aloud]");
  var synth = window.speechSynthesis;
  if (!box || !synth || typeof window.SpeechSynthesisUtterance !== "function") return;
  var button = box.querySelector("button");
  var label = box.querySelector("[data-label]");
  var pageLang = (document.documentElement.lang || "").toLowerCase();
  var pageEnglish = pageLang.indexOf("en") === 0;
  var pageHans = /hans|-cn\b/.test(pageLang);

  // 語音的語言代碼各家寫法不同：zh-TW、zh_TW、cmn-Hant-TW、yue-HK。數字越小越優先，-1 是不能用。
  // 中文頁先找同一種字的普通話語音，再找另一種字的普通話，粵語排最後
  function rank(tag) {
    tag = String(tag || "").toLowerCase().replace(/_/g, "-");
    var main = tag.split("-")[0];
    if (pageEnglish) return main === "en" ? 0 : -1;
    if (main === "yue" || /-(hk|mo)\b/.test(tag)) return 3;
    if (main !== "zh" && main !== "cmn") return -1;
    var hans = /-(hans|cn|sg)\b/.test(tag);
    var hant = /-(hant|tw)\b/.test(tag);
    if (pageHans) return hans ? 0 : hant ? 1 : 2;
    return hant ? 0 : hans ? 1 : 2;
  }

  var voice = null;
  var state = "idle";

  function pickVoice() {
    var list = synth.getVoices() || [];
    var best = null;
    var bestRank = 99;
    for (var i = 0; i < list.length; i++) {
      var v = list[i];
      // 線上語音（Chrome 的 Google 語音、Edge 的 Natural 語音）會把全文送到廠商的伺服器，一律不用
      if (v.localService !== true) continue;
      var r = rank(v.lang);
      if (r < 0) continue;
      if (r < bestRank || (r === bestRank && v["default"] && !best["default"])) {
        best = v;
        bestRank = r;
      }
    }
    if (state === "idle") {
      voice = best;
      box.hidden = !voice;
    }
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
    synth.cancel();
    for (var i = from; i < items.length; i++) {
      (function (i) {
        var u = new window.SpeechSynthesisUtterance(items[i].text);
        u.voice = voice;
        u.lang = voice.lang;
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
