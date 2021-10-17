import os, json, urllib.request , random

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

with open ("static/data/cities.json") as file:
    cities = json.load(file)

@app.route('/' ,methods=['GET','POST'])
def home():
    if request.method=='POST':
        city = request.form['city_name'].lower()

        city = city.replace(" ", "%20")

        # api_key = os.urandom(24)
        api_key = '2cb5ca9e7bcdd69ad9a80eae91e2c030'

        src = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}').read()
        
        list_of_data = json.loads(src)

        data = { 
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']), 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']),
            "feels_like": str(list_of_data['main']['feels_like']),
            "temp_min": str(list_of_data['main']['temp_min']),
            "temp_max": str(list_of_data['main']['temp_max']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "wind_speed": round(float(str(list_of_data['wind']['speed']))*10, 2),
            "visibility": round(float(str(list_of_data['visibility']))/1000, 2)
        }

        weather_wallpaper = [
            "https://wallpapercave.com/wp/wp4700773.jpg",
            "https://i.pinimg.com/originals/5d/08/8b/5d088b7f58e0123eba09917fd35db40e.jpg",
            "https://eskipaper.com/images/owls-birds-forest-nature-1.jpg",
            "https://i.pinimg.com/originals/73/d7/de/73d7dee7f8becedc39487cb316a35aeb.jpg"
        ]

        weather_wallpaper = random.choice(weather_wallpaper)

        return render_template('weather.html', weather_wallpaper=weather_wallpaper, data=data, city=city, list_of_data=list_of_data) 

    return render_template('index.html', cities=cities)

@app.route("/weather")
def weather():
    return render_template('weather.html')

@app.route("/check")
def check():
    return os.urandom(24)

if __name__ == '__main__':
    app.run(port=5000,debug=True)