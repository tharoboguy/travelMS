from django import forms
from .models import Booking, destination

class BookingForm(forms.ModelForm):

    destination = forms.ModelChoiceField(
        queryset=destination.objects.all(),
        empty_label="Select Destination",
    )

    class Meta:
        model = Booking
        fields = ['Name', 'destination', 'From', 'To', 'Price']
        widgets = {
            'From': forms.DateInput(attrs={'type': 'date'}),
            'To': forms.DateInput(attrs={'type': 'date'}),
        }

