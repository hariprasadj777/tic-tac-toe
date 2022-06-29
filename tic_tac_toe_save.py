import psycopg2
conn=psycopg2.connect(host='localhost',dbname='postgres',user='postgres',password='postgres',port=5432)
cur=conn.cursor()
result = None
position = {}
for i in range(10):
    position[i]=" "
position[0]=1
def load():
    cur.execute('select * from tictactoe')
    a=cur.fetchall()
    ld_val=a[0]
    for i in range(1,10):
        if ld_val[i] == 'null':
            position[i]=" "
        else:
            position[i]=ld_val[i]
    print(position[1]+"|"+position[2]+"|"+position[3])
    print(position[4]+"|"+position[5]+"|"+position[6])
    print(position[7]+"|"+position[8]+"|"+position[9])
def body(val):
    global result
    if position[1] == position[2] == position[3] == val:
        if val == "x":
            result = 1
        elif val == "o":
            result =0
    elif position[4] == position[5] == position[6] == val:
        if val == "x":
            result =1
        elif val == "o":
            result =0
    elif position[7] == position[8] == position[9] == val:
        if val == "x":
            result =1
        elif val == "o":
            result =0
    elif position[1] == position[4] == position[7] == val:
        if val == "x":
            result =1
        elif val == "o":
            result =0
    elif position[2] == position[5] ==position[8] == val:
        if val == "x":
            result =1
        elif val == "o":
            result =0
    elif position[3] == position[6] ==position[9] == val:
        if val == x:
            result =1
        elif val == o:
            result =0
    elif position[1] == position[5] ==position[9] == val:
        if val == "x":
            result =1
        elif val == "o":
            result =0
    elif position[3] == position[5] ==position[7] == val:
        if val == "x":
            result =1
        elif val == "o":
            result =0
    print(position[1]+"|"+position[2]+"|"+position[3])
    print(position[4]+"|"+position[5]+"|"+position[6])
    print(position[7]+"|"+position[8]+"|"+position[9])
def close():
    val=[]
    for i in range (10):
        if position[i]==" ":
             val.append("null")
        else:
            val.append(position[i])
    upd_val='''truncate tictactoe;
                insert into tictactoe
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
    ins_val=val
    cur.execute(upd_val,ins_val)
    conn.commit()
def chk():
    global result
    for i in range (1,10):
        if position[i]==" ":
            break
        elif i==9:
            result=3
ld=input("Do you want to load the game \n Type Y/N:")
if ld=="Y":
    load()
print("Type the number to enter X or O in respective position")
print("1|2|3")
print("4|5|6")
print("7|8|9")
for i in range(5):
    chk()
    if result==3:
        break
    pos = input("To save and exit type CLOSE \n Enter the position of X =")
    if pos == "CLOSE":
        close()
        break
    else:
        position[int(pos)] = "x"
        body("x")
    if result == 1 or result==3:
        break
    else:
        chk()
        if result==3:
            break
        pos = input("To save and exit type CLOSE \n Enter the position of O =")
        if pos == "CLOSE":
            close()
            break
        else:
            position[int(pos)] = "o"
            body("o")
        if result == 0 or result ==3:
            break

if result == 1:
    print("X is the winner")
elif result == 0:
    print("O is the winner")
elif result == 3:
    print("Draw")
conn.close()