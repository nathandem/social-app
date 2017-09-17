from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# UserCreationForm already here

class UserCreateForm(UserCreationForm): # different names

    class Meta:
        fields = ('username','email','password1','password2')
        # password2 is just a confirmation of password1
        model = get_user_model()

    # we overwrite the __init__ method to define our own labels
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs) # this 1st line is necessary
        # let's set up the labels!
        self.fields['username'].label = 'Display name'
        self.fields['email'].label = 'Email Address'
