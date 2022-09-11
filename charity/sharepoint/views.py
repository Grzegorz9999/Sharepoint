from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views import View
from .models import Donation, Institution, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout
from .forms import MyLoginForm
from django.http import HttpResponseRedirect

class LandingPage(View):
    def get(self, request):
        #quantity = Donation.objects.get(Donation.quantity).count()
        #quantity = Donation.quantity.all().count()
        quantity = list(Donation.objects.aggregate(Sum('quantity')).values())[0]
        institution = Institution.objects.all().count()
        foundation = Institution.objects.get(type=1, pk=1)
        foundations = Institution.objects.filter(type=1)
        non_governmentals = Institution.objects.filter(type=2)
        local_raises = Institution.objects.filter(type=3)
        categories = foundation.categories.all()
        return render(request, "index.html", {'quantity': quantity,
                                              'institution': institution,
                                              'foundation': foundation,
                                              'foundations': foundations,
                                              "non_governmentals": non_governmentals,
                                              "local_raises": local_raises,
                                              'categories': categories,
                                              })

class AddDonation(View):
    def get(self, request):
        category_forms = Category.objects.all()
        return render(request, "form.html", {'category_forms': category_forms})

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

#def register(request):
 #   form = CreateUserForm()

  #  if request.method == 'POST':
   #     form = CreateUserForm(request.POST)
    #    if form.is_valid():
     #       form.save()
      #      user = form.cleaned_data.get('username')
       #     messages.success(request, 'Account was created for ' + user)
        #    return redirect('login')

    #context = {'form': form}
    #return render(request, 'register.html', context)

class Login(View):
    def get(self, request):
        form = MyLoginForm()
        return render(request, 'login.html', {"form": form})

    def post(self, request):
        form = MyLoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=login, password=password)
            if user is not None:
                return render(request, 'index.html', {"form": form})
            else:
                return render(request, 'register.html', {"form": form})

class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class Register(View):
    def get(self, request):
        return render(request, "register.html")

class Base(View):
    def get(self, request):
        return render(request, "base.html")
