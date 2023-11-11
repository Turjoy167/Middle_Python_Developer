import requests


def get_geocoding(api_key, address):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"

    # Parameters for the Geocoding API request
    params = {
        "address": address,
        "key": api_key
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if the API returned results
        if data['status'] == 'OK':
            # Extract the latitude and longitude
            location = data['results'][0]['geometry']['location']
            lat, lng = location['lat'], location['lng']

            print(f"Coordinates for '{address}': Latitude {lat}, Longitude {lng}")
        else:
            print(f"Geocoding API returned status: {data['status']}")
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")


# Replace 'Did not given my actual API for security reason' with own Google API key
api_key = 'Did not given my actual API for security reason.'

# Example usage
address_to_geocode = "1600 Amphitheatre Parkway, Mountain View, CA"
get_geocoding(api_key, address_to_geocode)
