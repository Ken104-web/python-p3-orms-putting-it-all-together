import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
    all = []

    def __init__(self, name, breed):
        self.id = None 
        self.name = name
        self.breed = breed

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS dogs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """ 
            DROP TABLE IF EXISTS dogs
        
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.breed))
        CONN.commit() 
    
    @classmethod
    def create(cls, name, breed):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (name, breed))
        CONN.commit()

        new_id = CURSOR.lastrowid

        new_dog = cls(name=name, breed=breed)
        new_dog.id = new_id
        return new_dog
    
    @classmethod
    def new_from_db(cls, row):
        # new_id = CURSOR.lastrowid

        new_row = cls(name=row[1], breed=row[2])
        new_row.id = row[0]
        # print(new_row
        return new_row
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM dogs
        """       
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()

        # print ([list(row) for row in rows])
        # return ([list(row) for row in rows])
        # print ([(cls.new_from_db(row)).id for row in rows])
        # return ([cls.new_from_db(row) for row in rows])
        # real_dogs = []
        # for row in rows:
        #     real_dogs.append(cls.new_from_db(row))

        # print([f'{dog.id}, {dog.name}'for dog in real_dogs])
        # return real_dogs


        dogs = [cls.new_from_db(row) for row in rows]
        return dogs
    
    


    



    