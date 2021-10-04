import pandas as pd

data_elec_assm = pd.read_csv('output/조립전극.csv')
data_actv      = pd.read_csv('output/활성화.csv')


print(data_elec_assm)
data_final = pd.concat([data_elec_assm, data_actv])
data_final.to_csv('output/전체공정.csv', index = False, encoding='UTF-8-sig')

