from django.db import models
from django.utils.translation import gettext_lazy as _
class StatusChoices(models.TextChoices):
    DRAFT = 'draft', 'Draft'
    PUBLISHED = 'published', 'Published'
    ARCHIVED = 'archived', 'Archived'

class RecommendedChoices(models.TextChoices):
    YES = 'yes', 'Yes'
    NO = 'no', 'No'

class PositionChoices(models.TextChoices):
    MAIN = 'main', _('Main')
    PRIME = 'prime', _('Prime')



