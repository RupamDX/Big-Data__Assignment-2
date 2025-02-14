{{ config(materialized='table') }}

WITH stg AS (
    SELECT *
    FROM {{ ref('stg_parsed') }}
)
SELECT *
FROM stg
WHERE tag ILIKE ANY ('%Cash%', '%Operating%', '%Investing%', '%Financing%')
