import datetime

from .Forecasting import Forecasting
from rest_framework import serializers
from .models import Weather


class HistoricalSerializer(serializers.ModelSerializer):
    DATE = serializers.DateField(format="%Y%m%d")

    class Meta:
        model = Weather
        fields = ("DATE",)


#class DateIntField(serializers.Field):
#    def to_representation(self, value):
#        return int(value.strftime("%Y%m%d"))


class HistoricalLookupSerializer(serializers.ModelSerializer):
    DATE = serializers.DateField(format="%Y%m%d")

    class Meta:
        model = Weather
        fields = ("DATE", "TMAX", "TMIN")


class ForecastSerializer(serializers.Serializer):

    def to_representation(self, date):
        #date = datetime.datetime.strptime("{}-{}-{}".format(datestr[0][:4], datestr[0][4:6], datestr[0][6:]), "%m-%d-%Y")
        f = Forecasting.get_instance()
        forecast_tmax, forecast_tmin = f.get_forecast(date)
        result = []
        for i in range(7):
            tmax = float("{0:.1f}".format(forecast_tmax[i]))
            tmin = float("{0:.1f}".format(forecast_tmin[i]))
            result.append({"DATE": date.strftime("%Y%m%d"), "TMAX": tmax, "TMIN": tmin})
        return result
