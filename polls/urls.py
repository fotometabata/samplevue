from rest_framework.routers import DefaultRouter
from . import views

question_router = DefaultRouter()
question_router.register(r'', views.QuestionViewSets)

choice_router = DefaultRouter()
choice_router.register(r'', views.ChoiceViewSets)
