from django import forms  
from .models import *

class BookmarkForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    url = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    source_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Bookmark
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__' 

        labels = {
            'location': ('Please Drag the Pointer at Prticular Loaction (For storing Latitude & Longitude) - '),
        }

class CustomerBookmarkForm(forms.ModelForm):
    bookmark = forms.ModelChoiceField(queryset=Bookmark.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(),required=False,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = CustomerBookmark
        fields = '__all__'
