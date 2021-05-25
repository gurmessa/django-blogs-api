from django.urls import path
from .views import BlogViewSet #BlogList,BlogDetail

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('blogs', BlogViewSet, basename='blogs')
urlpatterns = router.urls


"""
urlpatterns = [
    path('',BlogList.as_view()),
    path('<int:pk>',BlogDetail.as_view())
]
"""