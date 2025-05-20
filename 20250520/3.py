import geopandas as gpd
import matplotlib.pyplot as plt

# 載入台灣的 GeoJSON 資料
gdf = gpd.read_file("twVillage1982.geo.json")

# 篩選北北基桃（台北市、新北市、基隆市、桃園市）
target_cities = ['台北市', '新北市', '基隆市', '桃園縣']  # 修改為資料中的實際名稱
filtered_gdf = gdf[gdf['COUNTYNAME'].isin(target_cities)]  # 修改 'COUNTYNAME' 為實際欄位名稱

# 繪製地圖
plt.figure(figsize=(10, 12))
filtered_gdf.plot(edgecolor='black', color='lightblue')

# 添加標題
plt.title("PEIPEIGITAO", fontsize=16)
plt.xlabel("longitude")
plt.ylabel("latitude")
# 設定坐標軸範圍

# 顯示地圖
plt.tight_layout()
plt.show()