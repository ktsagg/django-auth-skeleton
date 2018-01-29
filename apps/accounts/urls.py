# accounts/urls.py
from django.urls import path, re_path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('settings/password/', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('settings/password/done/', views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('settings/account/', views.UserUpdateView.as_view(), name='my_account'),
]
