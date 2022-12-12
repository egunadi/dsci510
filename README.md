# DSCI510 Final Project: Most Common Indonesian Dishes Orderable via Uber Eats USA

My main goal is to determine which dishes are most common in these restaurants and provide a listing of restaurants serving them. At least two datasets will be used, one containing Uber Eats restaurant menu items and another a comprehensive list of Indonesian dishes. By joining the two sets, we can procure a list of Indonesian dishes orderable via Uber Eats, along with their associated restaurants. 

The first dataset of interest is "Uber Eats USA Restaurants and Menus" from Kaggle <https://www.kaggle.com/datasets/ahmedshahriarsakib/uber-eats-usa-restaurants-menus>. This data was scraped from <https://www.ubereats.com> and comprises of two CSV files:

- "restaurants.csv" contains 40k+ entries of restaurants that have partnered with Uber eats accross the nation
- "restaurant-menus.csv" contains 3.71M menu items orderable from the restaurants in "restaurants.csv"

The dataset is updated frequently and, at the time of writing, was last updated three months ago. Both files will be joined via their "restaurant ID" field.

Also from Kaggle, the second dataset is "Indonesian Food Recipes" <https://www.kaggle.com/datasets/canggih/indonesian-food-recipes>. This data was scraped from <https://cookpad.com> and contains 14,000 Indonesian cuisine recipes, broken into eight CSV files based on food type (ex. chicken, beef, tofu, etc.). At the time of writing, the data was last updated three years ago.

## Dependencies

