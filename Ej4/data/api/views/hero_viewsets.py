from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from data.api.serializers import HeroSerializer
from data.models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by("name")
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, pk, *args, **kwargs):
        # User filter
        user = request.user
        hero = Hero.objects.filter(id=pk).first()
        if user.id == hero.owner.id:
            partial = kwargs.pop("partial", False)
            instance = self.get_object()
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial
            )
            if serializer.is_valid():
                self.perform_update(serializer)
                return Response(serializer.data)
        return Response(
            "Debe ser el usuario creador para modificarlo",
            status=status.HTTP_400_BAD_REQUEST,
        )
