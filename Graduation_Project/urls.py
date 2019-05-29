"""Graduation_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_view

import VirtualJudge.views as view
import accounts.views as account_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.home, name='home'),

    #accounts
    url(r'^signup/', account_view.signup, name='signup'),
    url(r'^login/$', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'logout/', auth_view.LogoutView.as_view(), name='logout'),

    #url(r'^settings/password/$', auth_view.PasswordChangeView.as_view(template_name='password_change.html'),name='password_change'),
    #url(r'^settings/password/done/$', auth_view.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    
    #VirturalJudge
    url(r'^home/$',view.home, name='home'),
    url(r'^problem/$',view.problem, name='problem'),
    url(r'^problem/(?P<pk>\d+)/$',view.problem_description, name='problem_description'),
    
    url(r'^contest/$',view.contest,name='contest'),
    url(r'^contest/overview/(?P<pk>\d+)', view.contestOverview, name='contestOverview'),
    url(r'^contest/problem/(?P<pk>\d+)', view.contestProblemDetail, name="contestProblemDetail"),
    url(r'^contest/status/(?P<pk>\d+)', view.contestStatus, name="contestStatus"),
    url(r'^contest/rank/(?P<pk>\d+)', view.contestRank, name="contestRank"),
    url(r'^status/$',view.status,name='status'),
    url(r'^status/codeView/(?P<pk>\d+)', view.codeView, name="codeView"),
    
]
