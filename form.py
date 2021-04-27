from django import forms


class get_url(forms.Form):
    image_url = forms.URLField()

    