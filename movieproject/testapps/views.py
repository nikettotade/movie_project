from django.shortcuts import render
from testapps.forms import MovieForm
from testapps.models import Movie

# Create your views here.

def index_view(request):
    return render(request, 'testapps/index.html')

def addmovie_view(request):
    form = MovieForm
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index_view(request)
    return render(request, 'testapps/addmovie.html', {'form': form})

def listmovie_view(request):
    movies_list = Movie.objects.all().order_by('-rating')
    return render(request, 'testapps/listmovie.html', {'movies_list': movies_list})


