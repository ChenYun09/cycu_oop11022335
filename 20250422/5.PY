import geopandas as gpd
import fiona

def read_station_names(file_path):
    """
    從 GeoJSON 檔案中讀取所有站名
    """
    try:
        # 設定 fiona 的編碼為 UTF-8
        with fiona.Env(encoding='utf-8'):
            # 讀取 GeoJSON 檔案
            gdf = gpd.read_file(file_path)

        # 提取站名 (BSM_CHINES 欄位)
        station_names = gdf["BSM_CHINES"].tolist()

        # 列印所有站名
        print("所有站名：")
        for name in station_names:
            print(name)

        return station_names
    except Exception as e:
        print(f"讀取檔案時發生錯誤：{e}")
        return None

if __name__ == "__main__":
    # 指定 GeoJSON 檔案路徑
    file_path = "c:/Users/User/Desktop/cycu_oop11022335/20250422/bus_stop2.geojson"

    # 呼叫函式讀取站名
    read_station_names(file_path)