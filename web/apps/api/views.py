from django.http import HttpRequest
from rest_framework import views
from rest_framework.response import Response

from api.tasks import test_task

from celery.result import AsyncResult
from django.http import JsonResponse

class TestAPIView(views.APIView):
    def get(self, request: HttpRequest):
        task = test_task.delay(2, 5)
        return Response({"task_id": task.id}, status=202)

def get_task_status(request, task_id: str):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result,
    }
    print(result)
    return JsonResponse(result)