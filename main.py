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


def set_custom_shutdown():
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


def show_menu():
    print()
    print("Windows 定时关机小工具")
    print("1. 30 分钟后关机")
    print("2. 1 小时后关机")
    print("3. 2 小时后关机")
    print("4. 自定义时间")
    print("5. 取消定时关机")
    print("0. 退出程序")


def main():
    while True:
        show_menu()

        choice = input("请选择功能：")

        if choice == "1":
            start_shutdown(30 * 60)
            print("已设置 30 分钟后关机")

        elif choice == "2":
            start_shutdown(1 * 3600)
            print("已设置 1 小时后关机")

        elif choice == "3":
            start_shutdown(2 * 3600)
            print("已设置 2 小时后关机")

        elif choice == "4":
            set_custom_shutdown()

        elif choice == "5":
            cancel_shutdown()
            print("已取消定时关机")

        elif choice == "0":
            print("已退出程序")
            break

        else:
            print("功能选择错误，请重新输入")


main()