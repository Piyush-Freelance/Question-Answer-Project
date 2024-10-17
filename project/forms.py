from django import forms

class PasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if not username and not email:
            raise forms.ValidationError("Please provide either a username or an email address.")
        
        return cleaned_data
