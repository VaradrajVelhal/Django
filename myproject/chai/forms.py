from django import  forms
from .models import ChaiVarity   

class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(),label='Select chai Variety')