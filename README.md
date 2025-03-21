# Snowflake-FastAPI-Streamlit

This project showcases how to **fetch data** from [Snowflake](https://www.snowflake.com/) using a **FastAPI** backend, then display that data in a **Streamlit** application. The backend is deployed on [Render](https://render.com/), and the front-end on [Streamlit Cloud](https://streamlit.io/cloud).


##Streamlit APP LINK:https://big-dataassignment-2-4znmzakwzd9uksved3xow6.streamlit.app/

##BackEnd Link: https://big-data-assignment-2.onrender.com

##Codelab Doc:https://codelabs-preview.appspot.com/?file_id=1DxRG82BB6EPuUBxK2cIVywoS1OmdwuE30waqx2Nrbas#8


## Overview

- **Backend**: A [FastAPI](https://fastapi.tiangolo.com/) application that connects to Snowflake and exposes data from three tables: `income_statement`, `balance_sheet`, and `cash_flow`.
- **Frontend**: A [Streamlit](https://streamlit.io/) app that provides a simple UI with buttons to view each table’s data (limited to 1,000 rows to avoid running out of memory).
- **Deployment**: The FastAPI service is hosted on Render, and the Streamlit UI is hosted on Streamlit Cloud.

---
## Architecture Diagram
![sec_data_processing_pipelines](https://github.com/user-attachments/assets/7909a62b-fc07-4269-b32c-71f5aefd881f)

## Tech Stack:
**AirFlow**
**DBT**
**Snowflake**
**streamlit**
**FastAPI**


## Project Structure

```bash
.
├── backend/
│   ├── app.py              # FastAPI application
│   └── requirements.txt    # Dependencies for FastAPI + Snowflake
├── frontend/
│   ├── streamlit_app.py    # Streamlit application
│   └── requirements.txt    # Dependencies for Streamlit + requests
└── README.md               # This file

----
##AiUseDisclosure
Tools used for debugging and understanding the tool setup flow Chatgpt Gemini
1.Used the tool to setup the applications in local , add integrations on different applications. 2.Used it for debugging and solving errors 3.Helped us understand the flow of different tools and optimize our solutions 4.Understand the basic use of airflow,snowflake and configure it.
