from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_prep_expenses_tracker.web.validators import validate_name_only_chars, file_size


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15
    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    FILE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_name_only_chars,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_name_only_chars,
        )
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        )
    )

    image = models.ImageField(
        null=True,
        blank=True,
        validators=(
            file_size,
        )
    )


class Expense(models.Model):
    EXPENSE_TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=EXPENSE_TITLE_MAX_LEN,
    )

    image = models.URLField()

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True,
    )
