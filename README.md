# TEAM 14
* 0616309 王祥任
* 0616031 李昀奇
* 0616098 黃秉茂

## 檔案說明
### main.ipynb
主要模組。

### Recoder.py
資料收集用。依賴於`DrawTablet.py`。需要`pygame`模組。

### DrawTablet_WithDetection.py
利用訓練完後的預測器，預測手寫輸入。必須先執行一次`main.ipynb`以獲得預測器。需要`pygame`模組。

寫完字母後按`D`會輸出預測結果於`Console`。
按`C`會清空當前畫布。