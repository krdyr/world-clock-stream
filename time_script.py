import time
import requests
from bs4 import BeautifulSoup

cities = ['America/New_York', 'Europe/London', 'Asia/Tokyo', 'Australia/Sydney']
city_colors = ["#FF4500", "#ADD8E6", "#FF69B4", "#1E90FF"] # Orange for New York, Light Blue for London, Hot Pink for Tokyo, Dodger Blue for Sydney

def get_city_time(city):
    response = requests.get(f'http://worldtimeapi.org/api/timezone/{city}')
    data = response.json()
    datetime = data['datetime']
    time = datetime.split('T')[1].split('.')[0]
    return time

while True:
    html_content = """
    <html>
    <head>
        <style>
            body {
                background-color: black;
                color: white;
                font-family: Arial, sans-serif;
                display: grid;
                grid-template-columns: 1fr 1fr;
                justify-items: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            .city {
                border: 1px solid white;
                padding: 20px;
                margin: 10px;
                text-align: center;
                width: 90%;
                box-sizing: border-box;
                background-color: rgba(255, 255, 255, 0.1);
            }
            h1 {
                font-size: 3em;
            }
            h2 {
                font-size: 2em;
            }
        </style>
    </head>
    <body>
    """

    for i in range(len(cities)):
        city_time = get_city_time(cities[i])
        html_content += f"""
        <div class='city' style='color:{city_colors[i]};'>
            <h2>{cities[i].split('/')[-1]}</h2>
            <h1>{city_time}</h1>
        </div>
        """

    html_content += "</body></html>"

    with open('index.html', 'w') as f:
        f.write(html_content)

    time.sleep(1)  # wait for 1 second before refreshing the time
