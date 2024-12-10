## START:

import folium
import numpy as np
import pandas as pd
import json


def if_youre_happy_and_you_know_it():
    """
    Generates a random happiness index for each state and visualizes it as a choropleth map.

    Args:
        None

    Returns:
        str: The file name of the saved HTML file.
    """

    # Load GeoJSON data
    stateGeo = 'us-states.json'

    # Load state names
    with open('states_list.json', 'r') as f:
        stateNames = json.load(f)

    # Generate random happiness indices for each state
    stateData = pd.DataFrame({
        'State Name': stateNames,
        'Happiness Index': np.random.rand(len(stateNames)) * 100
    })

    # Print state data
    print(stateData)

    # Create a folium map
    foliumMap = folium.Map(location = [37.8, -96], zoom_start = 4)

    # Add the choropleth map
    folium.Choropleth(
        geo_data = stateGeo,
        name = 'choropleth',
        data = stateData,
        columns = ['State Name', 'Happiness Index'],
        key_on = 'feature.properties.name',
        fill_color = 'YlGn',
        fill_opacity = 0.4,
        line_opacity = 0.8,
        legend_name = 'Happiness Index'
    ).add_to(foliumMap)

    # Add a layer control to toggle the choropleth
    folium.LayerControl().add_to(foliumMap)

    # Save the map to an HTML file
    outputFile = 'happiness_map.html'
    foliumMap.save(outputFile)

    return outputFile

if __name__ == '__main__':
    mapFile = if_youre_happy_and_you_know_it()
    print(f"Happiness map saved to {mapFile}")

## END.