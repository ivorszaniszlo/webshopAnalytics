with source as (
    select * from {{ ref('orders') }}
),

renamed as (
    select
        order_id,
        customer_id,
        cast(order_date as date) as order_date,
        order_value_cents
    from source
)

select * from renamed
