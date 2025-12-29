@app.route('/api/companies/<int:company_id>/alerts/low-stock')
def low_stock_alerts(company_id):
    alerts = []

    inventories = db.session.query(Inventory)\
        .join(Product)\
        .join(Warehouse)\
        .filter(Warehouse.company_id == company_id)\
        .filter(Product.sales_last_30_days > 0)\
        .all()

    for inv in inventories:
        threshold = inv.product.low_stock_threshold
        if inv.quantity < threshold:
            days_left = inv.quantity // max(1, inv.product.avg_daily_sales)

            supplier = inv.product.suppliers[0] if inv.product.suppliers else None

            alerts.append({
                "product_id": inv.product.id,
                "product_name": inv.product.name,
                "sku": inv.product.sku,
                "warehouse_id": inv.warehouse.id,
                "warehouse_name": inv.warehouse.name,
                "current_stock": inv.quantity,
                "threshold": threshold,
                "days_until_stockout": days_left,
                "supplier": {
                    "id": supplier.id,
                    "name": supplier.name,
                    "contact_email": supplier.contact_email
                } if supplier else None
            })

    return {
        "alerts": alerts,
        "total_alerts": len(alerts)
    }
