from django.contrib import admin
from .models import EventSubscriber


class EventSubscriberAdmin(admin.ModelAdmin):
    """Реєстрація моделі підписників до подій"""
    list_display = ('event', 'user', 'confirmation')
    search_fields = ('user__phone', 'user__first_name', 'user__last_name', 'user__email', 'event__name',
                     'event__city')
    list_filter = ('confirmation', 'created')

    class Meta:
        models = EventSubscriber


admin.site.register(EventSubscriber, EventSubscriberAdmin)
