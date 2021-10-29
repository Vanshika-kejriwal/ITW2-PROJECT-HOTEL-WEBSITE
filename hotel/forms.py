from django import forms
from .models import costomer

class dateinput(forms.DateInput):
    input_type = 'date'

class customer_registration(forms.ModelForm):
    class Meta:
         model = costomer 
         fields = ['name','Phone','IDproof','ID_num','Adults','children','RoomCategory','CheckIN','CheckOUT']
         widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'Phone':forms.TextInput(attrs={'class':'form-control'}),
            'IDproof':forms.Select( attrs={'class':'form-control'}, choices=(('1','--Select--'),('2','Passport'), ('3','Adhar Card'), ('4','Pan Card'), ('5','Driving Licence'))),
            'ID_num':forms.TextInput(attrs={'class':'form-control'}),
            'Adults':forms.NumberInput(attrs={'class':'form-control'}),
            'children':forms.NumberInput(attrs={'class':'form-control'}),
            'RoomCategory':forms.Select( attrs={'class':'form-control'}, choices=(('1','--Select--'),('Regular','Regular'), ('Deluxe','Deluxe'), ('Suite','Suite'))),
            'CheckIN': dateinput(attrs={'class':'form-control'}),
            'CheckOUT':dateinput(attrs={'class':'form-control'})
         }

class cancel_booking(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    CheckIN = forms.DateField(widget=dateinput(attrs={'class':'form-control'}))
    CheckOUT = forms.DateField(widget=dateinput(attrs={'class':'form-control'})) 
    room_catagory = forms.CharField(widget=forms.Select(attrs={'class':'form-control'}, choices=(('1','--Select--'),('Regular','Regular'), ('Deluxe','Deluxe'), ('Suite','Suite')))) 