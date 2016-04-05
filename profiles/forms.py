from django import forms
from .models import Profile, Reviews
from django.forms import extras
from django.contrib.auth.models import User
from django.forms.widgets import FileInput, CheckboxInput
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

class NotClearableFileInput(FileInput):

    template_with_initial = '%(clear_text)s: %(clear)s<br /><br />%(input_text)s: %(input)s<br />'

    url_markup_template = '<br/>'
    def render(self, name, value, attrs=None):
        substitutions = {
            'clear_text': "Remove Current Image",
            'input_text': "Change Image",

        }
        template = '%(input)s'
        substitutions['input'] = super(NotClearableFileInput, self).render(name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = format_html(self.url_markup_template,
                                               value.url,
                                               force_text(value))
            substitutions['clear'] = CheckboxInput().render("clear", False, attrs={'id': 'clear'})

        return mark_safe(template % substitutions)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    #password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("email", "password","first_name","last_name")
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs) 
        self.fields["email"].required = True
        self.fields["password"].required = True
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("body", "birthDate","gender","city","country","address","postalCode","phoneNumber","image")
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        


class EditUser(forms.ModelForm):
    class Meta:
        model=User
        fields = ("first_name","last_name") 

        def __init__(self,user,*args,**kwargs):
            #self.user=user
            super(EditUser, self).__init__(*args,**kwargs)

            self.fields["first_name"].initial = user.first_name
            self.fields["last_name"].initial = user.last_name

class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ("body", "birthDate","gender","city","country","address","postalCode","phoneNumber","image")
        widgets = {
             'image':NotClearableFileInput()
        }
        def __init__(self,*args,**kwargs):
            #self.profile=profile
            super(EditProfile,self).__init__(*args, **kwargs)

            self.fields["body"].initial=profile.body
            self.fields["birthDate"].initial=profile.birthDate
            self.fields["gender"].initial=profile.gender
            self.fields["city"].initial=profile.city
            self.fields["country"].initial=profile.country
            self.fields["address"].initial=profile.address
            self.fields["postalCode"].initial=profile.postalCode
            self.fields["phoneNumber"].initial=profile.phoneNumber




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("body", "ratings")
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)