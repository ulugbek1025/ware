from django.contrib import admin
from user.models import Order,Cilent,Product,UserStatus,All_categories,Categories

# Register your models here.
admin.site.register(Order)
admin.site.register(Cilent)
admin.site.register(Product)
admin.site.register(UserStatus)
admin.site.register(All_categories)
admin.site.register(Categories)

