from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from .models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for i in range(0,100):
            name = self.faker.name()
            User.object.create_user(
                "@" + name,
                first_name = name.split(" ")[0],
                last_name = name.split(" ")[1],
                email = name + "@example.org",
                password = name + "123",
                bio = self.faker.text(),
            )
    
