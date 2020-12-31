######################### it is program for taking screenshot###########################################

import tkinter as tk
import pyautogui

root=tk.Tk()
#for  title
root.title("Screenshot")
root.geometry("350x300")

#initolizing a function as capture_screenshot
def capture_screenshot():
    screenshot= pyautogui.screenshot()


    #Give location where you have to save you page
    screenshot.save('E:\screenshot.png')

#creating button
button=tk.Button(root, text="Capture Screenshot", command=capture_screenshot)

button.pack()
root.mainloop()