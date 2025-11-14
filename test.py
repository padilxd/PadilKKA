import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('nilai_siswa.csv')

# # print(data.info())
# print(data.head())
# print(data.describe())

# # print(data['Nilai'].mean())
# print(data['Nilai'].median())
# print(data['Nilai'].mode()[0])

# matematika = data[data['Matpel'] == 'Matematika']
# print(matematika)

# print(data.groupby('Matpel')['Nilai'].agg(['max','min']))

# rata = data.groupby('Matpel')['Nilai'].mean()
# rata.plot(kind='bar')
# plt.show()

