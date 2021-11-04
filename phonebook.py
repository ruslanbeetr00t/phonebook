import json


def info_about_user():
    name = input('Введіть ваше ім\'я').title()
    last_name = input('Введіть ваше прізвеще').title()
    initials = name[0] + last_name[0]
    person = (name, last_name, initials)
    return person


def name_person():
    user_info = info_about_user()
    json_user_info = {'name': user_info[0],
                      'surname': user_info[1],
                      'initials': user_info[2]}
    print(json_user_info)
    return json_user_info


def add_phone():
    try:
        phone = input('Додайте номер телефону')
        print(phone)
        if phone.isdigit() is True:
            if len(phone) == 10:
                return phone
            else:
                print('Введіть коректно номер телефону')
                return add_phone()
        else:
            print('Використовуйте лише цифри для введення номеру телефону')
            return add_phone()
    except ValueError:
        print('Використовуйте цифри')
        return add_phone()


def validator_phone_number():
    phone_validator = str(add_phone())
    if len(str(phone_validator)) == 10:
        correct_phone_number = {'phone': phone_validator}
        print(correct_phone_number)
        return correct_phone_number


def all_info():
    json_user_info = name_person()
    print(type(json_user_info))
    numbers = validator_phone_number()
    json_user_info.update(numbers)
    print(json_user_info)
    return json_user_info


def write_json_file():
    with open('user_info.json', 'w', encoding='utf-8') as file_json:
        json.dump(all_info(), file_json, ensure_ascii=False, indent=4)


write_json_file()


