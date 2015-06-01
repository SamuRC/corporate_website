# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User, Permission
from core.models import News, Category, Event, Product, Classification
from django_summernote.widgets import SummernoteWidget


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    user_permissions = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Permission.objects.filter(
            content_type_id__in=[4, 7, 8, 9, 10, 11, 12]), label="Permisos de usuario", required=False,)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'is_active', 'user_permissions')

    def save(self, commit=False):
        # Save the provided password in hashed format
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    user_permissions = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Permission.objects.filter(
            content_type_id__in=[4, 7, 8, 9, 10, 11, 12]), label="Permisos de usuario", required=False,)

    class Meta:
        model = User
        # Add all the fields you want a user to change
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active', 'user_permissions')


#noticias
class NewsForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Category.objects.all(),
        label="Categorías", required=False,)
    body = forms.CharField(widget=SummernoteWidget(), required=True, label='Cuerpo (*)')
    video = forms.CharField(required=False, help_text='URL de YouTube: ejm. https://youtu.be/m6uc8AinCZA')

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        self.fields['title'] = forms.CharField(required=True, label='Título (*)')
        self.fields['is_published'].label = 'Publicar'
        self.fields['is_published'].required = False
        self.fields['image'].label = 'Imagen'
        self.fields['image'].required = False

    class Meta:
        model = News
        fields = ('title', 'body', 'is_published', 'image', 'video', 'categories')


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)

        self.fields['name'].label = 'Nombre (*)'

    class Meta:
        model = Category
        fields = ('name', )


class EventForm(forms.ModelForm):
    information = forms.CharField(widget=SummernoteWidget(), required=True, label='Descripción (*)')
    start_time = forms.DateTimeField(widget=forms.DateTimeInput(format='%d-%m-%Y %H:%M'),
                                     input_formats=('%d-%m-%Y %H:%M',),
                                     required=False, label='Hora de inicio')

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Nombre'
        self.fields['is_published'].label = 'Publicar'
        self.fields['is_published'].required = False
        self.fields['address'].label = 'Dirección'
        self.fields['address'].required = False
        self.fields['image'].label = 'Imagen'
        self.fields['image'].required = False

    class Meta:
        model = Event
        fields = ('name', 'information', 'address', 'image', 'is_published', 'start_time',)


class ProductForm(forms.ModelForm):
    body = forms.CharField(widget=SummernoteWidget(), required=True, label='Cuerpo (*)')
    description = forms.CharField(widget=forms.Textarea(), label='Descripción (*)')
    classifications = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, queryset=Classification.objects.all(),
        label="Clasificación", required=False,)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Nombre (*)'
        self.fields['logo'].required = False
        self.fields['logo'].label = 'Imagen'

    class Meta:
        model = Product
        fields = ('name', 'logo', 'description', 'body', 'classifications')


class ClassificationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ClassificationForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    class Meta:
        model = Classification
        fields = ('name', 'description', 'image')

