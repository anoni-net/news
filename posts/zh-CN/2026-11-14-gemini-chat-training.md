---
title: Gemini 个人账号对话用于模型训练的范围与关闭方式
description: 年满 18 岁的 Gemini 个人账号默认开启“保留活动记录”（Keep Activity），开启时 Google 会用活动记录训练生成式 AI 模型，部分对话经人工审查（依 Google 说明页，11 月 8 日查阅）。关闭设置或改用临时对话（Temporary Chat）后，对话不用于训练（关闭设置时提供意见反馈例外），保留 72 小时。经人工审查的对话最多保留三年。说明页没有区分付费与免费方案。
date: 2026-11-14T00:05:00+08:00
slug: gemini-chat-training
categories:
  - tracking
sources:
  - title: Gemini Apps Privacy Hub
    url: https://support.google.com/gemini/answer/13594961?hl=en
    publisher: Google
    date: 2026-10-26
  - title: Gemini 系列應用程式隱私權專區
    url: https://support.google.com/gemini/answer/13594961?hl=zh-Hant
    publisher: Google
    date: 2026-10-26
  - title: 管理及刪除 Gemini 系列應用程式活動記錄
    url: https://support.google.com/gemini/answer/13278892?hl=zh-Hant
    publisher: Google
  - title: 使用 Gemini 系列應用程式
    url: https://support.google.com/gemini/answer/13275745?hl=zh-Hant
    publisher: Google
  - title: 關於透過「連結的應用程式」享有的個人化體驗
    url: https://support.google.com/gemini/answer/16836988?hl=zh-Hant
    publisher: Google
  - title: 在 Gemini 系列應用程式中使用 Gem
    url: https://support.google.com/gemini/answer/15146780?hl=zh-Hant
    publisher: Google
  - title: 和 Gemini Live 自然對話
    url: https://support.google.com/gemini/answer/15274899?hl=zh-Hant
    publisher: Google
  - title: Generative AI in Google Workspace Privacy Hub
    url: https://support.google.com/a/answer/15706919?hl=en
    publisher: Google
    date: 2026-10-06
  - title: "Tell HN: Gemini trains on chat history, even for subscribers (personal accounts)"
    url: https://news.ycombinator.com/item?id=50363461
    publisher: Hacker News
    date: 2026-11-04
  - title: Where you can use the Gemini web app
    url: https://support.google.com/gemini/answer/13575153?hl=en
    publisher: Google
  - title: Gemini mobile app availability
    url: https://support.google.com/gemini/answer/14579026?hl=en
    publisher: Google
  - title: 中华人民共和国个人信息保护法
    url: http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html
    publisher: 中国人大网
    date: 2021-08-20
  - title: 生成式人工智能服务管理暂行办法
    url: https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm
    publisher: 中国网信网
    date: 2023-07-13
authors:
  - anoni-net
---

年满 18 岁的用户登录个人 Google 账号使用 Gemini 时，“保留活动记录”（Keep Activity）设置默认为开启。开启期间，Google 会用活动记录改进服务与训练生成式 AI 模型，其中一部分对话会经过人工审查。默认值写在“管理及删除活动记录”说明页，用途写在 Gemini 帮助中心的隐私权专区（本文于 11 月 8 日查阅），工作或学校账号可能适用其他条款。11 月 4 日一则 Hacker News 帖子提到付费订阅者的对话同样会用于训练并引起讨论，下文的规则出自 Google 的现行文件，推论处另行标明。

依隐私权专区（隐私权声明 2026 年 10 月 13 日版、问答 10 月 26 日版），Google 列出的活动记录用途是提供、开发及改进服务（包括训练生成式 AI 模型），以及保护 Google、用户和一般大众。同一页提到系统不会使用 Gemini 对话作为展示广告的依据（日后调整会提供清楚说明），Google 也不会出售个人信息。

设置开启时，对话、上传的文件与共享的屏幕画面都会存进活动记录，关联应用（Connected Apps，让 Gemini 调用其他 Google 应用与第三方服务数据的功能）的数据与从其他 AI 平台导入的对话同样用于改进服务。活动记录默认 18 个月后自动删除，可以改成 3 个月、36 个月或不自动删除。音频、Gemini Live（以语音与 Gemini 自然对话的功能）的视频与屏幕共享默认不用于改进服务，需要另外勾选，Live 对话的转录稿与分享给 Live 的上传内容则在“保留活动记录”开启时用于改进服务。

隐私权专区提到 Google AI 方案（Google 的付费订阅方案）时，只把订阅相关信息列为收集项目，训练与人工审查的段落没有区分付费与免费。本文据此推论两者适用同一份声明，Google 没有明文写出这句话，到 11 月 8 日也查不到 Google AI 方案专属的隐私文件。

工作与学校账号的活动记录设置由 Google Workspace 管理员控制，适用的规则可能不同。Workspace 的生成式 AI 隐私权专区（10 月 6 日版）只适用符合资格的 Workspace 版本，未经 Workspace 客户（订阅的组织）事先许可或指示，客户数据不会用于训练模型。这些版本的 Gemini 应用里，对话与上传文件未经许可不会在组织域之外由人工审查，也不用于训练生成式 AI 模型。

