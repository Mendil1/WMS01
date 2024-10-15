
INSERT INTO products_category (category_name) 
VALUES 
('Engine Parts'),
('Brakes'),
('Suspension'),
('Transmission'),
('Exhaust'),
('Electrical'),
('Cooling System'),
('Filters'),
('Tires'),
('Interior Accessories');

INSERT INTO products_supplier (supplier_name, phone_number, email, address) 
VALUES 
('Tunisia Auto Parts Co.', '+216 71 123 456', 'info@tunisiaautoparts.tn', '12 Avenue Habib Bourguiba, Tunis'),
('Carthage Motors Supply', '+216 71 654 321', 'sales@carthagemotors.tn', '5 Rue de Marseille, Sfax'),
('Monastir Mechanical Supplies', '+216 73 101 202', 'contact@monastirmechanical.tn', '14 Avenue de la Liberté, Monastir'),
('Sousse Auto Supplies', '+216 73 505 707', 'support@sousseautosupplies.tn', '23 Rue Ibn Khaldoun, Sousse'),
('Bizerte Parts Distributors', '+216 72 303 404', 'bizerteparts@bizerteparts.tn', '7 Rue de la République, Bizerte'),
('Gabes Motor Co.', '+216 75 707 808', 'gabesmotors@gabesmotors.tn', '18 Rue Farhat Hached, Gabes'),
('Sfax Performance Auto', '+216 74 656 758', 'performance@sfaxauto.tn', '10 Rue Ali Belhouane, Sfax');

INSERT INTO products_product (product_name, category_id, quantity_in_stock, reorder_level, price_per_unit, supplier_id) 
VALUES 
('Oil Filter', 8, 150, 20, 12.50, 1),  -- Filters, Tunisia Auto Parts Co.
('Brake Pads Set', 2, 300, 50, 45.00, 2),  -- Brakes, Carthage Motors Supply
('Air Filter', 8, 200, 30, 15.00, 1),  -- Filters, Tunisia Auto Parts Co.
('Spark Plug', 6, 400, 50, 8.75, 3),  -- Electrical, Monastir Mechanical Supplies
('Engine Oil 5W30', 1, 500, 100, 30.00, 4),  -- Engine Parts, Sousse Auto Supplies
('Radiator', 7, 50, 10, 120.00, 5),  -- Cooling System, Bizerte Parts Distributors
('Exhaust Muffler', 5, 60, 10, 85.00, 4),  -- Exhaust, Sousse Auto Supplies
('Transmission Belt', 4, 100, 20, 25.50, 6),  -- Transmission, Gabes Motor Co.
('Shock Absorber', 3, 120, 25, 65.00, 7),  -- Suspension, Sfax Performance Auto
('All-Season Tires', 9, 80, 15, 95.00, 2),-- Tires, Carthage Motors Supply
('Fuel Pump', 1, 80, 10, 150.00, 6),  -- Engine Parts, Gabes Motor Co.
('Brake Disc', 2, 250, 40, 60.00, 5),  -- Brakes, Bizerte Parts Distributors
('Control Arm', 3, 90, 15, 75.00, 7),  -- Suspension, Sfax Performance Auto
('Clutch Kit', 4, 70, 10, 220.00, 2),  -- Transmission, Carthage Motors Supply
('Catalytic Converter', 5, 50, 5, 180.00, 4),  -- Exhaust, Sousse Auto Supplies
('Alternator', 6, 40, 10, 300.00, 3),  -- Electrical, Monastir Mechanical Supplies
('Water Pump', 7, 60, 12, 90.00, 1),  -- Cooling System, Tunisia Auto Parts Co.
('Cabin Air Filter', 8, 180, 25, 20.00, 1),  -- Filters, Tunisia Auto Parts Co.
('Windshield Wiper Blades', 9, 200, 50, 15.00, 3),  -- Tires (Accessories), Monastir Mechanical Supplies
('Steering Wheel Cover', 10, 120, 20, 35.00, 6),  -- Interior Accessories, Gabes Motor Co.
('Timing Chain', 1, 70, 10, 110.00, 7),  -- Engine Parts, Sfax Performance Auto
('ABS Sensor', 2, 130, 25, 55.00, 2),  -- Brakes, Carthage Motors Supply
('Ball Joint', 3, 90, 15, 40.00, 5),  -- Suspension, Bizerte Parts Distributors
('Manual Transmission Fluid', 4, 100, 20, 30.00, 6),  -- Transmission, Gabes Motor Co.
('Oxygen Sensor', 5, 65, 10, 85.00, 1),  -- Exhaust, Tunisia Auto Parts Co.
('Ignition Coil', 6, 45, 5, 95.00, 4),  -- Electrical, Sousse Auto Supplies
('Thermostat', 7, 55, 10, 35.00, 1),  -- Cooling System, Tunisia Auto Parts Co.
('Transmission Filter', 8, 150, 25, 25.00, 2),  -- Filters, Carthage Motors Supply
('Shock Mount', 3, 85, 10, 55.00, 5),  -- Suspension, Bizerte Parts Distributors
('Seat Covers', 10, 100, 15, 65.00, 6);  -- Interior Accessories, Gabes Motor Co.

-- Insert into Warehouses table
INSERT INTO warehouses_warehouse (name, location) VALUES ('Warehouse Carthage', 'Tunis');
INSERT INTO warehouses_warehouse (name, location) VALUES ('Warehouse Sfax ville', 'Sfax');
INSERT INTO warehouses_warehouse (name, location) VALUES ('Warehouse Kantaoui', 'Sousse');

