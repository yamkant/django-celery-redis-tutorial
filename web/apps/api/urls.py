from django.urls import path
from api.views import TestAPIView, get_task_status

app_name = "api"

urlpatterns = [
    path("test", TestAPIView.as_view(), name="retrieve"),
    path("tasks/<task_id>", get_task_status, name="get_task_status"),
]