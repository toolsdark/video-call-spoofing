import requests

# It helps to make an HTTP GET request to the PHP file, receives the JSON response, and extracts the access token and room name.
#  We wont charge extra to setup tool on your system. 

url = 'http://jagrithacker.com/video_call.php'  

try:
    # Make an HTTP GET request to your PHP file
    response = requests.get(url)

    
    if response.status_code == 200:
        
        data = response.json()

        access_token = data['access_token']
        room_name = data['room_name']

        
        print(f'Access Token: {access_token}')
        print(f'Room Name: {room_name}')
    else:
        print(f'Failed to fetch access token. Status Code: {response.status_code}')
except requests.exceptions.RequestException as e:
    print(f'Failed to make the HTTP request: {e}')
