from django.apps import apps
from django.contrib import admin
from django.urls import path, include , re_path
from django.conf import settings
from django.conf.urls.static import static


from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.views import generic

from oscar.core.application import OscarConfig
from oscar.core.loading import get_class

from userapplication import views
urlpatterns = [
  
    path('dash/', views.DashHomeView.as_view(), name="genDash"),
    
    path('employees/', include('employee.urls')),
    
    path('consortium/', views.ConsortiumView.as_view(), name="gen-consortium"),
    
    path('testresult/' ,include('drugtest.urls')),

    path('sqapi/', include('squarepayment.urls')),

    path('company-ops/', include('company.urls')),
    
    path('login/', views.AccountAuthView.as_view(), name='gen-login'),
            path('logout/', views.LogoutView.as_view(), name='gen-logout'),
            path('register/', views.AccountRegistrationView.as_view(), name='gen-register'),
            path('summary/', login_required(views.AccountSummaryView.as_view()), name='gen-summary'),
            path('change-password/', login_required(views.ChangePasswordView.as_view()), name='gen-change-password'),

            # Profile
            path('profile/', login_required(views.ProfileView.as_view()), name='gen-profile-view'),
            path('profile/edit/', login_required(views.ProfileUpdateView.as_view()), name='gen-profile-update'),
            path('profile/delete/', login_required(views.ProfileDeleteView.as_view()), name='gen-profile-delete'),

            # Order history
            path('orders/', views.MyOrdersView.as_view(), name="gen-orders" ),
            re_path(
                r'^order-status/(?P<order_number>[\w-]*)/(?P<hash>[A-z0-9-_=:]+)/$',
                views.AnonymousOrderDetailView.as_view(), name='gen-anon-order'
            ),
            path('orders/<str:order_number>/', login_required(views.OrderDetailView.as_view()), name='gen-order'),
            path(
                'orders/<str:order_number>/<int:line_id>/',
                login_required(views.OrderLineView.as_view()),
                name='gen-order-line'),

    

            # # Address book
            # path('addresses/', login_required(views.AddressListView.as_view()), name='gen-address-list'),
            # path('addresses/add/', login_required(views.AddressCreateView.as_view()), name='gen-address-create'),
            # path('addresses/<int:pk>/', login_required(views.AddressUpdateView.as_view()), name='gen-address-detail'),
            # path(
            #     'addresses/<int:pk>/delete/',
            #     login_required(views.AddressDeleteView.as_view()),
            #     name='gen-address-delete'),
            # re_path(
            #     r'^addresses/(?P<pk>\d+)/(?P<action>default_for_(billing|shipping))/$',
            #     login_required(views.AddressChangeStatusView.as_view()),
            #     name='gen-address-change-status'),

            # # Email history
            # path('emails/', login_required(views.EmailHistoryView.as_view()), name='gen-email-list'),
            # path('emails/<int:email_id>/', login_required(views.EmailDetailView.as_view()), name='gen-email-detail'),

            # Notifications
            # Redirect to notification inbox
            # path(
            #     'notifications/', generic.RedirectView.as_view(url='/accounts/notifications/inbox/', permanent=False)),
            # path(
            #     'notifications/inbox/',
            #     login_required(views.InboxView .as_view()),
            #     name='notifications-inbox'),
            # path(
            #     'notifications/archive/',
            #     login_required(self.notification_archive_view.as_view()),
            #     name='notifications-archive'),
            # path(
            #     'notifications/update/',
            #     login_required(self.notification_update_view.as_view()),
            #     name='notifications-update'),
            # path(
            #     'notifications/<int:pk>/',
            #     login_required(self.notification_detail_view.as_view()),
            #     name='notifications-detail'),

            # # Alerts
            # # Alerts can be setup by anonymous users: some views do not
            # # require login
            # path('alerts/', login_required(self.alert_list_view.as_view()), name='alerts-list'),
            # path('alerts/create/<int:pk>/', self.alert_create_view.as_view(), name='alert-create'),
            # path('alerts/confirm/<str:key>/', self.alert_confirm_view.as_view(), name='alerts-confirm'),
            # path('alerts/cancel/key/<str:key>/', self.alert_cancel_view.as_view(), name='alerts-cancel-by-key'),
            # path(
            #     'alerts/cancel/<int:pk>/',
            #     login_required(self.alert_cancel_view.as_view()),
            #     name='alerts-cancel-by-pk'),


  #  path('cart/', views.MyCartView, name="genCart"),
   # path('all-product/', views.AllProductView, name="genAllproduct"),





]



