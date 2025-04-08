# -*- coding: utf-8 -*-
import pandas as pd
import re
from playwright.sync_api import sync_playwright
import sqlite3
import csv
import json


class BusRouteInfo:
    def __init__(self, routeid: str, direction: str = 'go'):
        self.rid = routeid
        self.content = None
        self.url = f'https://ebus.gov.taipei/Route/StopsOfRoute?routeid={routeid}'

        if direction not in ['go', 'come']:
            raise ValueError("Direction must be 'go' or 'come'")

        self.direction = direction
        self.bus_data = []

        self._fetch_content()
        self._parse_content()

    def _fetch_content(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url)
            
            if self.direction == 'come':
                page.click('a.stationlist-come-go-gray.stationlist-come')
            
            page.wait_for_selector('pre', timeout=60000)  # 等待 JSON 資料加載
            self.content = page.inner_text('pre')  # 獲取 JSON 資料
            browser.close()

        # Write the rendered HTML to a file route_{rid}.html
        with open(f"data/ebus_taipei_{self.rid}.html", "w", encoding="utf-8") as file:
            file.write(self.content)

    def _parse_content(self):
        try:
            data = json.loads(self.content)
            bus_stops = data.get('data', {}).get('stops', [])

            if not bus_stops:
                print("無法取得公車站點資料，請檢查公車代碼是否正確。")
                return

            for stop in bus_stops:
                arrival_info = stop.get('arrival_info', '未知')
                stop_number = stop.get('stop_number', '未知')
                stop_name = stop.get('stop_name', '未知')
                stop_id = stop.get('stop_id', '未知')
                latitude = stop.get('latitude', '未知')
                longitude = stop.get('longitude', '未知')

                self.bus_data.append([
                    arrival_info, stop_number, stop_name, stop_id, latitude, longitude
                ])
        except json.JSONDecodeError:
            print("無法解析 JSON 資料，請確認 API 回應格式。")

    def save_to_csv(self, output_file: str):
        if not self.bus_data:
            print("無資料可儲存。")
            return

        try:
            with open(output_file, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["arrival_info", "stop_number", "stop_name", "stop_id", "latitude", "longitude"])
                writer.writerows(self.bus_data)
            print(f"公車路線資料已成功儲存至 {output_file}")
        except Exception as e:
            print(f"寫入 CSV 檔案時發生錯誤：{e}")


# 測試函數
if __name__ == "__main__":
    route_id = input("請輸入公車代碼（例如 '0100000A00'）：")
    output_file = "c:/Users/User/Desktop/cycu_oop11022335/20250408/bus_route_data.csv"

    bus_route = BusRouteInfo(routeid=route_id)
    bus_route.save_to_csv(output_file)