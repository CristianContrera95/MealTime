from typing import Dict
from uuid import UUID, uuid4
from datetime import datetime

from django.db.models import Model, UUIDField, DateTimeField


class CommonModel(Model):
    id: UUID = UUIDField(primary_key=True, default=uuid4)
    created_at: datetime = DateTimeField('Creado', auto_now_add=True, db_index=True)
    updated_at: datetime = DateTimeField('Actualizado', auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class ErrorMessages:
    @staticmethod
    def get_field(model: str, field: str, is_unique: bool = False,  # pylint: disable=too-many-arguments
                  is_null: bool = False, is_blank: bool = False,
                  is_enum: bool = False) -> Dict[str, str]:
        messages: Dict[str, str] = {'invalid': f'The {field} field is invalid.'}
        if not is_null:
            messages['null'] = f'The {field} field can\'t be null.'
        if not is_blank:
            messages['blank'] = f'The {field} field can\'t be blank.'
        if is_unique:
            messages['unique'] = f'{model} with this {field} already exists.'
        if is_enum:
            messages['invalid_choice'] = f'The {field} field is not one of available choices.'

        return messages

    @staticmethod
    def get_char_field(model: str, field: str, max_length: int = 255,  # pylint: disable=too-many-arguments
                       is_unique: bool = False, is_null: bool = False,
                       is_blank: bool = False, is_enum: bool = False) -> Dict[str, str]:
        messages: Dict[str, str] = {
            'invalid': f'The {field} field is invalid.',
            'max_length': f'The {field} field must be at most {max_length} characters.'
        }
        if not is_null:
            messages['null'] = f'The {field} field can\'t be null.'
        if not is_blank:
            messages['blank'] = f'The {field} field can\'t be blank.'
        if is_unique:
            messages['unique'] = f'{model} with this {field} already exists.'
        if is_enum:
            messages['invalid_choice'] = f'The {field} field is not one of available choices.'

        return messages
