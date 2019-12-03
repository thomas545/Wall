from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),

    path('', include('user_profile.urls')),
    path('', include('main.urls'))
]
