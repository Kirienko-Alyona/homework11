from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value


    @value.setter
    def value(self, value):
        self._value = value    


class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        if not value.isnumeric():
            raise ValueError("Phone must be in numbers") 
        if len(value) < 1 or len(value) > 2:
            raise ValueError("The phone must contain 10 numbers.")
        else:
            self._value = value    
    


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        current_day = datetime.now().date()
        birth = datetime.strptime(value, "%Y-%m-%d").date()
        if birth > current_day:
            raise ValueError("Birthday must be less than current year and date.")
        else:
            self._value = value    


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def get_info(self):
        phones_info = ""
        birthday_info = ""

        for phone in self.phones:
            phones_info += f"{phone.value}, "

        if self.birthday:
            birthday_info = f"Birthday: {self.birthday.value}"    

        return f"{self.name.value}: {phones_info[:-2]} {birthday_info}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for record_phone in self.phones:
            if record_phone.value == phone:
                self.phones.remove(record_phone)
                return True
        return False

    def change_phones(self, phones):
        for phone in phones:
            if not self.delete_phone(phone):
                self.add_phone(phone)

    def add_birthday(self, date):
        self.birthday = Birthday(date)            

    def return_days_to_next_birthday(self):  
        if not self.birthday:
            raise ValueError("This contact doesn't have information of birthday")

        birthday = datetime.strptime(self.birthday.value, "%Y-%m-%d").date()
        current_date = datetime.now()
        current_day_year = current_date.timetuple().tm_yday
        birth_day_of_year = birthday.timetuple().tm_yday
        
        if current_day_year > birth_day_of_year:
            next_year = current_date.timetuple().tm_year + 1
            next_year_birthday = birthday.replace(next_year)
            next_year_day_birth = next_year_birthday.timetuple().tm_yday
            days_to_birth = (365 - current_day_year) + next_year_day_birth
        else:
            days_to_birth = birth_day_of_year - current_day_year        

        return days_to_birth     


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def get_all_record(self):
        return self.data

    def has_record(self, name):
        return bool(self.data.get(name))

    def get_record(self, name) -> Record:
        return self.data.get(name)

    def remove_record(self, name):
        del self.data[name]

    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)

        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record

        raise ValueError("Contact with this name does not exist.")


    def iterator(self, count = 3):
        page = []
        i = 0

        for record in self.data.values():
            page.append(record)
            i += 1

            if i == count:
                yield page
                page = []
                i = count
        if page:
            yield page    


contacts_dict = AddressBook()        