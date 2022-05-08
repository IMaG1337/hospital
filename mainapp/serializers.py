from rest_framework.serializers import ModelSerializer

from .models import Doctor, Patient, Record


class RecordModelSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"


class DoctorModelSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientModelSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
