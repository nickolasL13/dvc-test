import pandas as pd
from sklearn.model_selection import train_test_split
import yaml

from pathlib import Path

DATA_PATH = Path("data/raw/data.csv")
TRAIN_PATH = Path("data/train")
TEST_PATH = Path("data/test")

TRAIN_PATH.mkdir(exist_ok=True)
TEST_PATH.mkdir(exist_ok=True)

def load_params():
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)

    return params["prepare"]

def split_data():

    params = load_params()

    TEST_SIZE = params["test_size"]
    RANDOM = params["random"]

    df_raw = pd.read_csv(DATA_PATH)

    y = df_raw["alcohol"]
    X = df_raw.drop(columns="alcohol")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, random_state=RANDOM)

    df_y_train = pd.DataFrame(y_train)
    df_X_train = pd.DataFrame(X_train)

    df_y_test = pd.DataFrame(y_test)
    df_X_test = pd.DataFrame(X_test)

    df_y_train.to_csv(TRAIN_PATH / "df_y_train.csv")
    df_X_train.to_csv(TRAIN_PATH / "df_X_train.csv")

    df_y_test.to_csv(TEST_PATH / "df_y_test.csv")
    df_X_test.to_csv(TEST_PATH / "df_X_test.csv")

    print(f"Datasets saved! {TEST_SIZE}")

if __name__ == "__main__":
    split_data()