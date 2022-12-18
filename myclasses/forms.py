from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, label="Password")
    

class ClassCreateForm(forms.Form):
    room_token = forms.CharField(max_length=100, required=True, label="Your unique Id")
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description', 'rows': 4, 'cols':40}))
    start = forms.CharField(max_length=100, required=False, label="Start date (Format=`2018-11-18T21:30:00+0000`)")
    end = forms.CharField(max_length=100, required=False, label="End date (Format=`2018-11-18T21:30:00+0000`)")
    max_participants = forms.IntegerField(required=False, label="Max participants")
    record_class = forms.BooleanField(required=False, label="Record class")
    
    
    
class UpdateClassForm(forms.Form):
    uuid = forms.CharField(max_length=100, required=True)
    room_token = forms.CharField(max_length=100, required=True, label="Your unique Id")
    description = forms.CharField(
        required=False, widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description', 'rows': 4, 'cols':40}))
    start = forms.CharField(max_length=100, required=False, label="Start date (Format=`2018-11-18T21:30:00+0000`)")
    end = forms.CharField(max_length=100, required=False, label="End date (Format=`2018-11-18T21:30:00+0000`)")
    max_participants = forms.IntegerField(required=False, label="Max participants")
    record_class = forms.BooleanField(required=False, label="Record class")

