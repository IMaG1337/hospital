"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from mainapp import views

doctor_records = views.RecordsDoctorModelViewSet.as_view(
    {
        "get": "retrieve",
    }
)

patient_records = views.RecordsPatientModelViewSet.as_view(
    {
        "get": "retrieve",
    }
)

create_record = views.RecordModelViewSet.as_view(
    {
        "post": "create",
    }
)

all_past_records_patient = views.AllPastPatientRecordsModelViewSet.as_view(
    {
        "get": "retrieve",
    }
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("doctor/<int:pk>/", doctor_records, name="doctor"),
    path("patient/<int:pk>/", patient_records, name="patient"),
    path("patient/<int:patient_pk>/doctor/<int:doctor_pk>", all_past_records_patient, name="patient_records"),
    path("record/", create_record, name="record"),
]
