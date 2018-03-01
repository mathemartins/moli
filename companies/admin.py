from django.contrib import admin

# Register your models here.
from companies.models import StartUp, Investor, Team, Technology, Market, Finance, Pitching

admin.site.register(StartUp)
admin.site.register(Investor)
admin.site.register(Team)
admin.site.register(Technology)
admin.site.register(Market)
admin.site.register(Finance)
admin.site.register(Pitching)