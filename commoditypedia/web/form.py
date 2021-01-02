from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import authenticate, get_user_model
from database.models import sex_choices
# from django.core.validators import RegexValidatorf

class SignIn(forms.Form):
    username= forms.CharField(
        label='نام کاربری',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': 'text',
                                      'class': 'form-control',
                                      'placeholder': 'نام کاربری',
                                      'name':'username',
                                      'id': "username",
                                      'aria-describedby': 'aria-emailHelp',


        })
    )
    password = forms.CharField(
        label="رمز عبور",
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "password",
                                      'class': "form-control",
                                      'placeholder': "رمز عبور",
                                      'name':'password',
                                      'id': 'password',
                                      'aria-describedby': 'aria-emailHelp'
        })
    )
    submit = forms.CharField(
        widget=forms.TextInput(attrs={'type': "submit",
                                      'class': "btn btn-block mybtn btn-primary tx-tfm",
                                      "placeholder": "رمز عبور",
                                      "name":"password",
                                      'id': "password",
                                      'value': "ورود"
        })
    )
###################################
class SignUp(forms.Form):
    username= forms.CharField(
        label='نام کاربری',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={"type": "text",
                                      "class": "form-control",
                                      "placeholder": "نام کاربری",
                                      "name":"username",
                                      "id": "username",
                                      "aria-describedby": "aria-emailHelp"
        })
    )
    email = forms.CharField(
        label='ایمیل',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "email",
                                      'class': "form-control",
                                      "placeholder": "ایمیل",
                                      "name":"email",
                                      'id': "email",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    password = forms.CharField(
        label='پسورد',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "password",
                                      'class': "form-control",
                                      "placeholder": "رمز عبور",
                                      "name":"password",
                                      'id': "password",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    re_password = forms.CharField(
        label='تکرار پسورد',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "password",
                                      'class': "form-control",
                                      "placeholder": "تکرار رمز عبور",
                                      "name":"re_password",
                                      'id': "re_password",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    submit = forms.CharField(
        widget=forms.TextInput(attrs={'type': "submit",
                                      'class': "btn btn-block mybtn btn-primary tx-tfm",
                                      "name":"submit",
                                      'value': "ثبت نام"
        })
    )
###################################
class Add(forms.Form):
    title = forms.CharField(
        label='عنوان',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "text",
                                      'class': "form-control",
                                      "placeholder": "عنوان",
                                      "name":"title",
                                      'id': "title",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    price = forms.IntegerField(
        label='قیمت',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.NumberInput(attrs={'type': "number",
                                      'class': "form-control",
                                      "placeholder": "قیمت",
                                      "name":"price",
                                      'id': "price",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    image = forms.ImageField(
        label='تصویر',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.FileInput(attrs={'type': "file",
                                      'class': 'form-control',
                                      "placeholder": "تصویر",
                                      "name":"image",
                                      'id': "image",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    description = forms.CharField(
        label='توضیحات',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "text",
                                      'class': "form-control",
                                      "placeholder": "توضیحات",
                                      "name":"description",
                                      'id': "description",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    submit = forms.CharField(
        widget=forms.TextInput(attrs={'type': "submit",
                                      'class': "btn btn-block mybtn btn-primary tx-tfm",
                                      "name":"submit",
                                      'value': "ارسال"
        })
    )
##########################################
class CommentSection(forms.Form):
    body = forms.CharField(
        label='دیدگاه',
        required=True,
        widget=forms.TextInput(attrs={'type': "text",
                                      'class': "form-control",
                                      "placeholder": "دیدگاه",
                                      "name":"body",
                                      'id': "body",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
##########################################
class UserInfos(forms.Form):
    customer = forms.BooleanField(
        label='مشتری',
        required=False,
    )
    full_name = forms.CharField(
        label='نام کامل',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "text",
                                      'class': "form-control",
                                      "placeholder": "نام کامل",
                                      "name":"full_name",
                                      'id': "full_name",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    bio = forms.CharField(
        label='توضیحات',
        required=False,
        widget=forms.TextInput(attrs={'type': "text",
                                      'class': "form-control",
                                      "placeholder": "توضیحات",
                                      "name":"bio",
                                      'id': "bio",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    job = forms.CharField(
        label='شغل',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "text",
                                      'class': "form-control",
                                      "placeholder": "شغل",
                                      "name":"job",
                                      'id': "job",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    sex = forms.ChoiceField(choices=sex_choices)
    phone_number = forms.CharField(
        label='شماره موبایل',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.TextInput(attrs={'type': "text",
                                      'class': "form-control",
                                      "placeholder": "شماره موبایل",
                                      "name":"phone_number",
                                      'id': "phone_number",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    birth_date = forms.DateField(
        label='تاریخ تولد',
        required=False,
        widget=forms.TextInput(attrs={'type': "text",
                                      'class': "form-control",
                                      "placeholder": "1996-01-30",
                                      "name":"birth_date",
                                      'id': "birth_date",
                                      'aria-describedby': "aria-emailHelp"
        })
    )    
    image = forms.ImageField(
        label='تصویر',
        error_messages={'required': 'لطفا این قسمت را تکمیل نمایید'},
        widget=forms.FileInput(attrs={'type': "file",
                                      'class': 'form-control',
                                      "placeholder": "تصویر",
                                      "name":"image",
                                      'id': "image",
                                      'aria-describedby': "aria-emailHelp"
        })
    )
    address_lat = forms.CharField(
        widget=forms.TextInput(attrs={'type': "hidden",
                                      "id":"address_lat",
        })
    )
    address_lon = forms.CharField(
        widget=forms.TextInput(attrs={'type': "hidden",
                                      "id":"address_lon",
        })
    )
    submit = forms.CharField(
        widget=forms.TextInput(attrs={'type': "submit",
                                      'class': "btn btn-block mybtn btn-primary tx-tfm",
                                      "name":"submit",
                                      'value': "ارسال"
        })
    )