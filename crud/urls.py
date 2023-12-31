from . import views
from django.urls import path

urlpatterns = [
    path('', views.list, name='list'),
    path('create', views.create, name='create'),
    path('list', views.list, name='list'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('view/<int:id>', views.view, name='software_view'),
    
]
