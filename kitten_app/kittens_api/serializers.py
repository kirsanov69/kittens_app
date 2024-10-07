from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Breed, Kitten, Rating

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'description']


class KittenSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(slug_field='name', queryset=Breed.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    def add_kitten(self, validated_data):
        breed_name = validated_data['breed']['name']
        return Kitten.objects.create(**validated_data)
    
    def update_kitten(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.age_months = validated_data.get('age_months', instance.age_months)
        instance.description = validated_data.get('description', instance.description)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.save()
        return instance

    class Meta:
        model = Kitten
        fields = ['id', 'name', 'color', 'age_months', 'description', 'breed', 'owner', 'created_at', 'updated_at']
        read_only_fields = ['owner', 'created_at', 'updated_at']


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    kitten = serializers.SlugRelatedField(slug_field='name', queryset=Kitten.objects.all())
    score = serializers.IntegerField()

    class Meta:
        model = Rating
        fields = ['id', 'kitten', 'user', 'score', 'created_at']
        read_only_fields = ['user', 'created_at']
    
    def validate_score(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Оценка должна быть от 1 до 5.")
        return value
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return Rating.objects.create(**validated_data)  