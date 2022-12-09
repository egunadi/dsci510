import pandas as pd
import re


def analyze_data():
    indorestaurants_filepath = "../data/indorestaurants.csv"

    # import data
    indorestaurants_df = pd.read_csv(indorestaurants_filepath, delimiter=',', encoding='utf-8')

    # generalize dishes
    dishes_df = indorestaurants_df.loc[:, ['restaurant_id', 'name_menuitem']].itertuples()

    foodmapping_dict = {'tempe': ['tempe'],
                        'noodle': ['kwetiauw', 'kweetiau', 'kwetiau', 'bihun', 'biehun', 'noodle', 'mie'],
                        'rice': ['rice', 'stir fried', 'nasi', 'bubur', 'hot plate', 'soto'],
                        'chicken': ['ayam', 'chicken'],
                        'vegetarian': ['gado.*gado', 'kangkung', 'pecel', 'sayur'],
                        'fish': ['ikan', 'fish', 'rica.*rica'],
                        'curry': ['laksa', 'curry'],
                        'beef': ['beef', 'rendang', 'sapi', '^bali$', 'bakso'],
                        'bread': ['bread', 'roti', 'bawang'],
                        'shrimp': ['siomay', 'shrimp', 'udang', 'batagor'],
                        'dessert_drinks': ['^es', 'ice cream', 'klapertart', 'coklat', 'dark roast'],
                        'lamb': ['kambing', 'lamb'],
                        'pork': ['pork', 'lumpia'],
                        'tofu': ['tofu', 'tahu']}

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
    generalized_dish_df.to_csv('../data/generalized_dish.csv', encoding='utf-8', index=False)

    # group dishes by category and count number of restaurants serving them
    dish_count_df = generalized_dish_df.groupby('category')['restaurant_id'] \
                                        .nunique() \
                                        .reset_index(name = 'count') \
                                        .sort_values(['count'], ascending = False)

    dish_count_df.to_csv('../data/dishcount.csv', encoding='utf-8', index=False)

    # for tempe, the most popular category, find menu items served by restaurants scored >= 4.9
    # note: per data source, max rating is 5
    left_df = generalized_dish_df.set_index(['restaurant_id', 'name_menuitem'])
    right_df = indorestaurants_df.set_index(['restaurant_id', 'name_menuitem'])
    merged_generalized_dish_df = left_df.join(right_df).reset_index()

    merged_generalized_dish_df = merged_generalized_dish_df \
                                    .rename(columns = { 'name_menuitem': 'Dish',
                                                        'description': 'Description',
                                                        'name_restaurant': 'Restaurant',
                                                        'score': 'Rating',
                                                        'full_address': 'Address'   })

    merged_generalized_dish_df['Description'] = merged_generalized_dish_df['Description'].replace(r'\n', ' ', regex = True)
    merged_generalized_dish_df['Description'] = merged_generalized_dish_df['Description'].fillna('Description Unavailable')

    tempe_df = merged_generalized_dish_df[  (merged_generalized_dish_df['category'] == 'tempe') &
                                            (merged_generalized_dish_df['Rating'] >= 4.9)    ] \
                .sort_values(['Rating'], ascending = False)

    export_columns_list = ['Dish', 'Description', 'Restaurant', 'Rating', 'Address']
    tempe_df.loc[:, export_columns_list] \
            .drop_duplicates() \
            .to_html('../result/tempe_dishes.html', index = False)

    with open('../result/tempe_dishes.html','r') as contents:
        save = contents.read()
    with open('../result/tempe_dishes.html','w') as contents:
        contents.write("<div style='height: 400px; overflow: auto; width: fit-content'>")
    with open('../result/tempe_dishes.html','a') as contents:
        contents.write(save)
    with open('../result/tempe_dishes.html','a') as contents:
        contents.write("</div>")

    # for non tempe dishes, find menu items served by restaurants scored >= 4.9
    non_tempe_df = merged_generalized_dish_df[  (merged_generalized_dish_df['category'] != 'tempe') &
                                                (merged_generalized_dish_df['Rating'] >= 4.9) &
                                                (merged_generalized_dish_df['Dish']
                                                    .str.contains('tempe', na=False, case=False)
                                                        == False)   ] \
                    .sort_values(['Rating'], ascending = False)

    non_tempe_df.loc[:, export_columns_list] \
                .drop_duplicates() \
                .to_html('../result/non_tempe_dishes.html', index = False)

    with open('../result/non_tempe_dishes.html','r') as contents:
        save = contents.read()
    with open('../result/non_tempe_dishes.html','w') as contents:
        contents.write("<div style='height: 400px; overflow: auto; width: fit-content'>")
    with open('../result/non_tempe_dishes.html','a') as contents:
        contents.write(save)
    with open('../result/non_tempe_dishes.html','a') as contents:
        contents.write("</div>")

    # for bonus assignment: 
    # 1. find cities with most indonesian restaurants 
    indorestaurants_df['city'] = indorestaurants_df['full_address'].str.extract(r'(\w+, \w{2}), \d{5}', expand = False)

    indorestaurant_cities_df = indorestaurants_df.groupby('city')['restaurant_id'] \
                                                    .nunique() \
                                                    .reset_index(name = 'count') \
                                                    .sort_values(['count'], ascending = False)

    # print(indorestaurant_cities_df.head(3))
    # OUTPUT
    """ 
                city  count
    15  Portland, OR     12
    20   Seattle, WA      8
    4       City, UT      3
    """

    # 2. find seattle restaurants
    seattlerestaurants_df = indorestaurants_df[indorestaurants_df['city'] == 'Seattle, WA']

    seattlerestaurants_df.to_csv('../data/seattlerestaurants.csv', encoding='utf-8', index=False)

if __name__ == '__main__':
    analyze_data()
