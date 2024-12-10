## START:

import pandas as pd
import folium


def capitals():
    """
    Reads a CSV file with capital cities' latitude and longitude,
    and writes an HTML file displaying markers for each capital city using folium.

    Args:
        None

    Returns:
        str: The file name of the saved HTML file.
    """

    # Read the CSV file into a DataFrame
    df = pd.read_csv('capitals_lat_lon.csv')

    # Create a folium map centered around the average coordinates
    mapCenter = [df['Latitude'].mean(), df['Longitude'].mean()]
    foliumMap = folium.Map(location = mapCenter, zoom_start = 2)

    # Add markers for each capital city
    for _, row in df.iterrows():
        folium.Marker(
            location = [row['Latitude'], row['Longitude']],
            popup = row['Capital']
        ).add_to(foliumMap)

    # Save the map to an HTML file
    outputFile = 'capitals_map.html'
    foliumMap.save(outputFile)

    return outputFile


if __name__ == '__main__':
    mapFile = capitals()
    print(f"Capitals map saved to {mapFile}")

## END.