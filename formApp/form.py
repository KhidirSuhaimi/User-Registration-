from django import forms

class UserRegistrationForm(forms.Form):
    userName = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)
    
    # def clean(self):
    #     user_cleaned_data = super().clean()
    #     inputFirstName = user_cleaned_data['firstName']
    #     if len(inputFirstName) >20:
    #         raise forms.ValidationError('The max length of firstName is 20 characters')
        
    #     inputEmail = user_cleaned_data['email']
    #     if inputEmail.find('@') == -1:
    #         raise forms.ValidationError('The email should contain @')

    def clean(self):
        user_cleaned_data = super().clean()
        inputPassword = user_cleaned_data['password']
        
        if len(inputPassword)<8:
            raise forms.ValidationError('Minimum 8 characters for Password')
        if not any(char.isupper() for char in inputPassword):
            raise forms.ValidationError('Password must contain at least one capital letter.')