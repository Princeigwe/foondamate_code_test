from rest_framework import serializers

class MathQuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length=50)