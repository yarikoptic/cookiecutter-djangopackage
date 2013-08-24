# -*- coding: utf-8 -*-

from django.contrib import admin

{% for model in cookiecutter.model_names.split(",") %}
from .models import {{ model }}
{% endfor %}

{% for model in cookiecutter.model_names.split(",") %}
admin.site.register({{model}})
{% endfor %}