依隐私权专区，人工审查员会评估回复是否质量低下、不准确或有害，并提出更好的回复。对话也会为了维护安全、处理违反服务条款的行为而接受审查。页面只写“部分对话”，没有公布比例。

对话送交受过专业训练的服务提供商审查之前，会先解除与账号的关联。审查过的对话与相关数据（例如使用语言、设备类型、位置信息）最多保留三年，页面没有区分审查原因，用户删除活动记录时也不会一并删除。本文据此推论，关闭设置后为保护用途审查过的对话，保留时间也可能超过 72 小时。用户在对话里写下的姓名或地址仍在文字之中，这也是本文的推论。

## 导读观点 {#perspective}

维持开启时，一般对话默认保留 18 个月，用于训练并有部分经人工审查。关闭“保留活动记录”后，日后的对话除提供意见反馈的情况外不用于训练、不经改进服务的人工审查，保留 72 小时。临时对话（Temporary Chat，逐次使用、不显示在活动记录与近期对话、离开后无法再访问的对话模式）同样保留 72 小时，不用于训练，也不经改进服务的人工审查。三种做法都不影响为保护 Google、用户和一般大众而处理对话（“过程中可能会借助人工审查”），审查过的对话最多保留三年，Gemini 设置也无法控制把对话处理成去标识化数据、借以改进 Google 服务的流程。

“保留活动记录”同时控制对话的存储与模型训练，查阅的说明页没有列出只保留对话、不用于训练的选项。隐私权专区的句子只涵盖日后的对话，没有提到关闭之前已存进活动记录的对话（包括已用于训练的数据）之后如何处理。关闭之后的短期保留，隐私权专区列出的用途是回复用户、处理意见反馈与保护 Google、用户和一般大众，举的例子是系统发生故障时数据可以访问。

隐私权专区写到 Gemini 设置无法控制去标识化处理，也写到关闭设置且不提供意见反馈时，日后的对话不会用于改进 AI 模型。两句的关系页面没有说明。

设置关闭时提交意见反馈，Google 会收集反馈内容、过去 24 小时内的对话，以及对话里的上传项目与关联应用的数据。反馈与相关对话会交由受过训练的团队审查，并依 Google 隐私权政策用于改进产品与机器学习技术。

依设置说明页，关闭之后可用的关联应用有设备小帮手（device assistant）、Gemini Notebook（存放笔记本来源文件的服务）、Google 信息（Google Messages）、电话与 WhatsApp。以 Gem（用户创建并保存、用来获得符合特定需求回复的自定义项目）创建的对话不会保留，Gem 本身留在账号里。关闭期间的对话事后无法在活动记录查阅。

不想关闭设置的人可以逐次使用临时对话。Google Messages 与 Chrome 里的 Gemini 没有这项功能，工作与学校账号也不能用。对话中无法使用 Gem、需要开启“保留活动记录”的关联应用与个性化回复，也无法提供意见反馈。

对话能否用于训练，牵涉用户对自己数据的控制与产品改进两种考量。Google 在隐私权专区的说明是审查员的建议会用来改善模型日后的回复，并请用户不要输入不想让审查员看到、或不愿供 Google 改进服务的机密信息。到 11 月 8 日，查不到 Google 对 Hacker News 帖子的公开回应，也查不到消费者团体或数据保护机构针对 Gemini 个人对话训练的正式文件。本文呈现的只有 Google 这一方的文件。

Gemini 网页版的服务地区清单里，中国大陆标注为“仅限 Workspace”，移动 App 的清单不含中国大陆（11 月 8 日查阅，说明页没有标日期）。隐私权专区说明的是个人账号的 Gemini 应用，个人账号的说明如何适用于大陆境内，本文没有查到 Google 的说明。中国大陆《个人信息保护法》第十三条把取得个人同意列为处理个人信息的合法情形之一，第四十四条赋予个人限制或拒绝他人处理其个人信息的权利。《生成式人工智能服务管理暂行办法》第七条要求涉及个人信息的训练数据取得个人同意或符合法律、行政法规规定的其他情形，依第二条第三款该办法只适用于向境内公众提供的服务，这些条文是否涵盖 Gemini 个人账号的对话本文没有查到解释。

电脑版的路径是在 `gemini.google.com` 依次点按“设置与帮助”（Settings & help）、“活动记录”（Activity），再到画面上方点“开启”，选“关闭”或“关闭并删除活动记录”（Turn off and delete activity，名称依正体中文界面转写，简体界面用字可能不同，说明页有移动 App 的步骤）。依隐私权专区的规则推论，不希望对话用于训练的人可以关闭设置或每次改用临时对话。需要长期保留对话、或在个人账号关联 Google Workspace 这类应用的人可以维持开启，敏感内容改用临时对话。机密内容能否输入，需要依各种做法留下的保留期与审查范围自行评估。
