import pandas as pd
import re

indorestaurants_filepath = "../data/indorestaurants.csv"

# import data
indorestaurants_df = pd.read_csv(indorestaurants_filepath, delimiter=',', encoding='utf-8')

# generalize dishes
dishes_df = indorestaurants_df.loc[:, ['restaurant_id', 'name_menuitem']].itertuples()

foodmapping_dict = {'tempe': ['tempe'],
                    'noodle': ['kwetiauw', 'kweetiau', 'kwetiau', 'bihun', 'biehun', 'noodle', 'mie'],
                    'rice': ['rice', 'stir fried', 'nasi', 'bubur', 'hot plate', 'soto'],
                    'chicken': ['ayam', 'chicken'],
                    'vegetarian': ['gado.*gado'],
                    'fish': ['ikan', 'fish', 'rica.*rica'],
                    'curry': ['laksa', 'curry'],
                    'beef': ['beef', 'rendang', 'sapi', '^bali$'],
                    'bread': ['bread', 'roti'],
                    'shrimp': ['siomay', 'shrimp', 'udang', 'batagor'],
                    'dessert_drinks': ['^es', 'ice cream', 'klapertart', 'coklat', 'dark roast'],
                    'lamb': ['kambing', 'lamb']}

generalized_dish_list = []

for dish in dishes_df:
    for category, keywords in foodmapping_dict.items():
        for keyword in keywords:
            if re.search(keyword, dish.name_menuitem.lower()):
                generalized_dish_list.append((  dish.restaurant_id,
                                                dish.name_menuitem,
                                                category    ))

generalized_dish_df = pd.DataFrame( generalized_dish_list,
                                    columns = ['restaurant_id', 'name_menuitem', 'category']    )

# group dishes by category and count number of restaurants serving them
dish_count_df = generalized_dish_df.groupby('category')['restaurant_id'] \
                                    .nunique() \
                                    .reset_index(name = 'count') \
                                    .sort_values(['count'], ascending = False)

# for bonus assignment: 
# 1. find cities with most indonesian restaurants 
indorestaurants_df['city'] = indorestaurants_df['full_address'].str.extract(r'(\w+, \w{2}), \d{5}', expand = False)

indorestaurant_cities_df = indorestaurants_df.groupby('city')['restaurant_id'] \
                                                .nunique() \
                                                .reset_index(name = 'count') \
                                                .sort_values(['count'], ascending = False)

if __name__ == '__main__':
    print(indorestaurant_cities_df.head(3))

# OUTPUT
""" 
            city  count
15  Portland, OR     12
20   Seattle, WA      8
4       City, UT      3
"""

# 2. find seattle restaurants
seattlerestaurants_df = indorestaurants_df[indorestaurants_df['city'] == 'Seattle, WA']
