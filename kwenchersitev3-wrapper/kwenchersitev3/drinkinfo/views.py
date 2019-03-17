from django.shortcuts import render, redirect
from models import SPECIALS_HDR_FCT, BEER_DIM, LOCATION_DIM, SPECIALS_LN_FCT
from forms import SPECIALS_HDR_FORM, SPECIALS_LN_FORM,PostForm
from django.utils import timezone
from datetime import datetime
from dal import autocomplete
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .forms import NameForm


def auth_view(request):
    username = request.POST.get("username", False)
    password = request.POST.get("password", False)
    user = authenticate(username = username, 
                        password = password)      
    
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login')


        # Re
##AUTOCOMPLETEVIEW
class location_auto_complete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = LOCATION_DIM.objects.all()
        if self.q:
            qs = qs.filter(PLACE_NAME__istartswith=self.q)
        return qs
    
    
##AUTOCOMPLETEVIEW
class beer_auto_complete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = BEER_DIM.objects.all()
        if self.q:
            qs = qs.filter(NAME__istartswith=self.q)
        return qs

# Create your views here.
def home_page(request):
    if request.user.is_authenticated:
        now = datetime.now()
        day_display = now.strftime("%A")
        day_field = now.strftime("%A")[:3].upper()
        if day_field == 'MON':
            specials_fct = SPECIALS_HDR_FCT.objects.filter(DAY_MON_FLG=True).order_by('START_TIME')
        elif day_field == 'TUE':
            specials_fct = SPECIALS_HDR_FCT.objects.filter(DAY_TUE_FLG=True).order_by('START_TIME')
        elif day_field == 'WED':
            specials_fct = SPECIALS_HDR_FCT.objects.filter(DAY_WED_FLG=True).order_by('START_TIME')
        elif day_field == 'THU':
            specials_fct = SPECIALS_HDR_FCT.objects.filter(DAY_THU_FLG=True).order_by('START_TIME')
        elif day_field == 'FRI':
            specials_fct = SPECIALS_HDR_FCT.objects.filter(DAY_FRI_FLG=True).order_by('START_TIME')
        elif day_field == 'SAT':
            specials_fct = SPECIALS_HDR_FCT.objects.filter(DAY_SAT_FLG=True).order_by('START_TIME')
        elif day_field == 'SUN':
            specials_fct = SPECIALS_HDR_FCT.objects.filter(DAY_SUN_FLG=True).order_by('START_TIME')
        location_dim = LOCATION_DIM.objects.filter(LOCATION_KEY__in = specials_fct)
        return render(request, 'home.html', {'specials_fct': specials_fct, 'day_display':day_display, 'location_dim':location_dim})
    else:
        return HttpResponseRedirect('/login')
##Displays list of beers with abv = 5
def beer_list(request,BEER_ID):
    if request.user.is_authenticated:
        beers = BEER_DIM.objects.get(BEER_ID=BEER_ID)
        return render(request, 'beers.html', {'beers': beers})
    else:
        return HttpResponseRedirect('/login')



# Login page
def login_page(request):
    return render(request, 'login.html')


##Displays all specials
def special_list(request, LOCATION_KEY):
    if request.user.is_authenticated:
        specials_fct = SPECIALS_HDR_FCT.objects.filter(LOCATION_KEY=LOCATION_KEY)
        location_dim = LOCATION_DIM.objects.get(LOCATION_KEY=LOCATION_KEY)    
        return render(request, 'specials.html', {'specials_fct': specials_fct, 'location_dim': location_dim})
    else:
        return HttpResponseRedirect('/login')
##add specials page
def add_specials(request):
    return render(request, 'addspecials.html')

##ADD SPECIAL FORM
def add_special_hdr(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SPECIALS_HDR_FORM(request.POST)
            form2 = SPECIALS_LN_FORM(request.POST)
            if form.is_valid(): 
                post = form.save(commit=False)
                post.save()
            if form2.is_valid():
                post2 = form2.save(commit=False)
                post2.SPECIAL_HDR_ID_id = post.SPECIAL_HDR_ID
                post2.save()
            return redirect('addspecials.html')
        else:
            form = SPECIALS_HDR_FORM()
            form2 = SPECIALS_LN_FORM()
        return render(request, 'addspecials.html', {'form': form, 'form2': form2})
    else:
        return HttpResponseRedirect('/login')
    
    
##ADD SPECIAL FORM
def add_posts(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('addpost.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'addpost.html', {'form': form})


##ADD SPECIAL FORM
def add_special_ln(request):
    if request.method == "POST":
        form = SPECIALS_LN_FORM(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('addlnspecials.html', pk=post.pk)
    else:
        form = SPECIALS_LN_FORM()
    return render(request, 'addlnspecials.html', {'form': form})