from rest_framework import generics
from .models import Form
from .serializer import FormSerializer


class FormtDetail(generics.ListCreateAPIView):
    serializer_class = FormSerializer
    queryset = Form.objects.all()

