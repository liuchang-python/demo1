import pandas as pd
import numpy as np

data = pd.DataFrame(pd.read_excel("12月份衣服销售数据.xlsx", header=0, index_col=0, parse_dates=True))


data['price'] = data["价格/件"] * data["销售量/每日"]

print('总销售额---{0:.2f}'.format(data['price'].sum()))

aver = data['销售量/每日'].sum() / data['price'].count()
print('日均销售量---{0:.2f}'.format(aver))

sales = pd.DataFrame(data.groupby('服装名称')['销售量/每日'].sum())
# print(sales)
sales['ratio/占比'] = sales['销售量/每日'] / sales['销售量/每日'].sum()
print(sales)

