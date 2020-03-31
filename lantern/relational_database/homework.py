import psycopg2


def task_1_add_new_record_to_db(con: psycopg2.extensions.connection) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    """

    sql = """
    INSERT INTO customers (customername, contactname, address, city, postalcode, country)
    VALUES ('Thomas', 'David', 'Some Address', 'London', '774', 'Singapore');
    """
    with con.cursor() as cursor:
        cursor.execute(sql)
        con.commit()


def task_2_list_all_customers(cur: psycopg2.extensions.cursor) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """

    cur.execute("SELECT * FROM customers;")
    return cur.fetchall()


def task_3_list_customers_in_germany(cur: psycopg2.extensions.cursor) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """

    cur.execute("SELECT * FROM customers WHERE country = 'Germany'")
    return cur.fetchall()


def task_4_update_customer(con: psycopg2.extensions.connection) -> None:
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        con: psycopg connection

    """

    sql = """
    UPDATE customers 
    SET customername = 'Johnny Depp'
    WHERE customerid = (SELECT MIN(customerid) FROM customers);
    """

    with con.cursor() as cursor:
        cursor.execute(sql)
        con.commit()


def task_5_delete_the_last_customer(con: psycopg2.extensions.connection) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """

    sql = """
    DELETE FROM customers
    WHERE customerid = (SELECT MAX(customerid) FROM customers)
    """
    with con.cursor() as cursor:
        cursor.execute(sql)
        con.commit()


def task_6_list_all_supplier_countries(cur: psycopg2.extensions.cursor) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """

    cur.execute("SELECT country from suppliers;")
    return cur.fetchall()


def task_7_list_supplier_countries_in_desc_order(cur: psycopg2.extensions.cursor) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """

    cur.execute("SELECT country from suppliers ORDER BY country DESC;")
    return cur.fetchall()


def task_8_count_customers_by_city(cur: psycopg2.extensions.cursor) -> list:
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """

    sql = '''
    SELECT COUNT(customername), city 
    FROM customers 
    GROUP BY city
    ORDER BY city DESC;
    '''

    cur.execute(sql)
    return cur.fetchall()


def task_9_count_customers_by_country_with_than_10_customers(cur: psycopg2.extensions.cursor) -> list:
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """

    sql = '''
    SELECT COUNT(customername), country 
    FROM customers 
    GROUP BY country 
    HAVING COUNT(*) > 10;
    '''

    cur.execute(sql)
    return cur.fetchall()


def task_10_list_first_10_customers(cur: psycopg2.extensions.cursor) -> list:
    """
    List first 10 customers from the table

    Results: 10 records
    """

    cur.execute("SELECT * FROM customers LIMIT 10;")
    return cur.fetchall()


def task_11_list_customers_starting_from_11th(cur: psycopg2.extensions.cursor) -> list:
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """

    cur.execute("SELECT * FROM customers WHERE customerid > 11;")
    return cur.fetchall()


def task_12_list_suppliers_from_specified_countries(cur: psycopg2.extensions.cursor) -> list:
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """

    sql = """
    SELECT supplierid, suppliername, contactname, city, country
    FROM suppliers 
    WHERE country in ('USA','UK','Japan');
    """

    cur.execute(sql)
    return cur.fetchall()


def task_13_list_products_from_sweden_suppliers(cur: psycopg2.extensions.cursor) -> list:
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """

    sql = """
    SELECT p.productname 
    FROM products as p 
    INNER JOIN suppliers as s
    ON p.supplierid = s.supplierid
    WHERE s.country = 'Sweden';
    """

    cur.execute(sql)
    return cur.fetchall()


def task_14_list_products_with_supplier_information(cur: psycopg2.extensions.cursor) -> list:
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """

    sql = """
    SET lc_monetary TO 'en_US.UTF-8';
    SELECT p.productid, p.productname, p.unit, p.price, s.country, s.city, s.suppliername
    FROM products as p
    INNER JOIN suppliers as s
    ON p.supplierid = s.supplierid
    """

    cur.execute(sql)
    return cur.fetchall()


def task_15_list_customers_with_any_order_or_not(cur: psycopg2.extensions.cursor) -> list:
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """

    sql = """
    SELECT c.customername, c.contactname, c.country, o.orderid
    FROM customers as c
    LEFT JOIN orders as o
    ON c.customerid = o.customerid
    """

    cur.execute(sql)
    return cur.fetchall()


def task_16_match_all_customers_and_suppliers_by_country(cur: psycopg2.extensions.cursor) -> list:
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """

    sql = """
    SELECT c.customername, c.address, c.country as customercountry,
    s.country as suppliercountry, s.suppliername
    FROM customers as c
    FULL JOIN suppliers as s
    ON c.country = s.country
    ORDER BY customercountry, suppliercountry
    """
    
    cur.execute(sql)
    return cur.fetchall()
