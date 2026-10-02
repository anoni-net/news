---
title: The UK Supreme Court ruling on state immunity in a spyware claim
description: "The UK Supreme Court ruled that Bahrain cannot claim state immunity to stop a UK court hearing claims that it hacked computers in the UK with spyware operated from abroad. The ruling decides only whether UK courts can hear the case, and whether the hacking happened has not been tried."
date: 2026-10-06T00:05:00+08:00
slug: uk-supreme-court-spyware-state-immunity
categories:
  - surveillance
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

On 27 July the UK Supreme Court dismissed Bahrain's appeal by a 3–2 majority, so two claimants living in the UK can keep suing the Bahraini government. Bahrain had claimed state immunity, the rule that a foreign government generally cannot be sued in another country's courts unless national law makes an exception. The claimants allege that Bahrain infected their computers with FinSpy (commercial spyware), and that learning of it caused them psychiatric injury. The ruling covers only whether UK courts can hear the case: Bahrain denies the allegations, which are left for trial, and courts outside the UK apply their own law.

Section 5 of the State Immunity Act 1978 removes immunity for claims over death, personal injury or damage to tangible property "caused by an act or omission in the United Kingdom". The claimants seek damages for psychiatric injury, which counts as personal injury. Claims over data exposure or economic loss alone, with no injury or property damage, fall outside it.

The core question is whether a hacker operating remotely from abroad, breaking into a computer in the UK, has committed an act in the UK. On the claimants' pleaded facts, the operators were likely abroad, using a command and control server in Bahrain, while the claimants and their computers were in the UK.

The UK is a party to the European Convention on State Immunity, whose Article 11 sets a similar exception with two conditions. The facts causing the injury must occur in the forum state, and the author of the injury must be present there at the time. Both sides agree the case fails the second condition on the claimants' pleaded facts, but section 5 does not spell that condition out, so the dispute is whether section 5 should be read to include it.

Of the five justices, the three in the majority held that Parliament deliberately left the Convention's presence requirement out of section 5, and that an "act" includes one carried out through software or a device operated remotely. On that view, remotely manipulating a UK computer from abroad is an act in the UK. The two dissenting justices held that section 5 should be read consistently with the Convention, so that it too requires the foreign agent to be present in the UK.

## Perspective {#perspective}

Bahrain argued that the harm was caused by commands entered abroad, with what happened on the claimants' computers as secondary events. One of the dissenting justices likened this to firing a rifle across a border river, placing the act in Bahrain where commands were entered and treating a camera switching on in the UK as its effect. The claimants listed ten classes of acts in the UK, including transmitting installation files, activating microphones and cameras, and logging keystrokes. The majority found that together they amount to surveillance in the UK.

The majority noted that Bahrain accepts it would have no immunity if its agents came to the UK and killed someone. On Bahrain's reading, the same killing carried out by a drone flown from abroad would attract immunity, which the majority called an arbitrary distinction. The same justice replied that such examples read the 1978 Act with hindsight, since no one drafting it could have foreseen drones or hacking. The justice added that a rule based on where the agent is located offers clarity and certainty.

A further dispute is whether widening the exception puts the UK in breach of international law. Beyond the Convention, that includes customary international law, the rules drawn from consistent state practice that states accept as legally binding. The majority found that the Convention lets states widen the exception, and that the UK had a reasonable basis in customary law to apply it to sovereign acts. Sovereign acts are things a government does in its capacity as a state, as opposed to ordinary commercial dealings, and both sides agree the alleged hacking counts.

Bahrain argued that widening the exception breaches the Convention and customary international law. The same dissenting justice agreed, reasoning that the Convention permits wider exceptions only within what customary law allows. That justice held that customary law allows the exception only where the agent is present, and found not a single state that denies immunity when the agent is abroad.

Asian laws differ on whether presence is required. Singapore's State Immunity Act 1979 uses the same wording as the UK Act, "caused by an act or omission in Singapore", with no express presence requirement, and whether such wording implies one is exactly what the UK justices split over. Japan's 2009 Act on the Civil Jurisdiction of Japan with respect to a Foreign State goes the other way, and it requires the person who performed the act to have been in Japan at the time.

Mainland China's Foreign State Immunity Law, in force since 2024, lifts immunity for compensation claims over injury, death or property loss caused by a foreign state's acts within Chinese territory. Like the UK and Singapore laws, it does not spell out whether the actor must be present.

Back in the High Court, the trial-level court that will now hear the facts, the claimants must prove attribution to Bahrain, causation and injury, according to a Lawfare article by researchers from Citizen Lab and Access Now. In another UK case the article describes, expert forensic evidence showed the claimant's phone had been hacked with Pegasus, another spyware product. The defendant state stopped taking part once the court rejected immunity, and the High Court then ruled for the claimant. The researchers note that how such claims fare against a real defence by a foreign state remains unclear.

Even a successful claimant faces limits on enforcement. Under the State Immunity Act, a foreign state's property cannot be seized to enforce a judgment unless it is in commercial use or the state consents in writing.

Anyone who suspects spyware can write to Access Now's free Digital Security Helpline. As of 29 September its page says it replies within two hours and first checks that the requester is within its civil society remit. None of its ten languages is Chinese, so Chinese speakers may need to use English. When comparing jurisdictions, ask whether a remote intrusion counts as a local act, how much a victim must prove to attribute it to a state, whether widening the exception breaches international law, and whether a judgment can be enforced.
