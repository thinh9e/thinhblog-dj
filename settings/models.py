from django.db import models


class Setting(models.Model):
    CATEGORY_CHOICES = {
        "general": "General",
        "social": "Social",
        "donation": "Donation",
    }

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
    key = models.CharField(max_length=50, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    value = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f"{self.category.title()}: {self.name}"
