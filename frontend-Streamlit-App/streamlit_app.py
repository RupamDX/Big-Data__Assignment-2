import streamlit as st
import requests

# Point this to your deployed FastAPI app (e.g., on Render)
API_BASE_URL = "https://my-fastapi-snowflake.onrender.com"

def fetch_table_data(table_name: str):
    """Fetch all rows from the specified Snowflake table via FastAPI."""
    url = f"{API_BASE_URL}/api/data/{table_name}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()  # e.g., {"table": "INCOME_STATEMENT", "rows": [...]}
        else:
            st.error(f"Error fetching data (status {response.status_code}): {response.text}")
    except Exception as e:
        st.error(f"Exception: {e}")
    return None

def main():
    st.title("Snowflake Tables Viewer")

    # The three tables in Snowflake
    tables = ["income_statement", "balance_sheet", "cash_flow"]

    st.write("Use the buttons below to view data from each table.")

    # For each table, show a button and display data on click
    for table in tables:
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button(f"View data: {table}", key=table):
                result = fetch_table_data(table)
                if result and "rows" in result:
                    st.write(f"**{result['table']}** - {len(result['rows'])} rows")
                    if result["rows"]:
                        # Show data in a table
                        st.dataframe(result["rows"])
                    else:
                        st.warning("No data found.")
        st.write("---")

if __name__ == "__main__":
    main()
