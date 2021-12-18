from django.urls import path
from . import views
# sets the urls for pages on the site
urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('ourstory', views.ourstory, name='ourstory'),
    path('addartifact/', views.addartifact, name='addartifact'),
    path('gallery', views.gallery, name='gallery'),
    path('editartifact/<int:artifact_id>', views.editartifact, name="editartifact")
]


