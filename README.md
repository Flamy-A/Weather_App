# Django Weather App

A modern and interactive weather application built with Django, featuring real-time weather data and dynamic background images based on the city.

## Features

*   **Current Weather Display:** Get current temperature, description, and an icon for any city worldwide.
*   **Dynamic Background Images:** Background images dynamically change based on the searched city, fetched from Unsplash.
*   **Modern UI:** Clean and aesthetically pleasing user interface with a glassmorphism effect.
*   **Responsive Design:** Adapts to different screen sizes.

## Technologies Used

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, JavaScript
*   **APIs:**
    *   [OpenWeatherMap API](https://openweathermap.org/api) for weather data.
    *   [Unsplash API](https://unsplash.com/developers) for dynamic city background images.

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### 1. Clone the Repository

First, clone the project repository from GitHub:

```bash
git clone https://github.com/Flamy-A/Weather_App.git
cd Weather_App
```

### 2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**On Windows (PowerShell):**
```bash
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Once your virtual environment is active, install the required Python packages:

```bash
pip install Django requests
```

### 4. Configure API Keys

This project uses external APIs for weather data and background images. You'll need to obtain API keys and update them in your `weather/views.py` file.

*   **OpenWeatherMap API Key:**
    1.  Go to [OpenWeatherMap](https://openweathermap.org/api).
    2.  Sign up for a free account.
    3.  Generate an API key (it might take a few minutes to become active).
    4.  Open `weather/views.py` and replace `'YOUR_OPENWEATHERMAP_API_KEY'` with your actual key:
        ```python
        weather_api_key = 'YOUR_OPENWEATHERMAP_API_KEY' # Replace with your key
        ```

*   **Unsplash API Access Key:**
    1.  Go to [Unsplash Developers](https://unsplash.com/developers).
    2.  Sign up and create a new application.
    3.  Copy your "Access Key".
    4.  Open `weather/views.py` and replace `'YOUR_UNSPLASH_ACCESS_KEY'` with your actual key:
        ```python
        unsplash_access_key = 'YOUR_UNSPLASH_ACCESS_KEY' # Replace with your key
        ```
    _Note: Unsplash has rate limits for development keys. If you frequently get errors, you might be hitting the limit._

### 5. Run Migrations

Apply the initial database migrations for Django:

```bash
python manage.py migrate
```

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

### 7. Access the Application

Open your web browser and go to:

```
http://127.0.0.1:8000/
```

Enter a city name in the input field and click "Search" to see the weather and a dynamic background image!

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

---