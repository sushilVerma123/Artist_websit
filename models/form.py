from django import forms
from django.forms import ModelForm
from .products import Products


class Add_form(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'category', 'description', 'image', 'prices']
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control form-control-lg", 'placeholder': "Title"}),
            'description': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Description"}),
            'image': forms.FileInput(attrs={'class': "form-control form-control-lg"}),
            'prices': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'category': forms.Select(attrs={'class': 'custom-select form-control form-control-lg'})

        }
        # fields = '__all__'
