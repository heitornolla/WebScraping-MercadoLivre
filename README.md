# Web Scraping Mercado Livre

**Disclaimer:**
_This is a personal project intended for educational purposes only_

## Overview

This project leverages Python's **Scrapy** library to perform web scraping on Mercado Livre, specifically collecting information about **5-string bass guitars**

## Adapting for other items

If you'd like to scrape data for a different item, it is totally possible!

### 1. Go to the file located in

```bash
extraction/spiders/mercadolivre.py
```

### 2. Update the start url

Set it to the item you wish to scrape
If you wish to scrape prices for Acer notebooks, the url would be

```bash
https://lista.mercadolivre.com.br/notebook-acer
```

### 3. Update the parse function

Click the "Next Page" button and observe the new URL. It should look like

```bash
https://lista.mercadolivre.com.br/informatica/portateis-acessorios/notebooks/acer/notebook-acer_Desde_49_NoIndex_True
```

Set this url as the _next page_ attribute in the MercadoLivreSpider class, but change _49_ to {offset}

This will ensure that the crawler moves through to the next pages

In the end, the code for the _next page_ attribute should look like

```bash
next_page = f"https://lista.mercadolivre.com.br/instrumentos-musicais/instrumentos-corda/baixos/baixo-5-cordas_Desde_{offset}_NoIndex_True_STRINGS*NUMBER_5-5"
```

### Dashboard

The dashboard currently looks like this:

!['Screenshot of the dashboard'](assets/screenshot.png)

You may search through all items and apply filters

## How to Install and Run the project

### With Docker

I have refactored the project to offer Docker support

You may install it with the following commands:

```bash
docker build -t mlscrape .
```

```bash
docker run -p 8501:8501 mlscrape
```

This will map your 8501 port to the one exposed on the Dockerfile

You will be able to access the dashboard by navigating to localhost:8501

### With a local Python installation

It is my personal recommendation that you make a new virtual Python environment for every project you run. To do so, open your preferred terminal and run the commands:

#### 1. Clone the repository

```bash
git clone https://github.com/heitornolla/mercadolivre-scraping.git
```

#### 2. Move to the project folder

```bash
cd mercadolivre-scraping
```

#### 3. Define the local Python version

```bash
pyenv local 3.12.1
```

#### 4. Create a new Python environment

You can do this with Venv with the command

```bash
python -m venv .venv
```

or use other environment managers, such as Conda

If you opted for Venv, activate the environment with

```bash
source .venv/Scripts/activate
```

#### 5. Install the Requirements

```bash
pip install -r requirements.txt
```

#### 6. Run the Project!

Run the crawl.py file to crawl Mercado Livre

To generate the dashboard based on your data, run

```bash
streamlit run dashboard/dashboard.py
```

## Technologies Used

Python, Scrapy, Pandas, Streamlit and Docker
