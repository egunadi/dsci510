import pandas as pd
import folium
import matplotlib.pyplot as plt
import seaborn as sns
import analyze_data

# import data
dish_count_df = analyze_data.dish_count_df
seattlerestaurants_df = analyze_data.seattlerestaurants_df

# bar plot of dish category counts
sns.set_style("ticks",{'axes.grid': True})
ax = sns.barplot(   x = dish_count_df['count'],
                    y = dish_count_df['category'].str.capitalize(),
                    color = 'deepskyblue')
ax.tick_params(bottom=False, left=False)
sns.despine(left=True, bottom=True)


plt.xlabel('Number of Uber Eats Restaurant(s) Serving Dish')
plt.ylabel('')
plt.title('Most Common Indonesian Dishes Served in Uber Eats')
ax.figure.savefig('visualization/dish-category-count.pdf', bbox_inches = 'tight')

# for bonus assignment: map of indo restaurants in seattle
seattle_map = folium.Map(   location = [47.6205, -122.3493], # space needle
                            zoom_start = 12   )

def add_map_markers(restaurant, map):
    folium.Marker(  location = [restaurant['lat'], 
                                restaurant['lng']], 
                    popup = restaurant['name_restaurant']    ).add_to(map)

seattlerestaurants_df.apply(add_map_markers, map=seattle_map, axis='columns')

seattle_map.save('visualization/seattle-indorestaurants-map.html')
