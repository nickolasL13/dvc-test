# dvc-test
Repository for learning how to use DVC (Data Version Control). 

## Setup
~ todo

## Stages
### Stage 1 - Ingestion

In here we get the raw data that is going to be used throughout the whole process, we generate it using the code in ```src/ingest.py``` and save it in ```data/raw/data.csv```.

The process is then saved on ```dvc.yaml``` using the following command:

    dvc stage add \
    -n ingest \
    -d src/ingest.py \
    -o data/raw/data.csv \
    python3 src/ingest.py

This creates the first step of the pipeline, and then we can reproduce the experiment using dvc.

To reproduce the pipeline we use the command ```dvc repro```.

### Stage 2 - Prepare

On this stage, the data is split in train and test datasets for future use in training and validation step. Four files are created, the X and Y datasets for training and testing, which are saved at ```data/train``` and ```data/test```. 

At this stage, we also introduce the use of parameters, which are saved in ```params.yaml``` and are a requirement to be able to run the pipeline (as they are required for the spliting step). 

This stage is added to dvc pipeline using the following command:

    dvc stage add \
    -n prepare \
    -p prepare.test_size -p prepare.random \
    -d data/raw/data.csv \
    -o data/test/df_X_test.csv -o data/test/df_y_test.csv -o data/train/df_X_train.csv -o data/train/df_y_train.csv \
    python3 src/prepare.py

The pipeline now runs the "prepare" stage everytime we run the command ```dvc repro```