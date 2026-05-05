from django.contrib import admin
from .models import Tweet

# Register your models here.

#credentials for superuser/admin.
#username: admin
#password: 12345

admin.site.register(Tweet)