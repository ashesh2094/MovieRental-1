from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('all/', views.customer, name="customer"),
    path('delete/<customer_id>/',views.customer_delete, name="deleteCustomer"),
    path('add/', views.customer_add, name="addCustomer"),
    path('update/<customer_id>/',views.customer_update,name="updatecustomer"),
]
