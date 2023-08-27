#27.08.2023

name_bot = "Данил"
rice_bot = 0.53

print(f"Привет, меня зовут {name_bot}, а тебя?")
name_user = input("Ваше имя: ")
print(f"Рад познакомится, {name_user}.")
age_user = int(input("Твой возраст: "))
print(f"Прикинь, тебе будет через 10 лет {age_user+10} лет")
rice_user = float(input("Твой рис: "))
print(f"Мой рис равен {rice_bot} м, ты выше меня на {rice_user-rice_bot} м")
print(f"""Твое имя: {name_user}
Твой возраст: {age_user}
Твой рост: {rice_user}
""")

while True:
    answer = input("""май функтион: 
    1-анехдод
    2-дать савет
    3-расксазващвза про дамашних пятомец
    
    Выбор: """)
    if answer == "1":
        print("кабачёк павесился")
    elif answer == "2":
        answer_two = input("""1-нет
2-нет
3-нет
4-нет
5-нет
6-нет
7-нет
8-да
9-нет
10-нет
11-нет

Выбор: 
""")
        if answer_two == "8":
            answer_eight = input("Вы уверены? ")
            if answer_eight == "Да" or answer_eight == "Yes" or answer_eight == "Нет" or answer_eight == "No" or answer_eight == "Не":
                print("Зачем тебе совет? Совета не будет.")
            else:
                print("Боклашан павесилось")
        else:
            print("Процесс отменен пользователем.")
    elif answer == "3":
        print("грустно но вкусно")
    else:
        print("\033[031mписать научись, дурак!\033[0m")