import os
import time
import subprocess

def modify_creation_time(file_path, creation_time):
    # 获取当前 Python 脚本的目录路径
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 构造 PowerShell 脚本的完整路径
    ps_script_path = os.path.join(script_dir, "Set-FileTime.ps1")
    print(f"ps_script_path {ps_script_path}")
    # 调用 PowerShell 脚本来修改文件创建时间
    command = [
        "powershell.exe",
        "-ExecutionPolicy", "Bypass",  # 允许执行脚本
        "-File", ps_script_path,   # PowerShell 脚本路径
        "-filePath", file_path,
        "-creationTime", creation_time
    ]
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"powershell An error occurred: {e}")

def traverse_and_modify(directory, creation_time, access_time, modification_time):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            modify_creation_time(file_path, creation_time)
            os.utime(file_path, (access_time, modification_time))  # 修改访问时间和修改时间
            print(f"Modified time for {file_path}")

def parse_time(time_str):
    # 将时间字符串转换为时间元组
    time_tuple = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    # 将时间元组转换为时间戳
    return time.mktime(time_tuple)

if __name__ == "__main__":
    directory = r"E:\3Proj\25EX102\CPLD\fun\EX102_CPLD"  # 请替换为目标目录
    # 使用统一的时间处理方法
    # 设置创建时间、访问时间和修改时间
    creation_time = "2024-12-19 10:38:31"
    modification_time = parse_time("2024-11-01 12:00:00")
    access_time = parse_time("2024-12-18 12:00:00")

    try:
        if os.path.isdir(directory):
            traverse_and_modify(directory, creation_time, access_time, modification_time)
            print(f"已完成")
        else:
            print(f"目录不存在 : {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")

