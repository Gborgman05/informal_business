# python3 -m pip install google_streetview
# Import google_streetview for the api module
import google_streetview.api
import google_streetview.helpers
import itertools

# Define parameters for street view api
key = 'mykey'

def gen_coords(south_west, north_east, intervals):
    """
    generates equally spaced coordinates between a southwest
    to north east coordinate, generating a total of intervals ** 2 coordinates
    """
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
    
    return [f"{i[0]:.6f},{i[1]:.6f}" for i in itertools.product(lat, lon)]

    
def main():
    # Define parameters for street view api
    coords = gen_coords((17.335162, 78.366367), (17.450953, 78.459989), 10)
    # unsure what to do for heading / pitch
    params = [{
    'size': '600x300', # max 640x640 pixels
    'location': coord,
    'heading': '151.78',
    'pitch': '-0.76',
    'key': key,
    'source': 'outdoor'
    } for coord in coords]
    

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
    main()
    # print(gen_coords((17.335162, 78.366367), (17.450953, 78.459989), 3))