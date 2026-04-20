import mysql.connector
# database connection function
def get_connection():
    return mysql.connector.connect(user='root', database='banking_app', password='Godblessyou@77')


#login function
def login(account_number, pin):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE account_number=%s AND pin=%s"
    cursor.execute(query, (account_number, pin))
    user = cursor.fetchone()

    conn.close()
    return user


#check balance function
def check_balance(account_number):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT balance FROM accounts WHERE account_number=%s"
    cursor.execute(query, (account_number,))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]
    return None


#deposit function
def deposit(account_number, amount):
    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE accounts SET balance = balance + %s WHERE account_number=%s"
    cursor.execute(query, (amount, account_number))

    conn.commit()
    conn.close()

    return True


#withdraw function
def withdraw(account_number, amount):
    conn = get_connection()
    cursor = conn.cursor()
    # Step 1: get current balance
    balance = check_balance(account_number)
    # Step 2: check if enough money
    if balance is None or balance < amount:
        conn.close()
        return False
    # Step 3: subtract money
    query = "UPDATE accounts SET balance = balance - %s WHERE account_number=%s"
    cursor.execute(query, (amount, account_number))

    conn.commit()
    conn.close()

    return True


#create account for admin function
def create_account(account_number, pin, balance):
    conn = get_connection()
    cursor = conn.cursor()

    # insert into users table
    cursor.execute(
        "INSERT INTO users (account_number, pin, role) VALUES (%s, %s, 'customer')",
        (account_number, pin)
    )

    # insert into accounts table
    cursor.execute(
        "INSERT INTO accounts (account_number, balance) VALUES (%s, %s)",
        (account_number, balance)
    )

    conn.commit()
    conn.close()

    return True


#delete account for admin function
def delete_account(account_number):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE account_number=%s", (account_number,))
    cursor.execute("DELETE FROM accounts WHERE account_number=%s", (account_number,))

    conn.commit()
    conn.close()

    return True


#modify account for admin function
def modify_pin(account_number, new_pin):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET pin=%s WHERE account_number=%s",
        (new_pin, account_number)
    )

    conn.commit()
    conn.close()

    return True