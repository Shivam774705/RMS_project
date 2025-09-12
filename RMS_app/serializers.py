from rest_framework import serializers


from .models import RmsAlarmCommon

class RmsAlarmCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RmsAlarmCommon
        fields = '__all__'  # Or a list of fields you want to expose