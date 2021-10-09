from django.db import models

class AnalysisModel(models.Model):
    image_path = models.CharField(
        blank=True,
        max_length=255,
        null=True
    )
    success = models.CharField(
        blank=True,
        max_length=255,
        null=True
    )
    message = models.CharField(
        blank=True,
        max_length=255,
        null=True
    )
    class_ai = models.IntegerField(
        blank=True,
        null=True,
        default=0
    )
    confidence = models.DecimalField(
        max_digits=5,
        decimal_places=4,
        blank=True,
        null=True,
        default=0.0000
    )
    request_timestamp = models.IntegerField(
        blank=True,
        null=True
    )
    response_timestamp = models.IntegerField(
        blank=True,
        null=True
    )
    def __str__(self):
        return self.message
