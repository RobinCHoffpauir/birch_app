import sqlite3

class Database:
    def __init__(self, db_name="birch_app.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.init_db()

    def init_db(self):
        """Initialize the database with the required tables"""
        # Apartment Units Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS apartment_units (
                unit_id INTEGER PRIMARY KEY,
                unit_number TEXT,
                size TEXT
            )
        ''')
        # Tenants Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tenants (
                tenant_id INTEGER PRIMARY KEY,
                name TEXT,
                contact_info TEXT,
                unit_id INTEGER,
                FOREIGN KEY (unit_id) REFERENCES apartment_units(unit_id)
            )
        ''')
        # Bills Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS bills (
                id INTEGER PRIMARY KEY,
                type TEXT,
                amount REAL,
                due_date TEXT
            )
        ''')
        # Dues Table
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS dues (
                id INTEGER PRIMARY KEY,
                tenant_id INTEGER,
                amount REAL,
                payment_date TEXT,
                FOREIGN KEY (tenant_id) REFERENCES tenants(tenant_id)
            )
        ''')
        self.conn.commit()

    # ... [Other database methods]

    def close(self):
        """Close the database connection"""
        self.conn.close()
