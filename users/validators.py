from datetime import date
from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError

from HW_30_Django_JWT.settings import USER_MIN_AGE


def check_is_published_status(status: bool):
    if status is True:
        raise ValidationError('Некорректный статус.')


def check_min_age(date_of_birth: date):

    difference = relativedelta(date.today(), date_of_birth).years

    if difference < USER_MIN_AGE:
        raise ValidationError(f"Минимальный возраст пользователя должен быть не менее {USER_MIN_AGE} лет.")