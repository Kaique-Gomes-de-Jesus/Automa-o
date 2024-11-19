import pyautogui as auto
import time
oi = input("Digite sua instituição:  ")
time.sleep(2)
auto.PAUSE = 0.5

auto.press("win")
auto.write("Word", interval= 0.25)
auto.press("enter")
time.sleep(2)

auto.moveTo(x=436, y=181, duration= 1)
auto.click(x=436, y=181)
time.sleep(1)
auto.press("enter")
time.sleep (2)

auto.dragTo(x=890, y=635, button="left")
auto.dragTo(1146, 756, 0.5)
auto.press("delete")
auto.write(oi, interval= 0.20)
