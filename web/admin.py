from django.contrib import admin

from .models import BasicRun, BitbucketRun

admin.site.register(BasicRun)
admin.site.register(BitbucketRun)
