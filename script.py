import os
import datetime

def main():
  os.chdir('extraction/extraction/')
  os.system(f'scrapy crawl mercadolivre -o ../../data/data.json')
  os.chdir('../../transforms')
  os.system('python data_transformation.py')


if __name__ == "__main__":
  main()