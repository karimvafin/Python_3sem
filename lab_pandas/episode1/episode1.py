import pandas as pd

df = pd.read_csv("transactions.csv")

df = df.drop(df.columns[0], axis=1)

print('3 самых крупных платежа с индексами :')
print(df.loc[df.STATUS == 'OK'].SUM.sort_values()[-3:])

print('\nCумма проведенных платежей в адрес Umbrella, Inc :')
print(df.loc[(df.STATUS == 'OK') & (df.CONTRACTOR == 'Umbrella, Inc')].SUM.sum())
