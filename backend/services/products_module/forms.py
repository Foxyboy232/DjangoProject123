from django import forms
from services.products_module.models import Product, Currency

class UpdateProductForm(forms.ModelForm):
    #currency_id = forms.IntegerField()

    in_stock = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    currency = forms.ModelChoiceField(
        queryset=Currency.objects.all(),
        to_field_name="pk",
        required=True,
        widget=forms.Select(attrs={"class": "form-control"})
    )
    class Meta:
        model = Product
        #fields = ('title', 'description', 'price', 'currency_id', 'in_stock')
        fields = ('title', 'description', 'price', 'in_stock', 'currency')


