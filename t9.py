# -*- coding: utf-8 -*-

import pandas as pd
import pymysql as MySQLdb

db = MySQLdb.connect(host='sz-int-generic-db01.sz.optilink.local', port=3306, user='pacific', passwd='pacific', db="pacific_loms_development" )

sql = 'SELECT id, charge, created_at FROM charges limit 10'
df = pd.read_sql(sql,db)
print(df)
db.close()

df.rename(columns={'charge':'费用', 'id':'ID', 'created_at':'创建时间' }, inplace = True)
writer = pd.ExcelWriter('pict.xlsx', engine='xlsxwriter')

df.to_excel(writer, 'Sheet1' , index=False)
writer.save()
writer.close()
