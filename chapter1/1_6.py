# 打鱼还是晒网
"""
中国有句俗语叫“三天打鱼两天晒网”。某人从1990年1月1日起便开始“三天打鱼两天晒网”，问这个人在以后的某一天中是“打鱼”还是“晒网”。
"""
# 这个题目关键是要获取当前日期和1990年1月1日之间的天数，求得天数后，对5取余，若是3就是打鱼，若是2就是晒网。
from datetime import datetime

year = input('请输入当前年份：')
month = input('请输入当前月份：')
date = input('请输入当前日期：')

date_end = datetime(int(year), int(month), int(date))
date_start = datetime(1990, 1, 1)

date_diff = date_end - date_start
days = date_diff.days+1
print(days)
if days%5==3:
    print("今天打鱼")
elif days%5==2:
    print("今天晒网")
else:
    print("今天啥也不干")
