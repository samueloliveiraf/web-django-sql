from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin

from accounts import urls as urls_accounts
from sql_query import urls as urls_sql_query
from core import urls as urls_core


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', include(urls_accounts)),
    path('sql/', include(urls_sql_query)),
    path('', include(urls_core)),
]
