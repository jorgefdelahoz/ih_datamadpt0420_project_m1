# IRONHACK DATA ANALYTICS - MODULE 1: DATA PIPELINE

*THIS API GOES WITH STABILISERS*

![Image](https://66.media.tumblr.com/f12be6275f5fb05d9d3cff544a53077e/tumblr_mhjvnpzadC1ruw1vso2_400.gifv)

---

### :raising_hand: **Name** 
Country-Gender-Jobs Pipeline

### :baby: **Status**
Alpha or... Beta, 2.1?
Ironhack Data Analytics Module 1 Project. 

### :running: **One-liner**
Retrieve Jobs Title with DDBB, API & Web Scraping.

### :computer: **Technology stack**
Libraries necesaries: Python, Pandas, Numpy, Argparse, SqlAlchemy, Jsonschema, BeautifulSoup4, lxml, Requests. 

Pycharm v2020.1.2

Jupyter Notebook

### :boom: **Core technical concepts and inspiration**
Report generator at date execution.

### :wrench: **Configuration**
[Database](http://www.potacho.com/files/ironhack/raw_data_project_m1.db)

[API Swagger](http://api.dataatwork.org/v1/spec/) (Work Data Initiative)

[Web Eurostat](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes) 

### :see_no_evil: **Usage**
Arguments HELP:
`  -h, --help            show this help message and exit
   -p PATH, --path PATH  Specify .db database path. Example: -p
                        /home/user/Documents/pollas.db
   -c COUNTRY, --country COUNTRY
                        Select country ***Default defined by ALL countries***`
                        

### :file_folder: **Folder structure**
```
└── ih_datamadpt0420_project_m1
    ├── __trash__
    ├── data
    |   ├── processed
    |   |   └── data_merged_info.csv
    |   ├── raw
    |   |   ├── raw_data_project_m1.db
    |   |   ├── raw_df_database_merge.csv
    |   |   ├── raw_db_jobs_tile.csv
    |   |   └── raw_df_scraping_countries.csv
    |   └── results
    |       ├── Bonus1-Data_Opinions.csv
    |       └── country_gender_analysed.csv
    ├── notebooks
    |   └── draft.ipynb
    ├── p_acquisition
    |   └── m_acquisition.py
    |── p_analysis
    |   └── m_analysis.py
    ├── p_wrangling
    |   └── m_wrangling.py
    ├── .env.txt
    ├── .gitignore
    ├── main.py
    ├── README.md
    └── requeriments.txt
        
```

> Do not forget to include `__trash__` and `.env` in `.gitignore` 

### :shit: **ToDo**
Bonus incomming...
