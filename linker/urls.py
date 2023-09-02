from django.contrib import admin
from django.urls import path , include

from .views import main_page

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path ('' , main_page , name = 'home'),
    path ('admin/', admin.site.urls),
    path ('auth/' , include ('auth_main.urls') , name = 'auth' ),
    path ('workflow/' , include ('workflow.urls') , name = 'workflow' ),
    path ('api/v1/' , include ('api.urls') , name = 'api'),

] + static(settings.STATIC_URL) + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
