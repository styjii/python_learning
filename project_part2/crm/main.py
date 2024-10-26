from crm import User

from faker import Faker
fake = Faker(locale="fr_FR")

for _ in range(100) :
    user = User(first_name = fake.first_name(),
                last_name = fake.last_name(),
                phone_number = fake.phone_number(),
                address = fake.address())
    
    user.save()