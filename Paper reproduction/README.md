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

2. **Setting Up the Environment**

All Python files needed to reproduce the plots and tables are available in the `python` directory. The Jupyter notebook `notebooks/reproduce_results.ipynb` provides a step-by-step guide to reproduce the analysis.
    
- Provide instructions for using the Dockerfile to create a reproducible environment:
      ```bash
      docker build -t reproducible-project .
      docker run -it reproducible-project
      ```

3. **Reproducing Results**
    - Describe how to run the automated scripts or notebooks to reproduce data and analyze results:
      ```bash
      bash scripts/run_analysis.sh
      ```
    - Mention Jupyter notebooks (if applicable):  
      Open `notebooks/reproduce_results.ipynb` to execute the analysis step-by-step.

### Encountered Issues and Improvements
- Report any challenges, errors, or deviations from the original study.
- Describe how these issues were resolved or improved, if applicable.

### Is the Original Study Reproducible?
- Summarize the success or failure of reproducing the study.
- Include supporting evidence, such as comparison tables, plots, or metrics.

## Replicability

### Variability Factors
- **List of Factors**: Identify all potential sources of variability (e.g., dataset splits, random seeds, hardware).  
  Example table:
  | Variability Factor | Possible Values     | Relevance                                   |
  |--------------------|---------------------|--------------------------------------------|
  | Random Seed        | [0, 42, 123]       | Impacts consistency of random processes    |
  | Hardware           | CPU, GPU (NVIDIA)  | May affect computation time and results    |
  | Dataset Version    | v1.0, v1.1         | Ensures comparability across experiments   |

- **Constraints Across Factors**:
    - Document any constraints or interdependencies among variability factors.  
      For example:
        - Random Seed must align with dataset splits for consistent results.
        - Hardware constraints may limit the choice of GPU-based factors.

- **Exploring Variability Factors via CLI (Bonus)**
    - Provide instructions to use the command-line interface (CLI) to explore variability factors and their combinations:
      ```bash
      python explore_variability.py --random-seed 42 --hardware GPU --dataset-version v1.1
      ```
    - Describe the functionality and parameters of the CLI:
        - `--random-seed`: Specify the random seed to use.
        - `--hardware`: Choose between CPU or GPU.
        - `--dataset-version`: Select the dataset version.


### Replication Execution
1. **Instructions**
    - Provide detailed steps or commands for running the replication(s):
      ```bash
      bash scripts/replicate_experiment.sh
      ```

2. **Presentation and Analysis of Results**
    - Include results in text, tables, or figures.
    - Analyze and compare with the original study's findings.

### Does It Confirm the Original Study?
- Summarize the extent to which the replication supports the original study’s conclusions.
- Highlight similarities and differences, if any.

## Conclusion
- Recap findings from the reproducibility and replicability sections.
- Discuss limitations of your
