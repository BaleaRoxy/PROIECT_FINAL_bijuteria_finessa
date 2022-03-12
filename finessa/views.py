from django.shortcuts import HttpResponse, render

def homepage_view(request):
    request.session['my_id'] =10
    return render(request, 'homepage.html', {
        'title': 'Love yourself',
        'Garantie': 'Garantia produselor', })


