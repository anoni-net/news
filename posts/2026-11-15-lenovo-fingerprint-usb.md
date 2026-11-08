---
title: Lenovo 指紋隨身碟的未加密 SD 卡與加密宣稱的判斷方式
description: 依研究者的投影片，Lenovo ThinkPlus FU100 指紋隨身碟標榜硬體加密與 AES-256，裡面卻是沒有加密的 SD 卡。Lenovo 的聲明寫這批產品只由 Lenovo 在中國大陸販售，受影響的客戶可以安排更換。聲明沒有回答 AES-256 宣稱是否屬實（11 月 8 日查證）。其他品牌標榜加密的隨身碟，可以從金鑰是否依賴密碼來判斷。
date: 2026-11-15T00:00:00+08:00
slug: lenovo-fingerprint-usb
categories:
  - encryption
watch:
  - date: 2026-12-15
    note: Lenovo 是否回應 AES-256 與硬體加密的宣稱，公告 LEN-210545 的原頁是否可以讀取，受影響型號與更換方式是否調整
sources:
  - title: Breaking Encrypted USB Drives with Time-Travel Debugging
    url: https://github.com/xusheng6/breaking_encrypted_USB_drives_with_TTD/blob/main/Breaking_Encrypted_USB_Drives_v2.pdf
    publisher: RE//verse 2026
  - title: NVD-CVE-2025-13453
    url: https://nvd.nist.gov/vuln/detail/CVE-2025-13453
    publisher: NVD
    date: 2026-01-14
  - title: "Lenovo's 'encrypted' fingerprint USB drive is just an unencrypted SD card in a fancy case — AI-assisted follow-up finds a backdoor and hardcoded keys in other ‘secure’ USB products (updated)"
    url: https://www.tomshardware.com/tech-industry/cyber-security/lenovo-fingerprint-usb-stick-sold-as-aes-256-encrypted-had-a-plain-sd-card-inside-ai-assisted-follow-up-finds-a-backdoor-and-hardcoded-keys-in-other-secure-usb-products
    publisher: Tom's Hardware
    date: 2026-11-01
  - title: Lenovo ThinkPlus Fingerprint USB Drive Sold as Encrypted Was a Plain SD Card Inside
    url: https://hackingpassion.com/lenovo-thinkplus-encrypted-usb-sd-card/
    publisher: HackingPassion
    date: 2026-10-29
  - title: FIPS 140-2 Cerified Flash Drives Have Security Flaw
    url: https://spectrum.ieee.org/fips-1402-cerified-flash-drives-have-security-flaw
    publisher: IEEE Spectrum
    date: 2010-01-12
  - title: Cryptographic Module Validation Program
    url: https://csrc.nist.gov/projects/cryptographic-module-validation-program
    publisher: NIST
  - title: Header Key Derivation, Salt, and Iteration Count
    url: https://veracrypt.io/en/Header%20Key%20Derivation.html
    publisher: VeraCrypt
  - title: VeraCrypt Downloads
    url: https://veracrypt.io/en/Downloads.html
    publisher: VeraCrypt
  - title: BitLocker overview
    url: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/
    publisher: Microsoft
  - title: BitLocker FAQ
    url: https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/faq
    publisher: Microsoft
  - title: Volume encryption with FileVault in macOS
    url: https://support.apple.com/guide/security/volume-encryption-with-filevault-sec4c6dc1b6e/web
    publisher: Apple
  - title: Encrypt and protect a storage device with a password in Disk Utility on Mac
    url: https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac
    publisher: Apple
  - title: Frequently Asked Questions Cryptsetup/LUKS
    url: https://gitlab.com/cryptsetup/cryptsetup/-/raw/main/FAQ.md
    publisher: cryptsetup
authors:
  - anoni-net
---

隨身碟標榜「加密」或「指紋解鎖」，不代表裡面的檔案經過加密。一位研究者 2026 年 3 月在逆向工程研討會 RE//verse 的投影片拆解了 Lenovo ThinkPlus FU100 指紋隨身碟，結論是外殼裡只有一張 SD 卡，資料沒有任何加密。依 Lenovo 經 Tom's Hardware 轉載的聲明，這批 ThinkPlus 儲存產品為中國市場設計，也只由 Lenovo 在中國大陸販售。投影片另外列出其他受影響的裝置，下面的判斷方式也可用在其他品牌標榜加密的產品。

拆解與結論都出自投影片，以下依投影片的文字與 Tom's Hardware、資安部落格 HackingPassion 的轉述。投影片寫著「It's just an SD card in a fancy case」（只是裝在漂亮外殼裡的 SD 卡），指紋辨識只控制 USB 連線。依 HackingPassion 的描述，指紋決定的是隨身碟要不要連上電腦，卡上的檔案不受它影響。

「硬體加密」與 AES-256（廣泛使用的加密演算法）兩項宣稱列在投影片的 FU100 介紹頁，圖片來源標示為 Alibaba.com。到 11 月 8 日，本文查不到 Lenovo 官網的 FU100 產品頁，無法確認 Lenovo 自己的通路是否用過同樣的文字。

依投影片與 HackingPassion，研究者 2025 年 8 月 2 日通報 Lenovo。2025 年 8 月 27 日的暫時修補是在 SD 卡上覆蓋一層環氧樹脂（epoxy），完整修補排在 2025 年 12 月。Lenovo 的聲明提到接獲通報後與研究者協調揭露，透過硬體與軟體升級修正，並在 2026 年 1 月發布安全公告與三個 CVE（公開的漏洞編號）。

