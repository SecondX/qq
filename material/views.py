from django.shortcuts import render

# Create your views here.

def formfill(request):
    if request.POST:
        company_name = request.POST['company_name']
    return render(request, 'formfill.html', locals())