```
name: dsci510
channels:
  - conda-forge
  - defaults
dependencies:
  - backcall=0.2.0=pyhd3eb1b0_0
  - beautifulsoup4=4.11.1=py39hecd8cb5_0
  - blas=1.0=mkl
  - bottleneck=1.3.5=py39h67323c0_0
  - branca=0.6.0=pyhd8ed1ab_0
  - brotli=1.0.9=hca72f7f_7
  - brotli-bin=1.0.9=hca72f7f_7
  - brotlipy=0.7.0=py39h9ed2024_1003
  - bs4=4.11.1=hd3eb1b0_0
  - ca-certificates=2022.10.11=hecd8cb5_0
  - certifi=2022.9.24=py39hecd8cb5_0
  - cffi=1.15.1=py39hc55c11b_0
  - charset-normalizer=2.0.4=pyhd3eb1b0_0
  - cryptography=37.0.1=py39hf6deb26_0
  - cycler=0.11.0=pyhd3eb1b0_0
  - debugpy=1.5.1=py39he9d5cce_0
  - decorator=5.1.1=pyhd3eb1b0_0
  - entrypoints=0.4=py39hecd8cb5_0
  - fftw=3.3.9=h9ed2024_1
  - folium=0.13.0=pyhd8ed1ab_0
  - fonttools=4.25.0=pyhd3eb1b0_0
  - freetype=2.11.0=hd8bbffd_0
  - giflib=5.2.1=haf1e3a3_0
  - gmp=6.2.1=he9d5cce_3
  - gmpy2=2.1.2=py39hd5de756_0
  - idna=3.4=py39hecd8cb5_0
  - intel-openmp=2021.4.0=hecd8cb5_3538
  - ipykernel=6.9.1=py39hecd8cb5_0
  - ipython=8.4.0=py39hecd8cb5_0
  - jedi=0.18.1=py39hecd8cb5_1
  - jinja2=3.1.2=pyhd8ed1ab_1
  - jpeg=9e=hca72f7f_0
  - jupyter_client=7.3.4=py39hecd8cb5_0
  - jupyter_core=4.10.0=py39hecd8cb5_0
  - kiwisolver=1.4.2=py39he9d5cce_0
  - lcms2=2.12=hf1fd2bf_0
  - lerc=3.0=he9d5cce_0
  - libbrotlicommon=1.0.9=hca72f7f_7
  - libbrotlidec=1.0.9=hca72f7f_7
  - libbrotlienc=1.0.9=hca72f7f_7
  - libcxx=12.0.0=h2f01273_0
  - libdeflate=1.8=h9ed2024_5
  - libffi=3.3=hb1e8313_2
  - libgfortran=5.0.0=11_3_0_hecd8cb5_28
  - libgfortran5=11.3.0=h9dfd629_28
  - libpng=1.6.37=ha441bb4_0
  - libsodium=1.0.18=h1de35cc_0
  - libtiff=4.4.0=h2ef1027_0
  - libwebp=1.2.4=h56c3ce4_0
  - libwebp-base=1.2.4=hca72f7f_0
  - llvm-openmp=14.0.6=h0dcd299_0
  - lz4-c=1.9.3=h23ab428_1
  - markupsafe=2.1.1=py39ha30fb19_2
  - matplotlib=3.5.2=py39hecd8cb5_0
  - matplotlib-base=3.5.2=py39hfb0c5b7_0
  - matplotlib-inline=0.1.6=py39hecd8cb5_0
  - mkl=2021.4.0=hecd8cb5_637
  - mkl-service=2.4.0=py39h9ed2024_0
  - mkl_fft=1.3.1=py39h4ab4a9b_0
  - mkl_random=1.2.2=py39hb2f4e1b_0
  - mpc=1.1.0=h6ef4df4_1
  - mpfr=4.0.2=h9066e36_1
  - mpmath=1.2.1=py39hecd8cb5_0
  - munkres=1.1.4=py_0
  - ncurses=6.3=hca72f7f_3
  - nest-asyncio=1.5.5=py39hecd8cb5_0
  - numexpr=2.8.3=py39h2e5f0a9_0
  - numpy=1.23.1=py39h2e5f0a9_0
  - numpy-base=1.23.1=py39h3b1a694_0
  - openssl=1.1.1s=hca72f7f_0
  - packaging=21.3=pyhd3eb1b0_0
  - pandas=1.4.4=py39he9d5cce_0
  - parso=0.8.3=pyhd3eb1b0_0
  - pexpect=4.8.0=pyhd3eb1b0_3
  - pickleshare=0.7.5=pyhd3eb1b0_1003
  - pillow=9.2.0=py39hde71d04_1
  - pip=22.1.2=py39hecd8cb5_0
  - ptyprocess=0.7.0=pyhd3eb1b0_2
  - pure_eval=0.2.2=pyhd3eb1b0_0
  - pycparser=2.21=pyhd3eb1b0_0
  - pyopenssl=22.0.0=pyhd3eb1b0_0
  - pyparsing=3.0.9=py39hecd8cb5_0
  - pysocks=1.7.1=py39hecd8cb5_0
  - python=3.9.13=hdfd78df_1
  - python-dateutil=2.8.2=pyhd3eb1b0_0
  - python_abi=3.9=2_cp39
  - pytz=2022.1=py39hecd8cb5_0
  - pyzmq=23.2.0=py39he9d5cce_0
  - readline=8.1.2=hca72f7f_1
  - requests=2.28.1=py39hecd8cb5_0
  - scipy=1.9.3=py39h3d31255_0
  - seaborn=0.12.0=py39hecd8cb5_0
  - setuptools=63.4.1=py39hecd8cb5_0
  - six=1.16.0=pyhd3eb1b0_1
  - soupsieve=2.3.2.post1=py39hecd8cb5_0
  - sqlite=3.39.2=h707629a_0
  - stack_data=0.2.0=pyhd3eb1b0_0
  - sympy=1.10.1=py39hecd8cb5_0
  - tabulate=0.8.10=py39hecd8cb5_0
  - tk=8.6.12=h5d9f67b_0
  - tornado=6.1=py39h9ed2024_0
  - tzdata=2022a=hda174b7_0
  - urllib3=1.26.12=py39hecd8cb5_0
  - wcwidth=0.2.5=pyhd3eb1b0_0
  - wheel=0.37.1=pyhd3eb1b0_0
  - xz=5.2.5=hca72f7f_1
  - zeromq=4.3.4=h23ab428_0
  - zlib=1.2.12=h4dc903c_2
  - zstd=1.5.2=hcb37349_0
  - pip:
    - appdirs==1.4.4
    - appnope==0.1.3
    - asttokens==2.0.8
    - executing==0.10.0
    - kaggle==1.5.12
    - little-mallet-wrapper==0.5.0
    - lxml==4.9.1
    - multitasking==0.0.11
    - prompt-toolkit==3.0.30
    - pygments==2.13.0
    - python-slugify==6.1.2
    - stack-data==0.4.0
    - text-unidecode==1.3
    - tqdm==4.64.1
    - traitlets==5.3.0
    - yfinance==0.1.85
prefix: /Users/egunadi/anaconda3/envs/dsci510
```

## Installation

The environment.yml file in GitHub can be used to recreate my environment. For topic modeling analysis, a tool called MALLET (MAchine Learning for LanguagE Toolkit) is used. It's written in Java, which means the Java Development Kit also has to be installed. Here is an article that provides guidance on how to set everything up:
<https://melaniewalsh.github.io/Intro-Cultural-Analytics/05-Text-Analysis/07-Topic-Modeling-Set-Up.html>

Note that my "mallet-2.0.8" directory resides in the git repository.

## Running the project

Results can be reproduced via "code/main.py", which runs the following functions in order:

- get_data.get_data()
  - This call is commented out since it can take several minutes to run. It's recommended to run this call on its own.
- consolidate_data.consolidate_indorecipes_data()
  - Consolidates all Cookpad recipes into one master file, "data/indofoods.csv" (included in the repo).
- topic_modeling.generate_topics()
  - Topic modeling, specifically latent Dirichlet allocation or "LDA", is used to generate a Indonesian dish key terms that can be grouped in categories ("results/indofoods_topics.txt").
