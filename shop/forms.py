from django import forms

from shop.models import Category


class ProductForm(forms.Form):

    name = forms.CharField(
        label='Product name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product name'
            }
        )
    )

    slug = forms.SlugField(
        label='Slug',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product slug'
            }
        )
    )

    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product description',
                'rows': 5
            }
        )
    )

    price = forms.IntegerField(
        label='Price',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product price'
            }
        )
    )

    category_id = forms.ModelChoiceField(
        label='Category',
        queryset=Category.objects.all(),
        empty_label='Select a category',
        widget=forms.Select(
            attrs={
                'class': 'form-select'
            }
        )
    )