
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

#### `model_to_dict`

Converts a Django model object into a dictionary, recursively including related model objects up to a specified depth.

##### Parameters

- object (required): The instance of the Django model that you want to convert to a dictionary.
- fields (optional): Specifies which fields of the model object should be included in the resulting dictionary. It can be either a list of field names, a dictionary where the keys are field names and the values are additional options for each field, or the string '__all__' to include all fields.
- current_recursion_depth (optional): The current recursion depth, tracking how many levels deep the function has traversed through nested models.
- max_recursion_depth (optional): The maximum depth of recursion allowed when converting a model object to a dictionary.

##### Examples

Basic Usage

```python
from django_extended_models.utils import model_to_dict
from django.db import models

# Example usage with a Django model instance
my_model_instance = MyModel.objects.get(pk=1)
resulting_dict = model_to_dict(my_model_instance)
print(resulting_dict)
```

Specify Fields

```python
from django_extended_models.utils import model_to_dict
from django.db import models

# Example usage with specific fields
my_model_instance = MyModel.objects.get(pk=1)
resulting_dict = model_to_dict(my_model_instance, fields=['field1', 'field2'])
print(resulting_dict)
```

Include All Fields

```python
from django_extended_models.utils import model_to_dict
from django.db import models

# Example usage to include all fields
my_model_instance = MyModel.objects.get(pk=1)
resulting_dict = model_to_dict(my_model_instance, fields='__all__')
print(resulting_dict)
```

Recursion Depth

```python
from django_extended_models.utils import model_to_dict
from django.db import models

# Example usage with recursion depth limit
my_model_instance = MyModel.objects.get(pk=1)
resulting_dict = model_to_dict(my_model_instance, max_recursion_depth=2)
print(resulting_dict)
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

## Contributing

Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues or have suggestions, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/EChachati/django-extended-models/blob/master/LICENSE) file for details.
