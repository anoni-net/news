---
title: Webloc, Penlink's ad-based location surveillance system, and its customers in more countries
description: According to Citizen Lab's update of 12 November relaying a Bloomberg investigation, security agencies in more countries, including the UK, Germany and Singapore, have acquired Webloc, which tracks phone locations using app and advertising data. The confirmed customers in Citizen Lab's April report were in the United States, El Salvador and Hungary, and the update adds that Austria's Ministry of the Interior has been confirmed as a customer (checked on 14 November). Phone settings for tracking and location permissions can reduce what apps send out, but the report says they cannot reliably prevent it.
date: 2026-11-16T00:05:00+08:00
slug: penlink-webloc-ad-location-tracking
categories: [surveillance]
sources:
  - title: Security Agencies Worldwide Found to Use Ad-Based Surveillance System
    url: https://citizenlab.ca/security-agencies-worldwide-found-to-use-ad-based-surveillance-system/
    publisher: Citizen Lab
    date: 2026-11-12
  - title: "Uncovering Webloc: An Analysis of Penlink’s Ad-based Geolocation Surveillance Tech"
    url: https://citizenlab.ca/research/analysis-of-penlinks-ad-based-geolocation-surveillance-tech/
    publisher: Citizen Lab
    date: 2026-04-09
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: National People's Congress
    date: 2021-08-20
  - title: 個人情報の保護に関する法律
    url: https://laws.e-gov.go.jp/law/415AC0000000057
    publisher: e-Gov 法令検索
  - title: 個人情報の保護に関する法律についてのガイドライン（通則編）
    url: https://www.ppc.go.jp/files/pdf/260614_guidelines01.pdf
    publisher: Personal Information Protection Commission
  - title: 個人資料保護法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021
    publisher: 全國法規資料庫
regions:
  - US
  - SV
  - HU
  - AT
authors:
  - anoni-net
---

According to an update Citizen Lab published on 12 November, a Bloomberg investigation building on Citizen Lab's April research has found security agencies in more countries that acquired Webloc. Webloc is a location surveillance system sold by Penlink, a US surveillance technology vendor, and it tracks where devices are and how they move using data bought from mobile apps and digital advertising. According to Citizen Lab's April report, maps in documents describing Webloc show it was used to track people in a number of countries, and any app that displays ads is potentially a source of the data.

The April report sorts customers into confirmed and potential ones. The confirmed customers are Hungary's domestic intelligence service (using Webloc since at least 2022 and still using it when the report was published), El Salvador's National Civil Police, which bought it in 2021, and in the United States, Immigration and Customs Enforcement (ICE), the US military, the Texas Department of Public Safety and police departments in several cities. A senior researcher quoted in the update describes Webloc as a tool "trickling down from military and intelligence agencies to federal law enforcement and then to state and local police." The evidence for potential customers includes vague answers to freedom of information requests, procurement records, training records and server analysis, and the report names the Netherlands, Mexico, Vietnam and Singapore as places where further research would be fruitful.

The update says Austria's Ministry of the Interior has since been confirmed as a customer, without saying where the confirmation came from. The April report had listed it as a potential customer because it bought Tangles in December 2024 and refused to say, in answer to a freedom of information request, whether the purchase included Webloc. As relayed by the update, the Bloomberg investigation found customers in other countries including the UK, the Netherlands, Germany, Mexico, Singapore, Saudi Arabia, the UAE and Israel, and the update says these findings align with the potential customers listed in April. Besides the countries it named for further research, the April report's discussion of potential customers also covers UK and Dutch agencies that refused to answer freedom of information requests, and Israeli military personnel trained on Webloc.

Webloc was developed by Cobwebs Technologies, an Israeli company, and has been sold by Penlink since the two companies merged in 2023, as an add-on to Tangles, a social media and web intelligence system. When the April report was published, Penlink's website mentioned Webloc only once, in connection with a training course, so the report's analysis draws on a technical proposal leaked from El Salvador's National Civil Police in 2021, contract documents from the US Office of Naval Intelligence and other sources.

According to 2021 documents cited in the report, Webloc offers a constantly updated stream of records from up to 500 million mobile devices worldwide (each tracked at least once a month), refreshed every 4 to 24 hours. A 2023 contract document from a US law enforcement agency says three years of historical data are available. The fields listed in the same 2021 documents include the advertising ID, a timestamp, coordinates derived from GPS or Wi-Fi, the IP address, the Wi-Fi network name, the device model and operating system, age, gender, language, the apps in use and advertising segments, for both Android and iOS. The researchers write that they cannot assess the current coverage and accuracy of this data.

According to Penlink's response, Webloc contains only location data tied to device identifiers, and no age, gender, parenthood, interest categories or websites visited. The researchers could not verify this, and they cite a 2025 Penlink document stating that Webloc "generates demographic insights". Even without those fields, the researchers write, location records on their own reveal a person's habits, interests and personal characteristics.

Analysts can draw an area on a map (a geofence) and list the devices that have been inside it, or find devices that appeared in two or more places. According to the El Salvador document, heat maps can show where a device usually is during the day and at night, from which a home and workplace can be inferred. The document also suggests sending "ground forces" to a suspect's location, and names identifying the people behind the devices as the purpose of Webloc.

