# COVID and Home Advantage in Football: An Analysis of Results and xG Data in European Leagues

## Introduction

This paper aims at reproducing and replicating the study "COVID and Home Advantage in Football: An Analysis of Results and xG Data in European Leagues" by Mathieu Acher. The original study investigates the impact of the COVID-19 pandemic on home advantage in football matches across European leagues. The authors analyze match results, expected goals (xG) and expected Points (xPts) data to assess changes in home advantage before and during the Covid-19 pandemic. 
Covid-19 has led to the suspension of football matches, the absence of fans in stadiums, and changes in match schedules. The study explores how these factors have influenced home advantage in football matches.

## Reproducibility

### How to Reproduce the Results
1. **Requirements**

In order to reproduce the results of the study, we used the following tools and libraries:
- Python 3.8
- Pandas, Numpy, Matplotlib
- Jupyter Notebook (Google Colab)
- Understat API 

2. **Reproducing the results**

All Python files needed to reproduce the plots and tables are available in the `python` directory. The Jupyter notebook `reproduce_results.ipynb` provides a step-by-step guide to reproduce the analysis.
    
- Instructions to use the Dockerfile to create a reproducible environment:
 run the following commands:

      docker build -t reproducible-project .
      docker run -p 8888:8888 reproducible-project

The Jupyter notebook will be available at the link printed in the terminal (e.g.,  http://127.0.0.1:8888/tree?token=17620a2e80167f90cc65bf6b9f898756c86446a103672451)

### Encountered Issues and Improvements


### Is the Original Study Reproducible?

