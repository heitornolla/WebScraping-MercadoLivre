import os

def main():
  os.chdir('extraction/extraction/')
  os.system('scrapy crawl mercadolivre -o ../../data/data.json')
  os.chdir('../../transforms')
  os.system('python data_transformation.py')
  os.chdir('../dashboard')
  os.system('streamlit run dashboard.py')


if __name__ == "__main__":
  main()