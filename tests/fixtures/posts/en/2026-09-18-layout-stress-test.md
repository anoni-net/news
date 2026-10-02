---
title: Layout stress test with an extraordinarily long English headline, unbroken URLs, a wide table and a code block in one story
description: A test story holding the content most likely to break a phone layout.
date:
  created: 2026-09-18
  updated: 2026-09-20
slug: layout-stress-test
sources:
  - title: "Collateral Damage of IP-Based Blocking During Football Streaming: A Measurement Study Across Nine Point Two Million Domains"
    url: https://example.org/research/2026/very/long/path/that/keeps/going/without/any/natural/break/point/collateral-damage-of-ip-based-blocking.html?utm_source=none&ref=aVeryLongQueryStringValueWithoutSpaces
    publisher: Example Research Institute
  - title: Second source without date
    url: https://example.org/second
authors:
  - night-owl
  - named-example
categories:
  - mobile
---

原始網址直接貼在內文裡：https://example.org/research/2026/very/long/path/that/keeps/going/without/any/natural/break/point.html

也有寫成連結的長網址：[example.org/research/2026/very/long/path/that/keeps/going/without/any/natural/break/point.html](https://example.org/research/2026/very/long/path/that/keeps/going/without/any/natural/break/point.html)

![對角線穿過方框的示意圖](https://assets.anoni.net/news/2026/09/layout-stress-test/figure-1.webp "圖：anoni.net 社群，CC-BY 4.0。測試用的圖，比手機螢幕寬很多")

## 量測結果 {#results}

| 國家 | 測點數 | 受影響的網域 | 比例 | 備註 |
|---|---|---|---|---|
| Spain | 1,234 | 554,500 | 5.8% | Measured with TCP and TLS handshakes against a control vantage point |
| Germany | 987 | 0 | 0% | Control |

## 重現方式 {#reproduce}

```bash
ooniprobe run websites --input-file ./a-very-long-file-name-for-testing-overflow-behaviour-on-small-screens.txt --no-collector
```

### 更小一層的小標 {#smaller-heading}

延伸閱讀：[什麼是 OONI](https://anoni.net/docs/tools/what-is-ooni/)、[OONI 網站檢測清單](https://anoni.net/docs/taiwan/ooni-checklist/)
