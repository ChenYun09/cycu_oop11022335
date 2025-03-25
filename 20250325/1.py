import pandas as pd
import matplotlib.pyplot as plt

# pip pandas
# pip install matplotlib
# pip install openpyxl

# 讀取 Excel 檔案
df = pd.read_excel('325.xlsx')

# 假設欄位名稱為 'x' 和 'y'
df['sum'] = df['資料日期'] + df['現金']

# 印出相加結果
print(df['sum'])

# 繪製散佈圖
plt.scatter(df['資料日期'], df['現金'])
plt.xlabel('資料日期')
plt.ylabel('現金')
plt.title('Scatter plot of 資料日期 and 現金')
plt.show()