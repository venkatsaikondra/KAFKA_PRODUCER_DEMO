from faker import Faker
faker=Faker()
def get_random_data():
    return {
        "name":faker.name(),
        "address":faker.address(),
        "DOB":faker.year(),
    }
if __name__ == "__main__":
    print(get_random_data())