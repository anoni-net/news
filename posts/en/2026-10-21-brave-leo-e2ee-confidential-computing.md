---
title: End-to-end Encrypted Chats and Confidential Computing in Brave Leo
description: From 15 October, Brave's AI assistant Leo encrypts chats with the GLM 5.3 Flash model in the browser and decrypts them only inside hardware-isolated enclaves. Other models are not covered. As of 20 October, Brave's servers still check the enclaves' attestations for the browser, and we found no statement of iOS support.
date: 2026-10-21T00:00:00+08:00
slug: brave-leo-e2ee-confidential-computing
categories:
  - encryption
sources:
  - title: "Another Brave User-First AI Win: Leo adds End-to-end Encryption, Oblivious HTTP, and Verifiable Confidential Computing"
    url: https://brave.com/blog/browser-ai-e2ee/
    publisher: Brave
    date: 2026-10-15
  - title: near-tee-verifier
    url: https://github.com/brave/near-verifier
    publisher: GitHub
  - title: "[AI Chat] Add support for end-to-end encryption with NEAR models"
    url: https://github.com/brave/brave-browser/issues/55247
    publisher: GitHub
    date: 2026-05-05
  - title: What are the differences between Leo's AI Models?
    url: https://support.brave.app/hc/en-us/articles/26727364100493
    publisher: Brave
  - title: Brave Leo AI
    url: https://brave.com/leo/
    publisher: Brave
  - title: "Verifiable Privacy and Transparency: A new frontier for Brave AI privacy"
    url: https://brave.com/blog/browser-ai-tee/
    publisher: Brave
    date: 2025-11-20
  - title: GLM-5.3-Flash
    url: https://huggingface.co/zai-org/GLM-5.3-Flash
    publisher: Hugging Face
  - title: ai_chat_ui_strings.grdp
    url: https://github.com/brave/brave-core/blob/master/components/resources/ai_chat_ui_strings.grdp
    publisher: GitHub
  - title: brave_components_resources_zh-TW.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-TW.xtb
    publisher: GitHub
  - title: Brave adds end-to-end encryption to chats with AI assistant Leo
    url: https://cyberinsider.com/brave-adds-end-to-end-encryption-to-chats-with-ai-assistant-leo/
    publisher: CyberInsider
    date: 2026-10-16
  - title: "TEE.fail: Breaking Trusted Execution Environments via DDR5 Memory Bus Interposition"
    url: https://tee.fail/
    publisher: TEE.fail
  - title: Is https://brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/brave.com
    publisher: GreatFire
  - title: Is https://laptop-updates.brave.com blocked in mainland China?
    url: https://en.greatfire.org/https/laptop-updates.brave.com
    publisher: GreatFire
  - title: OONI API
    url: https://api.ooni.org/api/v1/measurements?probe_cc=CN&test_name=web_connectivity&domain=ai-chat.bsg.brave.com&since=2026-07-20&until=2026-10-20
    publisher: OONI
  - title: iTunes lookup API (cn)
    url: https://itunes.apple.com/lookup?id=1052879175&country=cn
    publisher: Apple
  - title: iTunes lookup API (tw)
    url: https://itunes.apple.com/lookup?id=1052879175&country=tw
    publisher: Apple
  - title: brave_components_resources_zh-CN.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_zh-CN.xtb
    publisher: GitHub
  - title: brave_components_resources_ja.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_ja.xtb
    publisher: GitHub
  - title: brave_components_resources_ko.xtb
    url: https://github.com/brave/brave-core/blob/master/components/resources/strings/brave_components_resources_ko.xtb
    publisher: GitHub
authors:
  - anoni-net
---

Brave announced on 15 October that chats between its AI assistant Leo and the GLM 5.3 Flash model are now end-to-end encrypted. GLM 5.3 Flash is a model whose weights Z.ai publishes under the MIT licence. Chats are encrypted in the browser and decrypted and answered only inside trusted execution environments (TEEs, compute areas in the processor and GPU isolated from the rest of the host) run by NEAR AI. The encryption applies only when you pick GLM 5.3 Flash by hand in Leo's model menu, Leo's other models are not covered, and as of 20 October GLM 5.3 Flash is still labelled as in testing.

According to the blog, the feature is available to all Brave users in the release version and in the Nightly and Beta test channels, but the blog does not say which platforms. The GitHub development issue is tagged only for desktop and Android, and as of 20 October we found no statement of support for the iPhone version.

According to Brave's blog, the browser encrypts each prompt, and any web page shared with Leo, with Oblivious HTTP (OHTTP), a standard from the Internet Engineering Task Force (IETF), and the decryption keys exist only inside the TEE. Encrypted messages go first to Brave's own AI Gateway and are then relayed to NEAR AI. Brave can see the user's IP address but not the content, NEAR AI's TEE decrypts the content without seeing the IP address, and according to the blog neither NEAR AI nor the cloud host operators can read inside the enclave. Each turn re-encrypts the whole conversation with a new one-time key, and the history stays only on the user's device, stored by neither Brave nor NEAR AI.

