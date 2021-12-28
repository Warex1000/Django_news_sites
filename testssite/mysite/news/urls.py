from django.urls import path

from . import views
from .views import CreateNews

urlpatterns = [
    # path('', index, name='home'),
    path('', views.HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(extra_context={'title': 'Какой-то Тайтл'}), name='category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:pk>/', views.ViewsNews.as_view(), name='view_news'),
    # path('news/add-news/', views.add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]
