from django import forms
from books.models import Books, Genres
from django.utils.text import slugify

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'author', 'description', 'image', 'city', 'genre', 'owner', 'slug', 'status']  # Добавляем owner

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Получаем пользователя из kwargs
        super().__init__(*args, **kwargs)
        self.fields['genre'].queryset = Genres.objects.all()

        # Автоматическое заполнение slug
        if 'name' in self.data:
            self.fields['slug'].initial = slugify(self.data['name'])

        # Задаем владельца
        if user:
            self.fields['owner'].initial = user


        # Скрываем поля, которые не должны быть доступны для ввода
        self.fields['owner'].widget = forms.HiddenInput()
        self.fields['slug'].widget = forms.HiddenInput()


    

