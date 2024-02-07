from typing import Any, Dict, List, Optional, Tuple, Union

from django.db import models


def __get_first_two_fields(model: models.Model) -> List[str]:
    """
    The function returns the first two fields of a given model.

    Arguments:

    * `model`: Is expected to be an instance of a Django model class.
    It represents the model for which the first two fields need to be returned.

    Returns:

    A list containing the first two fields of a given model.
    """
    fields = []
    for field in model._meta.fields:
        if len(fields) == 2:
            return fields
        if not field.is_relation:
            fields.append(field.name)
    return fields


def __get_all_fields(model: models.Model) -> List[str]:
    return [field.name for field in model._meta.fields if field.name != "todictmixin_ptr"]


def __set_default_values(
    model: models.Model,
    fields: Optional[Union[List[str], Dict[str, Any], str]] = None,
) -> Tuple[Dict[str, Any], List[str]]:
    """
    The function sets default values for fields in a model if they are not provided.

    Arguments:

    * `model`: Is expected to be an instance of a Django model class.
    It represents the model for which default values need to be set.
    * `fields`: Is an optional dictionary that contains the field names and their default
    values. It is used to set default values for the fields of a given model.

    Returns:

    a tuple containing the dictionary and fields.
    """
    dictionary = {}
    if isinstance(fields, dict):
        dictionary.update(fields)
        fields = fields.keys()

    if fields is None:
        fields = __get_first_two_fields(model)
    elif fields == "__all__":
        fields = __get_all_fields(model)
    return dictionary, fields


def model_to_dict(
    object: models.Model,
    fields: Optional[Union[List[str], Dict[str, Any]]] = None,
    *,
    current_recursion_depth: int = 0,
    max_recursion_depth: int = 1,
) -> dict:
    """
    The `model_to_dict` function converts a Django model object into a dictionary,
    recursively including related model objects up to a specified depth.

    Arguments:

    * `object`: The instance of the Django model that you want to convert to a dictionary.
    * `fields`: Is used to specify which fields of the model object should be included in
    the resulting dictionary. It can be either a list of field names or a dictionary where
    the keys are field names and the values are additional options for each field.
    * `current_recursion_depth`: The current recursion depth is the depth at which the
    function is currently operating. It keeps track of how many levels deep the function
    has traversed through nested models.
    * `max_recursion_depth`: The `max_recursion_depth` parameter determines the maximum
    depth of recursion allowed when converting a model object to a dictionary.
    It specifies how many levels deep the function will traverse through related model
    objects. If the current recursion depth exceeds the maximum recursion depth,
    the function will only include the primary key (`pk`) of the related model object

    Returns:

    A dictionary representation of a Django model object.
    """
    dictionary, fields = __set_default_values(object, fields)

    for field in fields:
        value = getattr(object, field)
        if isinstance(value, models.Model):
            if current_recursion_depth >= max_recursion_depth:
                dictionary[f"{field}_id"] = value.pk
            else:  # current_recursion_depth < max_recursion_depth
                dictionary[field] = model_to_dict(
                    value,
                    current_recursion_depth=current_recursion_depth + 1,
                    max_recursion_depth=max_recursion_depth,
                )
        else:
            if dictionary.get(field, None) is not None and value is None:
                continue
            else:
                dictionary[field] = value
    return dictionary
