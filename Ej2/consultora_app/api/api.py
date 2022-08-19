from consultora_app.models import Programmer
from consultora_app.api.serializers import ProgrammerSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView


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
