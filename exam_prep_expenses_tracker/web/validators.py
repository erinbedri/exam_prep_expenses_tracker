from django.core.exceptions import ValidationError

NAME_ONLY_CHARS_EXCEPTION = 'Ensure this value contains only letters.'

FILE_SIZE_MAX_SIZE_IN_MB = 5
FILE_SIZE_LIMIT_EXCEPTION = f'Max file size is {FILE_SIZE_MAX_SIZE_IN_MB:.2f} MB'


def validate_name_only_chars(name):
    if not name.isalpha():
        raise ValidationError(NAME_ONLY_CHARS_EXCEPTION)


def file_size(value):
    limit = FILE_SIZE_MAX_SIZE_IN_MB * 1024 * 1024
    if value.size > limit:
        raise ValidationError(FILE_SIZE_LIMIT_EXCEPTION)
