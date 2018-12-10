from rest_framework import viewsets,mixins
from test_model.serializers import CategorySerializer, SkillSerializer
from test_model.models import Category, Skill

class CategoryViewSet(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SkillViewSet(mixins.ListModelMixin,
					mixins.CreateModelMixin,
					mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
