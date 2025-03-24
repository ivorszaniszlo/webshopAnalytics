{{ config(
    materialized='incremental',
    unique_key='order_id'
) }}

with source as (
    select
        order_id,
        customer_id,
        cast(order_date as date) as order_date,
        {{ cents_to_dollars("order_value_cents") }} as order_value_usd
    from {{ ref('stg_orders') }}
    {% if is_incremental() %}
      where order_date > (select max(order_date) from {{ this }})
    {% endif %}
)

select * from source
