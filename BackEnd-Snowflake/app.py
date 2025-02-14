from fastapi import FastAPI, HTTPException
import snowflake.connector
import os

app = FastAPI()

# Replace these with environment variables or your actual credentials
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER", "kiranss777")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD", "Workdaykiran123$")
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT", "feumdln-cm11635")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE", "ANALYTICS_WH")
SNOWFLAKE_DATABASE = os.getenv("SNOWFLAKE_DATABASE", "SEC_FINANCIALS")
SNOWFLAKE_SCHEMA = os.getenv("SNOWFLAKE_SCHEMA", "DEV")

# Whitelist valid table names (uppercase in Snowflake by convention)
VALID_TABLES = {"INCOME_STATEMENT", "BALANCE_SHEET", "CASH_FLOW"}

@app.get("/")
def root():
    return {"message": "Hello from FastAPI + Snowflake!"}

@app.get("/api/data/{table_name}")
def get_data(table_name: str):
    """
    Fetch data from one of the three tables: income_statement, balance_sheet, cash_flow.
    """
    # Convert to uppercase for matching our whitelist Check
    table_name_upper = table_name.upper() 

    # Validate table name
    if table_name_upper not in VALID_TABLES:
        raise HTTPException(status_code=400, detail="Invalid table name.")

    try:
        # Establish Snowflake connection
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        cur = conn.cursor()

        # Build the query (fetch all rows from the specified table)
        query = f"SELECT * FROM {table_name_upper}"
        cur.execute(query)

        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]

        # Convert rows to list of dicts
        data = []
        for row in rows:
            row_dict = {}
            for col_name, value in zip(col_names, row):
                row_dict[col_name] = value
            data.append(row_dict)

        cur.close()
        conn.close()

        # Return the data
        return {"table": table_name_upper, "rows": data}

    except Exception as e:
        # If there's an error, raise an HTTP exception
        raise HTTPException(status_code=500, detail=str(e))
