# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import pymysql as MySQLdb


db = MySQLdb.connect(host='sz-int-generic-db01.sz.optilink.local', port=3306, user='pacific', passwd='pacific', db="pacific_loms_development" )
sql = 'SELECT category, sum(charge) AS total_charge FROM charges \
    WHERE category IN %(categories)s GROUP BY category'
df = pd.read_sql(sql,db,
                 params = {'categories' : [
                         'order_actual_transportation_fee',
                         'order_additional_charge'
                         ]})
print(df)


charge_category_data = {
     'category': [
             'order_actual_transportation_fee',
             'order_additional_charge'
             ],
     'name': [
             '实际运费',
             '附件费'
             ]
     }
charge_category_dicts = pd.DataFrame(charge_category_data)
charge_category_dicts.set_index('category')
print(charge_category_dicts)

df = df.merge(charge_category_dicts, on='category')

print(df)
df.plot(kind='bar', figsize=(10,8))


plt.show()
