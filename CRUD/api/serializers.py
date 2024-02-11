from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.ModelSerializer):

    def validate_roll_number(self,value):
        if isinstance(value,str):
            raise serializers.ValidationError("A valid integer is required for roll_number")
        
        if self.instance:
            queryset=Students.objects.exclude(id=self.instance.id)
        else:
            queryset=Students.objects.all()
        if queryset.filter(roll_number=value).exists():
            raise serializers.ValidationError("This roll_number is already in use")
        return value


    class Meta:
        model=Students
        fields='__all__'
                

    def create(self, validated_data):
        return Students.objects.create(**validated_data)
        
    def update(self,instance,validated_data):
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.address = validated_data.get('address',instance.address)
        instance.roll_number=validated_data.get('roll_number',instance.roll_number)
        instance.mobile=validated_data.get('mobile',instance.mobile)

        instance.save()
        return instance

    