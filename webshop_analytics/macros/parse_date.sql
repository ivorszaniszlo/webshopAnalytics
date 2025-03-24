{% macro parse_date(date_string_column, format_string="'%Y-%m-%d'") %}
    strptime({{ date_string_column }}, {{ format_string }})
{% endmacro %}
