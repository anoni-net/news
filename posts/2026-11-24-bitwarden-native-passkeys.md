---
title: Bitwarden 桌面版與 Windows 11、macOS 的通行金鑰整合
description: 與已經在 Windows 11 或 macOS 上使用 Bitwarden 的人有關。Bitwarden 11 月 18 日公告桌面版可以設成系統的通行金鑰提供者，電腦上建立的通行金鑰可以存進 Bitwarden 保管庫、跟著帳號同步。Windows 11 要用 Microsoft Store 安裝的版本，依 Privacy Guides 的新聞簡訊，Linux 使用者這次無法使用。
date: 2026-11-24T00:00:00+08:00
slug: bitwarden-native-passkeys
categories:
  - security
sources:
  - title: Integrate Bitwarden with Windows and macOS for native passkey creation and use
    url: https://bitwarden.com/blog/integrate-bitwarden-native-passkeys/
    publisher: Bitwarden
    date: 2026-11-18
  - title: Bitwarden Adds Native Passkey Support for Windows and macOS
    url: https://www.privacyguides.org/news/2026/11/19/bitwarden-adds-native-passkey-support-for-windows-and-macos/
    publisher: Privacy Guides
    date: 2026-11-19
  - title: Autofill Passkeys
    url: https://bitwarden.com/help/storing-passkeys/
    publisher: Bitwarden
  - title: Bitwarden launches passkey management
    url: https://bitwarden.com/blog/bitwarden-launches-passkey-management/
    publisher: Bitwarden
  - title: Windows 11 expands passkey manager support
    url: https://techcommunity.microsoft.com/blog/windows-itpro-blog/windows-11-expands-passkey-manager-support/4467572
    publisher: Microsoft
    date: 2025-11-11
  - title: Passkeys
    url: https://learn.microsoft.com/en-us/windows/security/identity-protection/passkeys/
    publisher: Microsoft
  - title: Export Vault Data
    url: https://bitwarden.com/help/export-your-data/
    publisher: Bitwarden
  - title: Download Credential Exchange Specifications
    url: https://fidoalliance.org/specifications/download-credential-exchange-specifications/
    publisher: FIDO Alliance
authors:
  - anoni-net
---

Bitwarden 11 月 18 日公告，桌面版可以設成 Windows 11 與 macOS 的通行金鑰提供者（電腦上負責保存通行金鑰、登入時交出來使用的程式）。通行金鑰（passkey）用裝置的螢幕鎖定取代密碼登入，網站只存公開金鑰，登入用的私鑰存在裝置或密碼管理器裡。桌面版設成提供者之後，網站或桌面應用程式建立通行金鑰時跳出的系統視窗會列出 Bitwarden 作為存放位置。Windows 11 要用從 Microsoft Store 安裝的版本，Privacy Guides 的新聞簡訊則提到 Linux 使用者這次無法使用。

Bitwarden 從 2024 年初開始在瀏覽器擴充套件與手機 App 保管通行金鑰。依 Privacy Guides 11 月 19 日的新聞簡訊，擴充套件適用網站，登入桌面應用程式時可能要改用手機或硬體安全金鑰。在電腦上建立的通行金鑰，也可能被存進 Windows 或 macOS 預設的憑證管理工具，沒有進到 Bitwarden。

透過系統視窗建立的通行金鑰會成為保管庫裡的一筆登入項目，任何一個 Bitwarden App 都能管理。保管庫裡已經有使用者名稱相同的登入項目時，通行金鑰會自動加到這筆項目。項目裡原本就存了通行金鑰時，會先跳出覆寫的警告。

## 導讀觀點 {#perspective}

已經在 Windows 11 或 macOS 上使用 Bitwarden 的人才與這次的整合有關，沒有用 Bitwarden 的人不受影響。設定之後，電腦上建立的通行金鑰可以存進 Bitwarden 並跟著帳號同步到其他裝置，不必留在系統預設的工具裡。從公告描述的同步方式來看，私鑰跟著 Bitwarden 帳號走，帳號的保護與復原因此也牽動這些通行金鑰。之後要再搬到其他密碼管理器時，直接轉移用的協定還在草案階段。

建立與登入時的視窗由 Windows 11 與 macOS 提供，私鑰則存在 Bitwarden 保管庫。依 Microsoft 的說明，Windows 11 搭配第三方提供者時，通行金鑰由該提供者保護與管理。

要搬走或備份時，匯出成檔案只有 `.json` 格式包含通行金鑰，Bitwarden 在匯出頁建議選加密的格式。密碼保護（Password protected）的加密匯出才能匯入其他 Bitwarden 帳號，限定原帳號的只能匯回同一個帳號。Bitwarden 2024.3.1 版以前建立的通行金鑰帶有每次使用都會增加的計數器，匯出頁寫了這類匯出檔不適合當長期備份。

桌面版能不能直接轉移到其他密碼管理器，匯出頁沒有寫，列出的直接轉移只有手機的做法（各家的支援範圍見本站 10 月 19 日的[通行金鑰證明機制導讀](https://anoni.net/news/2026/10/passkey-attestation-debate/)）。直接轉移用的是 FIDO 聯盟的憑證交換協定（CXP），到 11 月 21 日，FIDO 聯盟頁面列出的 CXP 是 2024 年 10 月的工作草案。

想讓建立的通行金鑰存進 Bitwarden 保管庫的人，在 Windows 11 上要用 Microsoft Store 版的桌面版，Bitwarden 2025 年 11 月的測試版則是從 GitHub 安裝。Microsoft 表示這項能力隨 2025 年 11 月的安全性更新提供。之後在桌面版設定的 Passkey provider 一項選 Manage in system settings，再照系統跳出的視窗啟用 Bitwarden，macOS 跳出的是詢問是否使用 Bitwarden 自動填入的視窗。Bitwarden 在說明頁建議同時關閉瀏覽器擴充套件的通行金鑰功能，以免兩邊衝突。

登入 Bitwarden 帳號本身用的通行金鑰不會存進保管庫。既然保管庫不收這把金鑰，用通行金鑰登入 Bitwarden 的人就要另外保存它。Linux 使用者與不想換安裝來源的 Windows 11 使用者，仍可以用瀏覽器擴充套件在網站上保管與使用通行金鑰，登入桌面應用程式則不在範圍內。
