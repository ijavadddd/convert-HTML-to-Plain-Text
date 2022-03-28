from django import forms
from . import models

class Convert_Html_To_Text(forms.Form):
    HtmlCode=forms.CharField(widget=forms.Textarea)
    HtmlCode.widget.attrs.update({'placeholder':'Paste your HTML here to convert','class':'w-100 my-4 mx-auto px-2 px-2'})




