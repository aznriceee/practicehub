from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ["full_name", "email", "preference1", "preference2", "preference3"]
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        address, domain = email.split("@")
        site, com = domain.split(".")
        print email
        print self.cleaned_data.get('email')
        if not (site == "gmail" or site== "yahoo"):
            raise forms.ValidationError("Please use a gmail or yahoo account")
        return email