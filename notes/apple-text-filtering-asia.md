# Apple 的文字過濾在亞洲的研究紀錄（鍵盤建議清單與產品雕刻）

範圍是 Apple 產品裡過濾文字的機制，在亞洲各地或中文上有什麼差異的研究紀錄，目前有兩種：iOS 鍵盤的詞組清單（不出現在預測字詞、多數無法滑動輸入），以及產品雕刻的關鍵字過濾（拒絕訂製）。第一次整理是寫 anoni-net/news 的 iPhone 鍵盤詞組清單那篇（Reuters 2026-11-06 的獨家報導）的時候，查證日期 2026-11-15。

兩種機制不同，引用時不要混在一起。雕刻過濾是依銷售地區拒絕訂製，Citizen Lab 有地區比較。鍵盤清單只影響建議與滑動輸入，逐字輸入不受限，Swipeblocked 依語言解出清單，沒有比較不同國家或地區設定的 iPhone，所以不能寫成鍵盤清單依地區過濾。App Store 的下架見 `app-store-removal-asia.md`。

## iOS 鍵盤的中文清單（依語言，不依地區）

- 事實：中文清單上的詞在拼音輸入時仍會出現在候選字，選了之後鍵盤不再預測下一個詞。中文輸入引擎有一部分的程式碼，在詞為英文的「taiwan」或「tibet」時不提供建議
    - 照錄：「Chinese works differently. These words still appear as candidates when you type them in pinyin, but once you pick one the keyboard stops suggesting what comes next. In one part of the Chinese typing engine, Apple's code also skips suggestions whenever a word is “taiwan” or “tibet”, written in English.」
    - 來源：Swipeblocked: the phrases your iPhone won't suggest，<https://swipeblocked.com/>，研究者的網站，依 iOS 27.0 的鍵盤資料與 2026 年 10 月下載的語言資料，查證日期 2026-11-15
- 事實：網站列出的中文例子包括「六四」、「台独」、「钓鱼岛是日本」與「国民党」。國民黨的名稱在簡體中文與繁體中文的清單都擋，中國共產黨的名稱只在繁體中文的清單擋。簡體與繁體是兩份語言清單，不是中國大陸與台灣的地區清單
    - 照錄：「In Simplified Chinese the name of China's Communist Party isn't blocked; in Traditional Chinese both are.」
    - 來源：同上，查證日期 2026-11-15
- 事實：英文、中文與粵語的清單內建在系統映像，其他語言以下載的語言資料提供
    - 照錄：「English, Chinese and Cantonese ship in the system image」
    - 來源：Swipeblocked 的 How it works 頁（同一網站），查證日期 2026-11-15
- 查不到：清單是否依 iOS 的地區設定而不同、中國大陸販售的 iPhone 有沒有額外的詞、注音等拼音以外的輸入方式是否套用同一份清單、中國大陸與香港有沒有法規要求鍵盤過濾（2026-11-15）

## 產品雕刻的關鍵字過濾（依地區）

- 事實：Citizen Lab 2021 年分析 Apple 在六個地區（中國大陸、香港、台灣、日本、加拿大、美國）的產品雕刻過濾，找到 1,105 條關鍵字過濾規則，結論是 Apple 在中國大陸的政治審查有一部分也套用在香港與台灣
    - 照錄：「We analyzed Apple's filtering of product engravings in six regions, discovering 1,105 keyword filtering rules used to moderate their content.」
    - 照錄：「We found that part of Apple's mainland China political censorship bleeds into both Hong Kong and Taiwan. Much of this censorship exceeds Apple's legal obligations in Hong Kong, and we are aware of no legal justification for the political censorship of content in Taiwan.」
    - 照錄：「Apple's public-facing documents failed to explain how it derives their keyword lists.」
    - 來源：Engrave Danger: An Analysis of Apple Engraving Censorship across Six Regions，<https://citizenlab.ca/2021/08/engrave-danger-an-analysis-of-apple-engraving-censorship-across-six-regions/>，Citizen Lab，2021-08-18，查證日期 2026-11-15
- 事實：2022 年的後續研究（測試期間 2022 年 2 月 21 日到 27 日）發現 Apple 已移除台灣的中國政治審查，香港仍持續。這是 2022 年的狀態，之後沒有再查
    - 照錄：「Since our report in August 2021, we find that Apple has eliminated their Chinese political censorship in Taiwan. However, Apple continues to perform broad, keyword-based political censorship outside of mainland China in Hong Kong」
    - 來源：Engrave Condition: Apple's Political Censorship Leaves Taiwan, Remains in Hong Kong，<https://citizenlab.ca/2022/03/engrave-condition-apples-political-censorship-leaves-taiwan-remains-in-hong-kong/>，Citizen Lab，2022-03-22，查證日期 2026-11-15
- 查不到：2022 年之後雕刻過濾在各地的現況（2026-11-15）
