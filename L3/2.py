def user_info(name, surname, city, birth_year, phone, email):
    print(f"Привет, {name} {surname}! Теперь я знаю, что ты родился в {birth_year} году и", end=' ')
    print(f"живешь в городе {city}. Я даже знаю твои e-mail и телефон:  {email}, {phone}.")


user_name = input("Введите свое имя: ")
user_surname = input("Введите свою фамилию: ")
user_birth_year = input("Введите год своего рождения: ")
user_city = input("Введите город своего проживания: ")
user_email = input("Введите свой e-mail: ")
user_phone = input("Введите свой номер телефона: ")

user_info(name=user_name, surname=user_surname, birth_year=user_birth_year, city=user_city, email=user_email,
          phone=user_phone)
