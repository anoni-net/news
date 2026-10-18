---
title: 通行金鑰的證明機制爭議
description: 10 月 10 日一篇評論主張不要使用通行金鑰，理由是網站可以用證明（attestation）機制限制使用者能用的裝置與軟體，10 月 14 日有作者撰文回應。雙方都同意通行金鑰在多數情況下綁定網域、能防釣魚，爭點在證明會不會成為限制，以及該繼續用通行金鑰還是改用其他方式。
date: 2026-10-19T00:05:00+08:00
slug: passkey-attestation-debate
categories:
  - security
sources:
  - title: Passkeys are a trap. Do not use them.
    url: https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them
    publisher: Non-Functional
    date: 2026-10-10
  - title: Passkeys Are Not a Trap
    url: https://scotthelme.co.uk/passkeys-are-not-a-trap/
    publisher: scotthelme.co.uk
    date: 2026-10-14
  - title: "Web Authentication: An API for accessing Public Key Credentials - Level 3"
    url: https://www.w3.org/TR/webauthn-3/
    publisher: W3C
    date: 2026-08-25
  - title: NIST Special Publication 800-63B
    url: https://pages.nist.gov/800-63-4/sp800-63b.html
    publisher: NIST
  - title: Syncable Authenticators
    url: https://pages.nist.gov/800-63-4/sp800-63b/syncable/
    publisher: NIST
  - title: Passkeys
    url: https://fidoalliance.org/passkeys/
    publisher: FIDO Alliance
  - title: Download Credential Exchange Specifications
    url: https://fidoalliance.org/download-credential-exchange-specifications/
    publisher: FIDO Alliance
  - title: 關於通行密鑰的安全性
    url: https://support.apple.com/zh-tw/102195
    publisher: Apple
    date: 2024-09-27
  - title: 以密碼金鑰登入，不必再用密碼
    url: https://support.google.com/accounts/answer/13548313?hl=zh-Hant
    publisher: Google
  - title: Sync passkeys securely across your devices
    url: https://blog.google/technology/safety-security/google-password-manager-passkeys-update-september-2024/
    publisher: Google
    date: 2024-09-19
  - title: What are passkeys and why they matter
    url: https://support.microsoft.com/en-us/accounts-billing/security/what-are-passkeys-why-they-matter
    publisher: Microsoft
  - title: Export Vault Data
    url: https://bitwarden.com/help/export-your-data/
    publisher: Bitwarden
  - title: How to export your data from the 1Password apps
    url: https://support.1password.com/export/
    publisher: 1Password
  - title: "KeePassXC: User Guide"
    url: https://keepassxc.org/docs/KeePassXC_UserGuide
    publisher: KeePassXC
watch:
  - date: 2026-12-15
    note: FIDO 聯盟的憑證交換協定（CXP）是否發布工作草案以後的版本，主要的消費者網站是否開始要求通行金鑰的證明
authors:
  - anoni-net
---

通行金鑰（passkey）用手機或電腦的螢幕鎖定取代密碼登入，每組金鑰只能用在建立它的網域。10 月 10 日刊在 Substack 的一篇評論以「Passkeys are a trap. Do not use them.」為題，主張網站可以透過證明（attestation，存放金鑰的裝置或軟體向網站出示自身來歷的機制）逐步限制使用者能用的裝置與軟體。10 月 14 日有作者以「Passkeys Are Not a Trap」撰文回應，主張多數人用的同步通行金鑰（存在密碼管理器、會在裝置之間同步）不提供證明。兩篇都同意密碼不安全、通行金鑰在多數情況下綁定網域，爭點集中在證明，以及該繼續用通行金鑰還是改用其他方式。

評論的作者先指出，能否複製、存在硬體或軟體裡各不相同的東西都叫通行金鑰，並推測這個命名是刻意讓使用者不去細看。作者的核心論點是網站可以藉證明確認使用者用的是核准的密碼管理器，等到大多數使用者都不受影響，就能開始拒絕沒有證明的通行金鑰。作者寫到證明需要加密處理器、密碼管理器、作業系統與韌體都通過檢查（例如為了延續舊手機而改裝 LineageOS 的人可能無法通過）。作者也寫到證明有正當用途、多數網站目前不要求，正文建議改用驗證 App 產生的一次性密碼（TOTP），文末的補充段落另外推薦 YubiKey 這類硬體安全金鑰。

