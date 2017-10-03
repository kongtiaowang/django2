from django import forms

class SuggestionForm(forms.Form):
	"""docstring for SuggestionForm"""
	name = forms.CharField()
	email = forms.EmailField()
	suggestion = forms.CharField(widget=forms.Textarea)
