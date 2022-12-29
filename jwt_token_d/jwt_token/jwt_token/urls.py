# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from app import views
# from rest_framework.authtoken import views
# from rest_framework.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
# from rest_framework import routers
#
# router = routers.DefaultRouter()
# router.register('api', views.EmployeeCRUDCBV)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include(router.urls)),
#     path('gettoken', obtain_jwt_token, name='token_obtain_pair'),
#     path('refreshtoken', refresh_jwt_token, name='token_refresh'),
#     path('refreshtoken', verify_jwt_token, name='token_verify'),
# ]



from app import views
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,TokenVerifyView)
# from rest_framework.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
router = routers.DefaultRouter()
# router.register('api', views.EmployeeCRUDCBV)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken', TokenRefreshView.as_view(), name='token_refresh'),
    path('refreshtoken', TokenVerifyView.as_view(), name='token_verify'),
]