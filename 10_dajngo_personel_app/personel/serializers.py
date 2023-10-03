from rest_framework import serializers

from django.utils.timezone import now

from .models import Departman, Personel


class PersonelSerializer(serializers.ModelSerializer):

    departman = serializers.StringRelatedField()  # read_only
    departman_id = serializers.IntegerField()
    user = serializers.StringRelatedField() # read_only
    day_since_jobs = serializers.SerializerMethodField()

    class Meta:
        model = Personel
        fields = "__all__"
        read_only_fields = ['departman','departman_id',"start_date", 'id','day_since_jobs','user','user_id']


    def get_day_since_jobs(self, obj):
        return (now() - obj.start_date).days

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Personel.objects.create(**validated_data)
        return instance
        

class DepartmanSerializer(serializers.ModelSerializer):

    personel_count = serializers.SerializerMethodField()
    personels = PersonelSerializer(many=True, read_only=True)

    class Meta:
        model = Departman
        fields = "__all__"
        read_only_fields = ['id', 'personels']

    def get_personel_count(self, obj):
        return obj.personels.count()
    





# validated_data = {

#     "first_name": "Pakize",
#     "last_name": "KILIÇ",
#     "title": "Junior",
#     "gender": "f",
#     "salary": 30000,
#     "departman": "BackEndDeveloper",
#     "departman_id": 1,
#     "user": 
#     "user_id": 
# }