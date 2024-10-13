-- Create the Categories table
CREATE TABLE Categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL
);

-- Create the Suppliers table
CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(255),
    address VARCHAR(255)
);

-- Create the Products table
CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    category_id INT,
    quantity_in_stock INT DEFAULT 0,
    reorder_level INT DEFAULT 0,
    price_per_unit DECIMAL(10, 2),
    supplier_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

-- Create the Warehouses table
CREATE TABLE Warehouses (
    warehouse_id INT PRIMARY KEY AUTO_INCREMENT,
    warehouse_name VARCHAR(255) NOT NULL,
    location VARCHAR(255)
);

-- Create the Inventory_Movements table
CREATE TABLE Inventory_Movements (
    movement_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    warehouse_id INT,
    quantity INT NOT NULL,
    movement_type ENUM('IN', 'OUT') NOT NULL,
    date_moved DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id),
    FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id)
);

-- Create the Customers table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(255),
    address VARCHAR(255)
);

-- Create the Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    order_status ENUM('Pending', 'Shipped', 'Completed') DEFAULT 'Pending',
    total_amount DECIMAL(10, 2) DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Create the Order_Details table
CREATE TABLE Order_Details (
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity_ordered INT NOT NULL,
    price_per_unit DECIMAL(10, 2) NOT NULL,
    total_price DECIMAL(10, 2) GENERATED ALWAYS AS (quantity_ordered * price_per_unit) STORED,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- Create the Shipments table
CREATE TABLE Shipments (
    shipment_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    shipment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    delivery_date DATETIME,
    shipment_status ENUM('Pending', 'In Transit', 'Delivered') DEFAULT 'Pending',
    tracking_number VARCHAR(255),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

--********* TRIGGERS *********--

-- Decrease stock when an order is placed
CREATE TRIGGER update_stock_on_order
AFTER INSERT ON Order_Details
FOR EACH ROW
BEGIN
    UPDATE Products
    SET quantity_in_stock = quantity_in_stock - NEW.quantity_ordered
    WHERE product_id = NEW.product_id;
END;

-- Update stock on inventory movement (IN)
CREATE TRIGGER update_stock_on_movement_in
AFTER INSERT ON Inventory_Movements
FOR EACH ROW
BEGIN
    IF NEW.movement_type = 'IN' THEN
        UPDATE Products
        SET quantity_in_stock = quantity_in_stock + NEW.quantity
        WHERE product_id = NEW.product_id;
    END IF;
END;

-- Update stock on inventory movement (OUT)
CREATE TRIGGER update_stock_on_movement_out
AFTER INSERT ON Inventory_Movements
FOR EACH ROW
BEGIN
    IF NEW.movement_type = 'OUT' THEN
        UPDATE Products
        SET quantity_in_stock = quantity_in_stock - NEW.quantity
        WHERE product_id = NEW.product_id;
    END IF;
END;

--********* INDEXES *********--

-- Create indexes

-- Products table
CREATE INDEX idx_category_id ON Products(category_id);
CREATE INDEX idx_supplier_id ON Products(supplier_id);

-- Inventory_Movements table
CREATE INDEX idx_product_id ON Inventory_Movements(product_id);
CREATE INDEX idx_warehouse_id ON Inventory_Movements(warehouse_id);

-- Orders table
CREATE INDEX idx_customer_id ON Orders(customer_id);

-- Order_Details table
CREATE INDEX idx_order_id ON Order_Details(order_id);
CREATE INDEX idx_product_id_order_details ON Order_Details(product_id);

