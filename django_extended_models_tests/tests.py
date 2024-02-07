from django.test import TestCase

from django_extended_models_tests.models import (
    RelatedModel1,
    RelatedModel2,
    RelatedModel3,
    YourModel,
)


class TestExtendedModels(TestCase):
    def test_model_to_dict(self):
        related_model1 = RelatedModel1.objects.create(related_field1="related_field1")
        related_model2 = RelatedModel2.objects.create(related_field2="related_field2")
        related_model3 = RelatedModel3.objects.create(related_field1=related_model1)
        your_model = YourModel.objects.create(
            field1="field1",
            field2=1,
            related_field1=related_model1,
            related_field2=related_model2,
            related_field3=related_model3,
        )

        expected_dict = {
            "id": 1,
            "field1": "field1",
            "field2": 1,
            "timestamp": your_model.timestamp,
            "data": None,
            "related_field1": {
                "id": related_model1.id,
                "related_field1": "related_field1",
            },
            "related_field2": {
                "id": related_model2.id,
                "related_field2": "related_field2",
            },
            "related_field3": {"id": related_model3.id},
        }

        self.assertEqual(your_model.to_dict("__all__"), expected_dict)
        self.assertEqual(
            your_model.to_dict(fields=["field1", "related_field1"]),
            {
                "field1": "field1",
                "related_field1": {
                    "id": related_model1.id,
                    "related_field1": "related_field1",
                },
            },
        )
        self.assertEqual(
            your_model.to_dict(
                fields={
                    "field1": {"exclude": True},
                    "related_field1": {"fields": ["related_field1"]},
                    "data": "default",
                }
            ),
            {
                "field1": "field1",
                "related_field1": {
                    "id": related_model1.id,
                    "related_field1": "related_field1",
                },
                "data": "default",
            },
        )
