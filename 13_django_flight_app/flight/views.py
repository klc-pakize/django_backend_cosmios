from datetime import date, datetime

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer, StaffFlightSerializer
from .permissions import IsStaffOrReadOnly


class FlightView(ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsStaffOrReadOnly, IsAuthenticated]

    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        
        if self.request.user.is_staff:
            return Flight.objects.all()  # super().get_queryset()

        else:
            queryset = Flight.objects.filter(date_of_departure__gt = today)

            if Flight.objects.filter(date_of_departure = today):
                today_queryset = Flight.objects.filter(estimated_time_of_departure__gt = current_time)

                queryset = queryset.union(today_queryset)

            return queryset

    def get_serializer_class(self):
        seiralizer = super().get_serializer_class()  # == FlightSerializer

        if self.request.user.is_staff:
            return StaffFlightSerializer
        return seiralizer


class ReservationView(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()  # Reservation.objects.all()

        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user = self.request.user)