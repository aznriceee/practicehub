from django.contrib import admin

# Register your models here.
from .forms import SignUpForm
from .models import SignUp



class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "email", "preference1", "preference2", "preference3", "timestamp"]
    form = SignUpForm
        
        
admin.site.register(SignUp, SignUpAdmin)