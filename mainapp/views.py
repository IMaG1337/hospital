from datetime import date

from django.utils import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Doctor, Patient, Record
from .serializers import DoctorModelSerializer, PatientModelSerializer, RecordModelSerializer


class RecordsDoctorModelViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordModelSerializer

    def retrieve(self, request, *args, **kwargs):
        current_week = date.today().isocalendar()[1]
        doc_pk = self.kwargs["pk"]
        queryset = (
            self.get_queryset()
            .filter(doctor_UID=doc_pk, datetime__week=current_week)
            .values("pk", "doctor_UID", "patient_UID", "datetime")
        )
        content = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": [],
        }
        for i in queryset:
            content[i["datetime"].strftime("%A")].append(i)
        return Response(content)


class DoctorModelViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorModelSerializer


class PatientModelViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientModelSerializer


class RecordModelViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data["id"], status=status.HTTP_201_CREATED, headers=headers)


class RecordsPatientModelViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordModelSerializer

    def retrieve(self, request, *args, **kwargs):
        now = timezone.now()
        patient_pk = self.kwargs["pk"]
        queryset = (
            self.get_queryset().filter(patient_UID=patient_pk).values("pk", "doctor_UID", "patient_UID", "datetime")
        )
        content = {"Past": [], "Future": []}
        for i in queryset:
            if i["datetime"] < now:
                content["Past"].append(i)
            content["Future"].append(i)
        return Response(content)


class AllPastPatientRecordsModelViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordModelSerializer

    def retrieve(self, request, *args, **kwargs):
        now = timezone.now()
        patient_pk = self.kwargs["patient_pk"]
        doctor_pk = self.kwargs["doctor_pk"]
        queryset = (
            self.get_queryset()
            .filter(patient_UID=patient_pk, doctor_UID=doctor_pk, datetime__lt=now)
            .values("pk", "doctor_UID", "patient_UID", "datetime")
        )
        content = {
            "Monday": [],
            "Tuesday": [],
            "Wednesday": [],
            "Thursday": [],
            "Friday": [],
            "Saturday": [],
            "Sunday": [],
        }
        for i in queryset:
            content[i["datetime"].strftime("%A")].append(i)
        return Response(content)
