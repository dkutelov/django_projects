from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class FormControlClassFormMixin():
    def __init__(self, *args, **kwargs):
        for key in self.fields:
            self.fields[key].widget.attrs['class'] = 'form-control'


class UserLoginForm(AuthenticationForm, FormControlClassFormMixin):
    def __init__(self, *args, **kwargs):
        AuthenticationForm.__init__(self, *args, **kwargs)
        FormControlClassFormMixin.__init__(self)


class UserSignupForm(UserCreationForm, FormControlClassFormMixin):
    def __init__(self, *args, **kwargs):
        UserCreationForm.__init__(self, *args, **kwargs)
        FormControlClassFormMixin.__init__(self)