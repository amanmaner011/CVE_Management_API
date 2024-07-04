import csv
import sqlite3

def import_csv_to_sqlite(csv_file, db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cves (
        cve_id TEXT PRIMARY KEY,
        severity TEXT,
        cvss TEXT,
        affected_packages TEXT,
        description TEXT,
        cwe_id TEXT
    )
    ''')

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute('''
            INSERT INTO cves (cve_id, severity, cvss, affected_packages, description, cwe_id)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (row['CVE-ID'], row['Severity'], row['CVSS'], row['Affected Packages'], row['Description'], row['CWE-ID']))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    import_csv_to_sqlite('cve_database.csv', 'cves.db')
