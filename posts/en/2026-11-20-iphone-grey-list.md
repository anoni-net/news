---
title: Phrases excluded from iPhone keyboard suggestions and swipe typing
description: An independent researcher recovered a phrase list Apple has not disclosed from the keyboard data in iOS 27.0, with 4,513 English entries and lists for 27 other languages and scripts. Listed phrases do not appear in predictive text and most cannot be swipe-typed, while typing letter by letter is unaffected. Apple's reply to Reuters said the keyboard is set up to avoid suggestions that might be inappropriate or offensive, and as of 15 November its support page offers no setting to turn the list off.
date: 2026-11-20T00:05:00+08:00
slug: iphone-grey-list
categories:
  - mobile
sources:
  - title: 如何在 iPhone、iPad 或 iPod touch 上使用「自動修正」和預測字詞
    url: https://support.apple.com/zh-tw/104995
    publisher: Apple
    date: 2026-04-13
  - title: 在 iPhone 上設定常用文字的縮寫
    url: https://support.apple.com/zh-tw/guide/iphone/iph6d01d862/ios
    publisher: Apple
  - title: "Apple’s predictive text restrictions include ‘Dictator Trump’ and ‘Sleepy Joe,’ researcher finds: Reuters exclusive"
    url: https://www.cp24.com/news/world/2026/11/06/apples-predictive-text-restrictions-include-dictator-trump-and-sleepy-joe-researcher-finds-reuters-exclusive/
    publisher: Reuters (via CP24)
    date: 2026-11-06
  - title: "Swipeblocked: the phrases your iPhone won't suggest"
    url: https://swipeblocked.com/
    publisher: Swipeblocked
  - title: How to use Auto-Correction and predictive text on your iPhone, iPad, or iPod touch
    url: https://support.apple.com/en-us/104995
    publisher: Apple
    date: 2026-03-30
  - title: Set up shorthand for frequently used text on iPhone
    url: https://support.apple.com/guide/iphone/use-shorthand-for-frequently-used-text-iph6d01d862/ios
    publisher: Apple
  - title: "Revealed: Apple's secret list of slurs, insults, and political phrases that can't be swiped"
    url: https://macworld.com/article/3279221/revealed-apples-secret-list-of-slurs-insults-and-political-phrases-that-cant-be-swiped.html
    publisher: Macworld
    date: 2026-11-07
  - title: "Engrave Danger: An Analysis of Apple Engraving Censorship across Six Regions"
    url: https://citizenlab.ca/2021/08/engrave-danger-an-analysis-of-apple-engraving-censorship-across-six-regions/
    publisher: Citizen Lab
    date: 2021-08-18
  - title: "Engrave Condition: Apple’s Political Censorship Leaves Taiwan, Remains in Hong Kong"
    url: https://citizenlab.ca/2022/03/engrave-condition-apples-political-censorship-leaves-taiwan-remains-in-hong-kong/
    publisher: Citizen Lab
    date: 2022-03-22
authors:
  - anoni-net
---

According to a Reuters exclusive on 6 November, an independent researcher found that the iPhone's built-in keyboard carries a list of phrases Apple has not disclosed. Phrases on the list do not appear in predictive text (the next-word suggestions the keyboard shows during typing), and most cannot be produced by swipe typing (entering a word by sliding a finger across the letters). Typing letter by letter is unaffected, and nothing on the list stops anyone from writing a word. The lists are kept per language, and the researcher's site says Apple keeps similar lists for 27 other languages and scripts, giving a few examples.

The researcher told Reuters that in September he noticed swipe typing stumbling over "white man" but not "black man". With the help of AI coding tools he traced the behaviour to data stored deep in the operating system, and he put a conservative estimate at about 100,000 words and phrases, not including Chinese characters. According to Reuters, an engineer at a security company said he had independently recovered the same list and got "a near-perfect match". Swipeblocked, the site where the researcher publishes the list, has 4,513 English entries and says many of the other languages' lists are as long as the English one.

The researcher told Reuters that the entries are overwhelmingly vulgar, offensive or related to drugs, sex or violence. According to Reuters, other phrases are "politically salient", and Swipeblocked's examples include "Tibetan independence", "United Ireland", "Kashmir dispute", "sleepy Joe" and "make America great again". "Taiwan is country" is also on the list, and the site notes that only this wording is blocked, while "Taiwan is a country" is not. Some pairs are blocked on one side only, so "read gay smut" is blocked and "read smut" is not.

According to Swipeblocked's explanation, predictive text never offers a phrase on the list, "even when it's the obvious next word". Swipe typing won't produce most of them either: the keyboard picks another word, sometimes an implausible one, and can change a word already entered. In the site's demonstration, swiping "conspiracy" after "left wing" turns "wing" into "wrong". The rules match exact word sequences, so a slightly different wording can get through.

Reuters tested a small subset of the researcher's phrases on an iPhone and found they were all difficult to swipe-type or were not suggested via autocomplete. Swipe-typing "United Ireland" often yielded "United Iceland", and "Sleepy Joe" yielded "Sleepy hope". "Dictator Trump" could be swipe-typed but was not suggested, and Swipeblocked likewise lists it among the phrases kept out of suggestions that can still be swiped.

