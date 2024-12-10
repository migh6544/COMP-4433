## Start:


import pandas as pd
import json
import folium
import geopandas as gpd
from folium.features import GeoJson, GeoJsonTooltip
from branca.colormap import linear


def load_json(file_path):
    """
    Loads a JSON file and returns the data.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Loaded JSON data.
    """

    try:
        with open(file_path) as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading JSON file from {file_path}: {e}")
        return None

def load_geojson(geojson_path):
    """
    Loads the GeoJSON file and returns a GeoDataFrame.

    Args:
        geojson_path (str): Path to the GeoJSON file.

    Returns:
        gpd.GeoDataFrame: Loaded geographic data.
    """

    try:
        gdf = gpd.read_file(geojson_path)
        return gdf
    except Exception as e:
        print(f"Error loading GeoJSON file: {e}")
        return None

def the_48():
    """
    Generates choropleth visualizations for each column containing dates,
    showing timelines of achievement for each milestone/column in the dataset.

    Returns:
        folium.Map: A folium map with all the visualizations.
    """

    # Load the data
    sturm_data = pd.read_csv('SturmData.csv')
    states_hash = load_json('states_hash.json')

    if states_hash is None:
        print("Failed to load necessary JSON data.")
        return None

    # Load the GeoJSON file
    geojson_path = 'us-states.json'
    geojson_file = load_geojson(geojson_path)

    if geojson_file is None:
        print("GeoJSON loading failed. Please check the file path and format.")
        return None

    # Print the columns in the GeoJSON to identify the correct column for state names
    print("GeoJSON Columns:", geojson_file.columns)

    # Update the column name if necessary column name in the GeoJSON
    state_name_column = 'name'

    # Mapping state abbreviations to full names
    sturm_data['state_full'] = sturm_data['state'].map(states_hash)

    # Define the codebook
    code_book = {
        'debtfree': 'Year of passage of state law protecting married women’s separate property from her husband’s debts',
        'effectivemwpa': 'Year of passage of state law granting married women control and management rights over their separate property',
        'earnings': 'Year of passage of state law granting married women ownership of their wages or earnings on par with other separate property',
        'wills': "Year of passage of state law granting married women the ability to write wills without their husband's consent or other restrictions",
        'soletrader': 'Year of passage of state law granting married women as a class the right to sign contracts and engage in business without consent of husband'
    }

    # Create the base map for combined visualizations
    combined_map = folium.Map(location = [37.8, -96], zoom_start = 4)

    for col, description in code_book.items():
        # Merge the GeoJSON and the data
        merged = geojson_file.set_index(state_name_column).join(sturm_data.set_index('state_full'))

        # Ensure the 'name' column is retained
        merged.reset_index(inplace = True)

        # Debugging: Print merged DataFrame columns and sample data
        print(f"Columns in merged DataFrame for {col}:", merged.columns)
        print(merged.head())

        # Create the colormap
        colormap = linear.YlOrRd_09.scale(merged[col].min(), merged[col].max())
        colormap.caption = description

        # Add a choropleth layer to the combined map
        choropleth = folium.Choropleth(
            geo_data = geojson_file,
            data = merged,
            columns = ['name', col],
            key_on = 'feature.properties.name',
            fill_color = 'YlOrRd',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = description,
            nan_fill_color = 'black',  # For missing data
            nan_fill_opacity = 0.5,
            name=f'{description} (Color)'
        ).add_to(combined_map)

        # Add a cross-hatch pattern for missing data
        def style_function(feature):
            value = feature['properties'].get(col, None)
            return {
                'fillPattern': 'crosshatch' if value is None else 'none',
                'fillColor': colormap(value) if value is not None else 'black',
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.7 if value is not None else 0.5
            }

        geojson = GeoJson(
            data = merged.to_json(),
            style_function = style_function,
            tooltip = GeoJsonTooltip(
                fields = ['name', col],
                aliases = ['State', description],
                localize = True
            ),
            name = f'{description} (Color) Tooltip'
        ).add_to(combined_map)

        # Add grayscale compatibility to the combined map
        colormap_grey = linear.Greys_09.scale(merged[col].min(), merged[col].max())
        colormap_grey.caption = description + ' (Grayscale)'

        choropleth_grey = folium.Choropleth(
            geo_data = geojson_file,
            data = merged,
            columns = ['name', col],
            key_on = 'feature.properties.name',
            fill_color = 'Greys',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = description + ' (Grayscale)',
            nan_fill_color = 'black',
            nan_fill_opacity = 0.5,
            name = f'{description} (Grayscale)'
        ).add_to(combined_map)

        geojson_grey = GeoJson(
            data = merged.to_json(),
            style_function = style_function,
            tooltip = GeoJsonTooltip(
                fields = ['name', col],
                aliases = ['State', description],
                localize = True
            ),
            name = f'{description} (Grayscale) Tooltip'
        ).add_to(combined_map)

        # Create individual map for each milestone
        individual_map = folium.Map(location = [37.8, -96], zoom_start = 4)

        # Add the color choropleth layer to the individual map
        choropleth = folium.Choropleth(
            geo_data = geojson_file,
            data = merged,
            columns = ['name', col],
            key_on = 'feature.properties.name',
            fill_color = 'YlOrRd',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = description,
            nan_fill_color = 'black',  # For missing data
            nan_fill_opacity = 0.5,
            name = f'{description} (Color)'
        ).add_to(individual_map)

        geojson = GeoJson(
            data = merged.to_json(),
            style_function = style_function,
            tooltip = GeoJsonTooltip(
                fields = ['name', col],
                aliases = ['State', description],
                localize = True
            ),
            name = f'{description} (Color) Tooltip'
        ).add_to(individual_map)

        # Add the grayscale choropleth layer to the individual map
        choropleth_grey = folium.Choropleth(
            geo_data = geojson_file,
            data = merged,
            columns = ['name', col],
            key_on = 'feature.properties.name',
            fill_color = 'Greys',
            fill_opacity = 0.7,
            line_opacity = 0.2,
            legend_name = description + ' (Grayscale)',
            nan_fill_color = 'black',
            nan_fill_opacity = 0.5,
            name = f'{description} (Grayscale)'
        ).add_to(individual_map)

        geojson_grey = GeoJson(
            data = merged.to_json(),
            style_function = style_function,
            tooltip = GeoJsonTooltip(
                fields = ['name', col],
                aliases = ['State', description],
                localize = True
            ),
            name = f'{description} (Grayscale) Tooltip'
        ).add_to(individual_map)

        folium.LayerControl().add_to(individual_map)

        # Save the individual map to an HTML file
        individual_map.save(f'{col}_map.html')

    # Add layer control to the combined map
    folium.LayerControl().add_to(combined_map)

    return combined_map

if __name__ == '__main__':
    combined_map = the_48()
    if combined_map:
        # Save the combined map to a single HTML file
        combined_map.save('combined_maps.html')


## END.