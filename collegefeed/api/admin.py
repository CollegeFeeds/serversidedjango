from django.contrib import admin
from api.models import mphilresults,mphilcounters,undergradresults,undergradcounters,postgradresults,postgradcounters,ncwebresults,ncwebcounters



admin.site.register(mphilresults)
admin.site.register(mphilcounters)

admin.site.register(undergradresults)
admin.site.register(undergradcounters)

admin.site.register(postgradresults)
admin.site.register(postgradcounters)

admin.site.register(ncwebresults)
admin.site.register(ncwebcounters)
