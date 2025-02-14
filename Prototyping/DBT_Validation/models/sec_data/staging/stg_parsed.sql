{{ config(materialized='view') }}

SELECT
  data:cik::STRING  AS cik,
  data:filed::DATE  AS filed,
  data:fy::INTEGER  AS fy,
  data:fp::STRING   AS fp,
  data:tag::STRING  AS tag,
  data:value::FLOAT AS value,
  data:ddate::DATE  AS ddate
FROM {{ source('raw_data', 'raw_json_data') }}
