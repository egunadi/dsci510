import pandas as pd
import re

indorestaurants_filepath = "../data/indorestaurants.csv"
abridged_restaurants_filepath = "../data/ubereats/restaurants-abridged.csv"

# import data
indorestaurants_df = pd.read_csv(indorestaurants_filepath, delimiter=',', encoding='utf-8')
restaurants_df = pd.read_csv(abridged_restaurants_filepath, delimiter=',', encoding='utf-8')

# generalize dishes
dishes_df = indorestaurants_df.loc[:, ['restaurant_id', 'name_menuitem']].itertuples()

foodmapping_dict = {'tempe': ['tempe'],
                    'noodle': ['kwetiauw', 'kweetiau', 'kwetiau', 'bihun', 'biehun', 'noodle', 'mie'],
                    'rice': ['rice', 'stir fried', 'nasi', 'bubur', 'hot plate', 'soto'],
                    'chicken': ['ayam', 'chicken'],
                    'vegetarian': ['gado.*gado', 'kangkung', 'pecel'],
                    'fish': ['ikan', 'fish', 'rica.*rica'],
                    'curry': ['laksa', 'curry'],
                    'beef': ['beef', 'rendang', 'sapi', '^bali$'],
                    'bread': ['bread', 'roti'],
                    'shrimp': ['siomay', 'shrimp', 'udang', 'batagor'],
                    'dessert_drinks': ['^es', 'ice cream', 'klapertart', 'coklat', 'dark roast'],
                    'lamb': ['kambing', 'lamb']}

generalized_dish_set = set()

for dish in dishes_df:
    for category, keywords in foodmapping_dict.items():
        for keyword in keywords:
            if re.search(keyword, dish.name_menuitem.lower()):
                generalized_dish_set.add((  dish.restaurant_id,
                                            dish.name_menuitem,
                                            category    ))

generalized_dish_df = pd.DataFrame( generalized_dish_set,
                                    columns = ['restaurant_id', 'name_menuitem', 'category']    )

# group dishes by category and count number of restaurants serving them
dish_count_df = generalized_dish_df.groupby('category')['restaurant_id'] \
                                    .nunique() \
                                    .reset_index(name = 'count') \
                                    .sort_values(['count'], ascending = False)

# for tempe, the most popular category, find menu items served by restaurants scored 4.5+
# note: per data source, max rating is 5
tempe_df = pd.merge(generalized_dish_df, restaurants_df,
                    left_on='restaurant_id', right_on='id', 
                    suffixes=('_menuitem', '_restaurant'))

tempe_df = tempe_df[(tempe_df['category_menuitem'] == 'tempe') &
                    (tempe_df['score'] >= 4.9)] \
                .sort_values(['score'], ascending = False)

if __name__ == '__main__':
    print(tempe_df.loc[:, ['name_menuitem', 'name', 'score', 'full_address', 'zip_code']].to_markdown())

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
