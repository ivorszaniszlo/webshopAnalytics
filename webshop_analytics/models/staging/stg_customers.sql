with source as (
    select * from {{ ref('customers') }}
),

renamed as (
    select
        customer_id,
        customer_name,
        email,
        cast(signup_date as date) as signup_date
    from source
)

select * from renamed
