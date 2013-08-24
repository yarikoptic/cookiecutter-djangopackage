# -*- coding: utf-8 -*-

from django import forms

{% for model in cookiecutter.model_names.split(",") %}
from .models import {{ model }}
{% endfor %}

{% for model in cookiecutter.model_names.split(",") %}
class {{ model }}Form(forms.ModelForm):

    class Meta:
        model = {{ model }}

{% endfor %}