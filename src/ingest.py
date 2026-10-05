import pandas as pd
from sklearn.datasets import load_wine

from pathlib import Path

output_file = Path("data/raw/data.csv")

def ingest_data():
    wine = load_wine(as_frame=True)

    df = wine.frame

    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    
    print(f"Data ingested and saved to {output_file}")
    
if __name__ == "__main__":
    ingest_data()