from django.urls import path,include
from user import views
app_name='user'
urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
    path('User/',views.user_home,name='user_home'),
    path('User/add_user/',views.add_user,name='add_user'),
    path('User/delete_user/<str:pk>/',views.deleteUser,name='delete_user'),
    path('User/edit_user/<int:user_id>/',views.edituser,name='edituser'),
]
