import pandas as pd

def read_and_sum_excel(file_path):
    # 讀取 Excel 檔案
    df = pd.read_excel(file_path)
    
    # 假設欄位名稱為 'x' 和 'y'
    df['sum'] = df['x'] + df['y']
    
    # 印出結果
    print(df)

if __name__ == '__main__':
    file_path = '活頁簿1.xlsx'  # 替換為你的 Excel 檔案路徑
    read_and_sum_excel(file_path)