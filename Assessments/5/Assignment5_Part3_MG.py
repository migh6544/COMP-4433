## START:

import json
import folium


def states(kansasBoundary, nebraskaBoundary):
    """
    Constructs a GeoJSON file from the boundaries of Kansas and Nebraska.

    Args:
        kansasBoundary (list): Boundary for Kansas represented with 4 lat-lon points.
        nebraskaBoundary (list): Boundary for Nebraska represented with 6 lat-lon points.

    Returns:
        str: The file name of the saved GeoJSON file.
    """

    # Create a GeoJSON structure
    geojsonData = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"name": "Kansas"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [kansasBoundary]
                }
            },
            {
                "type": "Feature",
                "properties": {"name": "Nebraska"},
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [nebraskaBoundary]
                }
            }
        ]
    }

    # Save the GeoJSON data to a file
    outputFile = 'kansas_nebraska.geojson'
    with open(outputFile, 'w') as f:
        json.dump(geojsonData, f)

    return outputFile

def plot_states(fileName):
    """
    Reads a GeoJSON file and plots the result using folium.

    Args:
        fileName (str): The file name of the GeoJSON file to read.

    Returns:
        str: The file name of the saved HTML file.
    """

    # Load the GeoJSON data
    with open(fileName, 'r') as f:
        geojsonData = json.load(f)

    # Create a folium map centered around the middle of the US
    foliumMap = folium.Map(location=[39.0, -98.0], zoom_start = 5)

    # Add the GeoJSON data to the map
    folium.GeoJson(geojsonData).add_to(foliumMap)

    # Save the map to an HTML file
    outputFile = 'states_map.html'
    foliumMap.save(outputFile)

    return outputFile


if __name__ == '__main__':
    kansasBoundary = [
        [-102.0, 40.0], [-102.0, 36.993076], [-94.588413, 36.993076], [-94.588413, 40.0]
    ]
    nebraskaBoundary = [
        [-104.053514, 43.000325], [-104.053514, 40.0], [-95.30829, 40.0], [-95.30829, 42.998581], [-103.000022, 42.998581], [-103.000022, 43.000325]
    ]

    geojsonFile = states(kansasBoundary, nebraskaBoundary)
    mapFile = plot_states(geojsonFile)
    print(f"States map saved to {mapFile}")

## End.