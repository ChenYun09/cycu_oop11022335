import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

def load_bus_data(file_path):
    """
    從 CSV 檔案載入公車站點資料
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"檔案 {file_path} 不存在，請確認路徑是否正確。")
        return None

def find_route_by_route_name(df, route_name):
    """
    根據公車路線名稱查詢對應的站點資料
    """
    filtered_df = df[df["路線名稱"].str.contains(route_name, na=False)]
    if filtered_df.empty:
        print(f"找不到包含路線名稱 '{route_name}' 的公車站點資料。")
        return None
    return filtered_df

def plot_bus_route(df, output_file):
    """
    繪製公車路線並儲存為圖片
    """
    # 將經緯度轉換為 GeoDataFrame
    geometry = [Point(xy) for xy in zip(df["longitude"], df["latitude"])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry)

    # 繪製地圖
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, color="blue", markersize=50, label="Bus Stops")
    for x, y, label in zip(gdf.geometry.x, gdf.geometry.y, gdf["車站名稱"]):
        ax.text(x, y, label, fontsize=8, ha="right")
    plt.title("Bus Route")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.savefig(output_file)
    plt.show()

if __name__ == "__main__":
    # 載入公車站點資料
    file_path = "c:/Users/User/Desktop/cycu_oop11022335/20250422/bus_stops_0100000A00_go.csv"
    bus_data = load_bus_data(file_path)

    if bus_data is not None:
        # 輸入公車路線名稱
        route_name = input("請輸入公車路線名稱：")

        # 查詢對應的公車站點資料
        route_data = find_route_by_route_name(bus_data, route_name)

        if route_data is not None:
            # 繪製公車路線
            output_file = "bus_route_map.png"
            plot_bus_route(route_data, output_file)
            print(f"公車路線地圖已儲存為 {output_file}")