from django.db.models import Sum
from django.shortcuts import render
from django.views import View
from .models import Donation, Institution

class LandingPage(View):
    def get(self, request):
        #quantity = Donation.objects.get(Donation.quantity).count()
        #quantity = Donation.quantity.all().count()
        quantity = list(Donation.objects.aggregate(Sum('quantity')).values())[0]
        institution = Institution.objects.all().count()
        foundation = Institution.objects.get(type=1, pk=1)
        foundations = Institution.objects.all()
        categories = foundation.categories.all()
        return render(request, "index.html", {'quantity': quantity,
                                              'institution': institution,
                                              'foundation': foundation,
                                              'foundations': foundations,
                                              'categories': categories,
                                              })

class AddDonation(View):
    def get(self, request):
        return render(request, "form.html")

class Login(View):
    def get(self, request):
        return render(request, "login.html")

class Register(View):
    def get(self, request):
        return render(request, "register.html")

class Base(View):
    def get(self, request):
        return render(request, "base.html")