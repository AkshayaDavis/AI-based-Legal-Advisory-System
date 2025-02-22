from django.urls import path
from . import views
urlpatterns = [
    
    path('add_law',views.add_law,name="add_law"),

    path('view_laws',views.view_laws,name="view_laws"),

    path('edit_law/<int:id>',views.edit_law,name="edit_law"),

    path('delete_law/<int:id>',views.delete_law,name="delete_law"),

    path('add_jury',views.add_jury,name="add_jury"),

    path('view_juries',views.view_juries,name="view_juries"),

    path('edit_jury/<int:id>',views.edit_jury,name="edit_jury"),

    path('delete_jury/<int:id>',views.delete_jury,name="delete_jury"),
]