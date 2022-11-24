# DSCI510 Final Project: Most and Least Common Indonesian Dishes Orderable via Uber Eats USA

My main goal is to determine which dishes are most and least common in these restaurants. For both categories, a listing of their associated restaurants will also be provided. At least two datasets will be used, one containing Uber Eats restaurant menu items and another a comprehensive list of Indonesian dishes. By joining the two sets, we can procure a list of Indonesian dishes orderable via Uber Eats, along with their associated restaurants. 

The first dataset of interest is "Uber Eats USA Restaurants and Menus" from Kaggle <https://www.kaggle.com/datasets/ahmedshahriarsakib/uber-eats-usa-restaurants-menus>. This data was scraped from <https://www.ubereats.com> and comprises of two CSV files:

- "restaurants.csv" contains 40k+ entries of restaurants that have partnered with Uber eats accross the nation
- "restaurant-menus.csv" contains 3.71M menu items orderable from the restaurants in restaurants.csv

The dataset is updated frequently and, at the time of writing, was last updated three months ago. I plan on joining both files via their "restaurant ID" field.

Also from Kaggle, the second dataset is "Indonesian Food Recipes" <https://www.kaggle.com/datasets/canggih/indonesian-food-recipes>. This data was scraped from <https://cookpad.com> and contains 14,000 Indonesian cuisine recipes, broken into seven CSV files based on food type (ex. chicken, beef, tofu, etc.). At the time of writing, the data was last updated three years ago.

For the purposes of this project, I plan on merging all recipe files into a master list of Indonesian recipes. This list will probably have to be further consolidated so variations of the same dish are merged into one. For example, "Ayam goreng pedas gila ala Kfc" (spicy fried chicken KFC style) and "Ayam goreng tulang lunak" (soft bone fried chicken) should be consolidated into "Ayam goreng" (fried chicken).

At least two bar plots will be procured, one for the most common dishes orderable and another for the least common. To minimize clutter, only five dishes will be shown for each plot. For each dish, bar lengths will represent the number of restaurants serving said dish via Uber Eats. To emphasize the respective popularity and rarity of these dishes, bars for most common dishes will be sorted in descending order, while those for least common dishes will be sorted in ascending order.

To engage the audience, restaurants associated with both visualizations will also be listed. Both the restaurant name and address will be included so audiences can go and try these dishes if they wish. For brevity, each list will be limited to ten items and sorted in descending order based on popularity. I also aim to plot their locations on a map, so audiences can easily identify those closest to areas they may be familiar with.
