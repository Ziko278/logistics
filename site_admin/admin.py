from django.contrib import admin
from site_admin.models import *


admin.site.register(SiteSetupModel)
admin.site.register(LocationModel)
admin.site.register(CountryModel)
admin.site.register(LogisticModel)
admin.site.register(ShipmentProgressModel)