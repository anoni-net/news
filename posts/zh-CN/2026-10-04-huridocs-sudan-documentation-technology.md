---
title: 战时人权记录与技术工具的取舍
description: HURIDOCS 整理苏丹战时人权记录的专家会议。在高风险环境做记录的团体，引进新工具前要评估成本是否值得，以及数据能否与合作伙伴互通。一般用户不需要调整设置。
date: 2026-10-04T07:05:00+08:00
slug: huridocs-sudan-documentation-technology
sources:
  - title: "What wartime documentation demands of technology: Lessons from Sudan"
    url: https://huridocs.org/2026/09/what-wartime-documentation-demands-of-technology-lessons-from-sudan/
    publisher: HURIDOCS
    date: 2026-09-15
  - title: Uwazi
    url: https://huridocs.org/technology/uwazi/
    publisher: HURIDOCS
  - title: huridocs/uwazi
    url: https://github.com/huridocs/uwazi
    publisher: GitHub
    date: 2026-09-28
  - title: "Rising repression meets global resistance: Internet shutdowns in 2025"
    url: https://www.accessnow.org/wp-content/uploads/2026/03/KeepItOn-Internet-Shutdowns-2025-Annual-Report.pdf
    publisher: Access Now
    date: 2026-03-31
  - title: Welcome to the Uwazi demo!
    url: https://demo.uwazi.io/
    publisher: HURIDOCS
  - title: Is https://github.com blocked in mainland China?
    url: https://en.greatfire.org/https/github.com
    publisher: GreatFire
    date: 2026-09-27
regions:
  - SD
authors:
  - anoni-net
---

协助人权组织管理记录的 HURIDOCS 在 9 月 15 日发表文章，整理 9 月在内罗毕讨论苏丹战时人权记录的专家会议。在苏丹的记录者面对流离失所、安全威胁、时断时续的网络与设备不足。文中建议适用于在战争与高风险环境做人权记录的团体，一般用户不需要调整设置。

会议讨论信息如何从记录者传到研究者，之后可能交给检察官。记录可能用于刑事追诉时（例如国际刑事法院），作者认为最糟的结果是多年后才发现记录不能使用，因为当初没有完全符合可预见的证据标准或证据保管链（chain of custody，证据每次经手的记录）的要求。

作者列出技术能做的事，包括离线且安全地收集信息、保存出处记录（provenance），以及连接不同系统的数据。但新工具都要花时间学习，需要培训、设备、网络与维护，还可能造成对厂商或基础设施的依赖。在高风险环境也可能带来新的安全问题。作者的评估标准是成本是否值得技术带来的效益。

作者认为延续性是需要更多关注的挑战之一，比创新更值得留意。延续性是让三种知识能够衔接，包括人权运动的经验、记录者对自身处境的了解，以及日后可能使用数据的机构的需求。

## 导读观点 {#perspective}

据数字权利组织 Access Now 的统计，2025 年苏丹在内战期间断网三次，其中一次在 7 月考试期间。最多的是缅甸 95 次（含跨境断网），其次是印度 65 次、巴基斯坦 20 次，中国也有 2 次。

断网之外，证据还需要出处记录与保管链，记下每份文件的来源、取得时间与经手人。取得时计算哈希值（依内容产生的指纹），日后重算比对就知道是否被改过。

作者把互通性（interoperability）视为人权工作基础设施的一部分，不求所有人共用一个系统。各系统能导出、导入共同格式，数据才能在机构间流动。

HURIDOCS 维护的 Uwazi 是浏览器操作的人权记录数据库，代码以 MIT 许可证（允许自由使用与修改）在 GitHub 开源，9 月 28 日仍有新版本。操作日志（activity log）记下每次变更，数据可以导出成 CSV。

Uwazi 可以免费自行部署，需要 Elasticsearch（全文搜索引擎）等组件与至少 4 GB 内存，也可以用 HURIDOCS 托管。据检测中国网络审查的 GreatFire，到 9 月 27 日为止，从中国大陆连接 github.com 近七成受到干扰。境内部署时，下载代码可能受阻。

评估工具时可逐项检查学习与维护要多少人力、能否与伙伴交换数据、能否保存出处记录，以及断网时能否继续记录。想试 Uwazi 可以用官方 demo 页的公开账号登录。界面内置 11 种语言，包括阿拉伯文但没有中文，中文界面要自行翻译。
