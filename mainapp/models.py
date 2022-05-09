from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Doctor(models.Model):
    fio = models.CharField(max_length=200)
    specialization = models.CharField(max_length=120)

    def __str__(self) -> str:
        return f"{self.fio} | {self.specialization}"


class Patient(models.Model):
    fio = models.CharField(max_length=200)
    phone = PhoneNumberField()

    def __str__(self) -> str:
        return f"{self.fio} | {self.phone}"


class Record(models.Model):
    doctor_UID = models.ForeignKey(
        Doctor,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    patient_UID = models.ForeignKey(
        Patient,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    datetime = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.doctor_UID} | {self.patient_UID} |{self.datetime}"
