from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Result
from .serializers import CompetitionResultRequestSerializer, ResultSerializer

# Токен для упрощённой авторизации (например, хранится в настройках)
API_TOKEN = "your_secure_token_here"

class CompetitionResultView(APIView):
    def post(self, request):
        
        auth_header = request.headers.get("Authorization")
        if not auth_header or auth_header != f"Token {API_TOKEN}":
            return Response({"detail": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = CompetitionResultRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        competition = serializer.validated_data['competition']
        user_name = serializer.validated_data['user_name']
        scenario = serializer.validated_data['scenario']

        # Фильтруем результаты по competition, scenario и false_start=False
        qs = Result.objects.filter(
            competition=competition,
            scenario=scenario,
            false_start=False
        ).order_by('flight_time')

        print("qs: ", qs, " competition: ", competition, " user_name: ", user_name)

        # Формируем список результатов с позициями
        results = list(qs)

        # Находим позицию пользователя
        user_result_obj = None
        user_position = None
        for idx, res in enumerate(results, start=1):
            if res.user_name == user_name:
                user_result_obj = res
                user_position = idx
                break

        qs_false_start = Result.objects.filter(
            competition=competition,
            scenario=scenario,
            user_name=user_name,
            false_start=True
        )

        if len(qs_false_start) > 0:
            return Response({"detail": "User is disqulified due to false start"}, status=status.HTTP_404_NOT_FOUND)
        
        if user_result_obj is None:
            return Response({"detail": "User result not found"}, status=status.HTTP_404_NOT_FOUND)

        # Формируем ответ
        user_result = {
            "position": user_position,
            "user_name": user_result_obj.user_name,
            "flight_time": user_result_obj.flight_time,
            "command_name": user_result_obj.command_name,
        }

        # Другие результаты (без пользователя), максимум 9
        other_results_list = []
        count = 0
        for idx, res in enumerate(results, start=1):
            if res.user_name == user_name:
                continue
            other_results_list.append({
                "position": idx,
                "user_name": res.user_name,
                "flight_time": res.flight_time,
                "command_name": res.command_name,
            })
            count += 1
            if count >= 9:
                break

        response_data = {
            "user_result": user_result,
            "other_results": other_results_list
        }

        return Response(response_data, status=status.HTTP_200_OK)
