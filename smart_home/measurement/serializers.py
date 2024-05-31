from rest_framework import serializers

from measurement.models import Measurement, Sensor


class SensorCreateOutputSerializer(serializers.ModelSerializer):
    '''№№ 1, 4:  Создать датчик, вывести список датчиков (название, описание датчика)'''
    class Meta:
        model = Sensor
        fields = ['name', 'description']

class PutMeasurementSerializer(serializers.ModelSerializer):
    ''' №3: Добавить измерение. (ID датчика, температура)'''
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']
        
# class SensorSerializer(serializers.ModelSerializer):
#     '''№ 2: обновить датчик (ID, название и описание)'''
#     class Meta:
#         model = Sensor
#         fields = '__all__'
        
class MeasurementsSerializer(serializers.ModelSerializer):
    ''' №5 вложенная часть (температурой, время);
     Получить информацию по конкретному датчику, его измерения '''
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']
        
class InfoSensorSerializer(serializers.ModelSerializer):
    ''' №5 Получить информацию по конкретному датчику
    (ID, название, описание и список всех измерений с температурой и временем)'''
    measurements = MeasurementsSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']