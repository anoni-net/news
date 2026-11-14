---
title: Machine-checked proofs for Signal's one-to-one chats and a US grand jury subpoena
description: Google DeepMind used AI agents to prove encryption properties of libsignal, the Signal Protocol implementation, for one-to-one chats. Group chats, the servers and key generation are outside the scope, and as of 14 November we could find no reproduction by other researchers. Signal published an October grand jury subpoena in which only one of four phone numbers had an account, and what it handed over was the account creation time and the last connection date. Users do not need to change any settings.
date: 2026-11-18T00:00:00+08:00
slug: signal-verification-subpoena
categories:
  - encryption
sources:
  - title: "Introducing AlphaProof Code: a breakthrough in verifying complex software at depth"
    url: https://deepmind.google/blog/introducing-alphaproof-code/
    publisher: Google DeepMind
    date: 2026-11-10
  - title: "AlphaProof Code: Verifying Signal’s Security at the Machine-Code Level"
    url: https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf
    publisher: Google DeepMind
    date: 2026-11-10
  - title: Grand jury subpoena for Signal user data in the United States District Court for the District of Columbia (again!)
    url: https://signal.org/bigbrother/district-of-columbia-2/
    publisher: Signal
    date: 2026-11-03
  - title: Grand jury subpoena for Signal user data in the United States District Court for the District of Columbia
    url: https://signal.org/bigbrother/district-of-columbia/
    publisher: Signal
    date: 2026-03-06
  - title: Government Requests
    url: https://signal.org/bigbrother/
    publisher: Signal
  - title: Google DeepMind just mathematically verified key parts of Signal
    url: https://arstechnica.com/ai/2026/11/signals-encryption-just-passed-an-ai-powered-mathematical-checkup/
    publisher: Ars Technica
    date: 2026-11-11
  - title: 通訊保障及監察法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060044
    publisher: 全國法規資料庫
  - title: 電信管理法
    url: https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0060111
    publisher: 全國法規資料庫
  - title: 2025 ESG Report
    url: https://www.cht.com.tw/home/cht/-/media/web/pdf/sustainability/csr-report-download/csr-report-en/2025/2025-esg-report-en.pdf?sc_lang=en
    publisher: 中華電信
  - title: 刑事訴訟法（昭和二十三年法律第百三十一号）
    url: https://laws.e-gov.go.jp/law/323AC0000000131
    publisher: e-Gov 法令検索
  - title: 2026 Implementation Rules for Amending the Implementation Rules for Article 43 of the Law of the People’s Republic of China on Safeguarding National Security in the Hong Kong Special Administrative Region
    url: https://www.doj.gov.hk/en/legco/pdf/ajls20260324e1.pdf
    publisher: Department of Justice, HKSAR
    date: 2026-03-24
  - title: 署理律政司司長與保安局局長出席立法會司法及法律事務委員會及保安事務委員會聯席會議後會見傳媒開場發言（只有中文）
    url: https://www.doj.gov.hk/tc/community_engagement/press/pdf/pr20260324c2.pdf
    publisher: Department of Justice, HKSAR
    date: 2026-03-24
authors:
  - anoni-net
---

Google DeepMind announced on 10 November that its researchers had used AI agents to write computer-checked mathematical proofs for libsignal, the reference implementation of the Signal Protocol. The proofs cover how a one-to-one chat sets up a connection and updates its keys, and group chats are not included. On 3 November Signal published a grand jury subpoena issued in October by the US Attorney's Office in Washington, DC, in which only one of the four phone numbers named had an account, and Signal handed over the account creation time and the last connection date. Both matter to Signal users everywhere, and users do not need to change any settings.

DeepMind's blog post and technical paper state that the target was libsignal v0.105.4. The researchers compiled it with the standard Rust compiler into Linux machine code for AArch64 (the 64-bit ARM architecture), and the proofs apply to the compiled program, with the exception of the underlying cryptographic functions. The proofs come in two parts, one of which is PQXDH, the key exchange at the start of a conversation, which combines a conventional algorithm with one designed to resist future quantum computers. The other is the Triple Ratchet, which switches to a new key for every message.

The properties listed in the paper include forward secrecy (earlier messages stay unreadable even if a key leaks), secrecy and authentication of the handshake, and post-compromise security. Once an attacker has stolen the current keys, later messages are protected again as long as the attacker does not actively interfere at the next key update. The attacker modelled in the paper can control the network and the servers, and may also steal long-term keys or one party's entire state.

DeepMind calls the system AlphaProof Code. According to the blog post, the researchers worked with AI models to write Signal's security goals as mathematical specifications, and human experts reviewed each one. The proofs themselves were written by AI agents in Lean, a theorem prover that checks every step of reasoning by program. The paper states that the authors did not write a single line of proof by hand, that the agents produced about 6.5 million lines of Lean, and that five people completed the proof work in four weeks.

By the paper's count, the specifications and definitions a reader has to trust come to about 18,000 lines, plus about 8,000 lines of specification describing how machine code behaves. To check whether the system could tell flawed code apart, the researchers reinserted two old, since-fixed libsignal vulnerabilities into an isolated copy of the code, and both versions were proven insecure. According to WIRED's reporting as republished by Ars Technica, no new vulnerabilities were found in the verified parts.

DeepMind's blog post describes this as the first time the team has used AI to verify a widely deployed cryptographic protocol down to its implementation code. The post also claims that no widely deployed protocol like Signal had previously had its implementation formally verified by any method. The specifications and proofs have been released as open source. The post quotes Signal's chief technology officer as saying that automated theorem proving has given the team more confidence that the code delivers on its privacy guarantees.

