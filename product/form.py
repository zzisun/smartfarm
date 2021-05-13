from django import forms
from .models import Product

class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={'required':"Input product name."},
        max_length = 50, label = "Product name"
    )
    price = forms.IntegerField(
        error_messages={'required' : "Input price."},
        label = "price"
    )
    stock = forms.IntegerField(
        error_messages={'required':"Input stock."},
        label = "stock"
    )
    description = forms.CharField(
        error_messages={'required':"Text description"},
        label = "Product description"
    )
    image = forms.ImageField(
        error_messages={'required':'Image file'},
        label = "image"
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        stock = cleaned_data.get('stock')
        description = cleaned_data.get('description')
        image = cleaned_data.get('image')

        if not (name and price and stock and description and image):
            self.add_error('name', "No data.")
            self.add_error('price', "No data.")
            self.add_error('stock', "No data.")
            self.add_error('description', "No data.")
            self.add_error('image', "No data.")