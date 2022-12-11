def present_data():

    header = """# Most Common Indonesian Dishes Served in Uber Eats

<iframe src="result/dish-category-count.pdf" height="500" width="500"></iframe>

[Click here](result/dish-category-count.pdf) to explore this plot as its own web page.

Tempe (or "tempeh" in English) are fermented soybean blocks that have gone mainstream in the US as a meat substitute for protein. This is apparent in the bar plot above where, aside from rice dishes, there are at least double the number of restaurants serving tempe-based dishes compared to other Indonesian cuisines.

Here is a list of some tempe dishes available, along with their restaurants. Only restaurants rated greater than or equal to 4.9 are shown: 
      
"""
    
    with open('../result/tempe_dishes.html','r') as contents:
        tempe_table = contents.read()  

    observations = """Most items are Western dishes (ex. taco or burger) repurposed to use tempe as its protein. By excluding tempe we can see a more accurate list of authentic Indonesian dishes served by highly rated restaurants:

"""

    with open('../result/non_tempe_dishes.html','r') as contents:
        non_tempe_table = contents.read()

    footer = """# Bonus Assignment: Interactive Map of Uber Eats Restaurants Serving Indonesian Food in Seattle

<iframe src="result/seattle-indorestaurants-map.html" height="500" width="500"></iframe>
[Click here](result/seattle-indorestaurants-map.html) to explore this map as its own web page.
    
"""

    with open('../index.md','w') as contents:
        contents.write(header
                        + tempe_table
                        + '\n\n<br>\n\n'
                        + observations
                        + non_tempe_table
                        + '\n\n<br>\n\n'
                        + footer)

if __name__ == '__main__':
    present_data()