回應文章的作者寫到，網站就算要求證明，iCloud 鑰匙圈、Google 密碼管理工具、1Password 或 Bitwarden 裡的同步通行金鑰也只會回傳「none」（表示沒有證明）。依這位作者的推論，消費者網站如果只收有證明的通行金鑰，會立刻擋掉幾乎所有使用者。回應文章也提到，證明只告訴網站驗證器（存放金鑰的手機、密碼管理器或安全金鑰）的廠牌與型號，不包含作業系統、瀏覽器、擴充功能、韌體版本或手機是否越獄。對 YubiKey 的建議，作者的回應是每支 YubiKey 出廠都帶有 Yubico 簽發的證明憑證，擔心證明的人反而會被推向證明。

## 導讀觀點 {#perspective}

W3C 2026 年 8 月發布的 WebAuthn Level 3 規格把證明的預設值定為 none，證明的格式由驗證器決定。網站可以表達偏好，也可以依自己的政策決定接受哪些證明。規格以 AAGUID（標示驗證器型號的 128 位元識別碼）標示類型，也提醒證明憑證可能被用來追蹤使用者（緩解方式包括大量裝置共用同一張憑證、交給匿名化的憑證機構）。規格裡已列為棄用的 Android SafetyNet 格式，證明內容包含平台健康狀態的資訊（回應文章說證明不含作業系統狀態，依本文的整理要看格式而定）。

依同一份規格，可能包含能識別個別裝置資訊的企業證明（enterprise），要瀏覽器或驗證器的設定允許該網站時才會提供。美國國家標準與技術研究院（NIST）給聯邦機關的身分驗證指引（SP 800-63-4）提到，面向大眾的服務不應因為取得不到證明而擋下同步通行金鑰，否則使用者可能被推向容易被釣魚的方式。同一份指引也建議有證明時服務端應該用它判斷信任程度，聯邦機關的內部系統應實作證明。服務端也可以依「可備份」旗標（標示金鑰能否同步或備份的欄位）限制同步通行金鑰。

回應文章從 2026 年 10 月的現況出發，消費者網站多半不要求證明，主要的同步服務也不提供。回應文章也寫到，如果消費者網站真的開始要求證明，值得大聲反對。評論擔心的則是之後的走向，作者的推論是受影響的只有改裝系統的少數人，網站因此能在不引起注意的情況下逐步收緊。

回應文章的作者寫到 TOTP 可能被輸入到假網站，Evilginx 這類釣魚工具（架在使用者與真網站之間的轉送伺服器）能即時轉送密碼與驗證碼。NIST 的指引把需要手動輸入的一次性密碼排除在防釣魚驗證器之外，設定正確的同步通行金鑰則列為能防釣魚。評論的正文建議 TOTP，理由是使用者可以自由選擇軟體與硬體。文末的補充段落提到通行金鑰在多數情況下綁定網域、能抵擋中間人攻擊，並推薦安全金鑰。

兩篇都只帶過換裝置與搬移，評論提到換手機時要能帶走金鑰，回應文章則建議想搬移的人挑支援搬移的提供者。依 FIDO 聯盟的說明，同步通行金鑰經端對端加密在裝置之間同步。依兩家的說明頁，Apple 用 iCloud 鑰匙圈的託管紀錄復原，Google 要用密碼管理工具的 PIN 或舊 Android 裝置的螢幕鎖定。兩家的正體中文說明頁用詞不同，Apple 寫「通行密鑰」，Google 寫「密碼金鑰」。

到 10 月 18 日為止，Bitwarden 與 1Password 能透過 FIDO 的憑證交換協定直接匯出通行金鑰，這套協定仍是草案。兩家都需要 iOS 26 或 Android 14 以上（Bitwarden 的匯出頁寫 Android 10 以上），對方的 App 也要支援。KeePassXC 則把通行金鑰匯出成沒有加密的檔案。

依回應文章，到 10 月 18 日為止消費者網站多半不要求證明，已經在用同步通行金鑰的人登入不受影響。依 NIST 的指引，設定正確的通行金鑰登入時，假網站無法取得可重複使用的登入資訊。帳號原有的密碼與驗證碼仍可能被釣走，Google 的說明頁也提到新增通行金鑰不會移除既有的驗證方式。擔心被綁在某個平台的人，可以挑能直接匯出通行金鑰的密碼管理器。

在意證明的人可以比較兩種做法。依回應文章，同步通行金鑰不提供證明，YubiKey 則出廠帶有 Yubico 簽發的證明憑證。

NIST 建議服務端讓使用者綁定多個驗證方式供復原，依本文的推論，對使用者來說就是保留兩種以上的登入或復原方式。Microsoft 的說明也提醒，只存在單一裝置的通行金鑰，裝置遺失又沒有其他復原方式時就會失去它。
