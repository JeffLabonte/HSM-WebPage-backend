from django.db import models


class ScriptQueryAudit(models.Model):
    transaction_id = models.UUIDField(primary_key=True)
    created = models.DateField(auto_created=True)
