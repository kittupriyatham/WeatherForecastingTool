# import PyOWM api
# use it to get location longitude and latitude
# given city name using geocoding manager of PyOWM
# use it to get weather data
# given longitude and latitude using weather manager of PyOWM

import pyowm.owm as PyOWM
import config

# API key from config.py
api_key = config.api_key

# Create OWM object
owm = PyOWM.OWM(api_key)

# Create geocoding manager object
mgr = owm.geocoding_manager()

# Get location lat and lon
location = mgr.geocode('Boston, US')
lat = location[0].lat
lon = location[0].lon

# Create weather manager object
weather_mgr = owm.weather_manager()

# Get weather data given lat and lon
weather = weather_mgr.weather_at_coords(lat, lon)

# Get current weather data
current_weather = weather.weather

# display current weather data
print(current_weather)

# Get temperature
temperature = current_weather.temperature('celsius')

# display temperature
print(temperature)

# Get humidity
humidity = current_weather.humidity

# display humidity
print(humidity)

# Get wind
wind = current_weather.wind()

# display wind
print(wind)

# Get rain
rain = current_weather.rain

# display rain
print(rain)

# Get snow
snow = current_weather.snow

# display snow
print(snow)

# Get clouds
clouds = current_weather.clouds

# display clouds
print(clouds)

# Get reference time
reference_time = current_weather.reference_time('iso')

# display reference time
print(reference_time)

# Get sunrise time
sunrise_time = current_weather.sunrise_time('iso')

# display sunrise time
print(sunrise_time)

# Get sunset time
sunset_time = current_weather.sunset_time('iso')

# display sunset time
print(sunset_time)

# Get visibility distance
visibility_distance = current_weather.visibility_distance

# display visibility distance
print(visibility_distance)

# Get weather code
weather_code = current_weather.weather_code

# display weather code
print(weather_code)

# Get weather icon name
weather_icon_name = current_weather.weather_icon_name

# display weather icon name
print(weather_icon_name)

# Get weather status
weather_status = current_weather.weather_status

# display weather status
print(weather_status)

# Get detailed weather status
detailed_status = current_weather.detailed_status

# display detailed weather status
print(detailed_status)


# reformat above code to use functions and classes so that
# constructor should initiate the pyowm apikey and
# one function to get location lat and lon given city name
# second function to get weather data given lat and lon
# and another function display the weather data

class Weather:

    def __init__(self, api_key):
        self.api_key = api_key
        self.owm = PyOWM.OWM(api_key)
        self.weather_mgr = self.owm.weather_manager()

    def get_location(self, city_name):
        mgr = self.owm.geocoding_manager()
        location = mgr.geocode(city_name)
        lat = location[0].lat
        lon = location[0].lon
        return lat, lon

    def get_weather(self, lat, lon):
        weather = self.weather_mgr.weather_at_coords(lat, lon)
        current_weather = weather.weather
        return current_weather

    def display_weather(self, current_weather):
        print(current_weather)
        temperature = current_weather.temperature('celsius')
        print(temperature)
        humidity = current_weather.humidity
        print(humidity)
        wind = current_weather.wind()
        print(wind)
        rain = current_weather.rain
        print(rain)
        snow = current_weather.snow
        print(snow)
        clouds = current_weather.clouds
        print(clouds)
        reference_time = current_weather.reference_time('iso')
        print(reference_time)
        sunrise_time = current_weather.sunrise_time('iso')
        print(sunrise_time)
        sunset_time = current_weather.sunset_time('iso')
        print(sunset_time)
        visibility_distance = current_weather.visibility_distance
        print(visibility_distance)
        weather_code = current_weather.weather_code
        print(weather_code)
        weather_icon_name = current_weather.weather_icon_name
        print(weather_icon_name)
        weather_status = current_weather.weather_status
        print(weather_status)
        detailed_status = current_weather.detailed_status
        print(detailed_status)


# reformat the class Weather to include location and weather as attributes
# and donot return them from the functions
# instead store them in the attributes and
# use them in the display_weather function


class Weather:

    def __init__(self, api_key):
        self.api_key = api_key
        self.owm = PyOWM.OWM(api_key)
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
        print(self.current_weather)
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
        weather_status = self.current_weather.weather_status
        print(weather_status)
        detailed_status = self.current_weather.detailed_status
        print(detailed_status)


# in the above class Weather, reformat the display_weather function to
# display the weather data in the order of the weather_status,
# detailed_status, temperature, humidity, wind, rain, snow, clouds,
# reference_time, sunrise_time, sunset_time, visibility_distance,
# weather_code, weather_icon_name


import pyowm as PyOWM
import config


class Weather:

    def __init__(self):
        self.api_key = config.api_key
        self.owm = PyOWM.OWM(api_key)
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
# the weather data for the city of your choice as a command line argument
