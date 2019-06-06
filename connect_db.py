import pyodbc
import csv

class SQL_Connect:

    def __init__(self, server='localhost,1433', database='IMDB', username='SA', password='Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.docker_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+'')
        self.cursor = self.docker_conn.cursor()

    def query(self, sql_query):
        self.cursor.execute(sql_query)

    def create_table(self, table_name):
        self.query(f"CREATE TABLE [{table_name}] (TitleType VARCHAR(40), PrimaryTitle VARCHAR(100), "
                          f"OriginalTitle VARCHAR(100), IsAdult INT, StartYear INT, EndYear INT, "
                          f"RuntimeMinutes INT, Genres VARCHAR(100))")
        self.docker_conn.commit()


    def pull_imdb_data(self, csv_full_name):
        imdb_data = []
        with open(csv_full_name, newline='') as csv_file:
            imdb_csv = csv.reader(csv_file, delimiter=',')

            for row in imdb_csv:
                individual_row = []
                individual_row.append(row[0])
                individual_row.append(row[1])
                individual_row.append(row[2])
                individual_row.append(row[3])
                if 'N' in row[4]:
                    individual_row.append(0)
                else:
                    individual_row.append(row[4])

                if 'N' in row[5]:
                    individual_row.append(0)
                else:
                    individual_row.append(row[5])

                if 'N' in row[6]:
                    individual_row.append(0)
                else:
                    individual_row.append(row[6])
                individual_row.append(row[7])
                imdb_data.append(individual_row)

        # for row in imdb_data:
        #     print(row)
        for item in imdb_data[1:]:
            self.query(f"INSERT INTO Movies VALUES ('{item[0]}', '{item[1]}', '{item[2]}', '{item[3]}', '{item[4]}', '{item[5]}', '{item[6]}', '{item[7]}')")

        self.docker_conn.commit()
