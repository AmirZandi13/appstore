from django.urls import path
from appstore.views import (
    AppCreateView,
    signup,
    login,
    list_apps,
    purchase_app,
    list_purchased_apps
)

urlpatterns = [
    path('', AppCreateView.as_view(), name='app-create'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('list/', list_apps, name='list-apps'),
    path('purchase/<int:app_id>/', purchase_app, name='purchase-app'),
    path('purchased/', list_purchased_apps, name='list-purchased-apps'),
]
