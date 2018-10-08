from django import forms
from posts.models import Post
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
class postForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("gameName","console","description", "condition","price","image")
        def __init__(self, *args, **kwargs):
            super(postForm, self).__init__(*args, **kwargs)

class editForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("gameName","console","description", "condition","price","image")
        widgets = {
             'image':NotClearableFileInput()
        }
        def __init__(self, post,*args, **kwargs):
            self.post=post
            super(editForm, self).__init__(*args, **kwargs)
            self.fields["gameName"].initial=post.gameName
            self.fields["console"].initial=post.console
            self.fields["description"].initial=post.description
            self.fields["condition"].initial=post.condition
            self.fields["price"].initial=post.price
