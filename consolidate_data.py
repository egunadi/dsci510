import pandas as pd

ayam_filepath = "data/indorecipes/dataset-ayam.csv"
ikan_filepath = "data/indorecipes/dataset-ikan.csv"
kambing_filepath = "data/indorecipes/dataset-kambing.csv"
sapi_filepath = "data/indorecipes/dataset-sapi.csv"
tahu_filepath = "data/indorecipes/dataset-tahu.csv"
telur_filepath = "data/indorecipes/dataset-telur.csv"
tempe_filepath = "data/indorecipes/dataset-tempe.csv"
udang_filepath = "data/indorecipes/dataset-udang.csv"

# import data
ayam_df = pd.read_csv(ayam_filepath, delimiter=',', encoding='utf-8')
ikan_df = pd.read_csv(ikan_filepath, delimiter=',', encoding='utf-8')
kambing_df = pd.read_csv(kambing_filepath, delimiter=',', encoding='utf-8')
sapi_df = pd.read_csv(sapi_filepath, delimiter=',', encoding='utf-8')
tahu_df = pd.read_csv(tahu_filepath, delimiter=',', encoding='utf-8')
telur_df = pd.read_csv(telur_filepath, delimiter=',', encoding='utf-8')
tempe_df = pd.read_csv(tempe_filepath, delimiter=',', encoding='utf-8')
udang_df = pd.read_csv(udang_filepath, delimiter=',', encoding='utf-8')

# preserve data on source file
ayam_df['broadcategory'] = 'ayam'
ikan_df['broadcategory'] = 'ikan'
kambing_df['broadcategory'] = 'kambing'
sapi_df['broadcategory'] = 'sapi'
tahu_df['broadcategory'] = 'tahu'
telur_df['broadcategory'] = 'telur'
tempe_df['broadcategory'] = 'tempe'
udang_df['broadcategory'] = 'udang'

# consolidate data
indofoods_df =  pd.concat([ayam_df, ikan_df, kambing_df, sapi_df, tahu_df, telur_df, tempe_df, udang_df])

# export data
indofoods_df.to_csv('data/indorecipes/indofoods.csv', encoding='utf-8', index=False)
