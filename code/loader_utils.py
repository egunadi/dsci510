import os
os.environ['KAGGLE_USERNAME'] = "ebenflow"
os.environ['KAGGLE_KEY'] = "d9b9d7784aa0374e64bf8f7e4a55ff17"

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.dataset_download_files('ahmedshahriarsakib/uber-eats-usa-restaurants-menus', path="../data/ubereats")
api.dataset_download_files('canggih/indonesian-food-recipes', path="../data/indorecipes")

import zipfile
with zipfile.ZipFile('../data/ubereats/uber-eats-usa-restaurants-menus.zip', 'r') as zip_ref:
    zip_ref.extractall('../data/ubereats')

with zipfile.ZipFile('../data/indorecipes/indonesian-food-recipes.zip', 'r') as zip_ref:
    zip_ref.extractall('../data/indorecipes')
