# python3 -m pip install google_streetview
# Import google_streetview for the api module
import google_streetview.api
import google_streetview.helpers

# Define parameters for street view api
key = 'mykey'

def gen_coords(south_west, north_east, intervals):
    south,west = south_west
    north,east = north_east
    lat = []
    spacing = (north - south) / intervals
    for i in range(intervals):
        lat.append(south + spacing * i)
    lon = []
    spacing = (east - west) / intervals
    for i in range(intervals):
        lon.append(west + spacing * i)
    # lat = [l for l in range(south, north, abs(north - south) / intervals)]
    # lon = [l for l in range(west, east, abs(east - west) / interval)]
    return {"lat": lat,
            "lon": lon}

    
def main():
    # Define parameters for street view api
    params = [{
    'size': '600x300', # max 640x640 pixels
    'location': '46.414382,10.013988',
    'heading': '151.78',
    'pitch': '-0.76',
    'key': key
    }]

    # Create a results object
    results = google_streetview.api.results(params)

    # Preview results
    # Download images to directory 'downloads'
    results.download_links('downloads')

    # Save links
    results.save_links('links.txt')

    # Save metadata
    results.save_metadata('metadata.json')

if __name__ == "__main__":
    # main()
    print(gen_coords((17.335162, 78.366367), (17.450953, 78.459989), 3))