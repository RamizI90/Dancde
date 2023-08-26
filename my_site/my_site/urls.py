
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('calculate_geometry/', include('geometry.urls')),
    path('months/', include('months.urls')),
]
