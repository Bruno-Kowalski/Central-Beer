from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ("username", "nome", "perfil", "ativo")


class UsuarioChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = (
            "username",
            "nome",
            "perfil",
            "ativo",
            "is_superuser",
            "groups",
            "user_permissions",
        )


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    form = UsuarioChangeForm
    add_form = UsuarioCreationForm
    model = Usuario

    list_display = (
        "id",
        "username",
        "nome",
        "perfil",
        "ativo",
        "is_superuser",
    )

    list_filter = ("perfil", "ativo", "is_superuser")
    search_fields = ("username", "nome")
    ordering = ("username",)

    fieldsets = (
        ("Autenticação", {
            "fields": ("username", "password"),
        }),
        ("Informações do usuário", {
            "fields": ("nome", "perfil", "ativo"),
        }),
        ("Permissões", {
            "fields": ("is_superuser", "groups", "user_permissions"),
        }),
        ("Informações de acesso", {
            "fields": ("last_login", "criado_em"),
        }),
    )

    add_fieldsets = (
        ("Cadastro de usuário", {
            "classes": ("wide",),
            "fields": (
                "username",
                "nome",
                "perfil",
                "ativo",
                "password1",
                "password2",
            ),
        }),
    )

    readonly_fields = ("last_login", "criado_em")
    filter_horizontal = ("groups", "user_permissions")