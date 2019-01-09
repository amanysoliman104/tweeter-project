from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
    #to make sure that the user logged in frist  
    def form_valid(self,form):
        if self.request.user.is_authenticated(): # the identify of user is right ?
            form.instance.user=self.request.user
            return super(FormUserNeededMixin,self).form_valid(form)
        else:
            form.errors[forms.forms.NON_FIELD_ERRORS]=ErrorList([ "User must be logged to continue"])
            return self.form_invalid(form)

# when i log in with  user name and put contnet and data  with this user then i can update the tweets ... 
#but when i change my username for a specific tweet  i cannot update its data  so we do this class to prevent update  with new username
class UserOwnerMixin(object):
    def form_valid(self,form):

        if form.instance.user==self.request.user:
            return super(UserOwnerMixin,self).form_valid(form)

        else:
            form.errors[forms.forms.NON_FIELD_ERRORS]=ErrorList([ "this user not allowed to chande data ."])
            return self.form_invalid(form)