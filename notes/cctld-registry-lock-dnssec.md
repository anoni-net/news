# 國碼頂級網域的註冊鎖定與 DNSSEC

範圍是亞洲幾個國碼頂級網域的營運單位，有沒有提供註冊管理機構層級的鎖定服務（registry lock），以及 DNSSEC 的導入狀況。第一次整理是寫 anoni-net/news 的國碼頂級網域劫持那篇的時候，查證日期 2026-10-12。到這天為止，查不到下列營運單位針對 2026 年 9 月 .gh、.sl、.as 遭劫持事件的說明。

註冊鎖定能不能擋下營運單位自己的系統被入侵，查不到任何官方說法。Google 對那起事件的建議也沒有提到註冊鎖定。

## 中國大陸（.cn）

- 事實：中國互聯網絡信息中心（CNNIC，機構正式名稱）提供「國家域名保護鎖服務」，在註冊管理機構層級對 .cn 與 .中國 網域設定禁止刪除、禁止修改、禁止轉移三個狀態，解鎖要通過 CNNIC 的核驗流程 <!-- docs-style-lint: disable-line -->
    - 照錄：「域名保护锁服务从注册管理机构层面对“.CN”“.中国”域名设置 Server Delete Prohibited(禁止删除)、Server Update Prohibited (禁止修改)、Server Transfer Prohibited(禁止转移)三个状态，用户和注册服务机构均需通过中国互联网络信息中心严格的核验流程后才可对域名进行解锁操作。」
    - 來源：服务简介（國家域名保護鎖服務），中国互联网络信息中心，<https://www.cnnic.net.cn/n4/2022/0901/c56-10201.html>，頁面日期 2026-04-09
    - 註冊服務商的公告提到標準版、進階版與費用調整，CNNIC 官方頁面沒有看到這些區分，不引用
- 事實：.cn 與 .中國 已導入 DNSSEC，CNNIC 公告過 2016、2017 年的金鑰輪替
    - 照錄：「根据国家顶级域名“.CN”及“.中国”（简繁体）（以下简称“国家域名”）的《政策与实践声明》规定，国家域名KSK密钥于2017年12月19日进入轮转周期。」
    - 來源：关于“.CN”及“.中国”（简繁体）DNSSEC密钥轮转的公告，中国互联网络信息中心，<https://www.cnnic.net.cn/n4/2022/0401/c39-4073.html>，2017-12-25
- 查不到：中國大陸的主要瀏覽器或憑證機構對憑證透明度（CT）的官方要求。360 瀏覽器根憑證計畫的政策頁（版本 1.2）沒有提到 CT

## 台灣（.tw）

- 事實：TWNIC 提供 .tw 的 Registry Lock，鎖定後加上禁止修改、禁止轉移、禁止刪除三個狀態，解鎖要由 TWNIC 驗證服務管理人的身分，每筆網域每年新台幣 6,000 元。2026 年 12 月 31 日前新申請的首年優惠價是新台幣 4,800 元
    - 照錄（TWNIC 部落格）：「TWNIC之Registry Lock防護等級高於一般註冊商的Registrar Lock。即便註冊商遭到入侵，Registry Lock仍然可以堅固地保護註冊人的域名。」
    - 照錄（registrylock.tw）：「本服務每筆網域名稱收取申請費新台幣6,000元/年，最多可申請10年」
    - 照錄（registrylock.tw）：「享服務推廣專案優惠價新台幣4,800元/首年(原價6,000元/年)」
    - 來源：將您的域名「鎖」上——Registry Lock，TWNIC 部落格，<https://twnic.tw/blog/contents.php?id=25&lang=zh-tw>，2025-09-12。.tw 域名安全鎖服務 Registry Lock Service，TWNIC，<https://registrylock.tw/> <!-- docs-style-lint: disable-line -->
- 事實：2026 年 2 月 2 日起，使用 TWNIC DNS 代管服務的網域預設開啟 DNSSEC，範圍只限用 TWNIC 代管的網域
    - 照錄：「自2026年2月2日起，我們將針對所有使用 DNS代管服務的網域名稱，預設開啟DNSSEC（網域名稱系統安全擴充技術）功能。」
    - 來源：TWNIC DNS代管服務安全性升級：自2月2日起全面預設啟用DNSSEC功能，TWNIC，<https://twnic.tw/blog/contents.php?id=96>，2026-01-06

## 日本（.jp）

- 事實：JPRS 提供 .jp 的レジストリロックサービス，鎖定註冊資料與名稱伺服器設定，服務透過指定事業者（註冊商）提供，各家的提供方式與範圍不同，也有不提供的
    - 照錄：「本サービスはJPドメイン名の登録情報（登録者の氏名、組織名、ネームサーバー設定など）が意図せず書き換えられることを防ぐために、対象ドメイン名の情報をロックし、以下の申請の受付を制限するものです。」
    - 照錄：「指定事業者による本サービスの提供方法及び提供範囲は、指定事業者によって異なります。」
    - 來源：レジストリロックサービス，JPRS，<https://jprs.jp/about/dom-rule/registry-lock/>，頁面沒有日期

## 香港（.hk）

- 事實：HKIRC 2014 年 1 月推出 .hk LOCK，網域擁有者可以鎖定名稱伺服器記錄，每次變更由 HKIRC 以人工聯繫核實，只能透過認可的註冊商申請
    - 照錄：「Through the service, .hk domain name owners will have the ability to lock their domain name server (DNS) records and prevent any unauthorised changes.」
    - 照錄：「Each change request will be verified by HKIRC’s human-to-human contact.」
    - 來源：HKIRC Launches .hk LOCK，HKDNR，<https://www.hkdnr.hk/en/hkirc-launches-hk-lock/>，2014-01-15
    - 查不到：服務的現況與收費。HKIRC 官網的 .hk LOCK 頁面在 2026-10-12 抓取時只回應首頁，沒有服務說明
- 事實：.hk 提供 DNSSEC，要向註冊商詢問服務細節
    - 照錄：「.hk Domain Name System Security Extensions (DNSSEC) Service Available Now!」
    - 來源：DNSSEC，HKIRC，<https://www.hkirc.hk/en/our-services-support/cyber-security-services/dnssec/>

## 南韓（.kr）

- 事實：KRNIC 2012 年 9 月完成 .kr、.한국 等 31 個國家網域區域的 DNSSEC 導入
    - 照錄：「우리나라는 2011년 “.kr” 국가도메인 영역에 대한 DNSSEC 적용을 시작으로 2012년 9월 .kr, .한국 등 총 31개 국가도메인 영역 전체에 DNSSEC 적용을 완료하여 본격 서비스 제공 중에 있습니다.」
    - 來源：DNSSEC이란?，KRNIC，<https://krnic.kisa.or.kr/jsp/resources/dns/dnssecInfo/dnssecInfo.jsp>
- 查不到：KRNIC 提供註冊管理機構層級鎖定服務的官方說明
