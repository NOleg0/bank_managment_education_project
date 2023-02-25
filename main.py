import json
from bank.structure import Personal, Development, Bank
from bank.serializer import BankSerializer
import os

def passage_from_bank_to_deposit(development_name, bank, save_deposit):
    if bank.is_empty():
        return
    while bank.size() != 0:
        cur_development = bank.pop()
        if cur_development.development_number == development_name:
            bank.push(cur_development)
            return cur_development
        save_deposit.push(cur_development)

def passage_from_deposit_to_bank(development_name, bank, save_deposit):
    if save_deposit.is_empty():
        return
    while save_deposit.size() != 0:
        cur_development = save_deposit.pop()
        if cur_development.development_number == development_name:
            bank.push(cur_development)
            return cur_development
        bank.push(cur_development)

def add_personal_in_development(personal_name, position, some_development):
    for persons in some_development:
        if persons.last_name == personal_name:
            ans = input(f"\nСотрудник {personal_name} уже есть в отделе, добавить (y/n)")
            if ans == "y":
                persona = Personal(personal_name, position)
                some_development.add(persona)
                print(f"\nСотрудник {personal_name} добавлен в отдел\n")
                return
            elif ans == "n":
                return
    new_person = Personal(personal_name, position)
    some_development.add(new_person)
    print(f"\nСотрудник {personal_name} добавлен в отдел {some_development.development_number}")

def search_personal(personal_name, some_development):
    for index, persona in enumerate(some_development):
        if persona.last_name == personal_name:
            return index, persona
    return

def action():
    act = input("Добавить - 1\n"
                "Удалить - 2\n"
                "Изменить данные - 3\n"
                "Назад - 4\n")
    return act

def bank_act(act, bank, save_deposit):
    if act == "1":
        print(f"\n{bank.bank_name}\n")
    elif act == "2":
        bank.bank_name = input("Введите новое название банка: ")
    elif act == "3":
        ans = input("Вы уверены что хотите удалить все данные (y/n)")
        if ans == "y":
            bank.clear()
            save_deposit.clear()
            print("\nДанные удалены")
    elif act == "4":
        return

def development_act(act, bank, save_deposit):
    if act == "5":
        return
    new_development = input("Введите название отдела: ")
    cur_development = passage_from_deposit_to_bank(new_development, bank, save_deposit) or passage_from_bank_to_deposit(new_development, bank, save_deposit)

    if act == "1":
        if cur_development:
            print(f"\nОтдел {new_development} уже есть")
            return
        development = Development(new_development)
        bank.push(development)
        print(f"\nОтдел {new_development} добавлен")
        return
    elif cur_development:
        if act == "2":
            bank.pop()
            print(f"\nОтдел {new_development} былл удален")
            return
        elif act == "3":
            ans = input("Вы действительно хотите удалить все данные отдела (y/n)")
            if ans == "y":
                cur_development.clear()
                print("\nДанные отдела удалены")
            return
        elif act == "4":
            new_development_number = input("Введите новое название отдела: ")
            cur_development.development_number = new_development_number
            print("\nНазвание отдела изменено")
            return
    else:
        print(f"\nОтдел {new_development} не найден")

