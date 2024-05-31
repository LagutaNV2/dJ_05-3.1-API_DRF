# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateAPIView,
                                     CreateAPIView)

from measurement.models import Sensor, Measurement
from measurement.serializers import (SensorCreateOutputSerializer,
                                     PutMeasurementSerializer,
                                     InfoSensorSerializer)


class SensorsListView(ListCreateAPIView):
    """
         task 1: create a new sensor
         task 4: List all sensors
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorCreateOutputSerializer
    
class SingleSensorView(RetrieveUpdateAPIView):
    """
        task 2: Update sensor
        task 5: Get sensors info: ID, name, descript, list of measuremens (temp, time)
    """
    queryset = Sensor.objects.all()
    serializer_class = InfoSensorSerializer
   
    
class MeasurementCreateView(CreateAPIView, ListCreateAPIView):
    """
    task 3: Добавить измерение. Указываются ID датчика и температура
    """
    queryset = Measurement.objects.all()
    serializer_class = PutMeasurementSerializer


