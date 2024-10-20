import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host': 'tech0-gen-7-step4-studentwebapp-test.mysql.database.azure.com',
  'user': 'tech0gen7student',
  'password': 'F4XyhpicGw6P',  # 実際のパスワードに置き換えてください
  'database': 'legotest',  # 実際のデータベース名に置き換えてください
  'client_flags': [mysql.connector.ClientFlag.SSL],
  'ssl_ca': '/Users/takuya/Downloads/AzureMySQL_Connection/DigiCertGlobalRootCA.crt.pem'  # 実際の証明書パスに置き換えてください
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Drop previous users table if one exists
  cursor.execute("DROP TABLE IF EXISTS users;")
  print("Finished dropping table (if existed).")

  # Create users table with username and password columns
  cursor.execute("""
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      username VARCHAR(50) NOT NULL,
      password VARCHAR(50) NOT NULL
  );
  """)
  print("Finished creating users table.")

  # Insert data from the users dictionary
  users = {
      'yagimasa': 'password123',
      'lego': 'password456'
  }

  for username, password in users.items():
      cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s);", (username, password))
      print(f"Inserted user: {username}")

  # Commit the transaction
  conn.commit()

  # Cleanup
  cursor.close()
  conn.close()
  print("Done.")
