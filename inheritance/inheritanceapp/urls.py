from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# url patterns for the inheritance app
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('ourstory/', views.ourstory, name='ourstory'),
    path('gallery/',views.imagedisplay, name='gallery'), 
    path('addartifact/', views.image_upload_view, name='addartifact'),
    path('editartifact/', views.editartifact, name="editartifact"), 
]

urlpatterns += staticfiles_urlpatterns()
