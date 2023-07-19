from django.urls import path
from . import views

urlpatterns = [
    path("api/user/login/", views.LoginAPIView.as_view(), name="user-login"),
    path("api/user/signup/", views.SignupAPIView.as_view(), name="user-signup"),
    path("api/product/", views.CreateProduct.as_view(), name="create_product"),
    path("api/all_product/", views.AllProducts.as_view(), name="all_product"),
    path("api/details_product/<int:pk>", views.DetailsProduct.as_view(), name="details_product"),
    path("api/update_product/<int:pk>", views.UpdateProduct.as_view(), name="update_product"),
    path("api/delete_product/<int:pk>", views.DeleteProduct.as_view(), name="delete_product"),
    path("api/add_image_product/", views.AddImageProduct.as_view(), name="add_image"),
    path("api/image_by_id/<int:pk>", views.ImageProductById.as_view(), name="image_by_id"),
    path("api/create_cart/", views.CreateCart.as_view(), name="create_cart"),
    path("api/add_to_cart/", views.AddProductToCart.as_view(), name="add_to_cart"),
    path("api/cartitem/<int:pk>", views.CartItemById.as_view(), name="cartitem"),
    path("api/checkout/<int:pk>", views.CheckoutProduct.as_view(), name="checkout"),
    path('api/product/find', views.SearchProduct.as_view(),name="search_product"),
    path('api/part_cheakout/', views.PartCheckoutProduct.as_view(),name="part_cheakout"),
  ]
