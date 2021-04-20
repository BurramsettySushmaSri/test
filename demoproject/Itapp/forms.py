from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Itapp.models import Update



class UserReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(
		attrs={"class":"form-control","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(
		attrs={"class":"form-control","placeholder":"Enter Password"}))
	class Meta:
		model = User
		fields = ['username']
		widgets = {
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"})
		}


class UpdateUser(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		widgets = {
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Username"}),
		"first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First Name"}),
		"last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter LastName"}),
		"email":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Email"})
		}

class UpdateProfile(forms.ModelForm):
	class Meta:
		model = Update
		fields = ['age','gender','image']
		widgets = {
		'age':forms.NumberInput(attrs={"class":"form-control"}),
		'gender':forms.Select(attrs={"class":"form-control"}),
		}  