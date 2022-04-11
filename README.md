![img](./images/kc_header.png)

(image courtesy of [beautifulwashington.com](https://beautifulwashington.com/))

# Analysis of King County Real Estate Data

**Authored by:**
- Luke Dowker [(Github)](https://github.com/toastdeini) | [(LinkedIn)](https://www.linkedin.com/in/luke-dowker/)
- Jawwad Siddiqui [(Github)](https://github.com/jsiddiqui85) | [(LinkedIn)](https://www.linkedin.com/in/jsiddiqui85/)
- Xiaohua Su [(Github)](https://github.com/xiaohua-su) | [(LinkedIn)](https://www.linkedin.com/in/xiaohua-su/)

## Overview

The COVID-19 pandemic has [thrust residential real estate markets across the United States](https://www.curbed.com/article/inside-the-covid-19-housing-market-of-upstate-new-york.html) into near-perpetual "seller's market" status, and Seattle's relatively newfound position as a "tech hub" has [driven up the city's population](https://www.seattletimes.com/seattle-news/data/covid-slowed-but-didnt-stop-population-growth-in-seattle-washington-hits-7-7m-residents/) (and cultural cache!) substantially in the last decade.

UNIQUE Home Construction, LLC seeks to understand what **features** or **attributes** of a home best predict **sale price**. We examine a dataset from King County, WA that contains records for single-family home sales between May 2014 and May 2015. Using tools like pandas and scikit-learn, we developed several models to determine which features are the best predictors of a property's sale price, then included those features - `sqft_living`, `grade`, and `view` - in our final recommendations.

## Business Problem

A boutique residential contractor - **"Unique Home Construction, LLC"** - has tasked us with assessing which **features** of a house best predict its final sale price. They are looking to minimize the **risk** involved in constructing new builds without compromising features that are important to customers.

In other words, what attributes or features of a property should UNIQUE Home Construction, as custom home builders, focus on when constructing new homes?

## Data

![img](./images/kc_map.png)

The data used in this project covers home sales in King County, WA for a period spanning from May 2014 to May 2015. In addition to providing basic information about the sale itself - each house has a unique `id` value, and each record contains a value for `date` and `price` - the dataset lists various attributes of each home: whether it's on a `waterfront`, the `grade` of its build and materials, the `condition` of the home, whether it has a scenic `view`, the year of its renovation (`yr_renovated`, where applicable), among others.

## Methods

Our **target variable** `y` - i.e. what we are **trying to predict** - is the sale price of a home, represented under the column `price` in the dataset. We start with a baseline model using scikit-learn's `DummyRegressor` feature, then create a *simple model* using the correlated feature `sqft_living`. We then tested several models with different combinations of features.

## Results

### `sqft_living`

We can readily observe a linear relationship between `sqft_living` and sale `price`. We dropped outliers (homes with `sqft_living` and `price` values above the 75th percentile in their respective categories) in order to refine our dataset. We recommend building homes with livable square footage ranging between roughly 1,500 and 3,000 square feet. 

![img](./images/sqftliving.png)


### `grade`

As the quality of `grade` increases - e.g. from `Low` to `Fair`, and in each step thereafter - we see corresponding increases in sale `price`. Statistical testing demonstrated significant differences in each `grade` level at an alpha value of 0.05, with the lone exception being the difference between `Very Good` and `Excellent` grades. In short: Building homes from higher quality materials drives up `price`!

![img](./images/grade.png)


### `view`

We found a significant difference between homes with an `EXCELLENT` view and homes with *no* view (`NONE`), but difference in `price` between each step (e.g. `NONE` to `AVERAGE`) varies. **Visually**, there are differences in sale price between `NONE` and `AVERAGE`, and between `GOOD` and `EXCELLENT` -- but the differences between `AVERAGE`, `FAIR`, and `GOOD` are more difficult to tease out.

![img](./images/view.png)


### Final model

- **Train score:** `0.396`
- **Test score:** `0.395`
    - These values describe the **percentage of variance** in `price` that is explained by our **final model**. Our model performs about equally on both the train and test data sets.
    
- **Train RMSE:** `138796.17` (US dollars)
- **Test RMSE:** `141271.64` (US dollars)
    - These values illustrate **how much we can expect our predictions to vary** from actual sale `price`.
    
## Conclusions: Where to Focus!

![img](./images/new_build.png)

(image courtesy of [Al Jazeera](https://www.aljazeera.com/))

1. `sqft_living` - There's no need to construct mansions in order to fetch a high sale price, as there *are* diminishing returns on price vs. livable square footage past a certain point - we recommend somewhere in the range of 1,500 to 3,000 square feet.
2. `grade` - Ensuring that a house is built from high-quality materials, and constructed by competent professionals, will yield a higher sale price than "cutting corners" in the construction.
3. `view` - Buyers love a scenic view, and while homes with "excellent" views yield the highest sale prices on average, even a "good" or "average" view tends to make the property more valuable than a home *without* a view.

## Next Steps

1. Exploratory data analysis & descriptive statistics reveal that the mean price for a `waterfront` property is much higher than one without `waterfront` view - examining possibilities for waterfront construction can lead to further increases in sale
2. While the data stored in `zipcode` was not useful for the purposes of our modeling workflow, visualizing sale price with mapping software can potentially identify
3. Conduct more refined analysis on how `bedroom` and `bathroom` count can be optimized without "overbuilding" or constructing unnecessarily large properties.

## Repository Structure
```
├── Workspace_Notebooks  
│       ├── Workspace_Luke
│       │   ├── Analysis_Notebook_Luke.ipynb
│       │   └── Initial_EDA_Luke.ipynb
│       ├── Workspace_Jawwad
│       │   ├── EDA of Real Estate.ipynb
│       │   ├── Train Test Split.ipynb
│       │   └── Workspace_Jawwad.ipynb
│       └── Workspace_Xiaohua
│           ├── scratchwork_etc.ipynb
│           ├── Tukey_test_draft.ipynb
│           └── Xiaohua_EDA.ipynb
│
├── data
├── images
├── README.md
├── king_county_real_estate_presentation.pdf
└── King_County_Real_Estate_Analysis.ipynb
```
### Additional information and citations

- Full analysis available in the project [Jupyter notebook](https://github.com/xiaohua-su/King_County_Real_Estate_Analysis/blob/main/King_County_Real_Estate_Analysis.ipynb)
- Stakeholder-facing [presentation](https://github.com/xiaohua-su/King_County_Real_Estate_Analysis/blob/main/king_county_real_estate_presentation.pdf)


["Inside the Freak-out Housing Market of Upstate New York"](https://www.curbed.com/article/inside-the-covid-19-housing-market-of-upstate-new-york.html)

["What exodus? Seattle and Washington kept growing during pandemic"](https://www.seattletimes.com/seattle-news/data/covid-slowed-but-didnt-stop-population-growth-in-seattle-washington-hits-7-7m-residents/)
