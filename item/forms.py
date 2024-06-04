from django import forms

from .models import Item

FIELD_CLASSES = "w-full py-4 px-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "name", "description", "price", "image")
        widgets = {
            "category": forms.Select(attrs={"class": FIELD_CLASSES}),
            "name": forms.TextInput(attrs={"class": FIELD_CLASSES}),
            "description": forms.Textarea(attrs={"class": FIELD_CLASSES}),
            "price": forms.TextInput(attrs={"class": FIELD_CLASSES}),
            "image": forms.FileInput(attrs={"class": FIELD_CLASSES}),
        }
