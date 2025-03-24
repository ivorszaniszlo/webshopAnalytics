-- models/example/uppercase_demo.sql

{{ config(materialized='view') }}

select
  customer_id,
  {{ to_uppercase('customer_name') }} as customer_name_upper
from {{ ref('stg_customers') }}
