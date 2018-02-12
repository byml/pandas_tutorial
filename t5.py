# -*- coding: utf-8 -*-

import pandas as pd
import pymysql as MySQLdb
import matplotlib.pyplot as plt

db = MySQLdb.connect(host='sz-int-generic-db01.sz.optilink.local', port=3306, user='pacific', passwd='pacific', db="pacific_loms_development" )

sql = 'SELECT id, charge, created_at FROM charges limit 10'
df = pd.read_sql(sql,db)

print(df)

db.close()


plt.rcParams['font.sans-serif']=['SimHei']

plt.figure(figsize=(10,6))
#设置x轴柱子的个数
x= df['id']
#设置y轴的数值
y= df['charge']

#画出柱状图
plt.bar(x,y)

#
for i in range(0, x.size):
    plt.text(df['id'][i], df['charge'][i], df['charge'][i], color = '#3412f3', horizontalalignment='center', fontsize=14)

#x、y轴标签与图形标题
plt.xlabel('费用类型', fontsize=16)
plt.ylabel('金额', rotation='horizontal', horizontalalignment='right', fontsize=16)
plt.title('费用统计', fontsize=18)

plt.savefig('1.jpg')
plt.show()

df.rename(columns={'charge':'费用', 'id':'ID', 'created_at':'创建时间' }, inplace = True)
writer = pd.ExcelWriter('pict.xlsx', engine='xlsxwriter')

df.to_excel(writer, 'Sheet1' , index=False)


workbook  = writer.book
worksheet = writer.sheets['Sheet1']
worksheet.insert_image('F5', '1.jpg')

worksheet.conditional_format('B2:B100', {'type': '2_color_scale'})

writer.save()

writer.close()
