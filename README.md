
# django-extended-models

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/EChachati/django-extended-models/blob/master/LICENSE)

`django-extended-models` is a Django utility package that provides mixins and models with extended functionalities.

## Installation

Install the package using [Poetry](https://python-poetry.org/):

```bash
poetry add django-extended-models
```

## Features

### `utils.py`

#### `__set_default_values`

The function sets default values for fields in a model if they are not provided.

```python
from django_extended_models.utils import __set_default_values

# Example usage:
model = ...
fields = ...

dictionary, fields = __set_default_values(model, fields)
```

#### `model_to_dict`

Converts a Django model object into a dictionary, recursively including related model objects up to a specified depth.

```python
from django_extended_models.utils import model_to_dict

# Example usage:
object = ...
fields = ...

dictionary = model_to_dict(object, fields=fields)
```

### `mixins.py`

#### `ToDictMixin`

Provides a method `to_dict` that converts a model instance to a dictionary.

```python
from django_extended_models.mixins import ToDictMixin

# Example usage:
class MyModel(ToDictMixin):
    pass

instance = MyModel()
dictionary = instance.to_dict()
```

### `models.py`

#### `BaseModel`

A base model that includes the `ToDictMixin`.

```python
from django_extended_models.models import BaseModel

# Example usage:
class MyModel(BaseModel):
    pass
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/EChachati/django-extended-models/blob/master/LICENSE) file for details.
