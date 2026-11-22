---
title: Windows 11 诊断数据里的 coding agent 与开发工具记录
description: 一位研究者在一台 Windows 11 虚拟机上实测，系统组件会记录运行过哪些 coding agent 与哪几类开发工具，记录归在可选诊断数据并排进了上传队列。可选诊断数据可以在设置里关闭，必需诊断数据的清单另列有一条判断是否为开发者的分群事件，Microsoft 没说明它与上述记录的关系。
date: 2026-11-25T00:00:00+08:00
slug: windows-dev-tool-telemetry
categories: [tracking]
sources:
  - title: Windows 11 Is Collecting Data on Which Coding Agents and Developer Tools You Use
    url: https://xusheng.dev/posts/windows-coding-agent-telemetry/
    publisher: xusheng.dev
    date: 2026-11-16
  - title: Windows 11, versions 25H2 and 24H2 required diagnostic data events and fields
    url: https://learn.microsoft.com/en-us/windows/privacy/required-diagnostic-events-fields-windows-11-24h2
    publisher: Microsoft
  - title: Configure Windows diagnostic data in your organization
    url: https://learn.microsoft.com/en-us/windows/privacy/configure-windows-diagnostic-data-in-your-organization
    publisher: Microsoft
  - title: Diagnostics, feedback, and privacy in Windows
    url: https://support.microsoft.com/en-us/windows/diagnostics-feedback-and-privacy-in-windows-28808a2b-a31b-dd73-dcd3-4559a5199319
    publisher: Microsoft
  - title: Diagnostic Data Viewer
    url: https://learn.microsoft.com/en-us/windows/privacy/diagnostic-data-viewer-overview
    publisher: Microsoft
  - title: 診斷資料檢視器
    url: https://learn.microsoft.com/zh-tw/windows/privacy/diagnostic-data-viewer-overview
    publisher: Microsoft
  - title: For real Windows 10 privacy, you need the China Government Edition
    url: https://www.computerworld.com/article/3200375/microsoft-windows/for-real-windows-10-privacy-you-need-the-china-government-edition.html
    publisher: Computerworld
    date: 2017-06-12
authors:
  - anoni-net
---

Windows 11 的诊断数据除了崩溃记录与硬件信息，还可能包括用户运行过哪些 coding agent（替用户编写、修改代码的 AI 工具）与开发工具。一位研究者 11 月 16 日在个人博客发表逆向工程（拆解程序、还原它如何运作）与实测的结果，在一个系统组件里找到 `codex.exe`、`claude.exe`、`copilot.exe`、`cursor.exe` 等 coding agent，以及 `python.exe`、`gcc.exe` 等开发工具的可执行文件名称。组件比对程序运行时的文件名，读者可以从自己平常运行哪些程序判断是否相关。coding agent 的检查只在研究者自己的一台虚拟机上实测，其他计算机是否开启，他没有验证。

依研究者的分析，名为 `MissionControlAggregator` 的组件读取 Windows 原本就有的程序启动记录，比对成功就在一组位图（bitmap，每个位置只记有或没有）里标记。coding agent 逐一记录，开发工具只记到类别，例如 GCC 与 Clang 属于同一类。研究者的判读是，来源记录里的运行时间与交互次数看起来没有被保留。他没有在事件里找到提示词或源代码，但认为光是记录一个人用哪些工具，就有明显的隐私影响。

Windows 的诊断数据分成必需与可选两级，依 Microsoft 的支持页，用户第一次设置 Windows 时可以选择是否发送可选诊断数据。研究者另外用最新的官方镜像文件全新安装一台美国区域设置的 Windows 11 Home，在改任何隐私设置之前，可选数据的开关已经是开启的。新装的那台只用来看开关的默认值，他没有检查它是否启用 coding agent 的记录。

coding agent 的检查在研究者的虚拟机上已经启用，他没有手动开启。在允许可选数据的设置下，他在 Windows 的上传队列（等待发出的诊断数据暂存区）里找到工具使用的记录，记录标为可选数据。原文的结论是数据会上传到 Microsoft，他列出的证据到排进上传队列为止，没有实际发出的连接记录。

## 导读观点 {#perspective}

Microsoft 给组织的设置说明里，可选诊断数据包括应用程序的使用情况，例如启动了哪些程序、运行多久。同一份说明把完全不发送诊断数据的选项只开放给 Windows Server、Enterprise 与 Education，照这份说明整理，Home 与 Pro 的用户无法关闭必需数据。Microsoft 公开的必需诊断数据清单里，另列有一条依应用程序的使用情况、回报用户是否为开发者（IsDeveloper）的分群事件 `Segments.Cohorts`，跟研究者抓到、归在可选数据的记录是不同的事件。Microsoft 没有写判定方式，也没有说明两者是否相关。

在中国大陆，Windows 10 在 2017 年有过一个与中国电子科技集团（CETC）合作的中国政府版（Windows 10 China Government Edition）。依 Computerworld 引述的 Microsoft 博客，这个版本利用可管理性功能移除政府雇员不需要的功能（例如 OneDrive），也让政府在自己的计算机系统里使用自有的加密算法。同一句话还写到“manage all telemetry and updates”，研究者的实测也没有在中国版或政府版上进行。

想确认自己的计算机发出哪些诊断数据的人，可以从 Microsoft Store 安装诊断数据查看器（Diagnostic Data Viewer），再到“Settings > Privacy & security > Diagnostics & feedback”打开 Diagnostic Data Viewer（诊断数据查看器）的开关。开启之后 Windows 会把诊断数据存在本机、直到关闭为止，默认最多占用系统磁盘 1 GB，说明页上的建议因此是看完就关闭。说明页上也写了，开启后要照常使用几天再回来看，查看器列出的事件也不一定已经上传。研究者抓到的工具使用记录是否会列在查看器里，到 11 月 22 日还没有人公开验证。

平常在 Windows 11 运行开发工具或 coding agent、不想让工具记录成为诊断数据一部分的人，可以关闭“Diagnostic data”底下的 Send optional diagnostic data 开关。开关在同一个设置页，新安装时也可以在设置流程中拒绝，区域设置不是美国的读者可以直接到设置页看开关目前的状态。

研究者抓到的记录标为可选，依这个标记，关闭之后它应该不会再排进上传队列。Microsoft 的支持页写到，不发送可选数据的设备一样安全，也会正常运作。原文没有做关闭可选数据之后的对照实验，Microsoft 的公开页面也没有写工具使用记录的用途。
