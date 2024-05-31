from django.urls import path

from measurement.views import SensorsListView, SingleSensorView, MeasurementCreateView

urlpatterns = [
    path('sensors/', SensorsListView.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
