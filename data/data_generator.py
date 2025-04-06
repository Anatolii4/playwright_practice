from faker import Faker


class DataGenerator:

    @staticmethod
    def generate_full_name() -> str:
        fake = Faker()
        return fake.name()

    @staticmethod
    def generate_email() -> str:
        fake = Faker()
        return fake.email()

    @staticmethod
    def generate_address() -> str:
        fake = Faker()
        return fake.address()