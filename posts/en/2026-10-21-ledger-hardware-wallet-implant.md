---
title: Implanted chips in Ledger hardware wallets
description: On 15 October Ledger confirmed that a criminal group had fitted genuine hardware wallets with parts that capture the recovery phrase during setup, then put them on the market through resellers in Southeast Asia. As of 13 October, the thefts Ledger had confirmed were all tied to devices sold by authorised reseller CryptoBilis, and reports of implants from other channels were unconfirmed. Ledger's Genuine Check cannot detect these implants, and Ledger advises anyone who bought and set up a device from CryptoBilis to move their assets to a new device and a new recovery phrase.
date: 2026-10-21T00:05:00+08:00
slug: ledger-hardware-wallet-implant
categories:
  - security
sources:
  - title: Ledger’s Response to the Hardware Implant Attack
    url: https://www.ledger.com/blog-response-hardware-implant-attack
    publisher: Ledger
    date: 2026-10-15
  - title: Check hardware integrity
    url: https://support.ledger.com/article/4404382029329-zd
    publisher: Ledger Support
  - title: Best Practices To Securely Buy Your Ledger Signer
    url: https://www.ledger.com/academy/topics/ledgersolutions/best-practices-to-securely-buy-ledger-signer
    publisher: Ledger Academy
    date: 2026-03-06
  - title: Purchasing from an authorised reseller
    url: https://support.ledger.com/article/Purchasing-from-an-authorised-reseller
    publisher: Ledger Support
  - title: Find a Ledger Reseller around the world
    url: https://shop.ledger.com/pages/resellers
    publisher: Ledger
  - title: Why is Ledger Nano so Secure?
    url: https://www.ledger.com/academy/basic-basics/ledgers-bit-of-it/ledger-nano-security-made-easy
    publisher: Ledger Academy
  - title: Ledger says hardware implant in cryptocurrency wallets stole recovery phrases
    url: https://therecord.media/ledger-cryptocurrency-wallet-implant-theft
    publisher: The Record
    date: 2026-10-13
  - title: "Ledger Nano X: the spy implant."
    url: https://www.tibane.net/research/ledger-nano-x-implant
    publisher: Tibane Labs
  - title: The Ledger CryptoBilis hack took $102.0M from 335 wallets. One thief had all the keys
    url: https://bitquery.io/investigations/ledger-cryptobilis-hack
    publisher: Bitquery
    date: 2026-10-10
  - title: Who Is Planting Backdoors in Ledger Crypto Wallets?
    url: https://www.zetter-zeroday.com/who-is-planting-backdoors-in-ledger-crypto-wallets/
    publisher: Zero Day
    date: 2026-10-13
  - title: Ledger suspends retail sales in Germany as wallet implant probe continues
    url: https://crypto.news/ledger-suspends-retail-sales-in-germany-as-wallet-implant-probe-continues/
    publisher: crypto.news
    date: 2026-10-13
  - title: Ledger confirms hidden chip in crypto wallet amid $92M theft claims
    url: https://crypto.news/ledger-confirms-hidden-chip-in-crypto-wallet-amid-92m/
    publisher: crypto.news
    date: 2026-10-11
  - title: Ledger reveals how hidden chips stole wallet recovery keys
    url: https://crypto.news/ledger-reveals-how-hidden-chips-stole-recovery-phrases/
    publisher: crypto.news
    date: 2026-10-13
  - title: Ledger asks resellers to halt sales in Southeast Asia and Hong Kong
    url: https://cointelegraph.com/news/ledger-asks-resellers-to-halt-sales-in-southeast-asia-and-hong-kong
    publisher: Cointelegraph
    date: 2026-10-13
  - title: Check that your Ledger device has a genuine secure element with Ledger Wallet
    url: https://support.ledger.com/article/4404389367057-zd
    publisher: Ledger Support
    date: 2026-10-20
  - title: 立法院院會三讀通過「虛擬資產服務法」
    url: https://www.sfb.gov.tw/ch/home.jsp?id=95&parentpath=0%2C2&mcustomize=news_view.jsp&dataserno=202606300002&dtable=News
    publisher: Securities and Futures Bureau, Financial Supervisory Commission
    date: 2026-06-30
  - title: Virtual asset trading platforms operators
    url: https://www.sfc.hk/en/Welcome-to-the-Fintech-Contact-Point/Virtual-assets/Virtual-asset-trading-platforms-operators
    publisher: Securities and Futures Commission
  - title: "央行等八部门：虚拟货币业务非法，持续整治“挖矿”！"
    url: https://m.gmw.cn/2026-02/07/content_1304335528.htm
    publisher: Guangming Online
    date: 2026-02-07
  - title: Payment Services Act
    url: https://www.japaneselawtranslation.go.jp/en/laws/view/3965/en
    publisher: Japanese Law Translation
  - title: Payment Service Providers
    url: https://www.mas.gov.sg/publications/annual-report/2024/annual-report-2023-2024/responsible-and-trusted-financial-centre/payment-service-providers
    publisher: Monetary Authority of Singapore
