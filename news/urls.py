from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .models import Artical
from .forms import ArticalForm
from django.views.generic import ListView,DetailView, UpdateView, DeleteView


urlpatterns = [
    path('', views.news_home, name = 'news_home' ),
    path('create', views.create, name = 'create' ),
    path('<int:pk>/', DetailView.as_view(model=Artical, template_name="news/post.html"), name = 'ppost'),
    path('<int:pk>/update/', UpdateView.as_view(model=Artical, template_name="news/create.html", fields = ['title', 'anons', 'full_text', 'date']), name = 'update'),
    path('<int:pk>/delete/', DeleteView.as_view(model=Artical,success_url = '/news', template_name="news/delete.html" ), name = 'delete')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)