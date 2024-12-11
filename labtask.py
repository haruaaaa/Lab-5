import re
import csv

#1
file1 = open('task1-en.txt').read()

defis = re.findall(r'\b\w+-\w+\b', file1)
scobk = re.findall(r'\((.*?)\)', file1)

print(defis)
print(scobk)


#2
file2 = open('task2.html', 'r', encoding='utf-8').read()

sites = re.findall(r'\bhttps?://[^\s/$.?#].[^\s]*\.com\b', file2)
print(sites)


#3
file3 = open('task3.txt').read()

surname = re.findall(r'[A-Z][a-z]+', file3)
mail = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]', file3)
date = re.findall(r'\d{4}-\d{2}-\d{2}', file3)
site = re.findall(r'https?://[a-zA-Z0-9.-]+/', file3)

id_list = []
id = 1
while True:
    if str(id) in file3:
        id_list.append(id)
        id+=1
    else:
        break

table = []

for i in range(len(id_list)):
    table.append([id_list[i], surname[i], mail[i], date[i],site[i]])

with open('lab_task3.csv', 'w') as file4:
    written = csv.writer(file4)

    written.writerow(['id', 'surname', 'mail', 'date', 'site'])

    written.writerows(table)

print('Таблица создана в файле lab_task3.csv.')