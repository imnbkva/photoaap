
from django.urls import path, include # Import this function

urlpatterns = [
    path('admin/', admin.site.urls),
    # Main app
    path('', include('photoapp.urls')),
]