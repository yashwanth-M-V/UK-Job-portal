from datetime import datetime
import pandas as pd

def filter_active_jobs(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["deadline"] = pd.to_datetime(df["deadline"], errors="coerce")
    if df["deadline"].isna().any():
        raise ValueError("Invalid deadline date detected")

    today = pd.Timestamp(datetime.utcnow().date())

    active_df = df[df["deadline"] >= today]
    active_df = active_df.sort_values("deadline")

    return active_df
