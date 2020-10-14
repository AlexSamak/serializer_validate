from typing import Callable


class CurrentUserGenericDefault:
    """Дефолтное значение поля пользователя

    Позволяет брать дефолтные значения для полей в соответствии
    с пользователем, отправившим request.

    Example:
        В вашем сериалайзере:
        literal blocks::

            user_profile = serializers.HiddenField(
                default = CurrentUserGenericDefault(
                    lambda user: user.profile
                )
            )

    """
    requires_context = True

    def __init__(self, default_getter: Callable):
        """
        Args:
            default_getter (Callable): функция,
            в аргументы которой передается user.
            Возвращаемое значение может быть любое.

        Example:
            lambda-функция может быть вида: ``lambda user: user.profile`
        """
        self.default_getter = default_getter

    def __call__(self, serializer_field):
        user = serializer_field.context['request'].user
        return self.default_getter(user)

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class CurrentCompanyDefault(CurrentUserGenericDefault):
    """Устанавливает текущую компанию пользователя"""
    def __init__(self):
        super().__init__(lambda user: user.profile.current_company)
