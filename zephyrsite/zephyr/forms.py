from django import forms
 
# import GeeksModel from models.py
from .models import CA
 
# create a ModelForm
class CAForm(forms.ModelForm):
    # specify the name of model to use
    # phone_number=PhoneNumberField(widget=PhoneNumberPrefixWidget(initial="IN"))
    class Meta:
        model = CA
        fields = "__all__"