import os


def convert_to_seconds(value, unit):
    if unit == "m":
        return value * 60
    elif unit == "h":
        return value * 3600
    else:
        return None


def start_shutdown(seconds):
    command = f"shutdown -s -t {seconds}"
    os.system(command)


def cancel_shutdown():
    os.system("shutdown -a")


def get_time_value():
    user_input = input("请输入时间数字：")

    if not user_input.isdigit():
        print("时间必须是正整数")
        return None

    value = int(user_input)

    if value <= 0:
        print("时间必须大于 0")
        return None

    return value


def main():
    print("Windows 定时关机小工具")
    print("1. 开始定时关机")
    print("2. 取消定时关机")

    choice = input("请选择功能：")

    if choice == "1":
        value = get_time_value()

        if value is None:
            return

        unit = input("请输入单位，m 表示分钟，h 表示小时：")

        seconds = convert_to_seconds(value, unit)

        if seconds is None:
            print("单位输入错误，只能输入 m 或 h")
            return

        start_shutdown(seconds)
        print(f"已设置 {seconds} 秒后关机")

    elif choice == "2":
        cancel_shutdown()
        print("已取消定时关机")

    else:
        print("功能选择错误")


main()