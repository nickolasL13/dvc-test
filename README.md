# dvc-test
Repository for learning how to use DVC (Data Version Control). 

## Stages
### Stage 1 - Ingestion

In here we get the raw data that is going to be used throughout the whole process, we generate it using the code in src/ingest.py and save it in data/raw/data.csv.

The process is then saved on dvc.yaml using the following command:

    dvc stage add \
    -n ingest \
    -d src/ingest.py
    -o data/raw/data.csv
    python3 src/ingest.py

This creates the first step of the pipeline, and then we can reproduce the experiment using dvc. 

To reproduce the pipeline we use the command ```dvc repro```.

