from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),  # new
    path('feed/', views.feeds_view, name='feeds'),
]
