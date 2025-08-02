from django import forms
class GarbageForm(forms.Form):
    GARBAGE_CHOICES = [
        ('plasticbottle', 'Plastic Bottle'),
        ('can', 'Can'),
    ]
    garbage = forms.ChoiceField(choices=GARBAGE_CHOICES)