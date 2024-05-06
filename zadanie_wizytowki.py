import os
from faker import Faker


class BaseContact:
    def __init__(self, imie, nazwisko,telefon, e_mail):
        self.imie=imie
        self.nazwisko=nazwisko
        self.telefon=telefon
        self.e_mail=e_mail
    def contact(self):
            print(f"Wybieram numer {self.telefon} i dzwonie do {self.imie} {self.nazwisko}")
    def label_length(self):
            return (len(self.imie)+len(self.nazwisko)+1)

class BusinesContact(BaseContact):
    def __init__(self, nazwa_firmy, stanowisko, telefon_sluzbowy, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nazwa_firmy=nazwa_firmy
        self.stanowisko=stanowisko
        self.telefon_sluzbowy=telefon_sluzbowy
    def contact(self):
            print(f"Wybieram numer {self.telefon_sluzbowy} i dzwonie do {self.imie} {self.nazwisko}")
    def label_length(self):
            return (len(self.imie)+len(self.nazwisko)+1)
        
def create_contacts(rodzaj, ilosc):
    fake=Faker()
    contacts_list=[]
    if rodzaj == 'base':
        for i in range(ilosc):
            item=BaseContact(imie=fake.first_name(), nazwisko=fake.last_name(), telefon=fake.phone_number(), e_mail=fake.email())
            contacts_list+=[item]
    if rodzaj=='busines':
        for i in range(ilosc):
            item=BusinesContact(imie=fake.first_name(), nazwisko=fake.last_name(), e_mail=fake.email(), nazwa_firmy=fake.company(), stanowisko=fake.job(),telefon=fake.phone_number(), telefon_sluzbowy=fake.phone_number())
            contacts_list+=[item]
    return contacts_list


if __name__ == "__main__":
    os.system('clear')
    print("Program generujacy losowe wizytowki")
    rodzaj=input("Podaj rodzaj wizowek 'base' - dla prywatnych, 'busines' - dla biznesowych: ")
    ilosc=int(input("Ile wizytowek zrobic?: "))
    list=create_contacts(rodzaj,ilosc)
    print()
    for item in list:
         item.contact()
