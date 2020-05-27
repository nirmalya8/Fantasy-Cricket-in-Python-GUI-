import sqlite3
s= sqlite3.connect('DATA.db')
c = s.cursor()
#adding data to database tables

c.execute(''' CREATE TABLE STATT (
    Player TEXT(30) PRIMARY KEY,  
    Matches INTEGER,
    Runs INTEGER,
    Hundreds INTEGER,
    Fifties INTEGER,
    Price INTEGER,
    Type TEXT); ''')
try :
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('VIRAT KOHLI', 189,8257,28,43,120,'BAT');")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('YUVRAJ SINGH', 86,3589,54,21, 100, 'AR');")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('AJINKYA RAHANE', 158,5435,11,31, 100, 'BAT'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('SHIKHAR DHAWAN', 25,565,2,1, 75, 'BAT'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('MS DHONI', 178,6573,9,29, 90, 'WK'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('AXAR PATEL', 67,208,0,0, 85, 'BOW'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('HARDIK PANDYA', 60 ,790,1,4, 75, 'AR'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('RAVINDRA JADEJA',65 ,1090,0,4, 85, 'AR'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('KEDAR JADAV', 111 ,795,0,4, 90, 'BAT'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('RAVI ASHWIN', 152 ,600,0,5, 100, 'BOW');")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('ROHIT SHARMA', 120 ,5080,12,30, 110, 'BAT'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('RISHABH PANT', 40 ,890,1,6, 90, 'WK'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('JASPRIT BUMRAH', 90 ,200,0,0, 110, 'BOW'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('Md. SHAMI', 80 ,170,0,0, 90, 'BOW'  );")
    c.execute("INSERT INTO STATT (Player, Matches, Runs, Hundreds, Fifties, Price, Type ) VALUES ('BHUVNESHWAR KUMAR', 100 ,304,0,2, 100, 'BOW'  );")
except :
        print("Unexpected Error")
        c.rollback();

c.execute('''CREATE TABLE MATCHDATA(p TEXT NOT NULL,
r INTEGER,
b INTEGER,
f INTEGER,
s INTEGER,
bow INTEGER,
m INTEGER,
rc INTEGER,
w INTEGER,
c INTEGER,
st INTEGER,
ro INTEGER);
''')
try :
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s, bow,m,rc,w,c,st,ro) VALUES ('VIRAT KOHLI', 120,81, 10,5, 0,0,0,0,2,0,0 );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('YUVRAJ SINGH',32,20, 5,1, 5,0,24,1,1,0,0);")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('AJINKYA RAHANE',40,43, 3,1, 0,0,0,0,1,0,0 );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('SHIKHAR DHAWAN', 72,51, 10,5, 0,0,0,0,2,0,0 );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('MS DHONI', 30,15, 2,3, 0,0,0,0,0,2,0 );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('AXAR PATEL', 2,4, 0,0, 7,2,20,3,0,0,1  );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('HARDIK PANDYA', 55,22, 8,2, 6,0,33,1,1,0,0 );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('RAVINDRA JADEJA',  21,7, 5,0, 8,1,40,2,0,0,1  );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('KEDAR JADAV', 42,30, 4,3, 0,0,0,0,0,0,0 );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('RAVI ASHWIN',0,0, 0,0, 10,0,38,5,0,0,1);")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('ROHIT SHARMA' , 110,90, 8,6, 0,0,0,0,1,0,0 )  ;")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('RISHABH PANT', 40,25, 4,2, 0,0,0,0,0,2,1  );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('JASPRIT BUMRAH', 0,0, 0,0, 10,2,32,2,0,0,0  );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('Md. SHAMI', 0,0, 0,0, 10,0,48,4,0,0,0  );")
    c.execute("INSERT INTO MATCHDATA (p,r,b,f,s,bow,m,rc,w,c,st,ro) VALUES ('BHUVNESHWAR KUMAR', 0,0, 0,0, 10,3,44,3,0,0,0 );")
except :
        print("Unexpected Error")
        c.rollback();
c.execute('''
CREATE TABLE TEAM (name TEXT NOT NULL,
players TEXT NOT NULL,
value INTEGER);
''')
s.commit()
