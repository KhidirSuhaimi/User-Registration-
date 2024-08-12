from django.shortcuts import render
from . import form

# Create your views here.

def userRegistrationView(request):
    formactual = form.UserRegistrationForm
    if request.method == 'POST':
        formactual = form.UserRegistrationForm(request.POST)
        if formactual.is_valid():
            print("Form is Valid")
            print("User Name: ",formactual.cleaned_data['userName'])
            print('Password: ', formactual.cleaned_data['password'])
    return render(request,'formApp/userRegistration.html',{'form':formactual})

