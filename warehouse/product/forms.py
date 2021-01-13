from user.models import All_categories,Categories,Product
from django import forms

class AllCategoriesForm(forms.ModelForm):
    class Meta:
        model=All_categories
        fields=['name']
        labels={'name':'name'}
class CategoriesForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields='__all__'
        labels={'name':'name','status':'status'}