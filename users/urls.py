from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views.user import UserListView, UserDetailView, UserUpdateView, UserDeleteView, UserCreateView, Logout

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('user/<int:pk>/', UserDetailView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', UserDeleteView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/login/', views.obtain_auth_token),
    path('user/logout/', Logout.as_view()),
    path('user/token/', TokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),

]





