from django.urls import path
from . import views


urlpatterns = [
    # path('', views.tweet_list, name='tweet_list'),
    path('', views.home, name='home'),
    # path('create/', views.tweet_create, name='tweet_create'),
    # path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    # path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),

    #crm
    
    path('login/', views.login_user, name='login'),     # aqeel
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    # path('record/<int:pk>', views.customer_record, name='record'),
    # path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    # path('add_record/', views.add_record, name='add_record'),
    # path('update_record/<int:pk>', views.update_record, name='update_record'),
    
]
