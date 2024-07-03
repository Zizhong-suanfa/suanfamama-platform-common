import sqlite3

def get_total_ads_from_db(db_path: str):
    """
    Retrieves the total number of ads from the database.

    Args:
        db_path (str): Path to the database file.

    Returns:
        int: The total number of ads.
    """

    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the query to get the total number of users
    cursor.execute("SELECT COUNT(*) FROM ads")

    # Fetch the result
    total_ads = cursor.fetchone()[0]

    # Close the database connection
    conn.close()

    return total_ads

def get_ads_from_db(db_path: str):
    """
    Gets a list of ads from a SQLite database.

    Args:
        db_path: The path to the SQLite database file.

    Returns:
        A list of ads, where each ad is a dictionary with the following keys:
        - id: The ad's ID.
        - adname: The ad's adname.
        - creator: The ad's creator.
        - object-url: The object url of the ad
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execute the query to get all ads
    cursor.execute("SELECT * FROM ads")

    # Fetch all rows as a list of dictionaries
    ads = [
        dict(id=row[0], adname=row[1], creator=row[2], object_url=row[3])
        for row in cursor.fetchall()
    ]

    # Close the database connection
    conn.close()

    return ads