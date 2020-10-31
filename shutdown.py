import os
import keyboard as kb
import sys
import time

if __name__ == "__main__":
    print("Press 1-9, it means that your computer will be turned off in 1000s * 1-9\nPress N to cancel turning off\nPress ESC to Exit")
    while(True):
        try:
            if kb.is_pressed('esc'):
                break
            if kb.is_pressed('1'):
                os.system('shutdown -s -t 1')
                break
            if kb.is_pressed('2'):
                os.system('shutdown -s -t 2000')
                break
            if kb.is_pressed('3'):
                os.system('shutdown -s -t 3000')
                break
            if kb.is_pressed('4'):
                os.system('shutdown -s -t 4000')
                break
            if kb.is_pressed('5'):
                os.system('shutdown -s -t 5000')
                break
            if kb.is_pressed('6'):
                os.system('shutdown -s -t 6000')
                break
            if kb.is_pressed('7'):
                os.system('shutdown -s -t 7000')
                break
            if kb.is_pressed('8'):
                os.system('shutdown -s -t 8000')
                break
            if kb.is_pressed('9'):
                os.system('shutdown -s -t 9000')                
                break
            if kb.is_pressed('n'):
                os.system('shutdown -a')
                break
        except:
            print('except')
            pass
