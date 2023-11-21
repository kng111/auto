import random
def authenticate(username, password):
    # Здесь вы можете добавить базу данных или другой способ хранения пользовательских данных.
    # В этом примере мы будем использовать словарь для хранения пар логин/пароль.
    users = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3'
    }

    if username in users and users[username] == password:
        print(f'Пользователь {username} успешно авторизован.')
        return True
    else:
        print('Неверный логин или пароль.')
        return False

#  Ввод значений от пользователя 
username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')
# Пример использования функции авторизации
authenticated = authenticate(username, password)

if authenticated:
    # Код, который будет выполняться после успешной аутентификации
    random_array = [random.randint(1, 100) for _ in range(10)]
    print(f'Случайный массив: {random_array}')
    
    average = sum(random_array) / len(random_array)
    min_value = min(random_array)
    
    print(f'Среднее значение: {average}')
    print(f'Минимальное значение: {min_value}')
else:
    # Здесь вы можете добавить код, который будет выполняться в случае неудачной авторизации.
    pass
