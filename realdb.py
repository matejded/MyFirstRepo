import pyodbc

# V tomto kódu je důležité nahradit:
# your_server_name názvem nebo IP adresou vašeho SQL serveru,
# your_database_name názvem vaší databáze,
# your_username vaším uživatelským jménem pro přístup k databázi,
# your_password vaším heslem.
# Také se ujistěte, že máte nainstalovaný odpovídající ODBC driver, například "ODBC Driver 17 for SQL Server", který je v příkladu uveden.



# Parametry připojení
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Vytvoření připojení k MSSQL
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'UID=' + username + ';'
                      'PWD=' + password)

# Vytvoření kurzoru
c = conn.cursor()

# Provedení SQL dotazu
c.execute("SELECT * FROM studenti")

# Výpis výsledků dotazu
rows = c.fetchall()
for row in rows:
    print(row)

# Uzavření spojení s databází
conn.close()