from django.shortcuts import render
from django.views import View
from . import forms
# Create your views here.

class Main_Page(View):
    def get(self, request):
        context={
            'convertor_form':forms.Convert_Html_To_Text
        }
        return render(request,'main_page/main_page.html',context)