# 功能介绍

- 批量修改文件的时间属性：修改时间，创建时间，最后访问时间

# 使用方法

- 在python中调用 powershell 脚本，实现批量修改文件的时间属性

# 修改参数
##### 1 请替换为目标目录
 - directory = r"E:\3Proj\25EX102\CPLD\fun\EX102_CPLD" 
##### 2 设置创建时间
 - creation_time = "2024-12-19 10:38:31"
##### 3 设置修改时间
 - modification_time = parse_time("2024-11-01 12:00:00")
##### 4 设置访问时间
 - access_time = parse_time("2024-12-18 12:00:00")
# 运行
 - cmd中，运行 "python modifyFilesDateTime.py"