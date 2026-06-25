import os
import tkinter as tk
from tkinter import messagebox


def convert_to_seconds(value, unit):
    if unit == "分钟":
        return value * 60
    elif unit == "小时":
        return value * 3600
    else:
        return None


def start_shutdown(seconds):
    command = f"shutdown -s -t {seconds}"
    os.system(command)


def cancel_shutdown():
    os.system("shutdown -a")


def format_time_message(value, unit, seconds):
    return f"已设置 {value} {unit}后关机，约 {seconds} 秒"


def handle_start_shutdown():
    value_text = time_entry.get()
    unit = unit_var.get()

    if not value_text.isdigit():
        messagebox.showerror("输入错误", "时间必须是正整数")
        return

    value = int(value_text)

    if value <= 0:
        messagebox.showerror("输入错误", "时间必须大于 0")
        return

    seconds = convert_to_seconds(value, unit)

    if seconds is None:
        messagebox.showerror("输入错误", "单位错误")
        return

    start_shutdown(seconds)

    message = format_time_message(value, unit, seconds)
    status_label.config(text=message)
    messagebox.showinfo("设置成功", message)


def handle_cancel_shutdown():
    cancel_shutdown()
    status_label.config(text="已取消定时关机")
    messagebox.showinfo("取消成功", "已取消定时关机")


window = tk.Tk()
window.title("Windows 定时关机小工具")
window.geometry("360x220")
window.resizable(False, False)

title_label = tk.Label(window, text="Windows 定时关机小工具", font=("Microsoft YaHei", 14))
title_label.pack(pady=15)

input_frame = tk.Frame(window)
input_frame.pack(pady=5)

time_entry = tk.Entry(input_frame, width=10)
time_entry.pack(side="left", padx=5)

unit_var = tk.StringVar(value="分钟")

unit_menu = tk.OptionMenu(input_frame, unit_var, "分钟", "小时")
unit_menu.pack(side="left", padx=5)

start_button = tk.Button(window, text="开始定时关机", width=20, command=handle_start_shutdown)
start_button.pack(pady=8)

cancel_button = tk.Button(window, text="取消定时关机", width=20, command=handle_cancel_shutdown)
cancel_button.pack(pady=4)

status_label = tk.Label(window, text="等待操作", fg="gray")
status_label.pack(pady=10)

window.mainloop()