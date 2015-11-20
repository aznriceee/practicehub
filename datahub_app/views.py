from django.shortcuts import render
from .forms import SignUpForm
# Create your views here.



def home(request):
    
    if request.user.is_authenticated():
        title = "hello %s" %(request.user)
    form = SignUpForm(request.POST or None)
    
    context = {
        "title" : title,
        "form" : form
    }
    if request.method == "POST":
        print request.POST
        
    if form.is_valid():
        instance = form.save(commit = False)
        #commit = false allows you to do things before saving
        instance.save()
        context = {
            "title" : "THANK YOU!"
        }

    return render(request, "home.html", context)