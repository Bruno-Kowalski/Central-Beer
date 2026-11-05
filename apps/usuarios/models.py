from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, nome, password=None, **extra_fields):
        if not username:
            raise ValueError("O nome de usuário é obrigatório.")

        if not nome:
            raise ValueError("O nome completo é obrigatório.")

        username = self.model.normalize_username(username)

        usuario = self.model(
            username=username,
            nome=nome,
            **extra_fields,
        )

        if password:
            usuario.set_password(password)
        else:
            usuario.set_unusable_password()

        usuario.save(using=self._db)

        return usuario

    def create_superuser(self, username, nome, password=None, **extra_fields):
        extra_fields.setdefault(
            "perfil",
            self.model.Perfil.ADMINISTRADOR,
        )
        extra_fields.setdefault("ativo", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("O superusuário precisa ter is_superuser=True.")

        if extra_fields.get("perfil") != self.model.Perfil.ADMINISTRADOR:
            raise ValueError("O superusuário precisa ser administrador.")

        return self.create_user(
            username=username,
            nome=nome,
            password=password,
            **extra_fields,
        )


class Usuario(AbstractBaseUser, PermissionsMixin):

    class Perfil(models.TextChoices):
        ADMINISTRADOR = "ADMINISTRADOR", "Administrador"
        ATENDENTE = "ATENDENTE", "Atendente"

    id = models.BigAutoField(
        primary_key=True,
        db_column="ID",
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        db_column="USERNAME",
    )

    # O Django gerencia o hash da senha.
    # O nome físico da coluna segue o DER.
    password = models.CharField(
        max_length=128,
        db_column="SENHA",
    )

    nome = models.CharField(
        max_length=150,
        db_column="NOME",
    )

    perfil = models.CharField(
        max_length=20,
        choices=Perfil.choices,
        default=Perfil.ATENDENTE,
        db_column="PERFIL",
    )

    ativo = models.BooleanField(
        default=True,
        db_column="ATIVO",
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        db_column="CRIADO_EM",
    )

    objects = UsuarioManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["nome"]

    @property
    def is_active(self):
        return self.ativo

    @is_active.setter
    def is_active(self, value):
        self.ativo = value

    @property
    def is_staff(self):
        return self.perfil == self.Perfil.ADMINISTRADOR

    class Meta:
        db_table = "TB_USUARIO"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.nome} ({self.username})"
    