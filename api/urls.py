from django.urls import path,include
from api import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('',include('api.urls')),
    path('classes/',views.ClassView.as_view()),
    path('book/',views.BookView.as_view()),
    path('bookings/',views.BookingListView.as_view()),
]
