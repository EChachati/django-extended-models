from typing import Any, Dict, List, Optional, Union

from django.db import models

from django_extended_models.utils import model_to_dict


class ToDictMixin(models.Model):
    """
    The `ToDictMixin` class provides a method `to_dict` that converts a model instance to
    a dictionary.
    """

    def to_dict(
        self,
        fields: Optional[Union[List[str], Dict[str, Any], str]] = None,
    ) -> Dict[str, Any]:
        return model_to_dict(self, fields=fields)
