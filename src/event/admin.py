from django.contrib import admin
from .models import EventCategory, EventSocialLink, Event, EventSubscriber
from mptt.admin import MPTTModelAdmin


@admin.register(EventCategory)
class EventCategoryAdmin(MPTTModelAdmin):
    """Категорії подій"""
    list_display = ("id", "name", "parent", "slug", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    mptt_level_indent = 15
    list_filter = ("is_active",)


class EventSocialLinkAdmin(admin.ModelAdmin):
    """Реєстрація моделі посилань на соціальні мережі для подій"""

    list_display = ('id', 'event', 'type', 'link')
    search_fields = ('id', 'link', 'event__name')
    list_filter = ('type',)

    class Meta:
        model = EventSocialLink


admin.site.register(EventSocialLink, EventSocialLinkAdmin)


class EventAdmin(admin.ModelAdmin):
    """Реєстрація моделі подій в адмінпанелі"""
    list_display = ('category', 'name', 'organizer', 'created')
    search_fields = ('organizer__phone', 'organizer__first_name', 'organizer__last_name', 'organizer__email',
                     'name', 'city')
    list_filter = ('category', 'event_format', 'is_active')
    ordering = ('-created',)

    class Meta:
        models = Event


admin.site.register(Event, EventAdmin)


class EventSubscriberAdmin(admin.ModelAdmin):
    """Реєстрація моделі підписників до подій"""
    list_display = ('event', 'user', 'confirmation')
    search_fields = ('user__phone', 'user__first_name', 'user__last_name', 'user__email', 'event__name',
                     'event__city')
    list_filter = ('confirmation', 'created')

    class Meta:
        models = EventSubscriber


admin.site.register(EventSubscriber, EventSubscriberAdmin)











