# iOS 瀏覽器引擎規定在亞洲各地的適用範圍

範圍是 Apple 要求 iOS 上瀏覽網頁的 App 使用 WebKit 的規定，以及開放其他瀏覽器引擎的例外在亞洲哪些地方適用，包含日本、中國大陸、台灣、香港。歐盟的條件只在跟日本對照時寫到。各地 App Store 上架哪些瀏覽器寫在 `browser-access-mainland-china.md`，這份不重複。第一次整理是寫 anoni-net/news 的 iOS 瀏覽器引擎那篇導讀的時候，查證日期 2026-11-22。

## 全球規定

- 事實：App Store 審核指南 2.5.6 要求瀏覽網頁的 App 使用 WebKit，開發者可以申請使用其他引擎的授權，指南只列出歐盟與日本兩地的授權說明。條文用全球通用的寫法，沒有逐地區分
    - 照錄：「Apps that browse the web must use the appropriate WebKit framework and WebKit JavaScript. You may apply for an entitlement to use an alternative web browser engine in your app. Learn more about these entitlements for the EU and Japan.」
    - 來源（一手）：App Review Guidelines，Apple，<https://developer.apple.com/app-store/review/guidelines/>，頁尾寫 Last Updated: October 16, 2026
    - 查證日期：2026-11-22

## 日本

- 事實：日本《スマートフォンにおいて利用される特定ソフトウェアに係る競争の促進に関する法律》（英文 Act on Promotion of Competition for Specified Smartphone Software，簡稱 Mobile Software Competition Act，MSCA）禁止 JFTC 指定的業者以只允許自家引擎這類條件，妨礙其他開發者使用別的瀏覽器引擎。有安全、隱私等正當理由時可以例外
    - 照錄：「Designated providers must not prevent other application developers from using other browser engines, for example, by imposing conditions that only allow the use of designated providers' proprietary browser engines (Art. 8, (iii)).」
    - 照錄：「Exemptions may be made with justifiable reasons.」
    - 照錄（正當理由的範圍，寫在 Art. 7 那一列）：「Measures necessary to achieve the objectives of security, privacy, youth protection, and other objectives (“justifiable reasons”) can be taken if it is too difficult to achieve those objectives through less competition-restrictive alternatives.」
    - 來源（一手）：Outline of the Act on Promotion of Competition for Specified Smartphone Software (Mobile Software Competition Act (MSCA))，日本公平交易委員會（JFTC），2024 年 6 月，<https://www.japaneselawtranslation.go.jp/en/outlines/view/154>。照錄的句子出自一份首頁標 Attachment 2、June 2024 的 PDF，這份 PDF 與上面的網址是否同一份沒有核對。只讀了概要，法條全文沒有取得
    - 查證日期：2026-11-22
- 事實：Apple 在 iOS 26.2 以上開放日本的使用者使用 WebKit 以外的引擎，限兩種 App：完整的瀏覽器 App，以及由引擎管理者（browser engine steward）提供、內嵌引擎做 App 內瀏覽的 App
    - 照錄：「In iOS 26.2 and later, browser engines other than WebKit can be used in two types of apps for users in Japan: Dedicated browser apps that provide a full web browser experience, and apps from browser engine stewards that provide in-app browsing experiences using an embedded browser engine.」
    - 照錄：「A browser engine steward is an entity with the primary responsibility for operating a distinct web browser engine.」
    - 來源（一手）：Using alternative browser engines in Japan，Apple，<https://developer.apple.com/support/alternative-browser-engines-jp/>，頁面沒有發布日期。Apple 的新聞稿 Apple announces changes to iOS in Japan，<https://www.apple.com/newsroom/2025/12/apple-announces-changes-to-ios-in-japan/>，2025-12-17
    - 查證日期：2026-11-22
- 事實：日本頁的條件與歐盟頁逐項相同，包含已遭利用的漏洞及時修補（例子是最簡單的類別 30 天）與預設封鎖第三方 cookie。差異有三處。日本頁只寫 iOS，歐盟頁寫 iOS 與 iPadOS。日本頁的發行限制多一句 Apple 明示許可的例外。內嵌引擎在日本限引擎管理者，歐盟頁沒有這項限制
    - 照錄（日本頁）：「Be distributed solely on iOS in Japan (except for any other jurisdiction or Apple platform expressly permitted by Apple under the Developer Agreement - including any addenda - for which you have likewise obtained a corresponding entitlement profile);」
    - 照錄（歐盟頁）：「Be distributed solely on iOS and/or iPadOS in the European Union;」
    - 來源（一手）：同上，以及 Using alternative browser engines in the European Union，Apple，<https://developer.apple.com/support/alternative-browser-engines/>，頁面沒有發布日期。兩頁在 2026-11-22 逐段對讀
    - 查證日期：2026-11-22
- 事實（當事方的說法）：Mozilla 2026-11-20 的文章寫到，Apple 在日本公布條件將近一年，沒有任何開發者推出非 WebKit 的 iOS 瀏覽器。這是 Mozilla 的陳述，沒有附統計
    - 照錄：「Nearly three years since Apple introduced these conditions in the EU and almost a year since Japan, not one developer has been able to launch a non-WebKit browser on iOS.」
    - 來源：Why there are still no non-WebKit browsers on iOS，Mozilla，<https://blog.mozilla.org/en/mozilla/internet-policy/apple-ios-browser-engine-rules/>，2026-11-20
    - 查證日期：2026-11-22
- 查不到：JFTC 2025 年 7 月公布的指引原文、JFTC 的官方英文頁（回應 Access Denied），以及日本是否有開發者申請或取得授權。全面施行日 2025 年 12 月 18 日只有二手來源

## 中國大陸、台灣、香港

- 事實：Apple 的兩份引擎條件頁只寫歐盟與日本，審核指南 2.5.6 的例外也只列這兩地，Apple 沒有為中國大陸、台灣、香港另訂瀏覽器引擎規定。依據只有 2.5.6 的全球性文字，逐地的官方說明查不到。Apple 開發者網站的 `/tw/`、`/cn/` 頁面是日本頁的翻譯，不是另外的規定
    - 來源（一手）：見「全球規定」與「日本」兩節的 Apple 頁面
    - 查證日期：2026-11-22
- 查不到：三地要求 Apple 開放其他瀏覽器引擎的當地法規，到 2026-11-22 沒有找到
