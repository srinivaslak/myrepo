from django import forms
class StudentForm(forms.Form):
    sno = forms.IntegerField(
        label='Enter Student Number',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Student Number',
                'class': 'form-control',
            }
        )
    )
    sname = forms.CharField(
        label='Enter Student Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Student Name',
                'class': 'form-control',
            }
        )
    )
    sloc = forms.CharField(
        label='Enter Student Location',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Student Location',
                'class': 'form-control',
            }
        )
    )
    sfee = forms.IntegerField(
        label='Enter Student Fee',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Student Fee',
                'class': 'form-control',
            }
        )
    )