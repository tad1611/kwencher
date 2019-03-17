from django import forms
from datetime import *
from .models import SPECIALS_HDR_FCT,SPECIALS_LN_FCT, Post
from dal import autocomplete

    
    
class SPECIALS_HDR_FORM(forms.ModelForm):
    class Meta:
        model = SPECIALS_HDR_FCT
        fields =(
    'SPECIAL_HDR_ID',
    'SPECIAL_HDR_DESC',
    'LOCATION_KEY',
    'START_TIME' ,
    'END_TIME' ,
    'DAY_MON_FLG', 
    'DAY_TUE_FLG' ,
    'DAY_WED_FLG' ,
    'DAY_THU_FLG' ,
    'DAY_FRI_FLG' ,
    'DAY_SAT_FLG' ,
    'DAY_SUN_FLG')
        widgets = {
            'LOCATION_KEY': autocomplete.ModelSelect2(url='location-autocomplete'),
        }



class SPECIALS_LN_FORM(forms.ModelForm):
 
    class Meta:
        model = SPECIALS_LN_FCT
        fields =('BEER_ID', 'SERVING_SIZE', 'PRICE_AMT',)
        widgets = {
            'BEER_ID': autocomplete.ModelSelect2(url='beer-autocomplete')
        }


class NameForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)