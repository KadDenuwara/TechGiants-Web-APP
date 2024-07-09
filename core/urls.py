from django.urls import include, path
from .views import (
    ItemDetailView,
    HomeView,
    add_to_cart,
    delete_review,
    edit_review,
    remove_from_cart,
    ShopView,
    OrderSummaryView,
    remove_single_item_from_cart,
    CheckoutView,
    PaymentView,
    AddCouponView,
    CategoryView,
    order_list_view,
    search,
    page_not_found
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('category/<slug>/', CategoryView.as_view(), name='category'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('review/delete/<int:pk>/', delete_review, name='delete-review'),
    path('review/edit/<int:pk>/', edit_review, name='edit-review'),
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('newsletter/', include('newsletter.urls')),
    path('orders/', order_list_view, name='order-list'),
    path('search/', search, name='search'),
    path('page-not-found/', page_not_found , name='page_not_found'),
]
