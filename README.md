Shark Papers - Retrieval Augmented Generation
==============================

Question Answering on Shark publications in New Caledonia using LLMs.

Objectives
------------
Ask any question you have on sharks in New Caledonia.

The answers are based on scientific publications but also on other sources.

Steps
------------
- Turn documents into programmatic content
- Index the documents
- Find closest documents to the question
- Create a summarized answer

Technical stack
------------
- Nougat: https://facebookresearch.github.io/nougat/
- Data models: Pydantic for LLM output
- Data catalog: Kedro-dataset
- Will try without langchain
- LLM: OpenAI/Huggingface/Llama2
- Vectorstore: 

Inspirations
------------
- https://github.com/bp-high/research_buddy/tree/main
- https://github.com/vishwasg217/finsight/tree/main


Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   ├── data_manager.py
    │   │   └── clean_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

### Creating dedicated environment
    python3 -m venv .venv
    source .venv/bin/activate

### Installing development requirements
------------

    pip install -r requirements.txt
