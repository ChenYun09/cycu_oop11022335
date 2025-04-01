def get_arrival_time(dataframe, station_name):
    """
    Retrieve the arrival time for a specific station from the DataFrame.

    Args:
        dataframe (pd.DataFrame): The DataFrame containing stop information.
        station_name (str): The name of the station to search for.

    Returns:
        str: The arrival time for the specified station, or a message if not found.
    """
    # 查找站點名稱
    result = dataframe[dataframe['stop_name'] == station_name]
    if not result.empty:
        return result.iloc[0]['arrival_time']  # 返回到站時間
    else:
        return "找不到該站點的到站時間。"

# Test function
if __name__ == "__main__":
    rid = "10417"  # Test route ID
    try:
        df1, df2 = get_bus_route(rid)
        print("First DataFrame:")
        print(df1)
        print("\nSecond DataFrame:")
        print(df2)

        # 輸入站點名稱
        station_name = input("請輸入站點名稱：")
        # 查詢去程
        print("\n去程：")
        arrival_time = get_arrival_time(df1, station_name)
        print(f"{station_name} 到站時間：{arrival_time}")

        # 查詢回程
        print("\n回程：")
        arrival_time = get_arrival_time(df2, station_name)
        print(f"{station_name} 到站時間：{arrival_time}")

    except ValueError as e:
        print(f"Error: {e}")