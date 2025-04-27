import os
import datetime

def main():
    os.chdir('extraction/extraction/')
    
    # Check if data.json exists
    data_path = os.path.abspath('../../data/data.json')
    if os.path.exists(data_path):
        # Create a timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"../../data/data_{timestamp}.json"
        os.rename(data_path, new_name)
        print(f"Renamed existing data.json to data_{timestamp}.json")
    
    os.system('scrapy crawl mercadolivre -o ../../data/data.json')
    os.chdir('../../transforms')
    os.system('python data_transformation.py')
    os.chdir('../dashboard')
    os.system('streamlit run dashboard.py')

if __name__ == "__main__":
    main()
