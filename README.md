ResponSight — Emergency Response Intelligence



## Project Overview

ResponSight is a data analytics project that explores emergency ambulance calls, recorded response times, ambulance availability, and target response achievement. It uses SQL, Python, Excel, and Power BI to identify demand patterns and potential opportunities for better emergency resource planning.

## Objectives

\- Analyze emergency call volume by location, priority, and time of day.

\- Examine recorded response times and ambulance availability.

\- Evaluate the percentage of calls meeting the response target.

\- Present key findings through an interactive Power BI dashboard.

\- Generate summary reports using Python.



## Tools and Technologies

- **Excel:** Data review and preparation

- **SQL:** SQL queries and data analysis

- **Python:** Pandas and Matplotlib

- **Power BI:** Interactive dashboard and visualizations



## Dataset

\-Source:Hugging Face — `electricsheepafrica/africa-synth-ambulance-response-times-all`

\-File:`data/ambulance\_developing\_ems.csv`

\-Records:10,000

\-Columns:29

\-Important:The dataset is synthetic. Its results are for analytical and educational purposes and should not be treated as real-world emergency service statistics.



## Project Structure



ResponSight/

├── data/

│   └── ambulance\_developing\_ems.csv

├── excel/

│   └── ResponSight\_Cleaned.xlsx

├── sql/

│   └── SQL analysis scripts

├── python/

│   ├── responsight\_analysis.py

│   └── outputs/

│       ├── location\_analysis.csv

│       ├── priority\_analysis.csv

│       └── time\_of\_day\_analysis.csv

└── powerbi/

&#x20;   └── ResponSight.pbix



## Key Findings

\- The dataset contains 10,000 emergency call records.

\- Rural locations have the highest recorded call volume in this dataset.

\- Daytime has the highest call volume among the recorded time-of-day categories.

\- Recorded ambulance availability is 17.19%.

\- Response-time averages include recorded zero values, which require careful interpretation.



## How to Run the Python Analysis

1\. Install Python 3 and the required libraries:

&#x20;  ```bash

&#x20;  python -m pip install pandas matplotlib

&#x20;  ```

2\. Open a terminal in the `python` folder.

3\. Run:

&#x20;  ```bash

&#x20;  python responsight\_analysis.py

&#x20;  ```

4\. Find the generated CSV reports in `python/outputs/`.



## Limitations

\- The dataset is synthetic and does not represent verified real-world emergency incidents.

\- Location values are categories, not geographic coordinates.

\- Time of day is categorical, not an exact call timestamp.

\- Recorded zero response times may represent unavailable or unrecorded responses and should not automatically be interpreted as instantaneous responses.



## Future Improvements

\- Add further data-quality checks and response-time analysis.

\- Compare response performance across relevant call categories.

\- Improve the dashboard with additional validated analytical insights.



## Author

Developed as a data analytics portfolio project.



