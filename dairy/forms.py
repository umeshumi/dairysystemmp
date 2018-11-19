from django import forms
from .models import dairyNode


class dairyForm(forms.ModelForm):
	class Meta:
		model = dairyNode
		fields = ['Quantity_of_milk', 'Person_Name']

class searchForm(forms.Form):
	search_by_day = forms.BooleanField(required=False)
	Date = forms.DateField(widget=forms.SelectDateWidget(), required=False)
	Node = forms.CharField(required=False)