import pandas as pd
import sqlite3

from datetime import datetime
import os


def read_data(path_to_data: str = ''):
  if path_to_data == '':
    path_to_data = os.listdir('data')
    path_to_data = os.path.join('data', path_to_data.pop())

  try:
    df = pd.read_json(f'{path_to_data}')

  except:
    print("Error while loading data")

  return df


def add_columns(df: pd.DataFrame) -> pd.DataFrame: 
  df['_source'] = "https://lista.mercadolivre.com.br/baixo-5-cordas"
  df['scrap_date'] = datetime.now()

  return df


def fill_nulls(df: pd.DataFrame) -> pd.DataFrame:
  df['price'] = df['price'].fillna('0')
  df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
  df['reviews_amount'] = df['reviews_amount'].fillna('(0)')

  return df

def standardize_strings(df: pd.DataFrame) -> pd.DataFrame:
  df['price'] = df['price'].astype(str).str.replace('.', '', regex=False)
  df['reviews_amount'] = df['reviews_amount'].astype(str).str.strip('()')

  return df


def price_to_float(df: pd.DataFrame) -> pd.DataFrame:
  df['price'] = df['price'].astype(float)

  return df


def save_to_sqlite3(df: pd.DataFrame) -> pd.DataFrame:
  try:
    conn = sqlite3.connect('data/database.db')
    df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

  except:
    print("Error saving to SQLite")

  finally:
    conn.close()


def transform_data(path_to_data: str = ''):
  if path_to_data == '':
    path_to_data = ('../data/data.json')

  df = read_data(path_to_data)
  df = add_columns(df)
  df = fill_nulls(df)
  df = standardize_strings(df)
  df = price_to_float(df)
  save_to_sqlite3(df)


if __name__ == "__main__":
  transform_data('../data/data.json')
