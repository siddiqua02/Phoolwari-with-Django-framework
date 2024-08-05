from django.urls import path
from pages.views import index,about,bulk,suprise,Thank

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path('about',about,name="about"),
    path('bulk',bulk,name="bulkorder"),
    path('suprise',suprise,name="supriseorder"),
    path('Thank',Thank,name="ThankYou"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)