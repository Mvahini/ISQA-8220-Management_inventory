from django.conf.urls import url
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views


app_name = 'mi'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),

    #change password
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = "registration/changedpassword.html"), name='changedpassword'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(template_name = "registration/changePassword.html"), name='changePassword'),
    #forgot password
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name="registration/forgot_password.html"), name='forgot_password'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name='password_reset_complete'),

    #Client_details
    path('client_list', views.client_list, name='client_list'),
    path('client/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('client/<int:pk>/delete/', views.client_delete, name='client_delete'),

    #project_details
    path('project_list', views.project_list, name='project_list'),
    path('project/create/', views.project_new, name='project_new'),
    path('project/<int:pk>/edit/', views.project_edit, name='project_edit'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('client/<int:pk>/summary/', views.summary, name='summary'),
 ]

