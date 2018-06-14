from django.urls import path, include, re_path
from .views import Index, AboutView, detail_post_view, search
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('posts/<int:pk>/', detail_post_view, name='detail'),
    path('posts/search/', search, name='search'),
    path('about/', AboutView.as_view(), name='about')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
