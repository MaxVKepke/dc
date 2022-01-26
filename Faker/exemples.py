from faker import Faker


class GenerateFakeData:
    def phone_generate(self):
        fake_data = Faker()
        phone = fake_data.phone_number()
        print(phone)
        code = fake_data.country_calling_code()
        msisdn = fake_data.msisdn()
        print(f"{code}\n{msisdn}")

    def name_generate(self, local):
        fake_data = Faker(local)
        fake_name = fake_data.name()

        first_name = fake_data.first_name() # first_name_female(), first_name_male()
        last_name = fake_data.last_name()
        print(fake_name)
        print(first_name, last_name)

    def address_generate(self):
        fake_data = Faker()
        fake_address = fake_data.address()
        print(fake_address)

    def text_generate(self):
        fake_data = Faker('ru_RU')
        fake_text = fake_data.unique.text() #use unique

        print(fake_text)

    def pass_generate(self):
        fake_data = Faker("ru_RU")
        password = fake_data.password(length=120, special_chars=False, digits=False, upper_case=True, lower_case=True)
        print(password)

    def credit_card_generate(self):
        fake_data = Faker()
        expire = fake_data.credit_card_expire()
        number = fake_data.credit_card_number()
        code = fake_data.credit_card_security_code()
        full_data = fake_data.credit_card_full()
        print(expire, number, code)
        print(full_data)

    def test(self):
        fake_data = Faker("ru_RU")
        for _ in range(5):
            print(fake_data.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^'))

GenerateFakeData().phone_generate()