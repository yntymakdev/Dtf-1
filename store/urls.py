from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls'))
]
