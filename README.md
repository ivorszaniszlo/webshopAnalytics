# Webshop Analytics (dbt Core)

## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Screenshot](#screenshot)
* [Technologies](#technologies)
* [Setup & Start](#setup)
* [Deploy](#deploy)
* [Created](#created)
* [License](#license)

## General info <a id="general-info"></a>

A data transformation project using dbt Core to demonstrate analytics on e-commerce data. It uses CSV files as source input, transforms them into structured marts, and showcases various dbt functionalities such as tests, macros, and documentation.

## Description <a id="description"></a>

This small-scale project demonstrates the versatility of dbt Core within 2–4 hours of development. It includes:
- Source staging of CSV data (orders and customers)
- A customer-level summary mart
- Custom macros (e.g., cents to dollars)
- Built-in tests (`unique`, `not_null`)
- Schema documentation
- dbt Docs usage

The purpose is to show how dbt can be used for local analytics development quickly and effectively.

## Screenshot <a id="screenshot"></a>

![screenshot](./docs/screenshot.jpg)

## Technologies <a id="technologies"></a>

* dbt-core
* dbt-duckdb or dbt-postgres
* Jinja templating
* CSV as source data
* Optional: dbt-docs

## Setup & Start <a id="setup"></a>

* Clone or download the repo
* Navigate to the project folder
* Create and activate a Python virtual environment:
  ```bash
  python -m venv dbt-env
  .\dbt-env\Scripts\activate
  ```
* Install dependencies (example using DuckDB):
  ```bash
  pip install dbt-core dbt-duckdb
  ```
* Initialize dbt project:
  ```bash
  dbt init webshop_analytics
  ```
* Create the `profiles.yml` file in the following location:
  ```
  C:\Users\<your-username>\.dbt\profiles.yml
  ```

  Paste this content:
  ```yaml
  webshop_analytics:
    outputs:
      dev:
        type: duckdb
        path: dev.duckdb
        threads: 1

      prod:
        type: duckdb
        path: prod.duckdb
        threads: 4

    target: dev
  ```

* Load and run the project:
  ```bash
  dbt seed
  dbt run
  dbt test
  dbt docs generate
  dbt docs serve
  ```

## Deploy <a id="deploy"></a>

This is a local dbt Core project and not deployed online. Documentation can be served locally using `dbt docs serve`.

## Created <a id="created"></a>

2025

## License <a id="license"></a>

MIT
