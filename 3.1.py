from playwright.sync_api import sync_playwright
import csv
import json

def fetch_bus_route_data(route_id):
    with sync_playwright() as p:
        # 啟動瀏覽器
        browser = p.chromium.launch(headless=False)  # 設置 headless=False 以便調試
        page = browser.new_page()

        # 定義目標 URL
        url = f'https://ebus.gov.taipei/Route/StopsOfRoute?routeid={route_id}'
        page.goto(url)

        try:
            # 等待網頁的動態內容加載
            page.wait_for_selector('pre', timeout=60000)  # 設置超時為 60 秒

            # 獲取網頁中的 JSON 資料
            json_data = page.inner_text('pre')  # 網頁中的 JSON 資料通常會放在 <pre> 標籤內

            # 解析 JSON 資料
            data = json.loads(json_data)
            bus_stops = data.get('data', {}).get('stops', [])
            
            # 如果有車站資料，則開始處理
            if bus_stops:
                bus_data = []
                for stop in bus_stops:
                    arrival_info = stop.get('arrival_info', '')
                    stop_number = stop.get('stop_number', '')
                    stop_name = stop.get('stop_name', '')
                    stop_id = stop.get('stop_id', '')
                    latitude = stop.get('latitude', '')
                    longitude = stop.get('longitude', '')
                    
                    # 收集站點資料
                    bus_data.append([
                        arrival_info, stop_number, stop_name, stop_id, latitude, longitude
                    ])
                
                # 關閉瀏覽器
                browser.close()

                return bus_data
            else:
                print("無法獲取車站資料，請確認路線代碼是否正確。")
                browser.close()
                return []
        except TimeoutError:
            print("等待網頁內容加載超時，請檢查網路連線或網站狀態。")
            browser.close()
            return []
        except json.JSONDecodeError:
            print("無法解析 JSON 資料，請確認頁面格式。")
            browser.close()
            return []

def save_to_csv(data, filename):
    # 將資料寫入 CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # 寫入表頭
        writer.writerow(['arrival_info', 'stop_number', 'stop_name', 'stop_id', 'latitude', 'longitude'])
        
        # 寫入每行資料
        writer.writerows(data)

# 測試函數
route_id = '0100000A00'  # 這是測試用的公車代碼
bus_data = fetch_bus_route_data(route_id)

# 如果成功取得資料，則保存為 CSV
if bus_data:
    save_to_csv(bus_data, 'bus_route_data.csv')
    print("資料已成功儲存到 'bus_route_data.csv'")
else:
    print("未能獲取有效的公車資料。")