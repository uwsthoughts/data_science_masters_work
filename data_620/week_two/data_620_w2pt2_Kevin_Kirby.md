# DATA 620 Week Two, Part 2
## Network Analysis, Centrality Measures

Author: Kevin Kirby

## Dataset Overview

The dataset I chose is the [EU Air Transportation Multiplex Network](https://manliodedomenico.com/data.php), which represents airlines operating at airports as a series of networks:

* Nodes equal airports
* Edges equal flights between airports
* Layers equal different airlines, with each layer representing separate networks
* Categorical variable is the layer ID, representing the airline

## Loading and preparing the data

The following are steps I would take to load and prepare the data for analysis:

1. Ingest data files
   * Load the list of nodes with geographic metadata
   * Load the multiplex edge list, which includes layer ID and connections between nodes
   * Load the list of airline layers for reference

2. Construct graphs
   * Build one ggregate graph that comnbines all layers so I can understand overall connectivity
   * Potentially construct layer-specific subgraphs to compare airlines against each other

3. Add node attributes
   * Map geographic locations to each node
   * Assign  geographic categorical labels like region or country of origin or arrival

4. Calculate centrality
   * Degree centrality to know how many direct connections there are
        * Calculate both globally and locally 

5. Group and compare
   * Compare centrality metrics across airline layers and categorical groups
   * Group nodes by geographic region and/or airport size to allow for another categorical grouping


## Hypothetical Predictive Outcome

**Prediction Task**:
Predict whether an airport belongs to a budget or legacy carrier based on its centrality metrics

**Hypothesis**:
* Airports with concentrations of budget carriers will have higher average degree centrality and more connections to smaller airports
* Legacy carriers will have fewer but denser connections centered around major hubs

By comparing degree centrality distributions across airlines, I can predict the type of airline operating any given layer based on on the structure of its network.
