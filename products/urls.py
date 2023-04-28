from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    # path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    # path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]