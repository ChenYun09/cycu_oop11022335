import datetime

def get_day_and_julian_date(input_time: str):
    # 解析輸入時間
    input_time = datetime.datetime.strptime(input_time, '%Y-%m-%d %H:%M')
    
    # 計算星期幾
    day_of_week = input_time.strftime('%A')  # 星期幾的英文名稱
    
    # 計算Julian Date
    jd_input = 367 * input_time.year - (7 * (input_time.year + (input_time.month + 9) // 12)) // 4 + (275 * input_time.month) // 9 + input_time.day + 1721013.5 + (input_time.hour + input_time.minute / 60) / 24
    
    # 計算當前的 Julian Date
    current_time = datetime.datetime.utcnow()
    jd_now = 367 * current_time.year - (7 * (current_time.year + (current_time.month + 9) // 12)) // 4 + (275 * current_time.month) // 9 + current_time.day + 1721013.5 + (current_time.hour + current_time.minute / 60) / 24
    
    # 計算經過的 Julian 日數
    elapsed_days = jd_now - jd_input
    
    # 輸出結果
    return day_of_week, elapsed_days

# 從使用者輸入讀取時間
input_time = input("請輸入時間（格式為 YYYY-MM-DD HH:MM）：")
try:
    day_of_week, elapsed_days = get_day_and_julian_date(input_time)
    print(f"該天是星期: {day_of_week}")
    print(f"該時刻至今經過的太陽日數: {elapsed_days:.6f}")
except ValueError:
    print("輸入時間格式錯誤，請使用 'YYYY-MM-DD HH:MM' 格式")
