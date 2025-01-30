from django.core.exceptions import ValidationError

from django.forms import ModelForm

from catalog.models import Product

FORBIDDEN_WORDS = ("казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар",)

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        if name in FORBIDDEN_WORDS or description in FORBIDDEN_WORDS:
            raise ValidationError('Имя/описание продукта не может содержать это слово')
        return name, description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price