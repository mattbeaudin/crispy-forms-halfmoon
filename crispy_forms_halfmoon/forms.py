from crispy_forms.helper import FormHelper
from django import forms


class HalfmoonHelper(FormHelper):
    """Form Helper for Halfmoon CSS"""

    form_class = ""
    field_class = "form-control"
    template = ""


class HalfmoonForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = HalfmoonHelper(self)


class HalfmoonModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = HalfmoonHelper(self)
