from rest_framework import serializers

class CompetitionResultRequestSerializer(serializers.Serializer):
    competition = serializers.CharField()
    user_name = serializers.CharField()
    scenario = serializers.CharField()

class ResultSerializer(serializers.Serializer):
    position = serializers.IntegerField()
    user_name = serializers.CharField()
    flight_time = serializers.FloatField()
    command_name = serializers.CharField()