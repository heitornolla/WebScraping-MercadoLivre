import os
import datetime

from extraction.spiders.mercadolivre import MercadoLivreSpider
from transforms.data_transformation import transform_data

def main():   
    # Check if data.json exists
    data_path = os.path.abspath('data/data.json')

    if os.path.exists(data_path):      
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        new_name = f"data/data_{timestamp}.json"
        os.rename(data_path, new_name)
        print(f"Renamed existing data.json to data_{timestamp}.json")
    
    MercadoLivreSpider.run_spider()
    transform_data('data/data.json')

    # Streamlit apps must be run by calling streamlit run
    # I havent yet found an elegant solution for this
    os.system('streamlit run dashboard/dashboard.py')

if __name__ == "__main__":
    main()
