from django.urls import path
from . import views
urlpatterns = [
    
    path('add_law',views.add_law,name="add_law"),

    path('view_laws',views.view_laws,name="view_laws"),

    path('edit_law/<int:id>',views.edit_law,name="edit_law"),

    path('delete_law/<int:id>',views.delete_law,name="delete_law"),
]