from django.http import JsonResponse
from django.db import transaction
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from .serializers import *

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAdminUser]


class LotViewSet(viewsets.ModelViewSet):
    serializer_class = LotSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Lot.objects.all()


class BetViewSet(viewsets.ModelViewSet):
    queryset = Bet.objects.all()
    serializer_class = BetSerializer
    permission_classes = [IsAuthenticated]


class MyLotsDetail(generics.ListAPIView, generics.DestroyAPIView):
    serializer_class = BetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Lot.objects.all()

        lot_id = self.kwargs['pk']
        user = self.request.user
        return queryset.filter(owner=user).get(id=lot_id).bets.all()

    def destroy(self, request, *args, **kwargs):
        object = self.get_object()
        lot_owner = self.request.user
        bet_author = object.author
        bet_price = object.price
        queryset = self.queryset.get(id=object.id)

        with transaction.atomic():
            lot_owner.cash_balance += bet_price
            bet_author.cash_balance -= bet_price

        lot_delete = queryset.delete()
        return JsonResponse({'message': lot_delete[0] + ' was deleted!'}, status=status.HTTP_204_NO_CONTENT)



class MyLots(generics.ListAPIView):
    serializer_class = LotSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        queryset = Lot.objects.all()
        user = self.request.user
        return queryset.filter(owner=user)



# class SelectBetView(APIView):
#     serializer_class = SelectBetSerializer
#
#     def get_object(self, pk):
#         try:
#             queryset = Lot.objects.all()
#             lot_id = self.kwargs['pk']
#             user = self.request.user
#             lot_queryset = queryset.filter(owner=user).get(id=lot_id).bets.all()
#
#     def post(self, request):
#         bet_id = request.data.get('bet_id')
#         serializer = BetSerializer(data=bet_id)
#         queryset = Lot.objects.all()
#
#         lot_id = self.kwargs['pk']
#         user = self.request.user
#         bet_queryset = queryset.filter(owner=user).get(id=lot_id).bets.all()
#
#         if serializer.is_valid(raise_exception=True):
#             lot_owner = self.request.user
#             bet_author = .author
#             bet_price = object.price
#             queryset = self.queryset.get(id=object.id)
#
#             with transaction.atomic():
#                 lot_owner.cash_balance += bet_price
#                 bet_author.cash_balance -= bet_price
#
#             lot_delete = queryset.delete()

