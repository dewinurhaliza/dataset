import pandas as pd

# Membaca file Excel
dataframe = pd.read_excel('https://raw.githubusercontent.com/dewinurhaliza/dataset/master/fastfood.xlsx')
dataframe

kolom = ['calories', 'cal_fat', 'total_fat', 'sat_fat', 'trans_fat', 'cholesterol', 'sodium', 'total_carb', 'fiber', 'sugar', 'protein', 'vit_a', 'vit_c', 'calcium']
df = dataframe[kolom]

jumlah_calories = df['calories'].sum()
print('Jumlah Total Calories    : ', jumlah_calories)

jumlah_calories = df['cal_fat'].sum()
print('Jumlah Total cal_fat     : ', jumlah_calories)

jumlah_calories = df['total_fat'].sum()
print('Jumlah Total total_fat   : ', jumlah_calories)

jumlah_calories = df['sat_fat'].sum()
print('Jumlah Total sat_fat     : ', jumlah_calories)

jumlah_calories = df['trans_fat'].sum()
print('Jumlah Total trans_fat   : ', jumlah_calories)

jumlah_calories = df['cholesterol'].sum()
print('Jumlah Total cholesterol : ', jumlah_calories)

jumlah_calories = df['sodium'].sum()
print('Jumlah Total sodium      : ', jumlah_calories)

jumlah_calories = df['total_carb'].sum()
print('Jumlah Total total_carb  : ', jumlah_calories)

jumlah_calories = df['fiber'].sum()
print('Jumlah Total fiber       : ', jumlah_calories)

jumlah_calories = df['sugar'].sum()
print('Jumlah Total sugar       : ', jumlah_calories)

jumlah_calories = df['protein'].sum()
print('Jumlah Total protein     : ', jumlah_calories)

jumlah_calories = df['vit_a'].sum()
print('Jumlah Total vit_a       : ', jumlah_calories)

jumlah_calories = df['vit_c'].sum()
print('Jumlah Total vit_c       : ', jumlah_calories)

jumlah_calories = df['calcium'].sum()
print('Jumlah Total calcium     : ', jumlah_calories)

print()
print()

median_calories = df['calories'].median()
print('Median cal_fat     : ', median_calories)

median_calories = df['cal_fat'].median()
print('Median cal_fat     : ', median_calories)

median_calories = df['total_fat'].median()
print('Median total_fat   : ', median_calories)

median_calories = df['sat_fat'].median()
print('Median sat_fat     : ', median_calories)

median_calories = df['trans_fat'].median()
print('Median trans_fat   : ', median_calories)

median_calories = df['cholesterol'].median()
print('Median cholesterol : ', median_calories)

median_calories = df['sodium'].median()
print('Median sodium      : ', median_calories)

median_calories = df['total_carb'].median()
print('Median total_carb  : ', median_calories)

median_calories = df['fiber'].median()
print('Median fiber       : ', median_calories)

median_calories = df['sugar'].median()
print('Median sugar       : ', median_calories)

median_calories = df['protein'].median()
print('Median protein     : ', median_calories)

median_calories = df['vit_a'].median()
print('Median vit_a       : ', median_calories)

median_calories = df['vit_c'].median()
print('Median vit_c       : ', median_calories)

median_calories = df['calcium'].median()
print('Median calcium     : ', median_calories)

print()
print()

mean_calories = df['calories'].mean()
print('Mean calories    : ', mean_calories)

mean_calories = df['cal_fat'].mean()
print('Mean cal_fat     : ', mean_calories)

mean_calories = df['total_fat'].mean()
print('Mean total_fat   : ', mean_calories)

mean_calories = df['sat_fat'].mean()
print('Mean sat_fat     : ', mean_calories)

mean_calories = df['trans_fat'].mean()
print('Mean trans_fat   : ', mean_calories)

mean_calories = df['cholesterol'].mean()
print('Mean cholesterol : ', mean_calories)

mean_calories = df['sodium'].mean()
print('Mean soidum      : ', mean_calories)

mean_calories = df['total_carb'].mean()
print('Mean total_carb  : ', mean_calories)

mean_calories = df['fiber'].mean()
print('Mean fiber       : ', mean_calories)

mean_calories = df['sugar'].mean()
print('Mean sugar       : ', mean_calories)

mean_calories = df['protein'].mean()
print('Mean protein     : ', mean_calories)

mean_calories = df['vit_a'].mean()
print('Mean vit_a       : ', mean_calories)

mean_calories = df['vit_c'].mean()
print('Mean vit_c       : ', mean_calories)

mean_calories = df['calcium'].mean()
print('Mean calcium     : ', mean_calories)
