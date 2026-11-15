---
title: iPhone 键盘建议与滑动输入排除的词组清单
description: 一位独立研究者从 iOS 27.0 的键盘数据还原出 Apple 未公开的词组清单，英文有 4,513 条，另有 27 种语言与文字的清单。清单上的词组不会出现在预测建议，多数也无法用滑动输入打出，逐字输入不受影响。Apple 回复 Reuters 时表示键盘的设计是避免提供可能不当或冒犯的建议，到 11 月 15 日为止，说明页没有关闭这份清单的设置。
date: 2026-11-20T00:05:00+08:00
slug: iphone-grey-list
categories:
  - mobile
sources:
  - title: "Apple’s predictive text restrictions include ‘Dictator Trump’ and ‘Sleepy Joe,’ researcher finds: Reuters exclusive"
    url: https://www.cp24.com/news/world/2026/11/06/apples-predictive-text-restrictions-include-dictator-trump-and-sleepy-joe-researcher-finds-reuters-exclusive/
    publisher: Reuters（CP24 转载）
    date: 2026-11-06
  - title: "Swipeblocked: the phrases your iPhone won't suggest"
    url: https://swipeblocked.com/
    publisher: Swipeblocked
  - title: 如何在 iPhone、iPad 或 iPod touch 上使用「自動修正」和預測字詞
    url: https://support.apple.com/zh-tw/104995
    publisher: Apple
    date: 2026-04-13
  - title: 如何在 iPhone、iPad 或 iPod touch 上使用自动改正和预测文本功能
    url: https://support.apple.com/zh-cn/104995
    publisher: Apple
    date: 2026-04-13
  - title: 在 iPhone 上为常用文本设置简写
    url: https://support.apple.com/zh-cn/guide/iphone/iph6d01d862/ios
    publisher: Apple
  - title: 在 iPhone 上設定常用文字的縮寫
    url: https://support.apple.com/zh-tw/guide/iphone/iph6d01d862/ios
    publisher: Apple
  - title: "Revealed: Apple's secret list of slurs, insults, and political phrases that can't be swiped"
    url: https://macworld.com/article/3279221/revealed-apples-secret-list-of-slurs-insults-and-political-phrases-that-cant-be-swiped.html
    publisher: Macworld
    date: 2026-11-07
  - title: "Engrave Danger: An Analysis of Apple Engraving Censorship across Six Regions"
    url: https://citizenlab.ca/2021/08/engrave-danger-an-analysis-of-apple-engraving-censorship-across-six-regions/
    publisher: Citizen Lab
    date: 2021-08-18
  - title: "Engrave Condition: Apple's Political Censorship Leaves Taiwan, Remains in Hong Kong"
    url: https://citizenlab.ca/2022/03/engrave-condition-apples-political-censorship-leaves-taiwan-remains-in-hong-kong/
    publisher: Citizen Lab
    date: 2022-03-22
authors:
  - anoni-net
---

依 Reuters 11 月 6 日的独家报道，一位独立研究者发现 iPhone 内置键盘带着一份 Apple 没有公开的词组清单。列在清单上的词组不会出现在预测文本（predictive text，打字时键盘列出的下一个字词建议）里，多数也无法用滑动输入（手指在键盘上连续滑过字母来打字）打出来。一个字母一个字母输入时不受影响，清单不会阻止用户写出任何字。清单按语言区分，研究者的网站写到 Apple 另有 27 种语言与文字的类似清单，并各举了少数例子。

研究者对 Reuters 表示，他 9 月注意到滑动输入打「white man」时打不顺，打「black man」不会。他借助 AI 编程工具在操作系统深处找到这份数据，保守估计各语言合计约 10 万个词与词组（不含汉字）。依 Reuters，一家信息安全公司的工程师表示另外独立还原出同一份清单，比对结果几乎完全吻合。研究者整理的 Swipeblocked 网站列出英文清单 4,513 条，网站也写到其他语言的清单不少跟英文的一样长。

研究者对 Reuters 表示，清单上绝大多数是粗俗、冒犯或跟毒品、性、暴力相关的词组。Reuters 另外写到其中也有政治上敏感的词组，Swipeblocked 列出的例子包括「Tibetan independence」、「United Ireland」、「Kashmir dispute」、「sleepy Joe」与「make America great again」。「Taiwan is country」也在清单上，网站注明只挡这个写法，「Taiwan is a country」不挡。清单也有成对却只挡一边的例子，「read gay smut」被挡，「read smut」不挡。

根据 Swipeblocked 的说明，预测文本从不提供清单上的词组，即使那是最明显的下一个词。多数词组也无法用滑动输入打出，键盘会改选别的字，有时选得不合常理。键盘还可能改掉前一个已经输入的字，例如网站演示滑出「left wing conspiracy」的 conspiracy 时，前面的 wing 会变成 wrong。比对只认完全相同的词序，换个说法就可能通过。

