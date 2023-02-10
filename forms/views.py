from rest_framework import generics
from .models import Form
from .serializer import FormSerializer


class FormDetail(generics.ListCreateAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()

