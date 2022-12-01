import pandas as pd
import folium

indorestaurants_filepath = "data/indorestaurants.csv"

# import data
indorestaurants_df = pd.read_csv(indorestaurants_filepath, delimiter=',', encoding='utf-8')

# filter data
seattlerestaurants_df = indorestaurants_df[indorestaurants_df['full_address']
                                            .str.contains('seattle, wa,', na=False, case=False)]

seattle_map = folium.Map(   location = [47.6205, -122.3493], # space needle
                            zoom_start = 12   )

def add_map_markers(restaurant, map):
    folium.Marker(  location = [restaurant['lat'], 
                                restaurant['lng']], 
                    popup = restaurant['name_restaurant']    ).add_to(map)

seattlerestaurants_df.apply(add_map_markers, map=seattle_map, axis='columns')

seattle_map.save('maps/seattle-indorestaurants-map.html')
