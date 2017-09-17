from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
# we call views from 2 apps, our own and a built-in one

app_name = 'accounts'

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    # unlike with the login template, the default behavior for logout is to redirect to home page
    url(r'^signup/$',views.SignUp.as_view(),name='signup'),
]