authors:
  - anoni-net
---

Hardware wallet maker Ledger confirmed on its official blog on 15 October that a criminal group had spent months buying genuine Ledger devices. The group opened them and fitted hidden components that capture the recovery phrase (24 English words that can restore everything in the wallet) while the user sets the device up, then put the devices back on the market through resellers in Southeast Asia. According to the timeline from on-chain analytics firm Bitquery, the mass thefts began on 9 October. According to The Record, citing Ledger's 13 October statement, all confirmed thefts are linked to devices sold by CryptoBilis, an authorised Ledger reseller in Southeast Asia.

Cointelegraph reported that Ledger also said on 13 October it had not confirmed thefts from devices bought through other channels. Ledger's 15 October post says it has asked resellers in Southeast Asia and Hong Kong to pause sales. Ledger's Genuine Check, which connects to Ledger's servers to confirm that the secure element is original, cannot detect implants of this kind.

Ledger's 15 October post says there is no flaw in its chips, operating system or servers. In the post, Ledger describes the incident as a "localized distribution attack" that took place in the distribution channel after the devices left Ledger, and The Record also cites Ledger as saying the number of affected devices is limited. According to The Record, citing Ledger's 13 October statement, the implant reads what is shown on the screen, picks out the recovery phrase during setup and sends it out over the LTE mobile network through a built-in eSIM.

Tibane Labs, a blockchain research and development company, took apart two Nano X units bought from a Japanese auction site and a seller on Amazon Japan, and its page states that it did not test any CryptoBilis devices. The implant is a small computer soldered to the main board and wired to the screen's data line, and it makes no attempt to break the secure element (the chip that stores the private keys). Tibane Labs compared three versions and found that the dedicated antenna on the latest one is printed with a part number and version number, from which it inferred that the implant is mass-produced.

As of 20 October, Ledger has not disclosed the affected models, batches, number of people or amounts. Bitquery counted 335 wallets and US$102 million drained as of 16 October, and the US$92.9 million in earlier reports from crypto.news and others was an earlier Bitquery figure. Bitquery's page says the on-chain record points to a single actor holding the keys to every drained wallet, but the chain shows only transfers, not where the keys leaked from.

Zero Day, a security journalist's newsletter, reported on 13 October on claims of implants in devices bought outside CryptoBilis. An unnamed Japanese researcher told Zero Day he had bought ten units in total from unauthorised online sellers, the earliest in March, and every one had an implant. The same report cites a post on X by a German buyer who said he bought implanted Nano X units from MediaMarkt, which Ledger lists as an authorised reseller in Germany, at two of its stores. As of 20 October, Ledger has not confirmed these accounts.

The Record quotes Ledger's 13 October statement as saying it is "also reviewing reports of implants in other signers and locations". According to crypto.news, MediaMarkt paused sales with Ledger's agreement. Ledger said it had received no reports of lost funds in the German cases and had not established whether the German reports were related to the others. Ledger's 15 October post says it sent people to buy and open devices in markets including Germany and that "Every unit examined was clean", without giving the number of units examined.

## Perspective {#perspective}

According to Ledger's educational site Ledger Academy, the private keys are stored in the secure element. The device generates the recovery phrase at initialisation and displays it only that once. Ledger's support page on checking hardware integrity says Genuine Check verifies a key written into the secure element at the factory, which keeps out counterfeits. The same page notes that as long as the original secure element is intact, Genuine Check cannot detect physical modifications such as implants.

