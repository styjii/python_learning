from faker import Faker

fake = Faker(locale="fr_FR")

# numbers = [fake.unique.random_int() for _ in range(500)]
# assert len(numbers) == len(set(numbers))


for _ in range(10) :
    print(fake.file_path(depth=5))