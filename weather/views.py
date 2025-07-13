from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    weather_data = {}
    image_url = '' # Initialize image_url

    if 'city' in request.GET:
        city = request.GET['city'].strip()
        
        # OpenWeatherMap API
        weather_api_key = '8056ca23be302b9d96d4a43498d4fc99'
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric'
        weather_response = requests.get(weather_url)

        if weather_response.status_code == 200:
            data = weather_response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found or weather data unavailable'}
        
        # Unsplash API for background image
        unsplash_access_key = '4OnJHy3XZcco88qR9QScNs3AWX4TrWH13B-HYc3t-R0'
        unsplash_url = f'https://api.unsplash.com/search/photos?query={city}&client_id={unsplash_access_key}&orientation=landscape&per_page=1'
        
        try:
            unsplash_response = requests.get(unsplash_url)
            if unsplash_response.status_code == 200:
                unsplash_data = unsplash_response.json()
                if unsplash_data['results']:
                    image_url = unsplash_data['results'][0]['urls']['regular']
                else:
                    image_url = 'https://images.unsplash.com/photo-1542496658-00566378c8a1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w1ODc0Mjl8MHwxfHNlYXJjaHwxfHxkZWZhdWx0JTIwc2t5fGVufDB8fHx8MTcwMTk1NzU0Nnww&ixlib=rb-4.0.3&q=80&w=1080' # Default image if no city image found
            else:
                print(f"Unsplash API Error: {unsplash_response.status_code} - {unsplash_response.text}")
                image_url = 'https://images.unsplash.com/photo-1542496658-00566378c8a1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w1ODc0Mjl8MHwxfHNlYXJjaHwxfHxkZWZhdWx0JTIwc2t5fGVufDB8fHx8MTcwMTk1NzU0Nnww&ixlib=rb-4.0.3&q=80&w=1080' # Default on error
        except requests.exceptions.RequestException as e:
            print(f"Unsplash Request Error: {e}")
            image_url = 'https://images.unsplash.com/photo-1542496658-00566378c8a1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w1ODc0Mjl8MHwxfHNlYXJjaHwxfHxkZWZhdWx0JTIwc2t5fGVufDB8fHx8MTcwMTk1NzU0Nnww&ixlib=rb-4.0.3&q=80&w=1080' # Default on exception

    return render(request, 'weather/index.html', {'weather': weather_data, 'background_image': image_url})
