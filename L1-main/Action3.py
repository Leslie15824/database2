# 对汽车投诉信息进行分析
import pandas as pd

result = pd.read_csv('car_complain.csv')
#print(result)
# 将genres进行one-hot编码（离散特征有多少取值，就用多少维来表示这个特征）
result = result.drop('problem', 1).join(result.problem.str.get_dummies(','))
#print(result.columns)
tags = result.columns[7:]
print(tags)

df= result.groupby(['brand'])['id'].agg(['count'])
#print(df)

df1= result.groupby(['car_model'])['id'].agg(['count'])
#print(df1)

df2= result.groupby(['brand'])[tags].agg(['sum'])
df2 = df.merge(df2, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
df2.reset_index(inplace=True)
df2= df2.sort_values('count', ascending=False)
#print(df2)
#print(df2.columns)
df2.to_csv('brand.csv', index=False)

df3= result.groupby(['car_model'])[tags].agg(['sum'])
df3 = df1.merge(df3, left_index=True, right_index=True, how='left')
# 通过reset_index将DataFrameGroupBy => DataFrame
df3.reset_index(inplace=True)
df3= df3.sort_values('count', ascending=False)
#print(df3)
#print(df2.columns)
df3.to_csv('car_model.csv', index=False)

df4 = result.groupby(['brand'])['car_model'].agg(['nunique']).reset_index()
df5 = pd.merge(df, df4, left_on='brand',right_on='brand', how='left')
df5.insert(3,column='平均车型投诉数',value=df5['count'] / df5['nunique'])
df5= df5.sort_values('平均车型投诉数', ascending=False)
print(df5)