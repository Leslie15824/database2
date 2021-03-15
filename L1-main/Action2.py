
#构建数据
from pandas import Series, DataFrame
data = {'姓名': ['张飞', '关羽', '刘备', '典韦', '许褚'], 
        '语文': [68, 95, 98, 90,80], 
        '数学': [65, 76, 86, 88, 90], 
        '英语': [30, 98, 88, 77, 90]}
df = DataFrame(data)
print(df.to_string(index = False))
#统计并打印
df1 = df.drop(columns=['姓名']) 
sta = df1.agg(['mean','max','min','var','std'])
print(sta)
# 计算总分
df.insert(4,column='总分',value=df['语文'] + df['数学'] + df['英语'])
# 排序并打印
result = df.sort_values('总分', ascending=False)
print(result.to_string(index=False))
