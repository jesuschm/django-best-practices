import uuid

from django.db import models


class BaseModel(models.Model):
    """
    An abstract base class model that provides:
    id as primary key, self-updating 'created' and 'modified' fields.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    created = models.DateTimeField(
        verbose_name="created date",
        auto_now_add=True,
    )
    modified = models.DateTimeField(verbose_name="modified date", auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created",)
        indexes = [
            models.Index(fields=["created"]),
            models.Index(fields=["modified"]),
        ]
