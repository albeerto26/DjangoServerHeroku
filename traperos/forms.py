"""Import de forms para generacion de formularios."""
from django import forms


class AlertaForm(forms.Form):
    """Formulario de alertas."""

    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
