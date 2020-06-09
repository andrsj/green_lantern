from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(required=False)


class ArticleForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
