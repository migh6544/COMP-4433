## START:

import folium
from shapely.geometry import Polygon


def triangulation(lat1 = None, lon1 = None, lat2 = None, lon2 = None, lat3 = None, lon3 = None):
    """
    Displays points on a map and computes the area and perimeter of the triangle formed by them.

    Args:
        lat1 (float): Latitude of the first point.
        lon1 (float): Longitude of the first point.
        lat2 (float): Latitude of the second point.
        lon2 (float): Longitude of the second point.
        lat3 (float): Latitude of the third point.
        lon3 (float): Longitude of the third point.

    Returns:
        tuple: Area and perimeter of the triangle.
    """

    if lat1 is None or lon1 is None or lat2 is None or lon2 is None or lat3 is None or lon3 is None:
        # Ask the user for input if any of the coordinates are missing
        lat1, lon1 = map(float, input("Enter the latitude and longitude for the first point (e.g., '34.0 -6.8' for Rabat): ").split())
        lat2, lon2 = map(float, input("Enter the latitude and longitude for the second point (e.g., '-33.9 18.4' for Cape Town): ").split())
        lat3, lon3 = map(float, input("Enter the latitude and longitude for the third point (e.g., '2.0 45.3' for Mogadishu): ").split())

    points = [(lat1, lon1), (lat2, lon2), (lat3, lon3)]

    # Create a folium map
    foliumMap = folium.Map(location = [(lat1 + lat2 + lat3) / 3, (lon1 + lon2 + lon3) / 3], zoom_start = 4)

    # Add markers and a polygon for the points
    folium.Marker(location = [lat1, lon1]).add_to(foliumMap)
    folium.Marker(location = [lat2, lon2]).add_to(foliumMap)
    folium.Marker(location = [lat3, lon3]).add_to(foliumMap)

    folium.Polygon(locations = points).add_to(foliumMap)

    # Save the map to an HTML file
    outputFile = 'triangle_map.html'
    foliumMap.save(outputFile)

    # Compute the area and perimeter of the triangle
    polygon = Polygon(points)
    area = polygon.area
    perimeter = polygon.length

    return area, perimeter


if __name__ == '__main__':
    area, perimeter = triangulation()
    print(f"Area: {area}, Perimeter: {perimeter}")

## END.