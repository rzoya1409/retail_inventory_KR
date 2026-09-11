# Retail Inventory Knowledge Repository

## Aim

To create a cloud-based knowledge repository for a Retail Inventory and Reorder Management System and make it publicly accessible through GitHub.

## Problem Statement

Retail businesses need to monitor stock levels, identify products that need reordering, reduce losses from expired products, and improve sales of slow-moving products.

This project creates a rule-based knowledge repository that assists a store manager in making inventory decisions.

## Features

- Detects low-stock and urgent-reorder conditions
- Identifies expired and near-expiry products
- Detects slow-moving products
- Identifies fast-moving products
- Provides explainable recommendations using business rules
- Stores business knowledge in JSON format
- Uses a Python inference engine for knowledge resolution

## Repository Structure

| File | Purpose |
|---|---|
| `knowledge_base.json` | Contains inventory, expiry, and sales business rules |
| `inventory_advisory.py` | Python program that applies the rules |
| `sample_output.txt` | Example output of the system |
| `requirements.txt` | Required Python packages |
| `docs/index.html` | Public project webpage for GitHub Pages |

## How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the repository folder.
4. Run:

```bash
python inventory_advisory.py
```

5. Enter the product details.
6. The system will display inventory, expiry, and promotion recommendations.

## Example Rule

```text
IF current_stock <= reorder_level
THEN place a purchase order immediately.
```

## Disclaimer

This project is an educational prototype. A real retail system should also use sales forecasting, supplier lead time, product seasonality, purchase cost, profit margin, available storage, and business policies.
