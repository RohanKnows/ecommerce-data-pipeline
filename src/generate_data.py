import os, random, uuid
from datetime import datetime, timedelta
import pandas as pd

os.makedirs("data/raw", exist_ok=True)

N_USERS, N_ITEMS, N_EVENTS = 200, 300, 5000

# users
users = pd.DataFrame({
    "user_id": [f"u_{i}" for i in range(1, N_USERS+1)],
    "signup_dt": pd.date_range("2024-01-01", periods=N_USERS, freq="D").astype(str),
    "region": [random.choice(["IN","US","EU"]) for _ in range(N_USERS)]
})
users.to_csv("data/raw/users.csv", index=False)

# items
items = pd.DataFrame({
    "item_id": [f"i_{i}" for i in range(1, N_ITEMS+1)],
    "category": [random.choice(["apparel","electronics","home","beauty"]) for _ in range(N_ITEMS)],
    "price": [round(random.uniform(5, 200), 2) for _ in range(N_ITEMS)]
})
items.to_csv("data/raw/items.csv", index=False)

# events
start = datetime(2024, 5, 1)
rows = []
for _ in range(N_EVENTS):
    t = start + timedelta(minutes=random.randint(0, 60*24*120))
    rows.append({
        "event_id": str(uuid.uuid4()),
        "ts": t.isoformat(),
        "user_id": f"u_{random.randint(1, N_USERS)}",
        "item_id": f"i_{random.randint(1, N_ITEMS)}",
        "event_type": random.choices(
            ["view","add_to_cart","purchase"], weights=[0.75,0.18,0.07], k=1
        )[0],
    })
events = pd.DataFrame(rows)
events.to_csv("data/raw/events.csv", index=False)

print("✅ generated: data/raw/{users.csv, items.csv, events.csv}")