The history of the subpoena is published on Signal's "Government Requests" page. The prosecutor's office issued it on 5 October with a three-day deadline, seeking "all customer or subscriber account information" for four phone numbers over a period of time. Its attachment listed items including, but not limited to, the date and time of account creation and the date and time of the last connection. Signal concluded that the standard instructions attached were written for banks, since they also asked for images of cheques and deposit slips, and the page states that Signal does not collect such data in a way that can be linked to an account.

The American Civil Liberties Union (ACLU) replied on Signal's behalf on 6 October. Three of the four numbers had no Signal account, and for the remaining one Signal provided the date and time the account was created and the date it last connected to Signal's servers. Signal keeps only the date of the last connection, not the time, so it could not provide a time.

This subpoena came without a nondisclosure order (a court order forbidding Signal from revealing that it had received the subpoena), so Signal published the documents after redacting the phone numbers, the time period and the identities of government personnel. The previous subpoena from the same court, issued in 2025 and published by Signal in March, asked about 37 accounts. Seven did not exist, 24 had no relevant data for the period, and data was provided for the remaining six. According to Signal's page, law enforcement requests are increasingly focused on the small amount of data Signal actually collects.

## Perspective {#perspective}

The protocol proofs concern how messages are protected in transit, including when an attacker controls the network and the servers or has even stolen some keys, while the subpoena response shows what data is kept on the server side. Signal's page opens by listing messages, calls, contacts, groups, profile names and avatars as end-to-end encrypted, and Signal cannot hand over data it never had.

Among the qualifications in the paper, one set of theorems uses a symbolic model, which assumes the cryptographic algorithms are perfect. A symbolic model says nothing about how well the actual bytes are kept secret, but within it the handshake's secrecy was proven to hold against future quantum computers. Another set of theorems, in a computational model, considers only attackers with conventional computers. For SPQR, the post-quantum part of the Triple Ratchet, the proof only shows that the whole is no weaker than the older Double Ratchet, and does not prove the additional post-quantum recovery that SPQR is meant to provide.

The key generation code was not verified, and the underlying cryptographic functions are only described by specifications of how they should behave, with no proof of their own. Side-channel attacks (inferring keys from external signals such as power use or timing) and other secrets in memory are out of scope. The machine-code theorems apply only when each party uses a single device. Both parties are assumed to hold each other's identity keys from the start, so the step of confirming the other person's identity on first contact is not covered.

The paper lists group chats, sealed sender (the mechanism that hides who sent a message) and the server-side protocol as future work. The 8,000 lines of specification describing machine code cannot be proven to match real hardware, and the paper states that hardware and the operating system kernel are not things that can be proven. WIRED's report as republished by Ars Technica also states that the Signal app as a whole was not verified.

All of the paper's authors are from Google DeepMind and Google, and the acknowledgements thank three members of Signal for feedback on the method. As of 14 November we could find no record of peer review for the paper and no reproduction by researchers outside DeepMind.

The paper mentions that WhatsApp, Meta Messenger and Google Messages also use variants of the Signal Protocol. The verification covered libsignal's code, which does not mean those apps' implementations have passed the same proofs.

Signal's first published subpoena response in 2016 already stated that all it could provide from the server side was the date and time of registration and the date of the last connection. What it handed over in October was the same two items. Because the request was made by phone number, the reply also told the prosecutors that three of the four numbers had no Signal account.

We, a community based in Taiwan, have checked comparable laws in Asia for requests to telecom carriers and for demands that a person hand over a device password, but not how they apply to a foreign messaging app such as Signal. Taiwan's Communication Security and Surveillance Act (通訊保障及監察法) requires a prosecutor to apply to a court for a retrieval order (調取票) to obtain communication records, which include location information, except in emergencies. For offences with a minimum sentence of ten years and for listed offences such as robbery and fraud, the prosecutor can obtain the records on their own authority. The Telecommunications Management Act (電信管理法) obliges carriers to assist, and Chunghwa Telecom reported 247,032 law enforcement requests for customer information in 2025.

Japan's Code of Criminal Procedure (刑事訴訟法) lets investigators ask an organization to report necessary matters (Article 197(2)), while its preservation request only keeps a carrier's communication logs from being erased for up to 30 days and does not hand them over (Article 197(3)). Hong Kong goes to the person rather than the provider, a separate route to the data: under amended implementation rules for Article 43 of the National Security Law, gazetted on 23 March 2026, police investigating offences endangering national security can require a "specified person", such as a suspect or anyone believed to know the password, to provide the password or decryption method for an electronic device. Failing to comply without reasonable excuse carries a fine of up to HK$100,000 and one year in prison, and the Secretary for Security told the media that police must first obtain a search warrant from a court. According to the Department of Justice paper, the rules before the amendment already let police search electronic devices with a magistrate's warrant or where obtaining one was not reasonably practicable, and the paper does not say whether the new password requirement applies without a warrant.

Users do not need to change any settings. People who handle sensitive conversations on Signal can weigh the fact that the proofs cover only one-to-one chats and that the paper draws no conclusions about group chats. Based on the October reply, the server side keeps the account creation time and the last connection date. Going forward, it is worth watching whether other researchers reproduce DeepMind's open-source proofs and whether verification extends to group chats and sealed sender, for which the paper gives no timeline.
