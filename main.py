from flet import *
import sqlite3

conn=sqlite3.connect("data.db",check_same_thread=False)
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS student(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            stdname Text,
            stdmail Text,
            stdphone Text,
            stdaddress Text,
            math INTEGER,
            arabic INTEGER,
            france INTEGER,
            english INTEGER,
            draw INTEGER,
            physics INTEGER
                )""")
conn.commit()




def main (page: Page):
    page.title='ABDOU'
    page.scroll='auto'
    page.window.top=1
    page.window.left=960
    page.window.width=390
    page.window.height=740
    page.bgcolor='white'
    page.theme_mode=ThemeMode.LIGHT

    
    ##### DATABASE #####
    table_name='student'
    query=f'SELECT COUNT (*) FROM {table_name}'
    cursor.execute(query)
    result=cursor.fetchone()
    row_count=result[0]

    def add(e):
        cursor.execute("INSERT INTO student (stdname,stdmail,stdphone,stdaddress,math,arabic,france,english,draw,physics) VALUES (?,?,?,?,?,?,?,?,?,?)",(tname.value,tmail.value,tphone.value,taddress.value,math.value,arabic.value,france.value,english.value,draw.value,physics.value))
        conn.commit()
    def show(e):
        c=conn.cursor()
        c.execute("SELECT * FROM student")
        users=c.fetchall()
        print(users)

        if not users == "":
            keys=['id','stdname','stdmail','stdphone','stdaddress','math','arabic','france','english','draw','physics']
            result=[dict(zip(keys,values))for values in users]
            for x in result:
                page.add(
                    Card(
                    color='black',
                    content=Container(
                        content=Column([
                           ListTile(
                               leading=Icon(icons.PERSON,color='blue'),
                               title=Text(x['stdname'],color='white'),
                               subtitle=Text('Mail : '+x['stdmail'],color='red')
                           ),
                           Row([
                               Text('Phone : '+x['stdphone'],color='green'),
                               Text('Address : '+x['stdaddress'],color='green')
                           ],alignment=MainAxisAlignment.START),
                           Row([
                               Text('Math : '+ str(x['math']),color='amber'),
                               Text('Arabic : '+ str(x['arabic']),color='amber'),
                               Text('Francais : '+ str(x['france']),color='amber'),
                           ],alignment=MainAxisAlignment.END),
                           Row([
                               Text('English : '+ str(x['english']),color='amber'),
                               Text('Draw : '+ str(x['draw']),color='amber'),
                               Text('Physics : '+ str(x['physics']),color='amber'),
                           ],alignment=MainAxisAlignment.END),
                        ])
                    )
                )
                
            )
    ##################

    ##### Fileds #####
    tname=TextField(label='Fullname',icon=icons.PERSON,height=38)
    tmail=TextField(label='Mail',icon=icons.MAIL,height=38)
    tphone=TextField(label='Phone',icon=icons.PHONE,height=38)
    taddress=TextField(label='Address',icon=icons.MAP,height=38)
    ##################

    ##### marks #####
    marktxt=Text("Marks Students",text_align='center',weight='bold')
    math=TextField(label='Math',width=110,height=38)
    arabic=TextField(label='Arabic',width=110,height=38)
    france=TextField(label='France',width=110,height=38)
    english=TextField(label='English',width=110,height=38)
    draw=TextField(label='Draw',width=110,height=38)
    physics=TextField(label='Physics',width=110,height=38)
    ##################

     ##### Buttons #####
    addbtn=ElevatedButton(
        "Add new Student",width=170,
        style=ButtonStyle(bgcolor='blue',color='black',padding=15),
        on_click=add
    )
    showbtn=ElevatedButton(
        "Show all Students",width=170,
        style=ButtonStyle(bgcolor='blue',color='black',padding=15),
        on_click=show
    )



    page.add(
        Row([
            Image(src="home.gif",width=300)
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text("Student App",size=35,font_family="ALGERIAN")
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            Text("Nbr of students :",size=15,font_family="ALGERIAN",color='grey'),
            Text(row_count,size=15,font_family="ALGERIAN",color='blue')
        ],alignment=MainAxisAlignment.CENTER,height=20),
        tname,tmail,tphone,taddress,

        Row([
            marktxt,
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            math,arabic,france
        ],alignment=MainAxisAlignment.CENTER),

        Row([
            english,draw,physics
        ],alignment=MainAxisAlignment.CENTER),
    
        Row([
            showbtn,addbtn
        ],alignment=MainAxisAlignment.CENTER),
    
    )





    page.update()
app(main)
