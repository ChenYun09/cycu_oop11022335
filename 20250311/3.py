import pandas as pd
import matplotlib.pyplot as plt

def read_and_sum_excel(file_path):
    # 讀取 Excel 檔案
    df = pd.read_excel(file_path)
    
    # 假設欄位名稱為 'x' 和 'y'
    df['sum'] = df['x'] + df['y']
    
    # 印出結果
    print(df)
    
    # 繪製圖表
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['sum'], marker='o', linestyle='-', color='b', label='Sum of x and y')
    plt.xlabel('Index')
    plt.ylabel('Sum')
    plt.title('Sum of x and y')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    file_path = '311.xlsx'  # 替換為你的 Excel 檔案路徑
    read_and_sum_excel(file_path)