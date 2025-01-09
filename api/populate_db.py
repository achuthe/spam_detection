import random
from faker import Faker
from .models import User, Contact

fake = Faker()

def populate_users(num_users=10):
    for _ in range(num_users):
        user = User.objects.create_user(
            username=fake.user_name(),
            phone_number=fake.phone_number(),
            email=fake.email(),
            password='password123'
        )
        populate_contacts(user, random.randint(5, 15))

def populate_contacts(user, num_contacts=10):
    for _ in range(num_contacts):
        Contact.objects.create(
            owner=user,
            name=fake.name(),
            phone_number=fake.phone_number(),
            spam=random.choice([True, False])
        )
