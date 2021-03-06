from rest_framework import serializers 
from test_model.models import Category, Skill

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
