from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from appstore.models import App
from appstore.serializers import AppSerializer


class AppCreateView(generics.CreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]


# Mock Signup View
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    return Response({"message": "Mocked signup endpoint"}, status=201)


# Mock Login View (We use JWT authentication, so this is just a placeholder)
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    return Response({"message": "Use /api/token/ for authentication"}, status=200)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_apps(request):
    return Response({"message": "Mocked list of all apps"}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def purchase_app(request, app_id):
    return Response({"message": f"Mocked purchase of app {app_id}"}, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_purchased_apps(request):
    return Response({"message": "Mocked list of purchased apps"}, status=200)
