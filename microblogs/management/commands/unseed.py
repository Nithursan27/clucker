from django.core.management.base import BaseCommand, CommandError
#from microblogs.models import User
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        get_user_model().objects.filter(is_superuser = False).delete()



    
    
    