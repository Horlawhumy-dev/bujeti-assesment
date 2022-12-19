from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" id="username" type="text'}),
        max_length=100, label="Username", )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'shadow appearance-none border border-red-500 rounded w-full py-2 px-3 text-gray-700 mb-3 leading-tight focus:outline-none focus:shadow-outline mt-8'}),
        max_length=20, label="Password")
    

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

