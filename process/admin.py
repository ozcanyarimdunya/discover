from django.contrib import admin
from .models import (FirstConfig, SecondConfig, ThirdConfig, FourthConfig)

admin.site.register(FirstConfig)
admin.site.register(SecondConfig)
admin.site.register(ThirdConfig)
admin.site.register(FourthConfig)
