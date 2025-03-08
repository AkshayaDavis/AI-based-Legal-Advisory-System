from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
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

    path('edit_court/<int:id>/',views.edit_court,name="edit_court"),

    path('edit_court_profile',views.edit_court_profile,name="edit_court_profile"),

    path('lawyer_profileview',views.lawyer_profileview,name="lawyer_profileview"),

    path('court_profile',views.court_profile,name="court_profile"),

    path('edit_court_profile',views.edit_court_profile,name="edit_court_profile"),

    path('all_lawyers',views.all_lawyers,name="all_lawyers"),

    path('profile_lawyer/<int:id>/',views.profile_lawyer,name="profile_lawyer"),

    path('approve_lawyer/<int:id>/',views.approve_lawyer,name="approve_lawyer"),

    path('reject_lawyer/<int:id>/',views.reject_lawyer,name="reject_lawyer"),

    path('bookings/<int:id>/',views.bookings,name="bookings"),

    path('view_bookings',views.view_bookings,name="view_bookings"),

    path('approve_booking/<int:id>/',views.approve_booking,name="approve_booking"),

    path('reject_booking/<int:id>/',views.reject_booking,name="reject_booking"),

    path('delete_booking/<int:id>/',views.delete_booking,name="delete_booking"),

    # path('message_booking/<int:id>/',views.message_booking,name="message_booking"),

    path('my_bookings',views.my_bookings,name="my_bookings"),

    path('chat/<int:id>/',views.chat,name="chat"),

    path('all_courts',views.all_courts,name="all_courts"),

    path('courts_profileview',views.courts_profileview,name="courts_profileview"),

    path('profile_court/<int:id>/',views.profile_court,name="profile_court"),

    path('add_request_trial/<int:id>/', views.add_request_trial, name="add_request_trial"),

    path('trial',views.trial,name="trial"),

    path('view_trial',views.view_trial,name="view_trial"),

    path('approve_trial/<int:id>/',views.approve_trial,name="approve_trial"),

    path('reject_trial/<int:id>/',views.reject_trial,name="reject_trial"),

    path('delete_trial/<int:id>/',views.delete_trial,name="delete_trial"),

]
