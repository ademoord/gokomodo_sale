# Gokomodo Sales Customization Module

## Overview

This module is designed to help Gokomodo categorize their clients based on different business models and apply specific tax rules accordingly. It introduces new features to the Sale Order and Sale Order Line in Odoo 14 to support these business needs.

## Features

1. **Business Model Field**:
    - Adds a new required field `Business Model` to the Sale Order form.
    - Current business models include: Retail, Corporate, and Subscription.

2. **Custom Sale Order Display Name**:
    - Modifies the display name of Sale Orders to include the short name of the business model.
    - Example: `[RT]-S0001` for Retail, `[CORP]-S0002` for Corporate, `[SUB]-S0003` for Subscription.

3. **Group By Business Model in Quotations Tree View**:
    - Adds an option to group Sale Orders by the business model in the quotations tree view.

4. **Business Model Based Tax Selection**:
    - Filters the available taxes in the Sale Order Line based on the selected business model.

## Installation

1. Clone the repository to your Odoo addons directory:
    ```sh
    git clone https://github.com/yourusername/gokomodo_sales_customization.git
    ```
2. Restart your Odoo server:
    ```sh
    sudo service odoo restart
    ```
3. Update the app list from the Odoo Apps menu.
4. Install the `Gokomodo Sales Customization` module.

## Usage

### 1. Business Model Field

- When creating or editing a Sale Order, you will now see a new required field `Business Model`.
- Select one of the available options: Retail, Corporate, or Subscription.

### 2. Custom Sale Order Display Name

- The display name of the Sale Order will automatically include the short name of the selected business model.
- For example, a Sale Order with the name `S0001` and a business model `Retail` will be displayed as `[RT]-S0001`.

### 3. Group By Business Model in Quotations Tree View

- In the quotations tree view, you can now group Sale Orders by the business model.
- This allows for easier organization and filtering of orders based on the client category.

### 4. Business Model Based Tax Selection

- When adding or editing a Sale Order Line, the available taxes will be filtered based on the selected business model of the Sale Order.
- This ensures that only relevant taxes can be applied, reducing errors and improving consistency.

## Configuration

### Business Model Tax Configuration

To configure the taxes applicable for each business model:

1. Open the `Gokomodo Sales Customization` module.
2. Navigate to `Settings` > `Taxes`.
3. Define the taxes for each business model (Retail, Corporate, Subscription).

## Credit
Copyright (c) Ademord ERP 2024
