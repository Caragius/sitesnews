from  django.shortcuts import render, redirect, get_object_or_404
from .models import Artical
from .forms import ArticalForm
from django.views.generic import DetailView, DeleteView





def news_home(request):
    news = Artical.objects.all()

    return render(request, 'news/news_home.html', {'news': news})





def create(request):
    error = ''
    if request.method == "POST":
        form = ArticalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")
        else:
            error = "Форма была неверной"
    form = ArticalForm()

    data = {'form': form,
            "error": error}
    return render(request, 'news/create.html', data)