Lenovo 公告 LEN-210545 的原頁在 11 月 8 日查閱時回應 Access Denied，公告內容只能依二手來源與美國國家漏洞資料庫（NVD）的紀錄。NVD 上由 Lenovo 提交的紀錄寫到，有實體接觸的人可能讀取隨身碟上的資料，受影響的是 ThinkPlus FU100、FU200、TU800 與 TSD303 的第一代。

依 HackingPassion 與 Tom's Hardware，同一場演講裡的外接 SSD TSD303 有加密資料，問題出在密碼驗證。裝置會把正確的密碼以明文經 USB 傳回電腦上的程式比對。第一版修補改成加密後傳送，金鑰卻可由程式推算，2025 年 12 月的第二版改由裝置自行比對。依 HackingPassion 的整理，投影片列出的十款使用相同軟體套件的裝置（投影片上的廠商名稱經過遮蔽）有兩款把資料未加密存在 micro SD 卡上，八款的問題在密碼傳送。

Lenovo 的聲明沒有回答 AES-256 與硬體加密的宣稱是否屬實，也沒有承認或否認 SD 卡未加密。依 HackingPassion，Lenovo 與研究者都沒有提到有人實際遭到攻擊，本文到 11 月 8 日也沒有查到受害案例。

## 導讀觀點 {#perspective}

指紋與密碼畫面控制的可能只是連線，資料有沒有受到保護，要看解密金鑰從哪裡來。依 HackingPassion 的整理，第一種可靠的做法是金鑰由密碼經過 PBKDF2 或 Argon2 這類刻意放慢的函式衍生，每猜一次都要花時間。另一種是驗證完全在裝置自己的晶片內進行，密碼與金鑰都不離開晶片。依投影片，FU100 的資料沒有加密，兩種做法都沒有用上（本文的推論）。

儲存裝置廠商 Netac 的軟體加密工具在研究者測試的版本裡，AES-256 金鑰是寫在程式裡的固定值，跟使用者的密碼無關（依 Tom's Hardware 與 HackingPassion）。Tom's Hardware 也寫到，Netac 到研究者 2026 年 3 月的演講時沒有修補。軟體加密與 FU100 完全沒有加密的性質不同，標示 AES-256 同樣看不出金鑰的來源（本文的歸納）。

FIPS 140（美國政府的密碼模組標準）由 NIST 的密碼模組驗證計畫（CMVP）管理，模組交由獨立實驗室測試。證書可以在 NIST 的清單查詢，依 NIST 的頁面，FIPS 140-2 的證書在 2026 年 9 月 21 日後移到 Historical List（歷史清單）。依 IEEE Spectrum 的報導，德國資安公司 SySS 2009 年 12 月公開繞過多款 FIPS 140-2 認證隨身碟的方法，不論密碼為何都能在數秒內還原資料。IEEE Spectrum 引述 GCN 的報導，NIST 當時新聞稿的初步分析把問題指向授權解密的軟體（the software authorizing decryption）而非通過認證的密碼模組，也提到正在調查認證流程是否需要調整。

到 11 月 8 日，本文查不到 FU100 通過 FIPS 140 或中國商用密碼認證（中國對商用密碼產品的認證制度）的資料。HackingPassion 的建議是把隨身碟上的指紋或密碼畫面當成存取的鎖，除非廠商說明金鑰依賴它。NIST 的初步分析把問題指向軟體，本文據此推論，查到證書之後仍需要廠商說明金鑰如何產生、密碼在哪裡驗證。

手上有 NVD 列出的四款第一代裝置的人，依 Lenovo 的聲明可以聯繫支援安排更換。依 HackingPassion 轉述，免費升級（free upgrade）要撥打中國的服務專線，裝置會送回更換或到場升級韌體。同樣依 HackingPassion 轉述，Lenovo 建議送出前先備份資料，再抹除或格式化。

其他品牌的隨身碟要放敏感檔案時，可以在檔案放上去之前自行加密，讓金鑰來自自己設定的密碼（HackingPassion 列出的建議之一）。VeraCrypt（開源的磁碟加密軟體）的下載頁列出 Windows、macOS 與 Linux 版本，非系統磁碟區與檔案容器支援 PBKDF2 與 Argon2id 兩種金鑰衍生方式。代價是每台要開檔的電腦都要能執行 VeraCrypt。

Microsoft 的說明頁只列出 Windows Pro、Enterprise、Education 等版本可以啟用 BitLocker，Home 版不在表內。依 BitLocker FAQ，BitLocker To Go 涵蓋 USB 隨身碟與 SD 卡，加密後可以在另一台電腦用密碼開啟。Home 版能否解鎖已加密的隨身碟，本文沒有核對到官方文件。

Apple 的安全指南寫到 FileVault 保護內接與可移除的儲存裝置，磁碟工具程式也可以在格式化時用密碼加密外接裝置，加密前需先抹除裝置。LUKS（Linux 常用的磁碟加密格式）依 cryptsetup 的 FAQ 以 PBKDF2 或 Argon2 處理密碼，FAQ 也建議備份 LUKS 標頭（header），標頭損壞可能無法解密。macOS 加密的外接碟與 LUKS 能否在其他作業系統開啟，本文沒有核對到官方文件，要跨電腦使用的人需先實際試過。

自行加密可以應對隨身碟遺失或被別人取走的情況，電腦本身已遭入侵、密碼太短或忘記密碼時都幫不上忙（本文的推論）。只放公開資料的隨身碟不需要多做這一步，要放個人資料或工作文件的人，再衡量每台電腦都要能執行加密軟體的代價。
