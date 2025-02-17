from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
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

    @swagger_auto_schema(
        operation_description="Create a new app",
        request_body=AppSerializer,
        responses={
            201: openapi.Response(
                description="App created successfully",
                schema=AppSerializer
            ),
            400: openapi.Response(description="Invalid input"),
            401: openapi.Response(description="Authentication credentials were not provided"),
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    return Response({"message": "Mocked signup endpoint"}, status=201)


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
