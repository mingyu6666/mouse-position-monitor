import pyautogui
import time

print("鼠标位置监控中，按 Ctrl+C 停止")
while True:
    x, y = pyautogui.position()          # 获取鼠标当前坐标
    print(f"鼠标位置: ({x}, {y})   ", end="\r")   # 原地刷新，不刷屏
    time.sleep(0.2)                       # 每 0.2 秒取一次
