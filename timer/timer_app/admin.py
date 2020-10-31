from django.contrib import admin
from .models import Topic, SubTopic, Session
from django.contrib import admin


class SubTopicInlineAdmin(admin.TabularInline):
    model = SubTopic


class TopicAdmin(admin.ModelAdmin):
    # list_display = ('name', 'type')
    # list_filter = ('type',)
    inlines = [
        SubTopicInlineAdmin,

    ]


admin.site.register(Topic, TopicAdmin)
admin.site.register(SubTopic)
admin.site.register(Session)
