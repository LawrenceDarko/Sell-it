from django.urls import path
from . views import register
#from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/' , register , name='register') , 
    # path('login/', auth_views.LoginView.as_view(),  name='login'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(),  name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),  name='password_change_done'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(),  name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),  name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetDoneView.as_view(),  name='password_reset_done'),
    # path('reset/done/', auth_views.PasswordResetDoneView.as_view(),  name='password_reset_done'),
    
]