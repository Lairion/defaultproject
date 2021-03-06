from rest_framework.routers import SimpleRouter
from test_model.api import views
router = SimpleRouter()

router.register('category', views.CategoryViewSet)
router.register('skill', views.SkillViewSet)
urlpatterns = router.urls
