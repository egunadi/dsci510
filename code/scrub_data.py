import pandas as pd

menus_filepath = "../data/ubereats/restaurant-menus.csv"
restaurants_filepath = "../data/ubereats/restaurants.csv"

# import data
menus_df = pd.read_csv(menus_filepath, delimiter=',', encoding='utf-8')
restaurants_df = pd.read_csv(restaurants_filepath, delimiter=',', encoding='utf-8')
    
# scrub menus data
name_filter_list = ['ayam', 'ikan', 'kambing', 'sapi', 'tahu', 'telur', 'tempe', 'udang', 'indonesia']
menus_df = menus_df[(menus_df['category'].str.contains('indonesia', na=False, case=False)) |
                    (menus_df['name']
                        .str.contains('|'.join(name_filter_list), na=False, case=False))    ]

category_scrub_list = ['sake', 'medicines & treatments', 'bedding', 'storage & cleaning', 'home decor', 'wine', 'nursing & feeding', 'bookstore', 'retail']
menus_df = menus_df[menus_df['category']
                        .str.contains('|'.join(category_scrub_list), na=False, case=False) 
                            == False]
                            
name_scrub_list = ['gekkeikan', 'ramayama', 'mudang', 'nuegados', 'nayama', 'bayamon', 'quesapizza', 'quesapita', 'mikan', 'ketchikan', 'haikan', 'ayamashe', 'fishikan', 'pallipalayam', 'tempered', 'temper', 'tempest', 'ayamase', 'shikanjavi', 'nuegados', 'bikaneri', 'kottayam', 'sapitos']
menus_df = menus_df[menus_df['name']
                        .str.contains('|'.join(name_scrub_list), na=False, case=False) 
                            == False]

# scrub restaurants data
category_scrub_list = ['bookstore', 'personal care', 'mercado express', 'malaysian']
restaurants_df = restaurants_df[restaurants_df['category']
                        .str.contains('|'.join(category_scrub_list), na=False, case=False) 
                            == False]

# export data
menus_df.to_csv('../data/ubereats/restaurant-menus-abridged.csv', encoding='utf-8', index=False)
restaurants_df.to_csv('../data/ubereats/restaurants-abridged.csv', encoding='utf-8', index=False)
