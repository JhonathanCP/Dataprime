from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from jwt.exceptions import DecodeError
from authentication.models import CustomUser, UserActivity
from authentication.serializers import UserSerializer, UserRegistrationSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from core.models import Clasificacion  # Importa el modelo Clasificacion desde core.models

class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = serializer.save()
        self._register_activity(user, "User created")

    def _register_activity(self, user, action):
        UserActivity.objects.create(user=user, action=action)

class CustomTokenObtainPairView(TokenObtainPairView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            token = response.data.get('refresh')
            if token:
                try:
                    decoded_token = RefreshToken(token)
                    user_id = decoded_token.payload.get('user_id')
                    user = CustomUser.objects.get(id=user_id)
                    action = "Login"
                    details = "User logged in"
                    UserActivity.objects.create(user=user, action=action, details=details)
                except (TokenError, DecodeError):
                    pass

        return response

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')

        existing_user = CustomUser.objects.filter(username=username).first()
        if existing_user:
            return Response({"message": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        existing_email = CustomUser.objects.filter(email=email).first()
        if existing_email:
            return Response({"message": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        self._register_activity(user, f"User registered with '{user.role}' role")

    def _register_activity(self, user, action):
        UserActivity.objects.create(user=user, action=action)

class UserUpdateRoleView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        old_role = user.role
        # Verificar si el usuario actual es un superusuario
        if not request.user.is_superuser:
            return Response({"message": "You don't have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

        # Actualizar el rol del usuario
        new_role = request.data.get('role')
        if new_role:
            user.role = new_role
            user.save()
            self._register_activity(user, f"{user} role updated from '{old_role }' to '{new_role}'")
            return Response({"message": "User role updated successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Role field is required."}, status=status.HTTP_400_BAD_REQUEST)

    def _register_activity(self, user, action):
        UserActivity.objects.create(user=user, action=action)
