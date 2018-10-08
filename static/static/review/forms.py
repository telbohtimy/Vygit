from django import forms
from .models import Review
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("body", "ratings")
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)