According to Swipeblocked's changes page, the English list grew from about 1,700 phrases in iOS 14.0 in 2020 to 4,513 in iOS 27.0. Apple updates it with new versions of iOS and, in between, through language data the iPhone downloads in the background. "Dictator Trump" was added in iOS 16.1, while "President Trump" and "President Bush", blocked since a 2022 update, were removed in iOS 26.3. The only addition in iOS 27.0 was "Zionist propaganda".

In an email to Reuters, Apple did not comment directly on the findings, including the size or composition of the list or its reasons for flagging certain political terms. Apple's reply said that iPhone users have always been able to type specific words or phrases and override any predictive suggestion, and that the keyboard is set up to avoid offering suggestions that "might be inappropriate or offensive".

## Perspective {#perspective}

Swipeblocked's technical write-up says that before the keyboard offers a candidate, the two to six words it would complete are checked against the list. The list stores only a 32-bit fingerprint of each phrase rather than its text, and the researcher recovered the contents by generating candidate phrases and checking each one against Apple's table. Fingerprint matching also produces false hits, with 176 meaningless strings in the iOS 27.0 English list matching by coincidence, and on an iPhone these are blocked just like real phrases. The site also notes that parts of the list could not be decoded, and that a phrase's presence "says nothing about why Apple added it".

Based on the keyboard code in iOS 26.3, Swipeblocked also describes a separate set of labels on single words. Words labelled vulgar are not suggested until the user has typed them three times, and words labelled offensive are never suggested.

Macworld's editor writes that "This isn't a censorship list", because typing individual characters always works, though it can slow down anyone relying on swiping or suggestions to type faster. The researcher described it to Reuters as "a very light-touch form of censorship", adding that "at the scale that Apple is operating, it only takes a light touch to have a big impact." The Reuters report states that the list is not a ban, and that because hundreds of millions of people worldwide use iPhones, Apple's choices about which words its keyboard suggests "could quietly shape how they communicate".

On disclosure and customisation, a senior counsel at the Electronic Frontier Foundation (EFF, a digital civil liberties group) told Reuters that if Apple is going to do this, "this is something users should be really well aware of and have some ability to customize", and that it "should not be secret". Macworld's editor still calls Apple's approach "overreaching" and suggests a keyboard setting that is on by default but can be turned off. Apple's reply as reported by Reuters says nothing about disclosure or settings, and as of 15 November the keyboard page on Apple's support site has no such option. The same EFF lawyer said that while a part of him found the list "creepy" and he wondered about Apple's judgment calls, he could see an argument for it as a way to curb unwanted or inflammatory suggestions.

On what goes on the list, the researcher told Reuters it was understandable that Apple wanted to keep users from accidentally sending obscene messages or inflammatory slogans. He also said there were inconsistencies in how Apple applied it, pointing to "read gay smut" and "read smut". Macworld's editor suggests that Apple's motive is "likely less about policing your speech than it is about avoiding lawsuits and bad PR".

According to Swipeblocked, words on the Chinese list still appear as candidates when typed in pinyin, but once one is picked the keyboard stops suggesting the next word. The site's Chinese examples include 六四 (June Fourth, the 1989 Tiananmen crackdown), 台独 (Taiwan independence), 刘晓波 (Liu Xiaobo) and 习大大 (a nickname for Xi Jinping); the name of the Kuomintang (KMT) is blocked in both the Simplified and Traditional Chinese lists, while the name of China's Communist Party is blocked only in the Traditional Chinese one. In one part of the Chinese typing engine, Apple's code also skips suggestions whenever a word is "taiwan" or "tibet" written in English. The site's explanation does not cover input methods other than pinyin, such as Zhuyin (Bopomofo).

Citizen Lab, a research lab at the University of Toronto, analysed Apple's filtering of product engravings in six regions in 2021 and found 1,105 keyword filtering rules. It concluded that "part of Apple's mainland China political censorship bleeds into both Hong Kong and Taiwan", and that it was "aware of no legal justification for the political censorship of content in Taiwan". A 2022 follow-up found that Apple had eliminated its Chinese political censorship in Taiwan but continued broad, keyword-based political censorship in Hong Kong. Engraving filters refuse a custom order depending on the region of sale, a different mechanism from the keyboard list, which only affects suggestions and swipe typing; Swipeblocked decoded that list by language and did not compare iPhones set to different countries or regions.

On the iPhone's built-in keyboard, typing letter by letter is unaffected by the list. People who swipe-type may want to reread a message before sending it, since the keyboard can change an earlier word (our suggestion, based on Swipeblocked's demonstration). According to the keyboard page on Apple's support site, Predictive Text can be turned off under Settings > General > Keyboard. As of 15 November the page offers no setting to turn off the list, and does not say whether swipe typing still changes words once Predictive Text is off.

The same page describes Text Replacement, which lets users set shortcuts that automatically become longer words or phrases. The iPhone User Guide adds that filling in only the Phrase field and leaving the Shortcut field blank keeps a word or phrase the user types from being replaced. Neither page says whether either method brings listed phrases back into suggestions or swipe typing, and we have not tested it. For writing a phrase on the list, the method Swipeblocked confirms is typing letter by letter, and Macworld's editor gives the cost as slower typing.
