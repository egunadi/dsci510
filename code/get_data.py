import os

def get_data():
    os.environ['KAGGLE_USERNAME'] = "" -- enter own username 
    os.environ['KAGGLE_KEY'] = "" -- enter own key

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

if __name__ == '__main__':
    get_data()
