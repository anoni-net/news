---
title: The UK Supreme Court ruling on state immunity in a spyware claim
description: "On 27 July the UK Supreme Court ruled 3–2 that a foreign state cannot claim immunity in UK courts when spyware installed remotely from abroad causes personal injury in the UK. The ruling decides only jurisdiction, Bahrain denies the allegations, and courts outside the UK apply their own law."
date: 2026-10-06T07:05:00+08:00
slug: uk-supreme-court-spyware-state-immunity
sources:
  - title: "[2026] UKSC 25, Case UKSC/2024/0152"
    url: https://supremecourt.uk/cases/uksc-2024-0152
    publisher: UK Supreme Court
    date: 2026-07-27
  - title: Judgment (PDF)
    url: https://supremecourt.uk/uploads/uksc_2024_0152_judgment_a1ae6cd3a5.pdf
    publisher: UK Supreme Court
    date: 2026-07-27
  - title: Press summary (PDF)
    url: https://supremecourt.uk/uploads/uksc_2024_0152_press_summary_800976eda1.pdf
    publisher: UK Supreme Court
    date: 2026-07-27
  - title: State Immunity Act 1978
    url: https://www.legislation.gov.uk/ukpga/1978/33
    publisher: legislation.gov.uk
  - title: U.K. Supreme Court Opens Door for Spyware Victims to Sue Foreign States
    url: https://citizenlab.ca/uk-supreme-court-opens-door-for-spyware-victims-to-sue-foreign-states/
    publisher: Citizen Lab
    date: 2026-09-02
  - title: U.K. Supreme Court Opens Door for Spyware Victims to Sue Foreign States
    url: https://www.lawfaremedia.org/article/u.k.-supreme-court-opens-door-for-spyware-victims-to-sue-foreign-states
    publisher: Lawfare
    date: 2026-08-28
  - title: Digital Security Helpline
    url: https://www.accessnow.org/help/
    publisher: Access Now
  - title: State Immunity Act 1979
    url: https://sso.agc.gov.sg/Act/SIA1979
    publisher: Singapore Statutes Online
  - title: 外国等に対する我が国の民事裁判権に関する法律
    url: https://laws.e-gov.go.jp/law/421AC0000000024
    publisher: e-Gov 法令検索
  - title: 中华人民共和国外国国家豁免法
    url: http://www.npc.gov.cn/npc/c2/c30834/202309/t20230901_431424.html
    publisher: 中国人大网
    date: 2023-09-01
regions:
  - GB
  - BH
authors:
  - anoni-net
---

On 27 July the UK Supreme Court dismissed Bahrain's appeal by a 3–2 majority, so two claimants living in the UK can keep suing the Bahraini government despite state immunity (a foreign government generally cannot be sued in another country's courts, with exceptions set by national law). The claimants allege that from around September 2011 Bahrain infected their computers with FinSpy (commercial spyware), and that learning of it caused them psychiatric injury. The ruling covers only whether UK courts can hear the case. Bahrain denies the allegations, which are left for trial, and courts outside the UK apply their own law.

Filed in 2020, the claim survived Bahrain's immunity plea in the High Court in 2023 and the Court of Appeal in 2024. The State Immunity Act 1978 grants foreign states immunity, but section 5 excepts death, personal injury or damage to tangible property "caused by an act or omission in the United Kingdom".

Article 11 of the European Convention on State Immunity, which the UK has ratified, also requires the author of the injury to be present, and both sides agree this case fails that test. On the assumed facts, the operators were likely abroad, using a command and control server in Bahrain, while the claimants and their computers were in the UK.

The majority held that the absence of a presence requirement in section 5 was a deliberate departure from the Convention, and that an "act" includes one done through a device or by remote means. On that view, remotely manipulating a UK computer from abroad is an act in the UK.

## Perspective {#perspective}

Bahrain argued in court that the harm was caused by commands entered abroad, with file corruption or data copying on the claimants' computers as secondary events. One dissenting justice likened this to firing a rifle across a border river, placing the act in Bahrain where commands were entered and treating a camera switching on in the UK as its effect. The claimants listed ten classes of acts in the UK, including transmitting installation files, activating microphones and cameras, and logging keystrokes, which the majority found together amount to surveillance in the UK.

The majority wrote that Bahrain's reading would draw arbitrary distinctions, denying immunity to a state that sends agents in to kill but granting it to one that uses a drone flown from abroad. It also found that the Convention lets the UK widen the exception and that the UK had a reasonable basis to apply it to sovereign acts. The dissent replied that such examples read the 1978 Act with hindsight, and that a rule based on where the agent is located offers clarity and certainty. Bahrain argued this reading puts the UK in breach of the Convention, and the dissent found that customary international law allows the exception only where the author is present, with no state practice supporting a wider one.

Asian laws differ on this point. Section 7 of Singapore's State Immunity Act 1979 uses the same wording as the UK Act, "caused by an act or omission in Singapore", with no presence requirement. Japan's 2009 Act on the Civil Jurisdiction of Japan with respect to a Foreign State goes the other way: its Article 10 requires the person who performed the act to have been in Japan at the time. Mainland China's Foreign State Immunity Law, in force since 2024, lifts immunity under Article 9 for compensation claims over injury, death or property loss caused by a foreign state's relevant acts within Chinese territory, without spelling out a presence requirement.

In a Lawfare article, legal researchers from Citizen Lab and Access Now write that back in the High Court the claimants must prove attribution to Bahrain, causation and injury. In another UK case they describe, expert forensic evidence showed the claimant's phone had been hacked with Pegasus, but the defendant state had stopped defending once immunity was rejected, so how such claims fare against a substantive defence remains unclear. Claims over data exposure or economic loss alone fall outside section 5. Under section 13 of the State Immunity Act, even a successful claimant cannot seize a foreign state's property to enforce a judgment, unless the property is in commercial use or the state consents in writing.

Anyone who suspects spyware can write to Access Now's free Digital Security Helpline. As of 29 September its page says it replies within two hours and first checks that the requester is within its civil society remit. None of its ten languages is Chinese, so Chinese speakers may need to use English. When comparing jurisdictions, ask whether a remote intrusion counts as a local act, how much a victim must prove to attribute it to a state, whether widening the exception breaches international law, and whether a judgment can be enforced.
