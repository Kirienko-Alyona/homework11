from utility import input_func


def main():
    """
    Користувач вводить через пробіл:
        - команду для бота;
        - команду, ім'я контакта;
        - команду, ім'я контакта, номер телефону;
        - команду, ім'я контакта, дату народження контакта.
    Функція повертає відповідь бота
    Бот завершує роботу після слів "good bye" або "close" або "exit"
    """
    while True:
        input_string = input("Input command, please: ")
        get_command = input_func(input_string)
        print(get_command)
        if get_command == "Good bye!":
            break

    return           


if __name__ == '__main__':
    main()    