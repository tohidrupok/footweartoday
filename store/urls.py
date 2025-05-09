from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.company_list ,name='company_list'),
    path('company/<slug:company_slug>/', views.company_detail ,name='company_detail'),
    path('list_factory/', views.factorys_list ,name='list_factory'),
    path('InternationaCompany/', views.internation_company_list ,name='InternationaCompany'),

    path('core/option', views.option ,name='option'),
    path('core/lather', views.lather ,name='lather'),
    path('core/synthetic', views.synthetic ,name='synthetic'),
    path('core/esparadice', views.esparadice ,name='esparadice'),  
    
    


    path('news/', views.news_article_list ,name='news_all'),
    path('news/<slug:news_slug>/', views.news_detail ,name='news_detail'),
    path('event/', views.event_list ,name='event'),
    path('event/<slug:event_slug>/', views.event_detail ,name='event_details'),
    path('gallery/', views.gallery_list ,name='gallery'),


    path('leaders/', views.leaders ,name='leaders'),
    path('leaders/<slug:person_slug>/', views.persion_detail ,name='person_detail'), 

    path('search/', views.search_view ,name='search'),
    
] 