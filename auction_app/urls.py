from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

router = DefaultRouter()
router.register('animals', AnimalViewSet, basename='Animal')
router.register('lots', LotViewSet, basename='LotS')
router.register('bets', BetViewSet, basename='BetS')
#router.register('mylots', MyLots, basename='mylots')
#router.register('^mylots/(?P<pk>[^/.]+)/$', MyLotsDetaile, basename='lot-detail')

urlpatterns = [
    path('mylots', MyLots.as_view()),
    path('mylots/<int:pk>/', MyLotsDetail.as_view()),
]

urlpatterns += router.urls
