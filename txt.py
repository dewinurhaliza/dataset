import pandas as pd

# Membaca file txt
dataframe = pd.read_csv('https://raw.githubusercontent.com/dewinurhaliza/dataset/master/Normalized_Gain_Combined_Clean.txt')
dataframe

kolom = ['Course_Grade', 'Pre', 'Pre %', 'Post', 'Post %', '% Change', '%_Possible_Change', 'Normalized_Gain']
df = dataframe[kolom]

jumlah_calories = df['Course_Grade'].sum()
print('Jumlah Total Course Grade        : ', jumlah_calories)

jumlah_calories = df['Pre'].sum()
print('Jumlah Total Pre                 : ', jumlah_calories)

jumlah_calories = df['Pre %'].sum()
print('Jumlah Total Pre %               : ', jumlah_calories)

jumlah_calories = df['Post'].sum()
print('Jumlah Total Post                : ', jumlah_calories)

jumlah_calories = df['Post %'].sum()
print('Jumlah Total Post %              : ', jumlah_calories)

jumlah_calories = df['% Change'].sum()
print('Jumlah Total % Change            : ', jumlah_calories)

jumlah_calories = df['%_Possible_Change'].sum()
print('Jumlah Total %_Possible_Change   : ', jumlah_calories)

jumlah_calories = df['Normalized_Gain'].sum()
print('Jumlah Total Normalized_Gain     : ', jumlah_calories)

print()
print()

median_calories = df['Course_Grade'].median()
print('Median Course Grade        : ', median_calories)

median_calories = df['Pre'].median()
print('Median Pre                 : ', median_calories)

median_calories = df['Pre %'].median()
print('Median Pre %               : ', median_calories)

median_calories = df['Post'].median()
print('Median Post                : ', median_calories)

median_calories = df['Post %'].median()
print('Median Post %              : ', median_calories)

median_calories = df['% Change'].median()
print('Median % Change            : ', median_calories)

median_calories = df['%_Possible_Change'].median()
print('Median %_Possible_Change   : ', median_calories)

median_calories = df['Normalized_Gain'].median()
print('Median Normalized_Gain     : ', median_calories)

print()
print()

mean_calories = df['Course_Grade'].mean()
print('Mean CourseGrade         : ', mean_calories)

mean_calories = df['Pre'].mean()
print('Mean Pre                 : ', mean_calories)

mean_calories = df['Pre %'].mean()
print('Mean Pre %               : ', mean_calories)

mean_calories = df['Post'].mean()
print('Mean Post                : ', mean_calories)

mean_calories = df['Post %'].mean()
print('Mean Post %              : ', mean_calories)

mean_calories = df['% Change'].mean()
print('Mean % Change            : ', mean_calories)

mean_calories = df['%_Possible_Change'].mean()
print('Mean %_Possible_Change   : ', mean_calories)

mean_calories = df['Normalized_Gain'].mean()
print('Mean Normalized_Gain     : ', mean_calories)

print()
print()
print()
