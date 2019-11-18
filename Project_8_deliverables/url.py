from django.urls import path
from . import views
app_name = 'backend'
urlpatterns = [ 
    path('services/', views.ServiceListView.as_view(), name='service_list'), 
    path('services/<pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('subscribers/', views.SubscriberListView.as_view(), name='subscribers_list'), 
    path('subscribers/<pk>/', views.SubscriberDetailView.as_view(), name='subscribers_detail'),
    path('organizations/', views.OrganizationListView.as_view(), name='organization_list'), 
    path('organization/<pk>/', views.OrganizationDetailView.as_view(), name='organization_detail'),
]
