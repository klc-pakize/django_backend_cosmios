from rest_framework import serializers

from .models import Student

import datetime

class StudentSerializer(serializers.ModelSerializer):

    bron_year = serializers.SerializerMethodField()

    class Meta:
        model = Student
        # fields = "__all__"
        # exclude = ["number"]
        fields = (
            'id',
            'first_name',
            "last_name",
            "age",
            "number",
            'bron_year',
        )

    def get_bron_year(self, db_cekilen_student_datası):
        current_time = datetime.datetime.now()
        return current_time.year - db_cekilen_student_datası.age

class EKSİStudentSerializer(serializers.Serializer):

    first_name = serializers.CharField(max_length = 40)
    last_name = serializers.CharField(max_length = 50)
    number = serializers.IntegerField()
    age = serializers.IntegerField()

    def create(self, validated_data):
         return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
         instance.first_name = validated_data.get('first_name', instance.first_name)
         instance.last_name = validated_data.get('last_name', instance.last_name)
         instance.number = validated_data.get('number', instance.number)
         instance.age = validated_data.get('age', instance.age)
         instance.save()
         return instance

