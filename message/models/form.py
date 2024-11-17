from django import forms
from django.forms import ModelForm
from .profile import Profile


class Add_form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name', 'description', 'gender', 'mobile', 'address', 'image', 'instagram', 'twitter', 'facebook',
                  'linkedin']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': "form-control form-control-lg"}),
            'description': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Description"}),
            'address': forms.TextInput(attrs={'class': "form-control", 'placeholder': "Address"}),
            'image': forms.FileInput(attrs={'class': "form-control form-control-lg"}),
            'facebook': forms.URLInput(attrs={'class': "form-control form-control-lg"}),
            'instagram': forms.URLInput(attrs={'class': "form-control form-control-lg"}),
            'twitter': forms.URLInput(attrs={'class': "form-control form-control-lg"}),
            'linkedin': forms.URLInput(attrs={'class': "form-control form-control-lg"}),
            'mobile' :forms.NumberInput(attrs={'class': "form-control form-control-lg"}),
            'gender' : forms.Select(attrs={'class': "form-control form-control-lg"})

        }
