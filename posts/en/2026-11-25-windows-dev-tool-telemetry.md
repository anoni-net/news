---
title: Coding agent and developer tool records in Windows 11 diagnostic data
description: Testing on a Windows 11 virtual machine, a researcher found that a system component records which coding agents and which kinds of developer tools have been run, and that the record is classed as optional diagnostic data and placed in the upload queue. Optional diagnostic data can be turned off in Settings. Microsoft's list of required diagnostic data separately includes a cohort event that reports whether a user is a developer, and Microsoft has not explained how it relates to these records.
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

Besides crash reports and hardware details, Windows 11 diagnostic data may also include which coding agents (AI tools that write and edit code for the user) and developer tools a person has run. In a post on his personal blog, a researcher used reverse engineering (taking a program apart to work out how it functions) and testing to show that one system component contains the executable names of coding agents such as `codex.exe`, `claude.exe`, `copilot.exe` and `cursor.exe`, and of developer tools such as `python.exe` and `gcc.exe`. The component matches the file name of a program when it runs, so readers can judge from the programs they normally run whether this concerns them. He tested the coding agent check on only one virtual machine of his own, and did not verify whether it is switched on for other computers.

According to the analysis he published on 16 November, a component called `MissionControlAggregator` reads the program launch records that Windows already keeps, and when a name matches, it sets a mark in a bitmap (a row of positions, each holding only yes or no). Coding agents are recorded one by one, while developer tools are recorded only by category, so GCC and Clang, for example, fall into the same one. In the researcher's reading, the component "appears to discard" the run times and interaction counts in the source records. He found no prompts or source code in the event, but considers that "collecting which agents and developer tools someone uses already has significant privacy implications."

Windows diagnostic data comes in two levels, required and optional, and according to Microsoft's support page, users can choose whether to send optional diagnostic data when they first set up Windows. The researcher also did a clean install of Windows 11 Home from the latest official image with the region set to the United States, and found the optional data switch already on before he changed any privacy setting. He used that installation only to check the switch's default, and did not check whether the coding agent records were enabled on it.

On the researcher's virtual machine, the coding agent check was already enabled, and he had not switched it on himself. With optional data allowed, he found a tool usage record in the Windows upload queue (where diagnostic data is held until it is sent), marked as optional data. His conclusion in the post is that the data is uploaded to Microsoft, but the evidence he lists stops at the record being queued, with no record of an actual outgoing connection.

## Perspective {#perspective}

In Microsoft's guide for organizations on configuring diagnostic data, the contents of optional diagnostic data include "App activity, such as which programs are launched on a device, how long they run". The same guide states that the setting that sends no diagnostic data at all "is only available on Windows Server, Windows Enterprise, and Windows Education editions", so in our reading of the guide, Home and Pro users cannot turn off required data. Microsoft's published list of required diagnostic data includes a separate cohort event, `Segments.Cohorts`, described as one that "classifies users into Cohorts based on App usage", with the line "IsDeveloper is the only cohort being reported". It is a different event from the record the researcher captured, which is classed as optional, and Microsoft has neither published how a user is judged to be a developer nor explained whether the two are connected.

In mainland China, Microsoft released Windows 10 China Government Edition in 2017, developed with the Chinese technology and defence company China Electronics Technology Group Corp (CETC). In a Microsoft blog post quoted in a Computerworld column, the plan for the edition was to use Windows manageability features to remove features Chinese government employees do not need, such as OneDrive, "to manage all telemetry and updates", and to let the government use its own encryption algorithms. The researcher's tests ran on Windows 11 and did not cover this 2017 Windows 10 edition.

To see what diagnostic data your own computer sends, you can install the Diagnostic Data Viewer from the Microsoft Store, then go to Settings > Privacy & security > Diagnostics & feedback and switch on "Turn on the Diagnostic Data Viewer". Once it is on, Windows stores diagnostic data on the device until you turn it off, using up to 1 GB of the system drive by default, and according to the viewer's documentation, "We strongly recommend that you turn off data viewing when you're done". The instructions on the same page are to use the device as usual for a few days before coming back to look, and its wording on queued events is "Seeing an event doesn't necessarily mean it has been uploaded yet." As of 22 November, no one had publicly checked whether the tool usage records the researcher found appear in the viewer.

If you run developer tools or coding agents on Windows 11 and do not want that record to become part of your diagnostic data, you can turn off Send optional diagnostic data under Diagnostic data. The switch is on the same Settings page, and on a new installation you can also decline optional data during setup. Readers outside the United States can go straight to the Settings page to see the switch's current state.

The records the researcher found are marked optional, so in our reading of that label, they should no longer be queued for upload once the switch is off. According to Microsoft's support page, "Regardless of whether you choose to send Optional diagnostic data, your device will be just as secure and will operate normally." The researcher's post includes no comparison test with optional data turned off, and Microsoft has not published what the tool usage records are used for.
