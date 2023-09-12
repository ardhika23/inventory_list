from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name':'Inventory List',
        'name': 'Ardhika Satria Narendra',
        'class': 'PBP KKI'
    }

    return render(request, 'main.html', context)