from consultora_app.models import Programmer
from consultora_app.api.serializers import ProgrammerSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView


class ProgrammerListView(generics.ListAPIView):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer

    def post(self, request, format=None):
        programmers = request.data
        serializer = (
            ProgrammerSerializer(data=programmers)
            if type(programmers) == dict
            else ProgrammerSerializer(data=programmers, many=True)
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProgrammerLanguageListView(APIView):
    def get(self, request, lg):
        programmers = Programmer.objects.filter(program_lang=lg)

        serializer = ProgrammerSerializer(programmers, many=True)
        if programmers:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class ProgrammerDetailView(generics.RetrieveAPIView):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
