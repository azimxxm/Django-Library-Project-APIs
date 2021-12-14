from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(f'books', views.BooksViewSet)
router.register(f'lib-users', views.LibUserViewSet)
router.register(f'rentet-books', views.RentBookViewSet)