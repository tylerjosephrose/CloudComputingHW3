import datetime
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor


def read_data():
    buffer = np.genfromtxt('Forecast/dailyweather.csv', delimiter=',', skip_header=1)
    return buffer


def run(date):
    data = read_data()
    to_months = lambda x: (x // 100) - (x // 10000) * 100
    to_dates = lambda x: x - (x // 100) * 100

    data_train, data_test = train_test_split(data, test_size=0.33)

    dates_train = data_train[:, 0]
    dates_test = data_test[:, 0]
    x_train = np.swapaxes([to_months(dates_train), to_dates(dates_train)], 0, 1)
    x_test = np.swapaxes([to_months(dates_test), to_dates(dates_test)], 0, 1)
    y_train_max = data_train[:, 1]
    y_train_min = data_train[:, 2]
    y_test_max = data_test[:, 1]
    y_test_min = data_test[:, 2]
    regr_max = KNeighborsRegressor(n_neighbors=3)
    regr_min = KNeighborsRegressor(n_neighbors=3)
    print(x_train.shape)
    print(y_train_max.shape)
    regr_max.fit(x_train, y_train_max)
    regr_min.fit(x_train, y_train_min)
    max_mse = 0
    min_mse = 0

    test_samples = len(y_test_max)
    for i in range(test_samples):
        y_max = regr_max.predict([x_test[i]])
        y_min = regr_min.predict([x_test[i]])
        print("{}/{}: {} - {}".format(int(x_test[i][0]), int(x_test[i][1]), y_max[0], y_min[0]))
        max_mse += (y_test_max[i] - y_max[0]) ** 2
        min_mse += (y_test_min[i] - y_min[0]) ** 2

    max_mse = max_mse/test_samples
    min_mse = min_mse / test_samples
    print((max_mse + min_mse)/2)


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

