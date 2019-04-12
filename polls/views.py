from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, status, generics
from .models import Question, Choice
from .serializer import QuestionSerializer, ChoiceSerializer

# Create your views here.
class ChoiceViewSets(viewsets.ModelViewSet):
    """
    post:
        投票数を更新
    """

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    def post(self, request, pk=None):
        obj = generics.get_object_or_404(
            queryset = self.queryset,
            id = pk,
        )
        obj.votes += 1
        obj.save()
        s = ChoiceSerializer(instance=obj)
        return Response(s.data)


class QuestionViewSets(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