The blog then describes the checks before deployment, under which every NEAR AI deployment has to pass Brave's verifier before it is approved. The checks cover attestations signed by Intel and Nvidia (credentials signed by the hardware that prove the enclave is genuine and record which program runs inside it), and a rebuild from source to confirm it matches the program in production. The AI Gateway checks again before relaying each message, accepts verification results no more than an hour old, and does not relay anything that fails. The verifier, `near-tee-verifier`, is released under an open-source licence, and anyone with a NEAR AI API key can run it against the live service.

Brave trialled a first version in Nightly in November 2025, and according to the blog that protection rested on policy, with the checks also requiring trust in Brave. The new verifier is public and anyone with an API key can run it. As of 20 October, the browser-side check is still handled by Brave's servers.

As of 20 October, the help centre has no article on end-to-end encryption with GLM 5.3 Flash. Leo's model page still lists GLM 4.7 Flash and says all models are run by Brave itself. The development issue is marked to be left out of release notes, and none of the platforms' release notes mention end-to-end encryption.

## Perspective {#perspective}

A typical AI chat service decrypts prompts on its servers, so the operator can technically read them and users have to rely on the privacy policy. OHTTP splits "who is asking" from "what is asked" between two parties, so the relay knows only the IP address and the processor sees only the content. TEEs are designed so that even the host operator cannot read the enclave's memory, and attestation lets outsiders confirm that what runs inside is a published program. Brave's blog describes Leo's new approach as a move from policy promises to cryptographic proof.

According to the blog, at launch on 15 October the browser still relied on Brave's AI Gateway for the checks, with the browser to verify the hardware attestations directly in later stages. Also according to the blog, the whole chain ultimately rests on trust in Intel and Nvidia, dstack (the TEE's operating system), Sigstore for build records, GitHub, Hugging Face and public DNS. The `near-tee-verifier` documentation adds a caveat that a rebuild proves only that the live program comes from a specified version, not that the version has no backdoor. The inference software that runs the model is a third-party package, which according to the blog and the `near-tee-verifier` documentation is not rebuilt from source but pinned to a version through deployment records covered by the hardware attestation.

In TEE.fail, a paper accepted at the security conference IEEE S&P 2026, researchers attached an interposition device to a server's DDR5 memory bus and, in some cases, extracted the key that Intel TDX (the TEE technology on Intel processors) uses to sign attestations. Attestations forged with that key can pass verification, and the key can also be used to break confidential computing on Nvidia GPUs. According to the research site, the attack requires physical access to the server, and Intel does not count such physical attacks among the threats TDX is meant to defend against. The researchers also write that, to their knowledge, it has not been exploited in the wild.

Another section of the research site demonstrates against dstack that a malicious server provider can forge all the attestations and can also borrow attestations from Nvidia GPUs elsewhere. The site's advice to dstack users is to be aware that they have to trust the operator who actually manages the TDX hardware. The paper does not analyse the Brave and NEAR AI deployment, and when we searched on 20 October we found no independent analysis of Leo.

According to the `near-tee-verifier` documentation, the GPU attestation is not bound into the TDX attestation, so there is no way to confirm which GPU an answer came from. Closing that gap would need NEAR AI to add the binding between the two.

In mainland China, GreatFire's last test, on 18 October, found `brave.com` 100% blocked, with interference recorded since 13 May 2017, and its most recent valid test of `laptop-updates.brave.com`, used for downloads and updates, was also blocked. Leo's backend, `ai-chat.bsg.brave.com`, has no measurements, since OONI's public API holds no Web Connectivity measurement of it from China between 20 July and 20 October and GreatFire has not tested it, so we found no direct evidence on whether Leo is reachable there. Apple's iTunes lookup API returns no Brave listing in the mainland China App Store (we did not check Google Play), which is a lookup result rather than an announcement of removal by Brave or Apple.

The same lookup finds Brave 1.96 (6 October) in the Taiwan, Hong Kong, Japan, South Korea and Singapore App Stores. Brave's help centre has no clause restricting where Leo can be used and does not say whether Leo is offered in mainland China, and the Leo page says Leo is available on desktop and mobile. Brave's development branch already has strings for Leo's end-to-end encryption in Traditional Chinese, Simplified Chinese, Japanese and Korean, though translation files in the development branch do not mean the release version offers them.

People who want to use an AI chat for text or web pages they would rather the service provider not read can open Leo in Brave on desktop or Android and choose GLM 5.3 Flash from the model menu. According to the English strings in the source code's development branch, the model menu shows "Verifiably Private With NEAR AI TEE" next to GLM 5.3 Flash, and answers carry a "Verified" badge. Inferring from the source code and the blog, the badge reflects the result of Brave's server-side check, and as of 20 October the browser itself does not yet verify the attestations. Leo needs no account, and the help page mentions a usage limit on the free tier without giving a number.

Brave has not published which languages Leo's answers support, and the GLM 5.3 Flash model card on Hugging Face lists English and Chinese. According to the blog, the encryption covers only the chat content, and Brave, which relays the messages, can still see the IP address. Search queries generated by the model also leave the TEE and go to Brave Search (not tied to the IP address).