The server analysis relies on hostnames and login pages. Where a server shows a Tangles login page, the researchers have high confidence that it belongs to a Tangles deployment, while linking hostnames to Webloc and other products from the letters in them carries only medium confidence. Even for countries where they are confident related servers exist, the researchers write that it is still unknown whether the products are actually in operation. The researchers also do not know whether the country where a server sits is the country where the customer is.

Penlink replied to the summary of findings Citizen Lab sent on 3 April, and its response is published in full in the report. According to the response, the findings "appear to rely on either inaccurate information or a misunderstanding about how we operate, including practices that Penlink does not engage in following our acquisition of Cobwebs Technologies in 2023." The response also says the report names companies and products that no longer exist and countries Penlink does not do business in, without specifying which.

The response further states that the data comes from providers that obtain user consent through SDKs (third-party code libraries that app developers embed) and filter out sensitive locations, consistent with the requirements of the US Federal Trade Commission (FTC), and that the company complies with US state privacy laws. The report's assessment is that the response left most of its questions unanswered and did not address privacy laws outside the United States. The researchers also could not verify the claim about consent.

## Perspective {#perspective}

Surveillance based on app and advertising data has been called advertising intelligence (ADINT), a term the report says was reportedly coined by the surveillance industry itself. Real-time bidding (RTB) is one of the data sources described in the report's background section: every time an app or web page shows an ad, an auction runs in under a second, and the user's data is shared with dozens or hundreds of marketing firms in the process. Another source is third-party tracking code inside apps, and surveillance vendors typically buy that data from data brokers (companies that collect and resell personal data) who run such code. [Another Citizen Lab report](https://anoni.net/news/en/2026/10/adfection-targeted-ads-spyware/) we covered in October also exploited the advertising supply chain, but that was a different vendor delivering spyware through targeted ads, and a separate system from Webloc.

The report says it is not currently possible to determine where Penlink gets Webloc's data, which might come from tracking code in apps, from bidding data, or from both. The 2021 documents show Webloc holding Wi-Fi network names, which bidding data does not provide, and on that basis the researchers infer that the data then came from tracking code in apps. They also consider it almost certain that the 2026 sources differ from those of 2021, because these supply chains keep shifting, and data brokers collecting for surveillance vendors have repeatedly been cut off from their app data sources.

According to the report, location and advertising data can reveal a person's home, workplace, religion, political views, sexual orientation or health issues, and many parties can match an advertising ID to a name, email address and phone number. The update says the lawfulness of using such systems in Europe and the UK is highly controversial, and that their use in the authoritarian countries identified by reporting is particularly dangerous. Based on the responses to 96 freedom of information requests, the report concludes that governments in Europe and the UK are highly nontransparent.

As of 14 November, Citizen Lab's pages do not say which agencies in each country Bloomberg identified as customers or how they use Webloc, and do not cite any response from Penlink or those agencies to the Bloomberg investigation. With the data supply chain unknown, readers also have no way to tell which apps' data ends up in Webloc (our inference).

We, a community based in Taiwan, compared how the laws of mainland China, Japan and Taiwan treat the kind of location data Webloc is built on, and did not examine whether these provisions reach police or intelligence agencies that buy it. Mainland China's Personal Information Protection Law lists whereabouts among the categories of sensitive personal information, and handling them requires the person's separate consent (Articles 28 and 29). Under Article 23, a company providing personal information to another handler has to tell the person who the recipient is and for what purpose, and obtain separate consent.

The guidelines of Japan's Personal Information Protection Commission give a person's location information as one example of "personally referable information". Under Article 31 of the Act on the Protection of Personal Information, when the recipient is expected to acquire such information as data identifying the person, the company providing it has to confirm beforehand that the person's consent has been obtained, outside the listed exceptions. The Personal Data Protection Act of Taiwan has no provision specifically on advertising identifiers, real-time bidding or targeted advertising, and on our reading of the text, the categories its Article 6 restricts in principle (medical records, medical care, genetic data, sex life, health checks and criminal records) do not list location; we did not check regulator or court interpretations, or which general rules apply to such data. These rules govern companies handling the data and do not by themselves restrict agencies that buy it.

The report's advice for iPhone users is to deny new apps permission to track your activity across other companies' apps and websites when installing them, and to review the apps previously allowed to track you. The feature is not available on versions before iOS 14.5. On Android, depending on the device maker and system version, you can delete the advertising ID or opt out of ads personalization in settings. iPhone users can review which apps have access to location and other information, and Android users can review location permissions.

According to the report, these steps can minimize but not reliably prevent apps from sharing data with third parties, since an app may still pass data it processes to run the app directly from its own servers to other companies. It also cites Google's statement that once a user deletes the advertising ID, apps might use other "persistent or proprietary identifiers". Apps that show no ads may also share data directly or indirectly, so people who need to keep their movements private should assume, even after these settings are in place, that apps on their phone may still send location data (our inference from the report's caveats).
