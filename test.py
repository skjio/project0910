import random
import time
import os
import re

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
#可以清理終端數據
def intro():
    print("歡迎來到《迷失的地牢》")
    name = input("請輸入你的冒險者名稱：")
    while not re.match(r"^[A-Za-z\u4e00-\u9fa5]{1,10}$", name):
        name = input("請輸入有效的名稱（限中文或英文，最多10字）：")
    return name

def main_game(name):
    rooms = {
        "A": "怪物房",
        "B": "寶藏房",
        "C": "空房",
        "D": "陷阱房",
        "E": "補給房",
        "F": "謎語房",
        "G": "傳送房"
    }
    bag = []

    while True:
        print("\n你面前有七扇門：A / B / C / D / E / F / G")
        choice = input("你要前往哪個房間？(A~G) 或輸入 Q 離開：").upper()
        if choice == "Q":
            print("遊戲結束，感謝遊玩！")
            break
        elif choice in rooms:
            clear_screen()
            room_type = rooms[choice]
            print(f"你進入了{room_type}...")
            time.sleep(1)
            if room_type == "怪物房":
                print("你遇到了一隻哥布林！你決定快跑！")
            elif room_type == "寶藏房":
                item = random.choice(["金幣", "藥水", "鑰匙", "寶石"])
                print(f"你找到了一個寶物：{item}")
                bag.append(item)
            elif room_type == "空房":
                print("這裡什麼都沒有，繼續前進吧。")
            elif room_type == "陷阱房":
                print("你踩到了陷阱！幸好只是輕傷。")
            elif room_type == "補給房":
                print("你發現了一些食物與水，感覺好多了！")
            elif room_type == "謎語房":
                answer = input("謎語：什麼東西越洗越髒？\n你的答案：")
                if re.search(r"水|水池", answer):
                    print("答對了！你獲得了一顆智慧之石。")
                    bag.append("智慧之石")
                else:
                    print("答錯了！房間沉默不語。")
            elif room_type == "傳送房":
                print("一股神秘力量將你傳送到另一個房間！")
                continue
        else:
            print("請輸入有效的選項。")
    
    with open("game_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{name} 探索結束，背包內容：{bag}\n")

if __name__ == "__main__":
    clear_screen()
    player_name = intro()
    main_game(player_name)