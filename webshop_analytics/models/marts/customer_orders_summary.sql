with orders as (
    select * from {{ ref('stg_orders') }}
),

customers as (
    select * from {{ ref('stg_customers') }}
),

order_summary as (
    select
        o.customer_id,
        count(o.order_id) as total_orders,
        sum(o.order_value_cents) / 100.0 as total_spent_usd
    from orders o
    group by o.customer_id
)

select
    c.customer_id,
    c.customer_name,
    c.email,
    c.signup_date,
    s.total_orders,
    s.total_spent_usd
from customers c
left join order_summary s using (customer_id)
