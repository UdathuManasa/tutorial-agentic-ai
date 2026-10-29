import sqlite3

# Connect to store.db (this will create it if it doesn't exist)
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# Execute the SQL schema and inserts
sql_script = """
-- Products Table
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    is_organic INTEGER DEFAULT 0
);

-- Reviews Table
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    rating REAL CHECK(rating >= 1 AND rating <= 5),
    reviewer_name TEXT,
    review_text TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Orders Table (Left Empty)
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    product_name TEXT,
    price REAL,
    ordered_at TEXT,
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert Data for Products
INSERT OR IGNORE INTO products (id, name, category, price, description, is_organic) VALUES
(1, 'Organic Raw Honey', 'honey', 14.99, 'Pure organic raw honey, unfiltered and cold-pressed', 1),
(2, 'Wildflower Honey', 'honey', 12.99, 'Natural wildflower honey from local beekeepers', 0),
(3, 'Organic Manuka Honey', 'honey', 29.99, 'Premium organic Manuka honey from New Zealand', 1),
(4, 'Clover Honey', 'honey', 8.99, 'Classic clover honey, smooth and sweet', 0),
(5, 'Organic Buckwheat Honey', 'honey', 18.99, 'Dark and robust organic buckwheat honey, antioxidant-rich', 1),
(6, 'Orange Blossom Honey', 'honey', 15.99, 'Light and floral orange blossom honey', 0),
(7, 'Organic Acacia Honey', 'honey', 17.99, 'Light and mild organic acacia honey, low glycemic index', 1),
(8, 'Creamed Honey', 'honey', 11.99, 'Smooth creamed honey with spreadable texture', 0),
(9, 'Organic Extra Virgin Olive Oil', 'oil', 16.99, 'Cold-pressed organic EVOO from Mediterranean', 1),
(10, 'Coconut Oil', 'oil', 12.49, 'Refined coconut oil, great for high-heat cooking', 0),
(11, 'Organic Flaxseed Oil', 'oil', 14.99, 'Cold-pressed organic flaxseed oil, rich in omega-3', 1),
(12, 'Avocado Oil', 'oil', 18.99, 'Cold-pressed avocado oil, high smoke point', 0),
(13, 'Organic Almonds', 'nuts', 11.99, 'Raw organic almonds, unsalted, non-GMO certified', 1),
(14, 'Roasted Cashews', 'nuts', 9.99, 'Lightly salted dry-roasted cashews', 0),
(15, 'Organic Chia Seeds', 'seeds', 8.49, 'Organic black chia seeds, high in fiber and omega-3', 1),
(16, 'Mixed Nuts', 'nuts', 13.99, 'Premium mix of walnuts, pecans, almonds and cashews', 0),
(17, 'Organic Quinoa', 'grains', 10.99, 'Organic white quinoa, complete protein, gluten-free', 1);

-- Insert Data for Reviews
INSERT OR IGNORE INTO reviews (id, product_id, rating, reviewer_name, review_text) VALUES
(130, 1, 5.0, 'Alice', 'Amazing honey! Best I''ve ever tried.'),
(131, 1, 4.0, 'Bob', 'Good quality, will buy again.'),
(132, 1, 5.0, 'Carol', 'Excellent raw flavor, very pure.'),
(133, 1, 4.5, 'Dave', 'Very good, love that it''s unfiltered.'),
(134, 2, 4.0, 'Eve', 'Decent honey for the price.'),
(135, 2, 3.5, 'Frank', 'Average, nothing special.'),
(136, 2, 4.0, 'Grace', 'Good everyday honey.'),
(137, 3, 5.0, 'Henry', 'Worth every penny, incredible quality.'),
(138, 3, 4.5, 'Iris', 'Excellent antibacterial properties.'),
(139, 3, 5.0, 'Jack', 'Best honey I have ever tasted.'),
(140, 4, 3.5, 'Kate', 'Okay for cooking, nothing fancy.'),
(141, 4, 3.5, 'Leo', 'Nothing special, pretty generic.'),
(142, 4, 3.5, 'Mia', 'Average clover honey.'),
(143, 5, 5.0, 'Noah', 'Rich bold flavor, great in tea.'),
(144, 5, 4.0, 'Olivia', 'Good strong honey, unique taste.'),
(145, 5, 5.0, 'Paul', 'Love the dark color and deep flavor.'),
(146, 5, 4.5, 'Quinn', 'Great organic option at this price.'),
(147, 6, 4.0, 'Rachel', 'Nice floral flavor.');
"""

cursor.executescript(sql_script)
conn.commit()
conn.close()

print("Database setup complete and data inserted successfully!")