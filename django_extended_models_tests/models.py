from django.db import models

from django_extended_models.mixins import ToDictMixin


class RelatedModel1(models.Model):
    related_field1 = models.CharField(max_length=100)


class RelatedModel2(models.Model):
    related_field1 = models.ForeignKey(RelatedModel1, on_delete=models.CASCADE, default=1)
    related_field2 = models.CharField(max_length=100)


class RelatedModel3(models.Model):
    related_field1 = models.ForeignKey(RelatedModel1, on_delete=models.CASCADE)
    related_field2 = models.ForeignKey(RelatedModel2, on_delete=models.CASCADE, default=1)


class YourModel(ToDictMixin, models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField(blank=True, null=True)
    related_field1 = models.ForeignKey(RelatedModel1, on_delete=models.CASCADE)
    related_field2 = models.ForeignKey(RelatedModel2, on_delete=models.CASCADE)
    related_field3 = models.ForeignKey(RelatedModel3, on_delete=models.CASCADE)
