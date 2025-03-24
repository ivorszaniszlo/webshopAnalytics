-- macros/uppercase.sql

{% macro to_uppercase(string) %}
    upper({{ string }})
{% endmacro %}
