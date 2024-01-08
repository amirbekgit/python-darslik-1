#malumot turlari

malumot_turlari = 'json','integer','string', 'list', 'dict', 'set', 'booling'
# malumot turlari tipini ko`rish uchun print(type(o`zgaruvchi nomi`))`

#list
list_malumot_turi = [2011, 12, 13, 9, 'A','B','C']
print(list_malumot_turi)
print(type(list_malumot_turi))
print(list_malumot_turi[0])
print(list_malumot_turi[1])
print(list_malumot_turi[2])
print(list_malumot_turi[3])
print(list_malumot_turi[4])
print(list_malumot_turi[5])
print(list_malumot_turi[6])

list_malumot_turi.append(90)
list_malumot_turi[2] = 5
print(list_malumot_turi)