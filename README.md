# Snowflake-FastAPI-Streamlit

This project showcases how to **fetch data** from [Snowflake](https://www.snowflake.com/) using a **FastAPI** backend, then display that data in a **Streamlit** application. The backend is deployed on [Render](https://render.com/), and the front-end on [Streamlit Cloud](https://streamlit.io/cloud).


##Streamlit APP LINK:https://big-dataassignment-2-4znmzakwzd9uksved3xow6.streamlit.app/
##BackEnd Link: https://big-data-assignment-2.onrender.com
## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Requirements](#requirements)
- [Local Development](#local-development)
  - [Backend (FastAPI)](#backend-fastapi)
  - [Frontend (Streamlit)](#frontend-streamlit)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
  - [Deploying FastAPI on Render](#deploying-fastapi-on-render)
  - [Deploying Streamlit on Streamlit-Cloud](#deploying-streamlit-on-streamlit-cloud)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

- **Backend**: A [FastAPI](https://fastapi.tiangolo.com/) application that connects to Snowflake and exposes data from three tables: `income_statement`, `balance_sheet`, and `cash_flow`.
- **Frontend**: A [Streamlit](https://streamlit.io/) app that provides a simple UI with buttons to view each table’s data (limited to 1,000 rows to avoid running out of memory).
- **Deployment**: The FastAPI service is hosted on Render, and the Streamlit UI is hosted on Streamlit Cloud.

---

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
