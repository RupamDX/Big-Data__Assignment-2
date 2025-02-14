{{ config(materialized='table') }}

WITH stg AS (
    SELECT *
    FROM {{ ref('stg_parsed') }}
)
SELECT *
FROM stg
WHERE NOT (
    tag ILIKE '%Revenue%' OR 
    tag ILIKE '%Income%' OR 
    tag ILIKE '%Expense%' OR 
    tag ILIKE '%Profit%' OR 
    tag ILIKE '%Cash%' OR 
    tag ILIKE '%Operating%' OR 
    tag ILIKE '%Investing%' OR 
    tag ILIKE '%Financing%'
)