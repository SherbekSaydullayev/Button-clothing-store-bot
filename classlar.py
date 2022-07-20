import sqlite3
class Sql:
	def __init__(self):
		self.conn = sqlite3.connect("baza.db")
		self.c = self.conn.cursor()
	def baza_create(self):
		self.c.execute(""" CREATE TABLE IF NOT EXISTS info(
			id integer,
			username varchar(60),
			firt_name varchar(60),
			tel integer NULL,
			kor1 bigint NULL,
			kor2 bigint NULL
			) """)

	def user_add(self,idi,username,firt_name):
		self.c.execute("INSERT INTO info VALUES({}, '{}', '{}',NULL, NULL, NULL)".format(idi,username,firt_name))
		return self.conn.commit()


	def id_user(self,idi):
		self.c.execute(f"SELECT id FROM info WHERE id = {idi}")
		data = self.c.fetchone()
		return data

####### Kontact funksiya
	def contact_update(self,idi,raqam):
		self.c.execute(f"UPDATE info SET tel = {raqam} WHERE id = {idi}")
		return self.conn.commit()
		
	def location_update(self,idi,kor1,kor2):
		self.c.execute(f"UPDATE info SET kor1 = {kor1}, kor2 = {kor2} WHERE id = {idi}")
		return self.conn.commit()