
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import UserNew, SocialLink
from django.contrib.auth.admin import UserAdmin


class UserNewAdmin(UserAdmin):
    list_display = ('id', 'username', 'phone', 'get_image',)
    list_display_links = ('id', 'username', 'phone')
    readonly_fields = ('get_image',)
    search_fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Персональна інформація'), {'fields': ('first_name', 'last_name', 'gender', 'email', 'phone', 'bio',
                                                 'get_image', 'avatar', 'birthday')}),
        (('Доступи'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (('Важливі дати'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src={obj.avatar.url} width="50" height="50">')
        except ValueError:
            return mark_safe('<p>Відсутнє фото</p>')

    get_image.short_description = "Аватар"

    class Meta:
        model = UserNew


admin.site.register(UserNew, UserNewAdmin)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    '''Реєстрація моделі соціальних мереж'''
    list_display = ('id', 'user', 'link')
