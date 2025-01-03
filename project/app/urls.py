from django.urls import path
from . import views

urlpatterns=[
    path('createuser/',views.create_user,name='register'),
    path('signin/',views.signin,name='signin'),
    path('home/',views.home,name='home'),
    path('signout',views.signout,name='signout'),
    path('updatepwd/',views.PasswordChange,name='updatepassword'),
    path('identify/',views.identifyview,name='identify'),
    path('resetpassword/<str:username>/',views.reset_password,name='resetpassword'),
    path('product/',views.product,name='product'),
    path('product_details/<slug>/',views.product_details,name='product_details'),
    # path('', views.home, name='home'),
    path('category/<slug>/', views.category_detail, name='category_detail'),
    path(' ',views.home,name='home')


    
]