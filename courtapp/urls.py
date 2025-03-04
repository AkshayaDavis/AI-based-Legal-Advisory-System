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

    path('schedule_trial/<int:id>/',views.schedule_trial,name="schedule_trial"),

    path('reject_schedule/<int:id>/',views.reject_schedule,name="reject_schedule"),

    path('view_trial_schedule/<int:id>/',views.view_trial_schedule,name="view_trial_schedule"),

    path('edit_trial_schedule/<int:id>/',views.edit_trial_schedule,name="edit_trial_schedule"),

    path('delete_trial_schedule/<int:id>/',views.delete_trial_schedule,name="delete_trial_schedule"),

    path('schedule_page/<int:id>/',views.schedule_page,name="schedule_page"),
]