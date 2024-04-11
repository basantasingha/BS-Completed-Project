from django.urls import path,include
from . views import Blogviewset
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'Blogpost',Blogviewset)
urlpatterns = [
    path('',include(router.urls))
]
