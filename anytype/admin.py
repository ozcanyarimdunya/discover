from django.contrib import admin

from .models import (NullDataConfig, AgeDataConfig, SkillDataConfig, Data, Anytype)

admin.site.register(NullDataConfig)
admin.site.register(AgeDataConfig)
admin.site.register(SkillDataConfig)
admin.site.register(Data)
admin.site.register(Anytype)
