from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post-detail/<int:pk>', views.post_detail, name='post_detail'),
    path('politics/', views.politics, name='politics'),
    path('business/', views.business, name='business'),
    path('culture/', views.culture, name='culture'),
    path('technology/', views.technology, name='technology'),
    path('sports/', views.sports, name='sports'),
    path('environment/', views.environment, name='environment'),
    path('travel/', views.travel, name='travel'),
    path('local-news/', views.local_news, name='local_news'),
    path('international-news/', views.international_news, name='international_news'),
    path('education/', views.education_news, name='education'),
    path('search/', views.search_results, name='search_results'),
    path('sort/newest/', views.sort_newest, name='sort_newest'),  # New URL pattern for sorting
    path('sort/oldest/', views.sort_oldest, name='sort_oldest'),  # New URL pattern for sorting
]
