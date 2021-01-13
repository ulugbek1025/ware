from django.urls import path,include
from product import views
app_name='product'
urlpatterns = [
    path('home/',views.product_home,name='product_home'),
    path('home/add_categories/',views.add_categories,name='add_categories'),
    path('home/categories/<int:categories_id>/',views.Categories,name='categories'),
    path('home/product/<int:product_id>/',views.product,name='product'),
    path('home/add_categories2/',views.add_categories2,name='add_categories2'),
    path('home/update/<int:all_categories_id>/',views.update,name='update'),

]
