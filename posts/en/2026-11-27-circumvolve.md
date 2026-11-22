---
title: CircumVolve, a study using large language models to search for censorship evasion strategies
description: Researchers had a large language model repeatedly rewrite circumvention programs and, testing on networks in China, Iran, Pakistan and Kazakhstan, found 47 strategies that get past censorship equipment, though a strategy that works in one country does not necessarily work in another. The strategies reach users only after tool developers build them into their tools, and ordinary readers do not need to change any settings.
date: 2026-11-27T00:00:00+08:00
slug: circumvolve
categories:
  - censorship
sources:
  - title: "CircumVolve: Automated Discovery of Censorship Evasion Strategies Using Large Language Models"
    url: https://gfw.report/publications/ccs26/en/
    publisher: GFW Report
    date: 2026-11-16
  - title: alizohaib/ccs26-circumvolve
    url: https://github.com/alizohaib/ccs26-circumvolve
    publisher: GitHub
  - title: Kkevsterrr/geneva
    url: https://github.com/Kkevsterrr/geneva
    publisher: GitHub
  - title: "obfsgen: a generative approach towards tunnel obfuscation"
    url: https://github.com/net4people/bbs/issues/684
    publisher: GitHub
    date: 2026-11-18
  - title: goose-lab-cuhk/obfsgen
    url: https://github.com/goose-lab-cuhk/obfsgen
    publisher: GitHub
authors:
  - anoni-net
---

When a censor switches to a new way of blocking, the ways around it are still mostly found by researchers working by hand. They analyse blocking incidents, guess at what triggers them, hand-craft an evasion and test it, a cycle that, according to the paper, often takes weeks or months. On 16 November the GFW Report website published CircumVolve, a paper for the ACM CCS 2026 security conference, in which researchers had a large language model (LLM) repeatedly rewrite circumvention programs and tested the results in a simulated environment and on networks in China, Iran, Pakistan and Kazakhstan. According to the paper, it is meant as a discovery tool for circumvention researchers and tool developers, and ordinary readers do not need to change any settings.

A circumvention strategy is a change to the way packets or a protocol are written, so that censorship equipment cannot match a connection to a blocked site while the server still responds normally. The researchers write each strategy as an executable Python program, have the LLM produce variants over and over, and keep the versions that test well for further rounds of changes. The process is built on OpenEvolve, an open-source framework for evolving programs, and in each round the LLM proposes changes based on the score, the packets decoded into text, and any error messages. A strategy scores highly only if it both evades the censor and gets a correct response from the destination server, which stops the LLM from taking shortcuts such as deleting the blocked domain.

Existing automated tools can also search for circumvention strategies, for example Geneva, published in 2019. As the paper describes them, these tools combine packet operations according to fixed rules and cannot change what is inside encrypted protocols such as TLS (the encryption protocol HTTPS uses) and QUIC (a newer transport protocol for the web). The LLM writes ordinary Python code, which can handle the encryption within the program and so change the contents of encrypted protocols.

On a real network, researchers only learn whether a bypass succeeded or failed. The simulated environment uses OpenGFW, open-source software that simulates a censor, in place of real censorship equipment, so the researchers can trace why a strategy works. Strategies were also tested on datacenter VPSs (rented virtual servers) under the researchers' own control in censored regions, across five protocols: DNS (the lookup that turns domain names into IP addresses), TCP/IP, HTTP, TLS and QUIC. Each protocol was tested in two or three of the countries, chosen by how each country actually blocks it, and all experiments in Iran were completed before the nationwide internet shutdown there on 28 February 2026.

The researchers used CircumVolve to find 47 distinct strategies across the five protocols, 27 of which are, to the authors' knowledge, not documented in earlier work. At least one bypass was found for every protocol tested in every country, but a strategy does not necessarily work everywhere, and the authors "did not expect any strategy to work universally". In runs that did find a bypass, the median LLM API cost before the first successful evasion was less than US$1. The limitations the authors acknowledge include using a single model, GPT-5.1, for all experiments, and rewriting only the first packet of a connection for QUIC and TLS.

## Perspective {#perspective}

In the ethics section, the authors argue that "censors must perfectly parse all protocols while evaders need only one overlooked edge case." With CircumVolve, the researchers hand the large number of attempts needed to find such edge cases to an LLM, which can adjust the next round of changes to how the censorship equipment responded. The authors suggest that some of the DNS strategies could be difficult to discover through fuzzing (testing with randomly varied inputs) alone.

The system relies on researchers who know censorship well to define the evaluation criteria and design the prompts, and automated deployment is listed in the paper as future work. Researchers who want to run it themselves have to supply their own VPS and LLM API keys. The authors also warn that testing sends malformed packets from the vantage point, so the testing activity itself may be recognised by the censor.

The authors have released the code, prompts and successful strategies, but as of 22 November the root of the CircumVolve repository had no license file, and only the bundled `openevolve/` directory is under Apache-2.0. The terms for other projects that want to reuse the rest of the code directly are unclear.

On 18 November another research team introduced obfsgen on net4people, a discussion forum hosted on GitHub. obfsgen also uses a generative model, in this case to reshape the packet sizes and timing of encrypted tunnel traffic so that it resembles ordinary traffic. It is released under the MIT license, and it is marked in its README as not yet ready for production use.

In the ethics section the authors acknowledge that publication "may help censors identify and mitigate discovered strategies before circumvention tools deploy them." They publish anyway because "well-resourced censors can independently identify these techniques", and because, according to earlier research the paper cites, censors take some time (for example several months) to bring new techniques into their production systems. Given the low cost the paper reports and the release of the code and prompts, our reading is that a censor could test its own equipment the same way without much difficulty.

China, Pakistan and Kazakhstan all block QUIC connections by SNI (the name of the site being requested, carried in the first message of a TLS or QUIC connection), though not all in the same way. China began decrypting and inspecting the SNI of QUIC connections at scale in April 2024, and there the offending packet is allowed through while the packets that follow are dropped, according to the paper. Kazakhstan and Pakistan are, in the paper's words, "both consumers of China's censorship equipment exports". In both countries the equipment sits in the path of traffic, drops the offending packet and keeps blocking the connection afterwards.

According to the paper, researchers uncover evasion techniques "that developers subsequently deploy in the wild", so users get the new strategies only after their circumvention tools are updated. Until then, readers who use circumvention tools do not need to change any settings. The study targets censorship equipment that matches standard protocols against rules, and it did not test fully encrypted protocols, where the whole connection looks like random data, or proprietary protocols.
