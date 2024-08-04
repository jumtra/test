import pyautogui
import tkinter
import numpy as np
import time
import keyboard
import tkinter
import pyautogui
import numpy as np
import keyboard
import time

def natural_mouse_move(duration):
    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    is_auto = True

    while is_auto:
        current_pos = pyautogui.position()
        current_x = current_pos[0]
        current_y = current_pos[1]
        target_x = np.random.randint(400, width - 400)
        target_y = np.random.randint(200, height - 200)

        length = int(np.hypot(target_x - current_x, target_y - current_y))
        steps = max(1, int(length / 10))  # ステップ数を調整

        for i in range(1, steps + 1):
            if i%10 == 0:
                # 画面が切れないように定期的にボタンを押す
                pyautogui.press("esc")
            if keyboard.is_pressed("enter"):
                is_auto = False
                break

            t = i / steps
            noise = np.random.randn()
            pos_x = int(current_x + (target_x - current_x) * t) + noise
            pos_y = int(current_y + (target_y - current_y) * t) + noise

            pyautogui.moveTo(pos_x, pos_y, duration=duration / steps)
            time.sleep(0.000001)  # カーソルの移動を滑らかにするためのウェイト

        pyautogui.moveTo(target_x, target_y, duration=0)  # 最終的な位置調整
        print(target_x, target_y, pos_x, pos_y, length)

if __name__ == "__main__":
    natural_mouse_move(0.05)  # マウスの移動時間を指定
    