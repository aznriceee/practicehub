from django.db import models

# Create your models here.

class SignUp(models.Model):
    full_name = models.CharField(max_length = 50, blank = False)
    email = models.EmailField(blank = False)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False) 
    preference1 = models.CharField(max_length = 50, blank = False)
    preference2 = models.CharField(max_length = 50, blank = True)
    preference3 = models.CharField(max_length = 50, blank = True)
    #auto_now_add: save now, never changed; auto_now: save anytime
    
    def __unicode__(self):
        return self.full_name
    
