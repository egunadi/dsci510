import pandas as pd

menu_filepath = "data/ubereats/restaurant-menus.csv"

# import data
menu_df = pd.read_csv(menu_filepath, delimiter=',', encoding='utf-8')
    
# scrub data
name_filter_list = ['ayam', 'ikan', 'kambing', 'sapi', 'tahu', 'telur', 'tempe', 'udang']
menu_df = menu_df[menu_df['name']
                        .str.contains('|'.join(name_filter_list), na=False, case=False)]

category_scrub_list = ['sake', 'medicines & treatments', 'bedding', 'storage & cleaning', 'home decor', 'wine', 'nursing & feeding', 'bookstore', 'retail']
menu_df = menu_df[menu_df['category']
                        .str.contains('|'.join(category_scrub_list), na=False, case=False) 
                            == False]
                            
name_scrub_list = ['gekkeikan', 'ramayama', 'mudang', 'nuegados', 'nayama', 'bayamon', 'quesapizza', 'quesapita', 'mikan', 'ketchikan', 'haikan', 'ayamashe', 'fishikan', 'pallipalayam', 'tempered', 'temper', 'tempest', 'ayamase', 'shikanjavi', 'nuegados', 'bikaneri', 'kottaya', 'sapitos']
menu_df = menu_df[menu_df['name']
                        .str.contains('|'.join(name_scrub_list), na=False, case=False) 
                            == False]
# export data
menu_df.to_csv('data/ubereats/restaurant-menus-abridged.csv', encoding='utf-8', index=False)
