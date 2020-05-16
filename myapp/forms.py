from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=30)
    post_type = forms.BooleanField(required=False)
    text = forms.CharField(widget=forms.Textarea)
