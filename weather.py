import pyowm as PyOWM
import config
import sys


class Weather:
    def __init__(self):
        self.api_key = config.api_key
        self.owm = PyOWM.OWM(self.api_key)
        self.weather_mgr = self.owm.weather_manager()
        self.lat = None
        self.lon = None
        self.current_weather = None

    def get_location(self, city_name):
        mgr = self.owm.geocoding_manager()
        location = mgr.geocode(city_name)
        self.lat = location[0].lat
        self.lon = location[0].lon

    def get_weather(self):
        weather = self.weather_mgr.weather_at_coords(self.lat, self.lon)
        self.current_weather = weather.weather

    def display_weather(self):
        weather_status = self.current_weather.status
        print("Weather Status:", weather_status)
        detailed_status = self.current_weather.detailed_status
        print("Detailed Weather Status:", detailed_status)
        temperature = self.current_weather.temperature('celsius')
        print("Temperature:", temperature)
        humidity = self.current_weather.humidity
        print("Humidity:", humidity)
        wind = self.current_weather.wind()
        print("Wind:", wind)
        rain = self.current_weather.rain
        if len(rain) != 0:
            print("Rain:", rain)
        snow = self.current_weather.snow
        if len(snow) != 0:
            print("Snow:", snow)
        clouds = self.current_weather.clouds
        print("Clouds:", clouds)
        sunrise_time = self.current_weather.sunrise_time('iso')
        print("Sunrise Time:", sunrise_time)
        sunset_time = self.current_weather.sunset_time('iso')
        print("Sunset Time:", sunset_time)


# use the above class Weather to create a weather object and display
# the weather data for the city taken as input from command line argument

if __name__ == "__main__":
    city_name = sys.argv[1]
    weather = Weather()
    weather.get_location(city_name)
    weather.get_weather()
    weather.display_weather()
