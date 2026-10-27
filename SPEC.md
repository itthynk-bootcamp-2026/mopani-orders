# Spec: orders.py

Build these in Lab 1, using GitHub Copilot.

## order_total(items, vat_rate=0.15)

- `items` is a list of `{"name": str, "price": float, "qty": int}`.
- Returns the total **including VAT**, rounded to 2 decimals.
- Raises `ValueError` for an empty list, a negative price, or a qty below 1.

## delivery_fee(subtotal, distance_km)

- Free if the subtotal is R500 or more.
- Otherwise R50 within 10 km, and R80 from 10 to 30 km.
- Over 30 km raises `ValueError("Outside delivery area")`.
