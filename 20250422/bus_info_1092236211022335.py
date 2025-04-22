def bus_info():
    """
    顯示三條公車路線的資訊
    """
    routes = {
        "承德幹線": "台北車站 -> 承德路 -> 士林 -> 北投",
        "基隆路幹線": "台北車站 -> 基隆路 -> 信義區 -> 木柵"
    }

    print("公車路線資訊：")
    for route_name, route_path in routes.items():
        print(f"{route_name}：{route_path}")