import os
import psycopg
import pandas as pd
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    with psycopg.connect(
    host=os.getenv("DB_HOST"),
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD")
    ) as conn:

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM applications;")

            results = cur.fetchall()

            df = pd.DataFrame(
                results,
                columns=[
                   "application_id",
                    "application_date",
                    "identity_risk_score"
                ]
            )

            review_threshold = 700

            flagged_applications = df[
                    df["identity_risk_score"] >= review_threshold]

            review_rate = len(flagged_applications) / len(df) * 100

            print(f"Applications flagged: {len(flagged_applications):,}")
            print(f"Manual review rate: {review_rate:.2f}%")
