from django.contrib import admin
from news.models import Headlines, World, Tech_news, Economy, Sports

# Super user : myapp
# password  : mypassword

# Register your models here.

admin.site.register(Headlines)
admin.site.register(World)
admin.site.register(Tech_news)
admin.site.register(Economy)
admin.site.register(Sports)



