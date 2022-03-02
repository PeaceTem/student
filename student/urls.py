
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pwa.urls')),


    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('core/', include('core.urls')),
    path('quiz/', include('quiz.urls', namespace='quiz')),
    path('todo/', include('todo.urls', namespace='todo')),
    path('diary/', include('diary.urls', namespace='diary')),
    path('wallet/', include('wallet.urls', namespace='wallet')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
