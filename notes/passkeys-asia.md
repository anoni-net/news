# 通行金鑰在亞洲的採用與規定

範圍是亞洲各地政府與金融監理機關對通行金鑰（passkey）或防釣魚驗證的要求，以及通行金鑰在中國大陸依賴的雲端服務。第一次整理是寫 anoni-net/news 的通行金鑰證明機制那篇的時候，查證日期 2026-10-18。

## 日本

- 事實：金融廳修正對證券業者的監督指針，2025 年 10 月 15 日起適用，把登入、出金、變更出金帳戶等重要操作的防釣魚多要素認證列為觀察重點，例示是通行金鑰與 PKI 的認證，並要求預設啟用。條文列的是例示，沒有限定只能用通行金鑰
    - 照錄：「ログイン、出金、出金先銀行口座の変更など、重要な操作時におけるフィッシングに耐性のある多要素認証（例：パスキーによる認証、ＰＫＩ（公開鍵基盤）をベースとした認証）の実装及び必須化（デフォルトとして設定）」
    - 來源：「金融商品取引業者等向けの総合的な監督指針」等の一部改正（案）に対するパブリックコメントの結果等の公表について，金融廳，<https://www.fsa.go.jp/news/r7/shouken/20251015/20251015.html>，2025-10-15
- 事實：金融廳與日本證券業協會的意見交換資料寫到，證券業的防釣魚多要素認證原則上要在 2026 年 6 月底前完成
    - 照錄：「フィッシングに耐性のある多要素認証の必須化については、原則として 2026 年６月末までの実施をお願いしているところ」
    - 來源：金融廳，<https://www.fsa.go.jp/common/ronten/202511/06.pdf>，2025-11-18
- 事實：主要銀行等的監督指針 2026 年 2 月 27 日起適用相同的條文。銀行業的完成期限這次沒有找到一手資料
    - 來源：「主要行等向けの総合的な監督指針」等の一部改正（案）に対するパブリックコメントの結果等の公表について，金融廳，<https://www.fsa.go.jp/news/r7/sonota/20260227/20260227.html>，2026-02-27

## 新加坡

- 事實：新加坡金融管理局與銀行公會 2024 年 7 月 9 日宣布，主要零售銀行在三個月內逐步取消使用數位權杖客戶的一次性密碼登入。新聞稿沒有提到通行金鑰或 FIDO
    - 照錄：「major retail banks in Singapore will progressively phase out the use of One-Time Passwords (OTPs) for bank account login by customers who are digital token users within the next three months.」
    - 來源：Banks in Singapore to Strengthen Resilience Against Phishing Scams，MAS，<https://www.mas.gov.sg/news/media-releases/2024/banks-in-singapore-to-strengthen-resilience-against-phishing-scams>，2024-07-09
- 事實：政府數位身分 Singpass 從 2026 年 7 月 1 日起開放通行金鑰登入的測試版，先開放 iPhone，Android 之後跟進，原有的登入方式繼續保留
    - 照錄：「The initial beta phase is available to iPhone (iOS) users, with passkeys to be extended to Android users in subsequent phases.」
    - 來源：Singpass Launches Passkeys: A Safer Login Method，GovTech，<https://www.tech.gov.sg/media/singpass-launches-passkeys-a-safer-login-method/>，2026-06-30
- 事實：網路安全局的無密碼驗證說明把通行金鑰列為防釣魚，簡訊一次性密碼不是
    - 來源：Understanding Passwordless Authentication，CSA，<https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-011/>，2026-08-26（2026-09-18 更新）

## 台灣

- 事實：數位發展部 2023 年 1 月以政府會員身分加入 FIDO 聯盟，是內政部之後第二個加入的政府單位
    - 照錄：「數位發展部（下稱數位部）於今（2023）年 1 月加入國際身分識別標準組織 FIDO Alliance」
    - 來源：數位發展部加入國際標準組織 FIDO 聯盟 加速身分識別標準、接軌國際、擴大產業應用，數位發展部，<https://moda.gov.tw/ADI/news/latest-news/3687>，2023
- 事實：金管會自 2021 年推動「金融行動身分識別標準化機制」，2024 年 8 月 16 日起簡稱改為「金融 Fast-ID」。金管會的文件沒有要求使用通行金鑰
    - 來源：「金融行動身分識別標準化機制」簡稱自即日起更改為「金融Fast-ID」，金管會，<https://www.fsc.gov.tw/ch/home.jsp?id=96&parentpath=0&mcustomize=news_view.jsp&dataserno=202408160001&dtable=News>，2024-08-16
- 查不到：台灣金融監理機關要求使用通行金鑰的明文

## 中國大陸

- 事實：iCloud 在中國大陸由雲上貴州營運，資料存放在中國境內。Apple 的頁面沒有說明 iCloud 鑰匙圈與通行金鑰在雲上貴州營運的 iCloud 能不能使用
    - 照錄：「iCloud 在中国大陆由云上贵州（云上艾珀（贵州）技术有限公司）运营。」
    - 照錄：「当你使用由云上贵州运营的 iCloud 时，你的个人信息（包括你的照片、文件和其他 iCloud 数据）都会储存在中国境内。」
    - 來源：进一步了解 iCloud（中国大陆），Apple，<https://support.apple.com/zh-cn/111754>，2025-04-22。适用于中国客户的 Apple 和云上贵州数据隐私声明，Apple，<https://support.apple.com/zh-cn/121767>
- 事實：GreatFire 對 `https://accounts.google.com` 最近 6 次有結論的測試，到 2026 年 10 月 4 日為止都顯示在中國大陸受到干擾，GreatFire 對這個網址的評級是時有時無（Sometimes），從 2012 年 2 月 22 日起有干擾紀錄
    - 來源：GreatFire，<https://en.greatfire.org/https/accounts.google.com>
