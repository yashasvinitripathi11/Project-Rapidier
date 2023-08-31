from django.shortcuts import render,redirect

def home(request):
     return render(request,"home/index.html")

def faq(request):
     return render(request,"home/faq.html")
def contact(request):
     return render(request,"home/contact.html")
def about(request):
     return render(request,"home/about.html")






