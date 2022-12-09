import pandas as pd
import folium
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data():
    dish_count_path = "../data/dishcount.csv"
    seattlerestaurants_path = "../data/seattlerestaurants.csv"

    # import data
    dish_count_df = pd.read_csv(dish_count_path, delimiter=',', encoding='utf-8')
    seattlerestaurants_df = pd.read_csv(seattlerestaurants_path, delimiter=',', encoding='utf-8')

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
    ax.figure.savefig('../result/dish-category-count.pdf', bbox_inches = 'tight')

    # for bonus assignment: map of indo restaurants in seattle
    seattle_map = folium.Map(   location = [47.6205, -122.3493], # space needle
                                zoom_start = 12   )

    def add_map_markers(restaurant, map):
        folium.Marker(  location = [restaurant['lat'], 
                                    restaurant['lng']], 
                        popup = restaurant['name_restaurant']    ).add_to(map)

    seattlerestaurants_df.apply(add_map_markers, map=seattle_map, axis='columns')

    seattle_map.save('../result/seattle-indorestaurants-map.html')

if __name__ == '__main__':
    visualize_data()
