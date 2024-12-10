import random

school1 = """Учитель: — Якщо у вас є 5 яблук і я заберу 2, скільки у вас залишиться?
Учень: — 5! Я яблуками не ділюсь!"""
school2 = """— Чому ти не зробив домашку?
— Забув!
— Як забув?
— Ну, не знаю, як це пояснити, але вона просто зникла з моїх думок!"""
school3 = """— Чому ти не написав контрольну?
— Бо не встиг, бо думав, що в тебе ще є "опція перегляду"."""

technic1 = """— Мій телефон завжди зависає!
— Мабуть, він просто втомився від твого життя."""
technic2 = """— У тебе є Powerbank?
— Так, у мене є новий Power...waiting for charging.
"""
technic3 = """— Ти чому знову не відповідаєш на повідомлення?
— Вибач, мій телефон вирішив, що це неважливо."""

family1 = """Мама: — Як ти встиг так наївно відповісти на питання?
Дитина: — Я тільки намагаюся зробити день більш цікавим!"""
family2 = """Мама: — Ти чому не прибрав у своїй кімнаті?
Дитина: — Я організував хаос, щоб потім усе знаходити за лічені секунди!"""
family3 = """Тато: — Що це за новий звук із холодильника?
Дитина: — Це холодильник влаштовує "танці" для підняття настрою."""

friend1 = """— Як твої стосунки?
— У нас є розуміння: я – це я, а він – це він.
"""
friend2 = """Друг: — Ти чому не відповідаєш на мої повідомлення?
Я: — Я в пошуках нових способів бути зайнятим!"""
friend3 = """— Ти знову забув свій день народження?
— Я просто думав, що кожен рік ми святкуємо це по-різному!"""

sport1 = """— Ти чому не займаєшся спортом?
— Я займаюсь дуже інтенсивно… з моїм диваном."""
sport2 = """— Ти збираєшся бігати в марафоні?
— Збираюсь, тільки якщо буде конкурс на найшвидше переховування від бігу."""
sport3 = """— Чому ти знову не їси здорову їжу?
— Я їм здорово, якщо "здорово" — це шматок шоколадки і йогурт!"""

schools = [school1, school2, school3]
technics = [technic1, technic2, technic3]
familis = [family1, family2, family3]
friends = [friend1, friend2, friend3]
sports = [sport1, sport2, sport3]
dict = {"Школа": schools,
        "Техніка": technics,
        "Побут": familis,
        "Друзі": friends,
        "Спорт": sports}
while True:
    try:
        print("""Список категорій
        Школа
        Техніка
        Побут
        Друзі
        Спорт""")
        category = input("Виберіть категорію: ")
        if category == "Школа":
            ask = input("Ви хочите добавити свій анекдот?(Так/Ні) ")
            if ask == "Ні":
                numsch = random.randint(0, len(dict["Школа"]))
                if numsch == 1:
                    print(f"Рандомний анекдот цієї категорії: {school1}")
                elif numsch == 2:
                    print(f"Рандомний анекдот цієї категорії: {school2}")
                elif numsch == 3:
                    print(f"Рандомний анекдот цієї категорії: {school2}")
            elif ask == "Так":
                user_input = input("Введіть ваш анікдот ")
                schools.append(user_input)
                print(f"Як тепер виглядає дана категорія: {schools}")

        elif category == "Техніка":
            askk = input("Ви хочите добавити свій анекдот?(Так/Ні) ")
            if askk == "Ні":
                numtech = random.randint(0, len(dict["Техніка"]))
                if numtech == 1:
                    print(f"Рандомний анекдот цієї категорії: {technic1}")
                elif numtech == 2:
                    print(f"Рандомний анекдот цієї категорії: {technic2}")
                elif numtech == 3:
                    print(f"Рандомний анекдот цієї категорії: {technic3}")
            elif askk == "Так":
                user_input = input("Введіть ваш анікдот ")
                technics.append(user_input)
                print(f"Як тепер виглядає дана категорія: {technics}")
        elif category == "Побут":
            askkk = input("Ви хочите добавити свій анекдот?(Так/Ні) ")
            if askkk == "Ні":
                numpob = random.randint(0, len(dict["Побут"]))
                if numpob == 1:
                    print(f"Рандомний анекдот цієї категорії: {family1}")
                elif numpob == 2:
                    print(f"Рандомний анекдот цієї категорії: {family2}")
                elif numpob == 3:
                    print(f"Рандомний анекдот цієї категорії: {family3}")
            elif askkk == "Так":
                user_input = input("Введіть ваш анікдот ")
                familis.append(user_input)
                print(f"Як тепер виглядає дана категорія: {familis}")
        elif category == "Друзі":
            askkkk = input("Ви хочите добавити свій анекдот?(Так/Ні) ")
            if askkkk == "Ні":
                numfr = random.randint(0, len(dict["Друзі"]))
                if numfr == 1:
                    print(f"Рандомний анекдот цієї категорії: {friend2}")
                elif numfr == 2:
                    print(f"Рандомний анекдот цієї категорії: {friend1}")
                elif numfr == 3:
                    print(f"Рандомний анекдот цієї категорії: {friend3}")
            elif askkkk == "Так":
                user_input = input("Введіть ваш анікдот ")
                friends.append(user_input)
                print(f"Як тепер виглядає дана категорія: {friends}")
        elif category == "Спорт":
            ask1 = input("Ви хочите добавити свій анекдот?(Так/Ні) ")
            if ask1 == "Ні":
                numsport = random.randint(0, len(dict["Спорт"]))
                if numsport == 1:
                    print(f"Рандомний анекдот цієї категорії: {sport1}")
                elif numsport == 2:
                    print(f"Рандомний анекдот цієї категорії: {sport2}")
                elif numsport == 3:
                    print(f"Рандомний анекдот цієї категорії: {sport3}")
            elif ask1 == "Так":
                user_input = input("Введіть ваш анікдот ")
                sports.append(user_input)
                print(f"Як тепер виглядає дана категорія: {sports}")
        else:
            print("Ви не правильно ввели категорію")
    except:
        print("Сталась помилка")