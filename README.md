# Shop API

A small FastAPI service for viewing products and calculating order quotes.

## Planned endpoints

- GET /products — list all products.
- GET /products/{product_id} — return one product.
- POST /orders/quote — calculate a total from product IDs and quantities.

## Scope

Product prices come from a local JSON catalog.
The service calculates quotes but does not save orders or process payments.
The project will include input validation and pytest tests.

## Status

Initial setup. The API is not implemented yet.