Reuters 在 iPhone 上试了研究者列出的一小部分词组，全部都难以滑动输入，或不会出现在建议里。滑动输入「United Ireland」常变成「United Iceland」，「Sleepy Joe」变成「Sleepy hope」。「Dictator Trump」可以滑动输入，但不会出现在建议里，Swipeblocked 也把它列为只排除建议、仍可滑动输入的词组。

依 Swipeblocked 的变更页，英文清单在 2020 年的 iOS 14.0 约有 1,700 条，到 iOS 27.0 增加到 4,513 条。Apple 会随 iOS 新版更新清单，两版之间也通过 iPhone 在后台下载的语言数据更新。「dictator Trump」在 iOS 16.1 加入，「President Trump」与「President Bush」从 2022 年的一次更新起被挡，在 iOS 26.3 移除。iOS 27.0 唯一新增的是「Zionist propaganda」。

Apple 在给 Reuters 的电子邮件里没有直接回应研究者的发现，包括清单的规模、组成，以及收入特定政治词的理由。Apple 的回复提到用户一向可以自行输入特定的字词，也可以略过任何预测建议，键盘的设计是避免提供可能不当或冒犯的建议。

## 导读观点 {#perspective}

依 Swipeblocked 的技术说明，键盘列出候选字之前，会以要补全的两到六个词比对清单。清单只存每组词算出来的 32 位指纹，研究者逐一生成候选词组来比对，才还原出内容。指纹比对也会误判，iOS 27.0 的英文清单有 176 组无意义的字符串刚好吻合，在 iPhone 上一样被挡。网站也注明清单有解不出来的部分，词组列在清单上也不代表知道 Apple 收入的理由。

依 iOS 26.3 的键盘代码，Swipeblocked 另外写到一套独立的单字标签。标为粗俗的字要用户自行输入三次才会出现在建议，标为冒犯的字从不建议。

Macworld 的编辑认为清单不算审查清单，因为逐字输入一定可以，只是想靠滑动或建议打快一点的人会慢下来。研究者对 Reuters 形容这是非常轻度的审查，他认为以 Apple 的规模，轻轻一碰就有很大的影响。Reuters 的报道写明清单不是禁令。报道也写到全球有数亿人使用 iPhone，Apple 选择让键盘建议哪些字，可能悄悄影响他们沟通的方式。

公开与自定义方面，Reuters 引述的 EFF 资深律师认为 Apple 要这么做就应该让用户清楚知道并能够自定义，不该是秘密。Macworld 的编辑仍认为 Apple 管得太多，建议加一个默认开启、可以关闭的设置。Reuters 转述的 Apple 回复里没有提到公开或设置，Apple 支持网站的键盘说明页到 11 月 15 日为止也没有这样的选项。同一位 EFF 律师虽然有一部分觉得清单令人不安、对 Apple 的取舍有疑问，也看得出有理由把它当成减少不想要或煽动性建议的方法。

收录的标准方面，研究者对 Reuters 表示可以理解 Apple 不想让用户误传不雅信息或煽动性的口号。他也认为套用得不一致，例如「read gay smut」与「read smut」的差别。Macworld 的编辑推测 Apple 比较可能是想避免官司与公关风波。

依 Swipeblocked 的说明，中文清单上的词在拼音输入时仍会出现在候选字里，选了之后键盘就不再预测下一个词。网站列出的中文例子有「六四」、「台独」、「刘晓波」与「习大大」，中国共产党的名称在简体中文的清单不挡、在繁体中文的清单挡，国民党则两份都挡。中文输入引擎有一部分的代码，在词为英文的「taiwan」或「tibet」时不提供建议。网站只按语言列出清单，没有比较不同国家或地区设置的 iPhone，说明也没有提到五笔等拼音以外的输入方式。

Citizen Lab 另有 Apple 产品雕刻的地区性关键词过滤研究，命中时直接拒绝定制，跟只排除建议与滑动输入、逐字输入不受限的键盘清单不同。该机构 2021 年 8 月分析了六个地区，找到 1,105 条关键词过滤规则，并发现中国大陆的部分政治审查延伸到香港与台湾。2022 年 3 月的后续报告写到 Apple 已移除台湾的这类过滤，香港仍有大范围的关键词政治过滤。键盘清单是否依地区而不同，Swipeblocked 没有比较过。

用 iPhone 内置键盘的人，逐字输入不受清单影响。习惯滑动输入的人送出前可以回头看一遍，键盘可能已经改掉前一个字（本文依 Swipeblocked 的演示提出的建议）。依 Apple 支持网站的键盘说明页，「预测文本」可以在「设置 > 通用 > 键盘」关闭。说明页到 11 月 15 日为止没有关闭清单的设置，也没有写关掉「预测文本」之后滑动输入是否仍会改字。

同一页键盘说明另有「自定义短语」，可以设置输入码，输入码打出后自动换成一整个词组。iPhone 使用手册也写到「输入码」栏位留白、只填字词，能让自己常用的字词不被替换。这两种做法能否让清单上的词组回到建议或滑动输入，两份说明都没有写，我们也没有实测。想打出清单上的词组，Swipeblocked 确认可行的方式是逐字输入，Macworld 提到代价是打字变慢。
