from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('reg', views.reg),
    path('user_login/', views.user_login,name="user_login"),
    path('home',views.home,name="home"),
    path('user_logout', views.user_logout,name="user_logout"),
    path('about', views.about),
    path('contact', views.contact),
    path('service', views.service),
    path('team', views.team),
    path('view_user',views.view_user,name="view_user"),

    path('profile',views.profile,name="profile"),

    path('edit_profile',views.edit_profile,name="edit_profile"),

    path('forgot_password',views.forgot_password),

    path('reset_password',views.reset_password,name="reset_password"),

    path('delete_user/<int:id>/',views.delete_user,name="delete_user"),

    path('reg_option',views.reg_option,name="reg_option"),

    path('lawyer_reg', views.lawyer_reg,name="lawyer_reg"),

    path('lawyer_profile',views.lawyer_profile,name="lawyer_profile"),

    path('edit_lawyer_profile',views.edit_lawyer_profile,name="edit_lawyer_profile"),

    path('view_lawyer',views.view_lawyer,name="view_lawyer"),

    path('view_lawyer',views.view_lawyer,name="view_lawyer"),

    path('delete_lawyer/<int:id>/',views.delete_lawyer,name="delete_lawyer"),

    path('court_reg', views.court_reg,name="court_reg"),
    
    path('view_court',views.view_court,name="view_court"),

    path('delete_court/<int:id>/',views.delete_court,name="delete_court"),
]
