# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.db import TimeStampedModel

{% for model in cookiecutter.model_names.split(",") %}
class {{ model }}(TimeStampedModel):

    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

{% endfor %}