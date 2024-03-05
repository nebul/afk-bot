import pyautogui
import time

pyautogui.FAILSAFE = False
mouse_position_x_list = list()
mouse_position_y_list = list()

try:

    while True:
        mouse_position_x_list.clear()
        mouse_position_y_list.clear()
        for i in range(10) :
            current_mouse_position_x, current_mouse_position_y = pyautogui.position()
            time.sleep(1)
            mouse_position_x_list.append(current_mouse_position_x)
            mouse_position_y_list.append(current_mouse_position_y)

        if (mouse_position_x_list.count(mouse_position_x_list[0]) == len(mouse_position_x_list) and mouse_position_y_list.count(mouse_position_y_list[0]) == len(mouse_position_y_list) ):
            current_mouse_position_x, current_mouse_position_y = pyautogui.position()
            for i in range(0,100):
                pyautogui.moveTo(0,i*4)
            pyautogui.moveTo(current_mouse_position_x, current_mouse_position_y)

except KeyboardInterrupt:
    print("Interrupt")
