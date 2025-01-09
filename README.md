# COVID and Home Advantage in Football: An Analysis of Results and xG Data in European Leagues

## Introduction

This paper aims at reproducing and replicating the study "COVID and Home Advantage in Football: An Analysis of Results and xG Data in European Leagues" by Mathieu Acher. The original study investigates the impact of the COVID-19 pandemic on home advantage in football matches across European leagues. The author analyze match results, expected goals (xG) and expected Points (xPts) data to assess changes in home advantage before and during the Covid-19 pandemic.

Covid-19 has led to the suspension of football matches, the absence of fans in stadiums, and changes in match schedules. The study explores how these factors have influenced home advantage in football matches.

## Reproducibility

_Detailed analysis, chart by chart, is available in the notebook **reproduce_results.ipynb**._

### How to Reproduce the Results

1. **Requirements**

You need to install all the python libraries used in our project. To do this, run this command :

```
pip install -r requirements.txt
```

2. **Setting Up the Environment**

You can run the program using a docker environment by executing the following commands:

```
cd reproduction
docker build -t reproducible-project .
docker run -p 8888:8888 reproducible-project
```

Then simply click on the link in the terminal, which will open a web page with the Jupyter Notebook.

3. **Reproducing the results**

Now that the notebook is open, launch the cells one by one or launch them all at once.

### Encountered Issues and Improvements

During the process of reproducing the results, we encountered a couple of challenges that we addressed effectively, leading to improvements in our workflow.

- **Issue with Scipy Version and Wilcoxon Test Results:**
  we initially ran into a problem with the results from the Wilcoxon signed-rank test. The version of Scipy we were using produced different results than those found in the original study. This discrepancy was especially noticeable in the statistical tests comparing pre- and post-COVID home advantage. Once we identified the correct version and updated our setup, the results aligned with those reported in the study. However, this issue was not explicitly mentioned in the original paper, so it took us some time to figure out.

- **Simplified data retrieval**:
  one of the most significant improvements we made was in the process of retrieving the match data. The original study involved scraping data directly from the Understat website, which can be time-consuming and prone to errors. We were able to simplify this step by using the Python library Understat, which provides a cleaner and more efficient way to access the required data. This change saved us a considerable amount of time and allowed us to focus more on the analysis rather than dealing with data scraping issues.

### Is the Original Study Reproducible?

Our replication of the study gave very similar results to the original. We didn't encounter any particular difficulties in reproducing the study, as the entire methodology is detailed. Indeed, we knew that the data came from Understat and which libraries and statistical tools to use. However some values are different, in particular due to differences in versions. More details are available in the notebook comments.

## Replicability

Now that we've reproduced the experiment, we'll replicate it with a few modifications to the environment. Our aim is to see if the previous conclusions hold true on new data.

### Variability Factors

- **Data source** : before, our data source was Understat. However, there are other equivalent sites, each with different data. So if we want to be sure that Understat hasn't biased our analysis, we need a new data source: FBref.

- **More leagues** : we want to open up our analysis to other leagues, as COVID may only have had an impact on the major leagues. We've added the second divisions of England, Spain, Germany and France, as well as the first division of Portugal.

- **More seasons** : the analysis will be carried out from 2019 to 2024, so we'll have a new vision since we previously stopped at 2020.

These variability factors are intended to extend the scope of the analysis and make the conclusions more robust. By diversifying the sources of data, including other leagues, and extending the period studied, we can check if the original results remain valid in different contexts. This also helps reduce the risk of bias from using a single data source or a limited sample.

### Replication Execution

1. **Requirements**

As with reproduction, you need to install the python requirements :

```
pip install -r requirements.txt
```

2. **Setting Up the Environment**

Run the program using a docker environment by executing the following commands:

```
cd replication
docker build -t replicable-project .
docker run -p 8888:8888 replicable-project
```

### Does It Confirm the Original Study?

_Detailed analysis, chart by chart, is available in the notebook **replicate_results.ipynb**._

Our replication of the study with new data supports the conclusions drawn in the baseline study. By visualizing the difference between home and away points, we can see that playing at home is a clear advantage. With regard to the impact of COVID on this advantage, the conclusions of our replication are more moderate. In fact, not all leagues are affected, and some only in terms of expected goals.

**/!\TODO : analyse deux derniers charts**

## Conclusion

**/!\TODO**
