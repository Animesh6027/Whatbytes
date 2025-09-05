from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Patient(TimeStampedModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20)
    address = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.age})"


class Doctor(TimeStampedModel):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return f"Dr. {self.name} - {self.specialization}"


class PatientDoctorMapping(TimeStampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self) -> str:
        return f"{self.patient.name} ↔ {self.doctor.name}"

# Create your models here.
