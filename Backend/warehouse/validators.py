from django.core.exceptions import ValidationError

def validate_no_empty_string(value):
    if not value:
        raise ValidationError("El %(value)s no puede estar vacio", params={'value':value}, )

def validate_not_negative_number(value):
    if value > 0:
        raise ValidationError("El %(value)s no puede ser negativo", params={'value':value},)

   