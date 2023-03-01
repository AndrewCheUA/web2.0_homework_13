from django.forms import ModelForm, CharField, TextInput, ModelChoiceField, ModelMultipleChoiceField, SelectMultiple
from .models import Tag, Quote, Author


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=125, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):
    text = CharField(required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all())
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all().order_by('name'),
                                          widget=SelectMultiple(attrs={"class": "form-select", "size": "7"}))

    class Meta:
        model = Quote
        fields = ['text', 'author']
        exclude = ['tags']


class AuthorForm(ModelForm):
    fullname = CharField(max_length=250, widget=TextInput())
    born_date = CharField(widget=TextInput())
    born_location = CharField(widget=TextInput())
    description = CharField(widget=TextInput())

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']