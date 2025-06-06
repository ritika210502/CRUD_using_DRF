from django.urls import path
from api import views
urlpatterns = [
    path('',views.ApiOverview,name='home'),
    path('create/',views.add_items,name='add-items'),
    path('all',views.all_items,name='view-items'),
    path('update/<int:pk>',views.update_item,name='update-item'),
    path('delete/<int:pk>',views.delete_item,name='delete-item'),
]