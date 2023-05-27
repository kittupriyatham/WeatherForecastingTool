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
        weather_status = self.current_weather.weather_status
        print(weather_status)
        detailed_status = self.current_weather.detailed_status
        print(detailed_status)
        temperature = self.current_weather.temperature('celsius')
        print(temperature)
        humidity = self.current_weather.humidity
        print(humidity)
        wind = self.current_weather.wind()
        print(wind)
        rain = self.current_weather.rain
        print(rain)
        snow = self.current_weather.snow
        print(snow)
        clouds = self.current_weather.clouds
        print(clouds)
        reference_time = self.current_weather.reference_time('iso')
        print(reference_time)
        sunrise_time = self.current_weather.sunrise_time('iso')
        print(sunrise_time)
        sunset_time = self.current_weather.sunset_time('iso')
        print(sunset_time)
        visibility_distance = self.current_weather.visibility_distance
        print(visibility_distance)
        weather_code = self.current_weather.weather_code
        print(weather_code)
        weather_icon_name = self.current_weather.weather_icon_name
        print(weather_icon_name)


# use the above class Weather to create a weather object and display
# the weather data for the city taken as input from command line argument

if __name__ == "__main__":
    city_name = sys.argv[1]
    weather = Weather()
    weather.get_location(city_name)
    weather.get_weather()
    weather.display_weather()