def personal_act(act, bank, save_deposit):
    if act != "4":
        personal_name = input("Введите фамилию сотрудника: ")

        if act == "1":
            personal_position = input("Введите должность сотрудника: ")
            personal_development = input("Введите отдел для добавления сотрудника: ")

            cur_development = passage_from_bank_to_deposit(personal_development, bank, save_deposit) or passage_from_deposit_to_bank(personal_position, bank, save_deposit)

            if cur_development:
                add_personal_in_development(personal_name, personal_position, cur_development)
                return
            else:
                ans = input("Такого отдела нет, хотите создать? (y/n)")
                if ans == "y":
                    cur_development = Development(personal_development)
                    persona = Personal(personal_name, personal_position)
                    cur_development.add(persona)
                    bank.push(cur_development)
                    print(f"\nСотрудник {personal_name} добавлен в отдел {cur_development.development_number}")
                    return
                elif ans == "n":
                    return
        personal_development = input(f"Введите название отдела {'Для удаления' if act == '2' else 'для поиска'} сотрудника")
        cur_development = passage_from_bank_to_deposit(personal_development, bank, save_deposit) or passage_from_deposit_to_bank(personal_development, bank, save_deposit)

        if act == "2" or act == "3":
            if cur_development:
                if act == "2":
                    cur_personal = search_personal(personal_name, cur_development)
                    if cur_personal:
                        cur_development.pop(cur_personal[0])
                        print(f"\nСотрудник {personal_name} был удален")
                    else:
                        print(f"\nСотрудник {personal_name} не найден")

                else:
                    cur_personal = search_personal(personal_name, cur_development)[1]
                    if cur_personal:
                        ans = input("Изменить фамилию - 1\n"
                                    "Изменить должность - 2\n"
                                    "Изменить данные - 3\n")
                        if ans == "1":
                            new_personal_name = input("Введите фамилию сотрудника: ")
                            cur_personal.last_name = new_personal_name
                            print("\n")
                        elif ans == "2":
                            new_position = input("Введите должность сотрудника: ")
                            cur_personal.position = new_position
                        elif ans == "3":
                            new_personal_name = input("Введите фамилию сотрудника: ")
                            new_position = input("Введите должность сотрудника: ")
                            cur_personal.last_name = new_personal_name
                            cur_personal.position = new_position
                        print("Данные успешно изменены")
                    else:
                        print(f"\nСотрудник {personal_name} не найден")
            else:
                print(f"\nОтдел {personal_development} не найдена")
    else:
        return

def display_bank(bank, save_deposit):
    print(f"\nНазвание банка: {bank.bank_name}")
    if not save_deposit.size() and not bank.size():
        print("\nВ банке пока нет отделов")
        return
    passage_from_deposit_to_bank("-1", bank, save_deposit)
    while bank.size() != 0:
        cur_development = bank.pop()
        print(f"\nНазвание отдела: {cur_development.development_number}")
        if not cur_development.is_empty():
            for persons in cur_development:
                print(f"\n[{persons.last_name}: {persons.position}]", sep = ', ', end =' ')
            print()
        else:
            print("В отделе пока нет сотрудников")
        save_deposit.push(cur_development)

def download():
    save_deposit = Bank("Save Deposit")
    serializer = BankSerializer()
    if os.stat("bank_data.json").st_size == 0:
        bank = Bank(input("Введите название банка: "))
    else:
        with open("bank_data.json") as ouf:
            download_data = json.load(ouf)
        bank = serializer.deserialize(download_data)
    return bank, save_deposit, serializer

def save(serializer, bank, save_deposit):
    passage_from_deposit_to_bank("-1", bank, save_deposit)
    bank_serialize = serializer.serialize(bank)
    with open("bank_data.json", "w", encoding="utf-8") as inf:
        json.dump(bank_serialize, inf, ensure_ascii=False, indent = 3)
    print("\nСохранение завершено успешно")

def choice(user_choice, bank, save_deposit, serializer):
    if user_choice == "1":
        print("\nБанк: ")
        bank_act(input("Вывести название банка - 1\n"
                       "Изменить название банка - 2\n"
                       "Удалить все данные - 3\n"
                       "Назад - 4\n"), bank, save_deposit)
    elif user_choice == "2":
        print("\nОтдел: ")
        development_act(input("Добавить новый отдел - 1\n"
                              "Удалить отдел - 2\n"
                              "Удалить данные отдела - 3\n"
                              "Изменить название отдела - 4\n"
                              "Назад - 5\n"), bank, save_deposit)
    elif user_choice == "3":
        print("\nСотрудник: ")
        personal_act(action(), bank, save_deposit)
    elif user_choice == "4":
        display_bank(bank, save_deposit)
    elif user_choice == "5":
        save(serializer, bank, save_deposit)

def main():
    bank, save_deposit, serializer = download()
    while True:
        user_choice = input("\nБанк - 1\n"
                            "Отдел - 2\n"
                            "Сотрудник - 3\n"
                            "Вывод всей структуры - 4\n"
                            "Сохранение в файл - 5\n"
                            "Завершение работы - 6\n")
        if user_choice == "6":
            ans = input("Сохранить изменения? (y/n)")
            if ans == "y":
                save(serializer, bank, save_deposit)
            exit()
        choice(user_choice, bank, save_deposit, serializer)

if __name__ == "__main__":
    main()