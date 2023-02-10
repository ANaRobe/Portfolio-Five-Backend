from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Workshop
from .serializers import WorkshopSerializer


class WorkshopList(generics.ListCreateAPIView):
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Workshop.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        filters.SearchFilter,
    ]

    search_fields = [
        'owner__username',
        'title',
        'location',
    ]


class WorkshopDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkshopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Workshop.objects.all()
