import pandas as pd
import numpy as np

from tabulate import tabulate



data = pd.read_csv('./survey/responses.csv')
print(data.head())


print(data['Gender'].value_counts())


male_like_rock = data.loc[(data['Rock'] >= 4) & (data['Gender'] == 'male')].shape[0]
male_dislike_rock = data.loc[(data['Rock'] <= 2) & (data['Gender'] == 'male')].shape[0]

female_like_rock = data.loc[(data['Rock'] >= 4) & (data['Gender'] == 'female')].shape[0]
female_dislike_rock = data.loc[(data['Rock'] <= 2) & (data['Gender'] == 'female')].shape[0]

table = np.array(
    [
        [male_like_rock, male_dislike_rock],
        [female_like_rock, female_dislike_rock],
    ]
)
new_row = np.sum(table, axis=0)
new_column = np.append(np.sum(table, axis=1), [0])
new_table = np.vstack([table, new_row])
new_table = np.column_stack([new_table, new_column]).tolist()
new_table[2][2] = sum(new_table[2])
for i, val in zip(range(3), ['Мужской', 'Женский', '']):
    new_table[i].insert(0, val)
    
new_table.insert(0, ['Пол', 'Нравится рок', 'Не нравится рок', ''])


print(tabulate(
    new_table,
    tablefmt='grid'
))

