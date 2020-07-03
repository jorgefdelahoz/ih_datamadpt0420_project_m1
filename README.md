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
Retrieve Jobs Title with DDBB, API & Web Scrapping.

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
    |   |   └── raw_df_scrapping_countries.csv
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
Next steps, features planned, known bugs (shortlist).

### :information_source: **Further info**
Credits, alternatives, references, license.

### :love_letter: **Contact info**
Getting help, getting involved, hire me please.

---

> Here you have some repo examples:
- [Mamba (OCR-Translator-Assistant)](https://github.com/YonatanRA/OCR-translator-assistant-project)
- [Art Classification](https://github.com/serguma/art_classification)
- [OSNet-IBN (width x 1.0) Lite](https://github.com/RodMech/OSNet-IBN1-Lite)
- [Movie Founder](https://github.com/Alfagu/final-project-Ironhack-0419mad)
- [Convolutional Neural Network to detect Pneumonia](https://github.com/jmolins89/final-project)
- [Brain tumor detection project](https://github.com/alonsopdani/brain-tumor-detection-project)
- [Policy-Gradient-Methods](https://github.com/cyoon1729/Policy-Gradient-Methods)

> Here you have some tools and references:
- [Make a README](https://www.makeareadme.com/)
- [Awesome README](https://github.com/matiassingers/awesome-readme)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

