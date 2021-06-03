from django import forms


class OrderForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={'required': "Input quantity."},
        label="quantity", widget = forms.HiddenInput
    )
    product = forms.IntegerField(
        error_messages={'required': "Input product name."},
        label="product" , widget = forms.HiddenInput
    )
    option = forms.CharField(
        error_messages={'required': "Add Feature"},
        label="option description", widget = forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.user
        option = self.request.POST.getlist('selected')

        if not (quantity and product and user):
            self.add_error('quantity', "수량이 없습니다.")
            self.add_error('product', "상품이 없습니다.")

class CartForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    quantity = forms.IntegerField(
        error_messages={'required': "Input quantity."},
        label="quantity", widget=forms.HiddenInput
    )
    product = forms.IntegerField(
        error_messages={'required': "Input product name."},
        label="product", widget=forms.HiddenInput
    )
    option = forms.CharField(
        error_messages={'required': "Add Feature"},
        label="option description", widget = forms.HiddenInput
    )
    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        user = self.request.user
        option = self.request.POST.getlist('selected')
        if not (quantity and product and user):
            self.add_error('quantity', "수량이 없습니다.")
            self.add_error('product', "상품이 없습니다.")
