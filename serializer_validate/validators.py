"""
Общие валидаторы для проекта cargosoft
"""
from typing import Callable

from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.validators import qs_exists, qs_filter


class ForeignKeyValidator:
    """Валидирует ForeignKey-поля

    Проверяет есть ли значение ForeignKey-поля в queryset, полученном от
    пользователя из запроса (request).
    Queryset для валидации задается в виде lambda-функции.

    Example:
        Данный код проверит, действительно ли принадлежит
        указанная лицензия пользователю, который совершает запрос:

        .. code-block:: py

            license = YourSerializerField(
                validators=[
                    ForeignKeyValidator(lambda user: user.profile.licenses)
                ]
            )
    """
    message = _('You cannot set value: {value}.')
    requires_context = True

    def __init__(self, qs_getter: Callable):
        """
        Args:
            qs_getter (Callable): lambda-выражение. Функция вернет queryset
            context_getter (Callable): lambda-выражение. Ее не надо трогать,
            она нужна для переопределения.
        """
        self.qs_getter = qs_getter

    def __call__(self, value, serializer_field):
        user = serializer_field.context['request'].user

        cur_comp = self.qs_getter(user)
        print(f'{cur_comp} -- {value}')

        if value.id != cur_comp.id:
            raise ValidationError(
                self.message.format(value=value),
                code='foreign-key'
            )


class CompanyForeignKeyValidator(ForeignKeyValidator):
    """Валидирует ForeignKey-поля

    Shortcut над ``ForeignKeyValidator``. Отличается тем,
    что в lambda-выражение ``qs_getter`` передается текущая
    компания пользователя.

    Example:
        В данном контексте ``company`` это ``user.profile.current_company``:

        .. code-block:: py

            qs_getter = lambda company: company.payments

    """
    def __init__(self, qs_getter: Callable):
        print(qs_getter)
        super().__init__(qs_getter)
