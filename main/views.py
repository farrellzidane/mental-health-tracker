from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275600',
        'name': 'Farrell Zidane Raihandrawan',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
# Create your views here.
