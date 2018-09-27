from .models import Resources
from .serializers import ResourcesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class ResourcesList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        resources = Resources.objects.all()[:10]
        resources_serializer = ResourcesSerializer(resources, many=True)
        return Response(resources_serializer.data)
