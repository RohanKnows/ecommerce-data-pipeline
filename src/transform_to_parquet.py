import os
import pandas as pd

os.makedirs("data/processed", exist_ok=True)

for name in ["users","items","events"]:
    df = pd.read_csv(f"data/raw/{name}.csv")
    if name == "events":
        df["ts"] = pd.to_datetime(df["ts"])
    out = f"data/processed/{name}.parquet"
    df.to_parquet(out, index=False)
    print(f"wrote {out}")

print("✅ transform complete")
