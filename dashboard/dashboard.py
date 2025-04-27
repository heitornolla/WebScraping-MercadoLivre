import pandas as pd
import sqlite3
import streamlit as st


def get_df_from_db(db_path: str) -> pd.DataFrame:
  try:
    conn = sqlite3.connect(db_path)

    df = pd.read_sql_query("SELECT * FROM mercadolivre_items", conn)

  except:
    print("Error loading data")

  finally:
    conn.close()

  return df


def get_dashboard(df: pd.DataFrame):
  st.title("Scraping Results from Mercado Livre")
  st.subheader("By Heitor Nolla")

  col1, col2 = st.columns(2)

  total_itens = df.shape[0]

  col1.metric(label="Total Items Found", value=total_itens)

  avg_price = df['price'].mean()
  col2.metric(label="Average BRL Price", value=f"{avg_price:.2f}")


if __name__ == "__main__":
  df = get_df_from_db('../data/database.db')
  get_dashboard(df)
