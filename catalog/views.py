from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def test_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return redirect('catalog/test_form.html')
    return render(request, 'catalog/contact.html')
