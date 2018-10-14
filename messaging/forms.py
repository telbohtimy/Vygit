from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs) 
        self.fields['body'].required = True