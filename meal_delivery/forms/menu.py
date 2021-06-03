from django.forms import ModelForm, DateInput
from meal_delivery.models.menu import Menu


class MenuForm(ModelForm):

    class Meta:
        fields = 'for_day',
        model = Menu
        widgets = {
            'for_day': DateInput(format='%Y-%m-%d',
                                 attrs={'class':'form-control', 'type':'date'})
        }
