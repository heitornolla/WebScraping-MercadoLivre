import os
import datetime

def main():
  os.chdir('extraction/extraction/')
  os.system(f'scrapy crawl mercadolivre -o ../../data/data-{datetime.date.today()}.json')

if __name__ == "__main__":
  main()