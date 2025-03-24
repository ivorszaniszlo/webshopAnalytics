{% macro cents_to_dollars(cents_column) %}
    ({{ cents_column }} / 100.0)
{% endmacro %}
