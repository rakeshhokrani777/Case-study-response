## Database Design

### Core Tables
- Company(id, name)
- Warehouse(id, company_id, name)
- Product(id, name, sku UNIQUE, price, type)
- Inventory(id, product_id, warehouse_id, quantity)
- InventoryLog(id, inventory_id, change, reason, created_at)
- Supplier(id, name, contact_email)
- ProductSupplier(product_id, supplier_id)
- Bundle(id, parent_product_id, child_product_id, quantity)

### Design Decisions
- Inventory acts as a junction table to support multiple warehouses
- InventoryLog enables auditing and analytics
- SKU is globally unique for consistency
- Index on (product_id, warehouse_id) improves query performance
