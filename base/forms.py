from django import forms
from .models import UserForm,Mailing


class UserFormQuestion(forms.ModelForm):
    name = forms.CharField(max_length=40,widget=forms.TextInput(attrs={
        "type":"name",
        "class":"form-control",
        "id":"name",
        "placeholder":"Name",
        "required":"",
        "pattern":"[A-Za-z]{3,}",
        "title":"minimal lenght 3"
    }))

    phone = forms.CharField(max_length=15,widget=forms.TextInput(attrs={
        "type":"text",
        "class":"form-control",
        "name":"phone",
        "id":"phone",
        "required":"",
        "placeholder":"Your Phone",
        "pattern":"^(\d{3}[- .]?){2}\d{4}$",
        "title":"Input number in format xxx xxx xxxx",

    }))

    date = forms.DateField(widget=forms.DateInput(attrs={
        "type":"date",
        "class":"form-control",
        "name":"date",
        "id":"date",

    }))

    time = forms.TimeField(widget=forms.TimeInput(attrs={
        "type": "time",
        "class": "form-control",
        "name": "time",
        "id": "time",
    }))

    text = forms.CharField(max_length=500,widget=forms.Textarea(attrs={
        "class":"form-control textarea",
        "name":"message",
        "rows":"5",
        "placeholder":"Message Theme"

    }))
    class Meta:
        model = UserForm
        fields = "__all__"


class MailingForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "type" : "email",
        "class" :"form-control mail-input",
        "id" : "mailing",
        "placeholder" : "Enter your email",
    }))

    class Meta:
        model = Mailing
        fields = ("email",)