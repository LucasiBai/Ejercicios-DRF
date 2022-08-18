from todoapp.models import Todo
from todoapp.api.serializers import TodoSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView


class TodoList(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)


class TodoDetail(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUncompletedList(APIView):
    def get(self, request):
        todo = Todo.objects.filter(completed=False)
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
