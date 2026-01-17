from rest_framework import viewsets, permissions
from .models import LearningTask
from .serializers import LearningTaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer

class LearningTaskViewSet(viewsets.ModelViewSet):
    serializer_class = LearningTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LearningTask.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created successfully"})
    return Response(serializer.errors, status=400)
