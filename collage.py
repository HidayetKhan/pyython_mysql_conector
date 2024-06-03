import mysql.connector 

#conn=mysql.connector.connect(host='localhost',username='root',password='Hidaya@2001',database='collage')
class DPCONECT:
    def __init__(self):
       self.conn=mysql.connector.connect(host='localhost',username='root',password='root123',database='col1')
       query='create table if not exists example(user_id int primary key,start int ,end int,collage_name varchar(200))'
       c=self.conn.cursor()
       c.execute(query)



    def insert_data(self,id,start,end,name):
       query="insert into example(user_id,start,end,collage_name)values({},{} ,{},'{}')".format(id,start,end,name)
       c=self.conn.cursor()
       c.execute(query)
       self.conn.commit()



    def read_data(self):   
       query="select * from example"
       c=self.conn.cursor()
       c.execute(query)
       for i in c:
          print('user_id',i[0])
          print('start',i[1])
          print('end',i[2])
          print('name',i[3])
          print()

    def update_data(self,user_id,new_start,new_end,collage_name):
       query="update example set start={},end={},collage_name={} where user_id={}".format(new_start,new_end,collage_name,user_id)
       c=self.conn.cursor()
       c.execute(query)
       self.conn.commit()
       print('your desired data is updated')


    def delete_data(self,user_id):
       query="delete from example where user_id={}".format(user_id)
       c=self.conn.cursor()
       c.execute(query)
       self.conn.commit()
       print('your desire data is deleted')

   
    def check_marks_data(self,marks):
       query="select collage_name from example where{}between start and end ".format(marks)
       c=self.conn.cursor()
       c.execute(query)
       for i in c:
          print(i[0])

obj1=DPCONECT()
#obj1.insert_data(3,300,400,'aims collage')
#obj1.delete_data(2)
#obj1.update_data(3,200,300,'bhawans')
obj1.read_data()
