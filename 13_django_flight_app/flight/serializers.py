from rest_framework import serializers

from .models import Flight, Reservation, Passenger

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = "__all__"


class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
    passenger = PassengerSerializer(many=True)
    flight =  serializers.StringRelatedField() #read_only=True
    flight_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = "__all__"

    def create(self, validated_data):
        passenger_data = validated_data.pop('passenger')
        validated_data['user_id'] = self.context['request'].user.id
        reservation = Reservation.objects.create(**validated_data)

        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)

        reservation.save()
        return reservation

class StaffFlightSerializer(serializers.ModelSerializer):
    reservation = ReservationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Flight
        fields = "__all__"



    # VALİDATED_DATA = 
    # {
    #     "passenger": [
    #         {
    #             "id": 1,
    #             "first_name": "Anne",
    #             "last_name": "Keleş",
    #             "email": "test@gmail.com",
    #             "phone_number": 323244242,
    #             "update_date": "2023-10-15T18:08:49.889958Z",
    #             "create_date": "2023-10-15T18:08:49.889958Z"
    #         },
    #         {
    #             "id": 2,
    #             "first_name": "Baba",
    #             "last_name": "Keleş",
    #             "email": "test1@gmail.com",
    #             "phone_number": 234234422,
    #             "update_date": "2023-10-15T18:09:04.912504Z",
    #             "create_date": "2023-10-15T18:09:04.912504Z"
    #         }
    #     ],
    #     "flight_id": 1,
    #     "user": "Sultan",
    #     "user_id":5,
    
    # }

