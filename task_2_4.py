text = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(text)):
    print('Привет,', text[i].rsplit(' ', 1)[1].capitalize())
