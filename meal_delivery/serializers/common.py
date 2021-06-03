from typing import Set

from rest_framework.serializers import ModelSerializer


class DynamicFieldsSerializer(ModelSerializer):
    def __init__(self, *arguments, **keyword_args) -> None:
        if 'fields' in keyword_args:
            fields = keyword_args.pop('fields', None)
        else:
            fields = None

        super().__init__(*arguments, **keyword_args)
        if fields is not None:
            allowed: Set = set(fields)
            existing: Set = set(self.fields.keys())
            for field in existing - allowed:
                self.fields.pop(field)
