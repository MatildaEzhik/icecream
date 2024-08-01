from django.contrib import admin

from kiosk.models import Kiosk, IceCream, Parent, Child

# Register your models here.

admin.site.register(Kiosk)
admin.site.register(IceCream)
admin.site.register(Parent)
admin.site.register(Child)