-- Insert into InventoryMovements table
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (1, 1, 50, 'IN', '2024-10-01');
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (2, 2, 30, 'OUT', '2024-10-02');
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (3, 3, 20, 'IN', '2024-10-03');
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (1, 1, 15, 'OUT', '2024-10-04');
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (2, 1, 25, 'IN', '2024-10-05');
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (3, 2, 10, 'IN', '2024-10-06');
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (1, 3, 5, 'OUT', '2024-10-07');
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (2, 2, 20, 'IN', '2024-10-08');
INSERT INTO warehouses_inventorymovement (product_id, warehouse_id, quantity, movement_type, date_moved) VALUES (3, 1, 30, 'OUT', '2024-10-09');

-- Customers Data --
INSERT INTO customers_customer (name, phone_number, email, address) 
VALUES ('Tunis Auto Parts', '+216 71 123 456', 'contact@tunisautoparts.tn', '123 Avenue Habib Bourguiba, Tunis');

INSERT INTO customers_customer (name, phone_number, email, address) 
VALUES ('Sfax Car Shop', '+216 74 654 321', 'info@sfaxcarshop.tn', '456 Rue de la République, Sfax');

INSERT INTO customers_customer (name, phone_number, email, address) 
VALUES ('Monastir Mechanics', '+216 73 987 654', 'sales@monastirmechanics.tn', '789 Avenue de la Liberté, Monastir');

INSERT INTO customers_customer (name, phone_number, email, address) 
VALUES ('Bizerte Spare Parts', '+216 72 321 654', 'support@bizertespareparts.tn', '321 Boulevard de la Marine, Bizerte');

INSERT INTO customers_customer (name, phone_number, email, address) 
VALUES ('Gabès Auto Service', '+216 75 789 123', 'service@gabesautoservice.tn', '987 Rue Farhat Hached, Gabès');

INSERT INTO customers_customer (name, phone_number, email, address) 
VALUES ('Sousse Motor Parts', '+216 73 567 890', 'inquiry@soussemotorparts.tn', '654 Rue du 9 Avril, Sousse');

INSERT INTO customers_customer (name, phone_number, email, address) 
VALUES ('Nabeul Parts Center', '+216 72 908 765', 'admin@nabeulpartscenter.tn', '234 Rue de la Paix, Nabeul');

INSERT INTO customers_customer (name, phone_number, email, address) 
VALUES ('Kairouan Auto Supplies', '+216 77 456 789', 'orders@kairouanautosupplies.tn', '654 Avenue de la Victoire, Kairouan');


-- Insertion de commandes dans la table orders_order
INSERT INTO orders_order (order_date, order_status, total_amount, customer_id) 
VALUES 
('2024-10-01', 'Completed', 450.00, 1),  -- Tunis Auto Parts
('2024-10-02', 'Pending', 225.00, 2),    -- Sfax Car Shop
('2024-10-03', 'Shipped', 380.00, 3),    -- Monastir Mechanics
('2024-10-04', 'Delivered', 600.00, 4),  -- Bizerte Spare Parts
('2024-10-05', 'Cancelled', 300.00, 5),  -- Gabès Auto Service
('2024-10-06', 'Completed', 750.00, 6),  -- Sousse Motor Parts
('2024-10-07', 'Shipped', 620.00, 7),    -- Nabeul Parts Center
('2024-10-08', 'Pending', 800.00, 8);    -- Kairouan Auto Supplies


-- Insertion de détails de commande dans la table orders_orderdetail
INSERT INTO orders_orderdetail (quantity_ordered, price_per_unit, total_price, order_id, product_id)
VALUES
(10, 12.50, 125.00, 1, 1),  -- Order 1, Oil Filter
(5, 45.00, 225.00, 2, 2),   -- Order 2, Brake Pads Set
(4, 8.75, 35.00, 3, 4),     -- Order 3, Spark Plug
(2, 150.00, 300.00, 4, 11), -- Order 4, Fuel Pump
(3, 85.00, 255.00, 5, 7),   -- Order 5, Exhaust Muffler
(6, 65.00, 390.00, 6, 9),   -- Order 6, Shock Absorber
(5, 95.00, 475.00, 7, 10),  -- Order 7, All-Season Tires
(8, 25.00, 200.00, 8, 28);  -- Order 8, Transmission Filter


-- Insertion de données d'expéditions dans la table orders_shipment
INSERT INTO orders_shipment (shipment_date, delivery_date, shipment_status, tracking_number, order_id)
VALUES
('2024-10-02', '2024-10-03', 'Delivered', 'TN123456789', 1),  -- Order 1
('2024-10-03', NULL, 'Pending', 'TN987654321', 2),            -- Order 2
('2024-10-04', NULL, 'Shipped', 'TN654321987', 3),            -- Order 3
('2024-10-05', '2024-10-06', 'Delivered', 'TN321654987', 4),  -- Order 4
('2024-10-06', NULL, 'Cancelled', 'TN852741963', 5),          -- Order 5
('2024-10-07', '2024-10-08', 'Delivered', 'TN741852963', 6),  -- Order 6
('2024-10-08', NULL, 'Shipped', 'TN159753852', 7),            -- Order 7
('2024-10-09', NULL, 'Pending', 'TN456789123', 8);            -- Order 8
