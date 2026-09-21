---
name: Bug 報告
about: 建立一份能協助團隊快速重現並修復問題的報告
title: '[模組名稱] 簡述問題發生狀況（例如：結帳頁點擊送出無反應）'
labels: bug
assignees: ''
---

## 1. 問題描述 (Title / Summary)
發生什麼事？在哪裡發生？（一句話說明具體現象）

## 2. 環境資訊 (Environment)
- **作業系統 (OS)**：[例如：Windows 11 / macOS 14.5 / iOS 17.5 / Android 14]
- **瀏覽器與版本 (Browser)**：[例如：Chrome 126.0 / Safari 17.2，若為 App 請填 App 版本]
- **裝置/URL**：[例如：iPhone 15 Pro 或發生問題的網頁網址]

## 3. 重現步驟 (Steps to Reproduce)
請由已知的初始狀態開始，以條列式寫出操作步驟：
1. 前往頁面：`[輸入網址或畫面名稱]`
2. 點擊 / 輸入：`[具體動作，例如：在帳號欄位輸入測試信箱]`
3. 執行動作：`[例如：點擊登入按鈕]`

## 4. 預期結果 (Expected Result)
畫面上應該要發生什麼事？
- 系統應跳出「登入成功」提示，並導向首頁。

## 5. 實際結果 (Actual Result)
畫面上實際發生了什麼事？
- 畫面停留在登入頁，按鈕呈現無限讀取中，且控制台跳出錯誤。

## 6. 相關證據 (Evidence)
請附上錯誤截圖、錄影畫面，或 Console / Network 的錯誤訊息日誌：
- **截圖/影片**：`[拖曳上傳截圖或貼上連結]`
- **Console 錯誤訊息**：
  ```text
  Uncaught TypeError: Cannot read properties of undefined (reading 'id')
  ```

## 7. 影響範圍與替代方案 (Impact & Workaround)
- **受影響對象**：[例如：所有使用優惠券結帳的會員]
- **替代方案 (Workaround)**：[例如：重新整理頁面後可暫時恢復正常，無則填「無」]

## 8. 嚴重性評估 (Severity)
- [ ] **Critical**（系統全面癱瘓、資料遺失）
- [ ] **Major**（主要功能受阻、無替代方案）
- [ ] **Minor**（次要功能受阻、有替代方案）
- [ ] **Cosmetic**（視覺、排版、錯字等小問題）
