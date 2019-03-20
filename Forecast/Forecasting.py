import datetime
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor


def read_data():
    buffer = np.genfromtxt('Forecast/dailyweather.csv', delimiter=',', skip_header=1)
    return buffer


class Forecasting:
    __instance = None

    @staticmethod
    def get_instance():
        """
        Accessor for the singleton
        :return: Forecasting class
        """
        if Forecasting.__instance == None:
            Forecasting()
        return Forecasting.__instance

    def __init__(self):
        if Forecasting.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            data = read_data()
            to_months = lambda x: (x // 100) - (x // 10000) * 100
            to_dates = lambda x: x - (x // 100) * 100

            dates = data[:, 0]
            x_train = np.swapaxes([to_months(dates), to_dates(dates)], 0, 1)
            y_train_max = data[:, 1]
            y_train_min = data[:, 2]
            self.regr_max = KNeighborsRegressor(n_neighbors=3)
            self.regr_min = KNeighborsRegressor(n_neighbors=3)
            self.regr_max.fit(x_train, y_train_max)
            self.regr_min.fit(x_train, y_train_min)
            Forecasting.__instance = self

    def get_forecast(self, date):
        dates = [[date.month, date.day]]
        for i in range(6):
            date += datetime.timedelta(days=1)
            dates.append([date.month, date.day])

        print(dates)

        # turn datetimes into what we need to put in
        forecast_tmax = self.regr_max.predict(dates)
        forecast_tmin = self.regr_min.predict(dates)

        return forecast_tmax, forecast_tmin


if __name__ == "__main__":
    f = Forecasting()
    f.get_forecast(datetime.datetime.now())

