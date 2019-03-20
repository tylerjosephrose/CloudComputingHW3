import requests
from django.conf import settings
from django.shortcuts import render, reverse
from django.views.generic import TemplateView

import datetime

from Forecast.forms import ForecastForm


class Forecast(TemplateView):

    def get(self, request):
        form = ForecastForm()
        url = '/table/'
        return render(request, 'Forecast/index.html', {'form': form, 'table_url': url})


class Table(TemplateView):

    def get(self, request, date):
        r = requests.get(settings.URL + reverse('api:forecast', kwargs={'date': date}))

        if r.status_code == 200:
            json = r.json()
            headers = []
            tmax = []
            tmin = []
            for entry in json:
                headers.append(datetime.datetime.strptime(entry['DATE'], '%Y%m%d').strftime('%B %d, %Y'))
                tmax.append(str(entry['TMAX']) + ' ℉')
                tmin.append(str(entry['TMIN']) + ' ℉')
            return render(request, 'Forecast/table.html', {'table_headers': headers, 'tmax': tmax, 'tmin': tmin})
