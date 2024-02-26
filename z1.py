import csv

f = open("students.csv").read()
f = f.split("\n")
data = [i.split(",") for i in f]
header = data.pop(0)
print(header)
mid = 0
cou = 0
nn = 0
nf = open('student_new.csv', "w")
wr = csv.writer(nf)
for i in data:
    if not nn and "Хадаров Владимир" in i[1]:
        print(f'Ты получил: {i[-1]}, за проект - {i[-3]}')
        nn = 1
    if i[-1] != "None" and i[-1]:
        mid += int(i[-1])
        cou += 1
gr = round(mid/cou, 3)
for i in data:
    if i[-1] == "None":
        i[-1] = gr
    wr.writerow(i)
nf.close()

