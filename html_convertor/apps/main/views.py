from django.shortcuts import render
from django.views import View
from . import forms
import re
# Create your views here.

class Main_Page(View):
    def get(self, request):
        form=forms.Convert_Html_To_Text(request.GET)    
        context={
            'convertor_form':form
        }
        return render(request,'main_page/main_page.html',context)
    
    def post(self, request):
        form=forms.Convert_Html_To_Text(request.POST)    
        if form.is_valid():
            data=form.cleaned_data
            html_code=data["HtmlCode"]
            ss=re.sub("(?:</*\w.*?>)","",html_code)
            plain_text=re.sub("\n\s\s","\n",ss)
        context={
            'convertor_form':form,
            "plain_text":plain_text,
        }
 
        return render(request,'main_page/main_page.html',context)
