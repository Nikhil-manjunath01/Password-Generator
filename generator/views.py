from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):
    characters=list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('UPPERCASE'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('NUMBERS'):
        characters.extend(list('1234567890') )
    if request.GET.get('SPECIAL CHARACTER'):
        characters.extend(list('!@#$%^&*()'))
    length=int(request.GET.get('length',12))
    thepassword=''
    for x in range(length):
        thepassword+=random.choice(characters)            
    return render(request,'generator/password.html',{'password':thepassword})
    