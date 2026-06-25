import os


def convert_to_seconds(value, unit):
    if unit == "m" or unit == "分钟":
        return value * 60
    elif unit == "h" or unit == "小时":
        return value * 3600
    else:
        return None


def start_shutdown(seconds):
    command = f"shutdown -s -t {seconds}"
    os.system(command)


def cancel_shutdown():
    os.system("shutdown -a")


def format_time_message(value, unit, seconds):
    if unit == "m" or unit == "分钟":
        return f"已设置 {value} 分钟后关机，约 {seconds} 秒"
    elif unit == "h" or unit == "小时":
        return f"已设置 {value} 小时后关机，约 {seconds} 秒"
    else:
        return f"已设置 {seconds} 秒后关机"