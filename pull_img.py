import google_streetview.api
import itertools

# Define parameters for street view api
key = 'mykey'

def gen_coords(south_west, north_east, x_interval, y_interval):
    """
    generates equally spaced coordinates between a southwest
    to north east coordinate, generating a total of intervals ** 2 coordinates
    """
    south,west = south_west
    north,east = north_east
    lat = []
    spacing = (north - south) / y_interval
    for i in range(y_interval):
        lat.append(south + spacing * i)
    lon = []
    spacing = (east - west) / x_interval
    for i in range(x_interval):
        lon.append(west + spacing * i)
    
    # formatting coordinates how the api wants it
    return [f"{i[0]:.6f},{i[1]:.6f}" for i in itertools.product(lat, lon)]

    
def main():
    # Define parameters for street view api
    
    coords = gen_coords((17.372985, 78.432067), (17.489595, 78.504851), 10, 100)
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
    print("making request")
    print(len(params))
    results = google_streetview.api.results(params)
    print("done with request")

    # Preview results
    # Download images to directory 'downloads'
    city = "hyderabad"
    results.download_links(city)

    # Save links
    # results.save_links(f'./{city}/links.txt')

    # Save metadata
    results.save_metadata(f'./{city}/metadata.json')

if __name__ == "__main__":
    main()
    # print(gen_coords((17.335162, 78.366367), (17.450953, 78.459989), 3))