The implant described by The Record and Tibane Labs leaves the secure element alone and reads the recovery phrase off the screen's data line at the moment it is displayed. The hardware integrity page says that on the Nano X and Nano S Plus, the secure element checks the main microcontroller's firmware at startup and shows a warning if it has been altered. The other check the page lists is opening the case and comparing the inside with Ledger's official photos to make sure no extra chip has been added. Tibane Labs' page says the device itself cannot detect the implant, and that the latest version is painted the same colour as the original circuit board.

According to The Record, citing Ledger's 13 October statement, anyone with a CryptoBilis device that has not been set up should leave it that way and contact support. Those who have already set one up should move their assets to a new device and a new recovery phrase as soon as possible, and should not enter or restore any recovery phrase on a device bought from CryptoBilis. Victims should contact Ledger and local police before deciding whether to open the device or send it anywhere.

For people who bought a Nano X of unknown origin through other channels and have already set it up, Ledger had made no recommendation to change the recovery phrase as of 20 October. Tibane Labs' page recommends replacing any recovery phrase that was shown on a Nano X of unknown origin, generating a new one on a trusted device and moving the assets to it. The page also says a recovery phrase shown on a modified screen should be treated as leaked even if the device has never been online. According to the hardware integrity page, people comfortable with hardware can open the case and compare, but damage from opening it is not covered by the warranty.

People who have not bought a device yet, or have just received one, can follow the purchasing guidance on Ledger's support site. Do not use a device whose packaging looks opened or resealed, or that comes with a card already filled in with a recovery phrase, and contact support instead. Ledger recommends buying from its official store or an authorised reseller, and as of 20 October its reseller page lists six resellers in Taiwan and five in Hong Kong, with no pause marked on the Hong Kong entries. These support pages had no Traditional Chinese version as of 20 October.

Elsewhere in Asia, the same reseller page lists six resellers in Singapore, only Amazon Japan for Japan, and no entry for mainland China. As of 20 October it marks "Sales temporarily paused" only on CryptoBilis in Indonesia and Malaysia and on some online shops in Malaysia and the Philippines. According to Cointelegraph, which reported a social media post from Ledger, the 13 October request covered resellers in Indonesia, Singapore, Thailand, the Philippines, Vietnam, Malaysia and Hong Kong, but the Hong Kong and Singapore entries carry no pause label. As of 20 October, Ledger's list of official Amazon stores includes Japan and Singapore but not Taiwan, Hong Kong or mainland China.

The crypto rules we found in Taiwan, Hong Kong, mainland China, Japan and Singapore concern service providers, trading platforms or crypto businesses, and as of 20 October we found no provision on selling, importing or owning hardware wallets themselves (which does not mean none exists). Taiwan's Virtual Asset Service Act, passed by the Legislative Yuan on 30 June 2026 with a start date still to be set by the Executive Yuan, covers seven kinds of virtual asset service providers, including exchanges, trading platforms, transfer services and custodians. The press release from the Securities and Futures Bureau of the Financial Supervisory Commission does not mention wallets or self-custody.

Hong Kong's Securities and Futures Commission (SFC) requires centralised virtual asset trading platforms doing business in Hong Kong or marketing to Hong Kong investors to be licensed, and its page does not mention wallets. The 2020 English translation of Japan's Payment Services Act counts managing crypto-assets on behalf of another person as a crypto-asset exchange service; we did not check later amendments, and the translation does not mention wallets. The Monetary Authority of Singapore (MAS) brought custody of digital payment tokens under its Payment Services Act from April 2024, and its page does not mention wallets either.

In mainland China, eight departments including the People's Bank of China issued a notice on further preventing and dealing with risks related to virtual currency on 6 February 2026. We read only a media reprint of its full text, which treats domestic virtual currency exchange and trading as suspected illegal financial activity and says that civil acts of investing in virtual currency that violate public order and good morals are void, but it does not mention wallets.

CryptoBilis and MediaMarkt are both on Ledger's list of authorised resellers, and Ledger Academy's buying guide says "no global supply chain is entirely immune". Our inference is that buying through authorised channels lowers the risk but cannot guarantee a device has not been tampered with.

In its 15 October post, Ledger asks resellers to stop placing devices on shelves and in display cases and to hand them to buyers directly from stock, and repeats that returned devices must never be resold. The same post says Ledger will publish fuller technical details and is developing product-level protections. What comes of these two, and whether Ledger widens the scope of what it has confirmed, are the things to watch next.
