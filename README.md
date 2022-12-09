# DSCI510 Final Project: Most Common Indonesian Dishes Orderable via Uber Eats USA

My main goal is to determine which dishes are most common in these restaurants and provide a listing of restaurants serving them. At least two datasets will be used, one containing Uber Eats restaurant menu items and another a comprehensive list of Indonesian dishes. By joining the two sets, we can procure a list of Indonesian dishes orderable via Uber Eats, along with their associated restaurants. 

The first dataset of interest is "Uber Eats USA Restaurants and Menus" from Kaggle <https://www.kaggle.com/datasets/ahmedshahriarsakib/uber-eats-usa-restaurants-menus>. This data was scraped from <https://www.ubereats.com> and comprises of two CSV files:

- "restaurants.csv" contains 40k+ entries of restaurants that have partnered with Uber eats accross the nation
- "restaurant-menus.csv" contains 3.71M menu items orderable from the restaurants in "restaurants.csv"

The dataset is updated frequently and, at the time of writing, was last updated three months ago. Both files will be joined via their "restaurant ID" field.

Also from Kaggle, the second dataset is "Indonesian Food Recipes" <https://www.kaggle.com/datasets/canggih/indonesian-food-recipes>. This data was scraped from <https://cookpad.com> and contains 14,000 Indonesian cuisine recipes, broken into eight CSV files based on food type (ex. chicken, beef, tofu, etc.). At the time of writing, the data was last updated three years ago.

## Methodology

To filter restaurants by those that serve Indonesian cuisine, all recipe files are merged into a master list of Indonesian recipes. This list will have to be further consolidated so variations of the same dish are merged into one. For example, "Ayam goreng pedas gila ala Kfc" (spicy fried chicken KFC style) and "Ayam goreng tulang lunak" (soft bone fried chicken) should be consolidated into "Ayam goreng" (fried chicken). These generalized Indonesian dishes are what is used to filter the Uber Eats food menu items and their respective restaurants.

A bar plot is procured showing the most common general dish types orderable to the least common. For each dish type, bar lengths represent the number of restaurants serving said dish type via Uber Eats. To emphasize the respective popularity and rarity of these dishes, bars are sorted in descending order.

For the most popular dish type, tempe (or "tempeh" in English), a list of available dishes and their restaurants are provided. Only restaurants with scores greater than or equal to 4.9 are shown.

As a bonus, an analysis is done on which cities have the most Uber Eats restaurants serving Indonesian food. An interactive map of one of the top cities, Seattle, is generated showing its restaurant locations. Although Portland has a higher restaurant count, Seattle was chosen due to personal preference.

## Running the Project

### Install Dependencies

```
conda env create -f environment.yml
```

### Downloading the Original Data

As can be seen in "code/data_collection_code/loader_utils.py", the original data is downloaded using the Kaggle API. Both a KAGGLE_USERNAME and KAGGLE_KEY are saved as environment variables for the API to authenticate.

- "restaurants.csv" contains entries of restaurants that have partnered with Uber eats across the nation. Its data is organized with the following columns: 'id', 'position', 'name', 'score', 'ratings', 'category', 'price_range', 'full_address', 'zip_code', 'lat', 'lng'.
- "restaurant-menus.csv" contains menu items orderable from the restaurants in "restaurants.csv". Its data is organized with the following columns: 'restaurant_id', 'category', 'name', 'description', 'price'.
- "Indonesian Food Recipes" contain Indonesian cuisine recipes, broken into eight CSV files based on food type (ex. chicken, beef, tofu, etc.). Each CSV file is organized with the following columns: 'Title', 'Ingredients', 'Steps', 'Loves', 'URL'.

### Data Preprocessing 

As can be seen in "code/data_etl_code/scrub_data.py", the Uber eats data files are first filtered by removing restaurants and menus without Indonesian cuisine. This is done purely to minimize memory bloat and does not alter the data format.

"code/data_etl_code/consolidate_data.py" does a couple of things. It first concatenates all eight CSVs from "Indonesian Food Recipes" into one CSV. A 'broadcategory' column is added to indicate which original CSV file (a.k.a. food type) each entry came from. Secondly, it also consolidates the filtered Uber eats data by joining both CSV files via their "restaurant ID" fields. Overlapping columns are given suffixes, "_menuitem" for restaurant menus and "_restaurant" for restaurants. 

## Analysis

In progress.

### Visualizations

The visualizations produced can be seen here:
https://egunadi.github.io/dsci510/

List of available visualizations:

- Bonus Assignment: Interactive Map of Uber Eats Restaurants Serving Indonesian Food in Seattle
