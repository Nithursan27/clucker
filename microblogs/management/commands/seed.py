from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        for i in range(0,100):
            name = self.faker.name()
            User.objects.create_user(
                "@" + name.split(" ")[0] + name.split(" ")[1],
                first_name = name.split(" ")[0],
                last_name = name.split(" ")[1],
                email = name + "@example.org",
                password = name.split(" ")[0] + "123",
                bio = self.faker.text(),
            )
    
