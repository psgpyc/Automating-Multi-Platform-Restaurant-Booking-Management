from django.urls import path
from bookings.views import (
    BookiPlatformListAPIView, RestaurantListAPIView, 
    TableListAPIView, ReservationCreateAPIView, 
    ReservationListAPIView, ReservationDetailAPIView,
    OrdersListApiView, OrdersCreateApiView
)


urlpatterns = [
    path('booking_platform/', BookiPlatformListAPIView.as_view(), name='booking_platform_list_view'),
    path('restaurants/', RestaurantListAPIView.as_view(), name='restaurant_api_list_view'), 
    path('tables/', TableListAPIView.as_view(), name='tables_api_list_view'),
    path('reservations/create', ReservationCreateAPIView.as_view(), name='reservation_api_list_view'),
    path('reservations/list', ReservationListAPIView.as_view(), name='reservation_api_list_view'),
    path('reservations/<int:pk>',ReservationDetailAPIView.as_view(), name='reservation_api_detail_view' ),

    path('orders/', OrdersListApiView.as_view(), name='orders_list_view'),
    path('orders/<int:pk>/', OrdersCreateApiView.as_view(), name="orders_create_view")

    
]



# {
#   "is_completed": false,
#   "order_items": [
#     { "menu_item": 1, "quantity": 1 },
#     { "menu_item": 2, "quantity": 2 },
#     { "menu_item": 3, "quantity": 2 }
#   ]
# }