- scrub_data.scrub_ubereats_data()
  - Uses the topics from "results/indofoods_topics.txt", along with my domain knowledge of Indonesian cuisine, to filter out non-Indonesian restaurants and menus from the Uber Eats data. This on its own may take a minute to complete.
- consolidate_data.consolidate_ubereats_data()
  - Merges the filtered restaurant and menu data files into one master file, "data/indorestaurants.csv" (included in the repo).
- analyze_data.analyze_data()
  - Uses the topics and groups from "results/indofoods_topics.txt", along with my domain knowledge of Indonesian cuisine, to sort menu items into general categories. The number of restaurants serving each category is counted and saved in "data/dishcount.csv". 
  - For tempe, the most popular category, menu items served by restaurants scored >= 4.9 are exported as an html table ("result/tempe_dishes.html"). The same is done for all non-tempe dishes ("result/non_tempe_dishes.html").
  - As a bonus, a quick analysis was done on the top three cities with the most Indonesian restaurants. For one of them, Seattle, a list of restaurants in that city is exported, both as "data/seattlerestaurants.csv" and as an HTML table ("result/seattlerestaurants.html").
- visualize_data.visualize_data()
  - "data/dishcount.csv" is used to generate a bar plot showing the most common general dish types orderable to the least common ("result/dish-category-count.pdf").
  - "data/seattlerestaurants.csv" is used to create a map of Seattle with markers of its Indonesian restaurants ("result/seattle-restaurants-map.html").
- present_data.present_data()
  - Used to put together "index.md", which when pushed to GitHub presents my findings at <https://egunadi.github.io/dsci510>.

## Methodology

Before producing visualizations, the data first had to be processed to exclude non-Indonesian dishes. This filter was procured by first generating LDA topics, then cherry picking and adding to the list using my domain knowledge of Indonesian dishes. Each keyword in the filter was then manually labelled with a general category. For instance, "bubur" (poridge) and "soto" (rice wih broth) belong to the "rice" category. This keyword-category dictionary was used to extract and categorize the Indonesian dishes of interest. On top of this, I should mention the Uber Eats menu did come with its own category column. I preserved all menu items containing "Indonesia" in its prepackaged category column.

## Visualization

After processing, a bar plot was procured showing the most common general dish types orderable to the least common. For each dish type, bar lengths represent the number of restaurants serving said dish type via Uber Eats. To emphasize the respective popularity and rarity of these dishes, bars are sorted in descending order.

For the most popular dish type, tempe (or "tempeh" in English), a list of available dishes and their restaurants are provided. Only restaurants with scores greater than or equal to 4.9 are shown. For comparison, the same is done for all non-tempe dishes.

As a bonus, an analysis has been done on which cities have the most Uber Eats restaurants serving Indonesian food. An interactive map of one of the top cities, Seattle, has been generated showing its restaurant locations. Although Portland has a higher restaurant count, Seattle was chosen due to personal preference. For those curious, a table is also outputted showing the complete list of mapped restaurants and their Indonesian dishes. For fun, I used Yelp to validate my map and was delighted to find a couple of crossovers.

## Future Work

My initial goal was to analyze Indonesian restaurants around the LA area. Living in LA, not only would that have been more relatable to me and my audience, but we would also be able to better validate the result. Given more time, I'd do a more targeted data search for Indonesian restaurants in LA, perhaps even scraping data off individual websites. While scraping websites can be time consuming, this could save time in determining which dishes are Indonesian or not, especially in the case where generic dish names like "stars special noodle" are used.

Seeing that the LDA topics generated from Cookpad were also missing common dishes, I'd spend more time searching for a more comprehensive list of Indonesian dishes. Perhaps there's a catalog or wiki out there that would be better served for this purpose. Additionally, I'd look at examples of how LDA has been used for food-related topics. Perhaps there are certain "gotchas" in this domain that I simply overlooked due to inexperience, or perhaps the LDA model is not suitable for such data in the first place.

I tackled the question of which Indonesian dishes are most common my counting the number of restaurants serving them. Even if there were a hundred variations of "nasi goreng" (fried rice), they would all only count as one if only one restaurant served them all. Another methodology worth exploring would be to also count at the number of distinct dishes regardless of restaurant. That way, variations of the same dish type within a restaurant contribute to the dish's popularity or availability. 

As for the map of Indonesian restaurants in Seattle, an interesting next step would be to color code the markers according to what food type (rice, noodle, tempe, etc.) they are known for or serve the most of. As the map expands to include more states, we could then see if certain regions are more prone to specialize in certain types of Indonesian foods.

Last but not least, improvements could be made with documentation in general. Instead of just verbally describing how to reproduce my results, it would also be nice to have a data flow diagram showing exactly how the raw data got transformed into the final visualizations. If more data sources get added down the line, that diagram would be invaluable for others to quickly see and understand the approach used.
