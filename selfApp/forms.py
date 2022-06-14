from turtle import title
from django import forms
from .models import * 

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Actor
        fields = ['title', 'content', 'category','photo','is_published']
    
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content': forms.Textarea(attrs={'cols':60,'rows':8})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title)>200:
            raise forms.ValidationError('Длина больше 200 символов')
        return title
    