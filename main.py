from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, 
    QGroupBox, QLabel, QLineEdit, 
    QPushButton, QHBoxLayout,QRadioButton,QTabWidget,QScrollArea,QGridLayout,QMessageBox,QTableWidget,QTableWidgetItem)
from PyQt5.QtGui import (QPixmap,QFont,QIcon)
from PyQt5.QtCore import Qt,QSize
import json
from random import randint
import datetime
#import psycopg2 as ps
import sqlite3
from qtwidgets import PasswordEdit
user_login=''


def test_key(user_login):
    prokrutka=-1
    db=sqlite3.connect('base.db')
    cur=db.cursor()
    for value in cur.execute(f"SELECT key FROM user WHERE Login ='{user_login}'"):

        if value[0]==0:
            prokrutka=3

        elif value[0]!=0:
            prokrutka=0

    db.close()
    return prokrutka

class AuthWindow(QWidget):
    
    def __init__(self):

        super().__init__()
        self.prokrutka=-1
        self.window2=None
        self.init_ui()

    def init_ui(self):
        
        self.setWindowTitle('Умная столовая')
        self.setGeometry(100, 100, 400, 200)
        self.setStyleSheet("""background-color:#FFCCCC;""") 

        self.win = QVBoxLayout()

        self.main_groupbox = QGroupBox("Авторизация/Регистрация")

        self.login_fbutton = QPushButton('Войти')
        self.register_fbutton = QPushButton('Зарегистрироваться')
        self.login_fbutton.setStyleSheet("""
            height: 25px;
            background: lightblue;
            margin-left: 10px;
            margin-right: 5px""")
        self.register_fbutton.setStyleSheet("""
            height: 25px;
            background: lightblue;
            margin-left: 10px;
            margin-right: 5px""")



        self.login_fbutton.clicked.connect(self.show_login_form)
        self.register_fbutton.clicked.connect(self.show_register_form)
        self.First_name=QLineEdit()
        self.last_name=QLineEdit()
        self.loginUser=QLineEdit()
        self.password=PasswordEdit()
        self.class_number=QLineEdit()
        self.radioPlat=QRadioButton('Платник')
        self.radioBespl=QRadioButton('Бесплатник')


        self.enter_login=QLineEdit()
        self.enter_password=PasswordEdit()

        self.pitanie=''    


        self.main_line = QVBoxLayout()
        self.main_line.addWidget(self.login_fbutton)
        self.main_line.addWidget(self.register_fbutton)

        self.main_groupbox.setLayout(self.main_line)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.addWidget(self.main_groupbox)
        self.setLayout(self.main_layout)

        self.login_groupbox = self.create_groupbox("Авторизация", [
            QLabel('Логин:'),
            QLabel('Пароль:'), 
        ],QPushButton('Назад'),QPushButton('Войти'),self.enter_login,self.enter_password)

        self.register_groupbox = self.create_groupbox_regest("Регистрация", [
            QLabel('Фамилия:'),
            QLabel('Имя:'),
            QLabel('Логин:'),
            QLabel('Пароль:'),
            QLabel('Класс:'),
        ], QPushButton('Назад'),QPushButton('Зарегистрироваться'),self.radioBespl,self.radioPlat,self.First_name,self.last_name,self.loginUser,self.password,self.class_number)

        self.login_groupbox.hide()
        self.register_groupbox.hide()

    def create_groupbox(self, title, widgets, button,button2,login,password):
        groupbox = QGroupBox(title)
        layout = QVBoxLayout(groupbox)
        k=0
        for widget in widgets:
            k+=1
            layout.addWidget(widget)
            if k==1:
                layout.addWidget(login)
            elif k==2:
                layout.addWidget(password)
    

    
        layout.addWidget(button)
        layout.addWidget(button2)
        button.clicked.connect(self.goto_main)
        button2.clicked.connect(self.login)
        return groupbox
    
    def create_groupbox_regest(self, title, widgets, button,button2,radioBut1,radioBut2,First_name,last_name,login,password,class_number):
        groupbox = QGroupBox(title)
        layout = QVBoxLayout(groupbox)
        k=0
        for widget in widgets:
            k+=1
            layout.addWidget(widget)
            if k==1:
                layout.addWidget(First_name)
            elif k==2:
                layout.addWidget(last_name)
            elif k==3:
                layout.addWidget(login)
            elif k==4:
                layout.addWidget(password)
            elif k==5:
                layout.addWidget(class_number)
        
        layout.addWidget(radioBut1)
        layout.addWidget(radioBut2)
        layout.addWidget(button)
        layout.addWidget(button2)
        


        button.clicked.connect(self.goto_main)
        button2.clicked.connect(self.register)



        return groupbox
    

    def Plat(self):
        self.pitanie='platnoe'



    def Besplat(self):
        self.pitanie='besplat'


    
    def show_login_form(self):
        self.main_groupbox.hide()
        self.login_groupbox.show()

    def show_register_form(self):
        self.radioPlat.clicked.connect(self.Plat)
        self.radioBespl.clicked.connect(self.Besplat)
        self.main_groupbox.hide()
        self.register_groupbox.show()



    def goto_main(self):
        self.login_groupbox.hide()
        self.register_groupbox.hide()
        self.main_groupbox.show()


    def error_enter(self):
        box=QMessageBox()
        box.setText('Неверный логин или пароль')
        box.exec_()





    def login(self):
        global user_login
        user_login=self.enter_login.text()
        user_password=self.enter_password.text()
        
        if  user_login=='' or user_password=='' :
            self.show_error()
        
        else:
            db=sqlite3.connect('base.db')
            cur=db.cursor()
            for value in cur.execute(f"SELECT Login,Password FROM user WHERE Login='{user_login}'"):
                if  self.enter_password.text() == value[1]:
                    self.prokrutka=test_key(user_login)
                    self.window2=MainWin(images)
                    self.window2.prokrutka=self.prokrutka
                    window.hide()

                    self.login_groupbox.hide()
                    self.register_groupbox.hide()
                    db=sqlite3.connect('base.db')
                    cur=db.cursor()
                    window.hide()
                        
                    self.window2.show()
                else:
                    self.error_enter()





            cur.execute(f"SELECT Login,Password,key FROM user WHERE Login='{user_login}'")
            
            db.close()

        




    def show_error(self):
        box=QMessageBox()
        box.setText('Введенны неверные данные')
        box.exec_()


    def register(self):
        global user_login
        key=randint(123,214254)
        if key not in keys:
            key=randint(123,214254)
        else:
            key=randint(124124,214254124)
        user_key=key
        key2=randint(2134,125156)

        keys.append(key)
        user_pitanie=self.pitanie
        user_key2=key2
        user_first_name=self.First_name.text()
        user_last_name = self.last_name.text()
        user_login=self.loginUser.text()
        user_password=self.password.text()
        user_class_number=self.class_number.text()

        if user_first_name=='' or user_last_name=='' or user_login=='' or user_password=='' or user_class_number=='':
            self.show_error()

        else:
            db=sqlite3.connect('base.db')
            cur=db.cursor()
            cur.execute(f"SELECT Login FROM user WHERE Login='{user_login}'")
            if cur.fetchone() is None:
                cur.execute(f"INSERT INTO user VALUES (?,?,?,?,?,?,?,?)",(user_first_name,user_last_name,user_login,user_password,user_class_number,user_pitanie,user_key,user_key2))
                db.commit()
                cur.execute("SELECT * FROM user")
                db=sqlite3.connect('base.db')
                cur=db.cursor()
                db.close()
                self.prokrutka=test_key(user_login)
                self.window2=MainWin(images)
                self.window2.prokrutka=self.prokrutka
                self.login_groupbox.hide()
                self.register_groupbox.hide()
                window.hide()
                self.window2.show()

            else:
                message=QMessageBox()
                message.setText('Логин занят')
                message.exec_()
            db.close()
        
      

            




class MainWin(QWidget):
    def __init__(self,images):
        self.images = images
        super().__init__()
        self.prokrutka=window.prokrutka
        self.init_ui()   
        

    def init_ui(self):
        
        db=sqlite3.connect('base.db')
        cur=db.cursor()


        self.voit=0
        if self.prokrutka == 0 and len(images)>0:
            db=sqlite3.connect('base.db')
            cur=db.cursor()
            for value in cur.execute(f"SELECT Food_voites FROM food WHERE food_name='{spisok[1]}'"):
                self.voit=value[0]
        
        cur.execute('SELECT Login FROM user')
        print(cur.fetchall())
        db.close()


        self.setWindowTitle('Умная столовая')
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("""background-color: #bdccccff;""") 

        self.butAdm=QPushButton('Админ')
        self.butPit=QPushButton('Я питаюсь!')
        self.butBack=QPushButton("Назад")
        self.but_like=QPushButton('Лайк')
        self.butList=QPushButton('Списки')
        self.but_dislike=QPushButton('Дизлайк')
        self.but_Results=QPushButton('Итоги')

        
        self.voites=QLabel('Количество голосов:'+ str(self.voit))
        self.voites.setFont(QFont("Arial",20)) 

        self.text=QLabel('Выбери блюдо на '+self.SetTime())
        self.text.setFont(QFont("Arial",15))

        if len(images)>0:
            self.label=QLabel()
            self.label.setBaseSize(400,400)
            self.label.setPixmap(im)
            self.but_like.show()
            self.but_dislike.show()
        elif len(images)==0:
            self.label=QLabel('Зайдите позже,администратор еще не добавил блюда')
            self.label.setFont(QFont("Arial",30))
            self.but_like.hide()
            self.but_dislike.hide()


        self.butPit.setMinimumSize(65,45)
        self.but_like.setMinimumSize(95,55)
        self.but_dislike.setMinimumSize(95,55)
        self.butList.setMinimumSize(85,45)
        self.butBack.setMinimumSize(85,45)

        self.but_like.setStyleSheet("""
            background-color: lightgreen;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;""")
        self.but_dislike.setStyleSheet("""
            background-color: red;
            border-style: outset;
            border-width: 2px;
            border-radius: 10px;
            border-color: beige;
            font: bold 14px;
            min-width: 10em;
            padding: 6px;""")
        self.butBack.setStyleSheet( """
            width: 130px;
            height: 40px;
            color: #fff;
            border-radius: 5px;
            padding: 10px 25px;
            font-family: 'Lato', sans-serif;
            font-weight: 500;
            background: rgb(50, 103, 184);"""
                                        )
        self.voites.setStyleSheet("""
            background: gray;
            border: 1px inset gray;
            position: absolute;
            top: 1px;
            right: 1px;
            bottom: 1px;
            left: 1px


        """)



        self.main_layout=QVBoxLayout()

        self.first_layout=QHBoxLayout()
        self.second_layout=QHBoxLayout()
        self.third_layout=QHBoxLayout()
        self.fourth_layout=QHBoxLayout()
        self.five_layout=QHBoxLayout()
        if user_login!='admin':
            self.butAdm.hide()
            self.unvisText=QLabel(' ')
            self.unvisText.setFont(QFont("Arial",1))
            self.unvisText.setStyleSheet("background-color: #bdccccff")
            self.first_layout.addWidget(self.unvisText,alignment=Qt.AlignmentFlag.AlignLeft)
        else:
            self.first_layout.addWidget(self.butAdm,alignment=Qt.AlignmentFlag.AlignLeft)


        self.first_layout.addWidget(self.text,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.first_layout.addWidget(self.butPit,alignment=Qt.AlignmentFlag.AlignRight)
        self.second_layout.addWidget(self.label,alignment=Qt.AlignmentFlag.AlignCenter)
        self.third_layout.addWidget(self.but_like,alignment=Qt.AlignmentFlag.AlignCenter)
        self.third_layout.addWidget(self.but_dislike,alignment=Qt.AlignmentFlag.AlignCenter)
        self.fourth_layout.addWidget(self.voites,alignment=Qt.AlignmentFlag.AlignLeft)
        self.fourth_layout.addWidget(self.butList,alignment=Qt.AlignmentFlag.AlignRight)
        self.five_layout.addWidget(self.but_Results,alignment=Qt.AlignmentFlag.AlignRight)
    

        self.main_layout.addLayout(self.first_layout)
        self.main_layout.addLayout(self.second_layout)
        self.main_layout.addLayout(self.third_layout)
        self.main_layout.addLayout(self.fourth_layout)
        self.main_layout.addLayout(self.five_layout)
        self.main_layout.addWidget(self.butBack,alignment=Qt.AlignmentFlag.AlignRight)
        
        self.setLayout(self.main_layout)



        self.butPit.clicked.connect(self.Pitanie)
        self.but_like.clicked.connect(self.Like)
        self.but_dislike.clicked.connect(self.Dilike)
        self.butBack.clicked.connect(self.go_toregest)
        self.butAdm.clicked.connect(self.go_to_adminWin)
        self.butList.clicked.connect(self.go_to_list)
        self.but_Results.clicked.connect(self.go_to_Results)
        if self.prokrutka==3:
            self.finish_voit()

            


    def Pitanie(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        #cur.execute(f"""UPDATE user SET key = 0 where Login = '{user_login_now["Login"]}'""")
        #cur.execute(f"SELECT key FROM user WHERE Login = '{user_login_now['Login']}'")
        cur.execute("SELECT Login FROM user_eat")
        users = cur.fetchall()


        users_data = []
        
        for userr in users:
            userr=userr[0]

            besplat_count = userr
            

            users_data.append((besplat_count))

        if user_login in users_data:
            Message=QMessageBox()
            Message.setText('Ты уже отметился')
            Message.exec_()
        else:
            cur.execute("INSERT INTO user_eat VAlUES (?,?)",(user_login,1))
        db.commit()
        db.close()
            

    def go_to_Results(self):
        window.window2.hide()
        window5.show()



    def SetTime(self):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=2)
        tomorrow.strftime("%d %B, %Y")
        if tomorrow.strftime('%A')=='Saturday':
            tomorrow+=datetime.timedelta(days=2)
            day='Суббота'
        elif tomorrow.strftime('%A')=='Sunday':
            tomorrow+=datetime.timedelta(days=1)
            day='Воскресенье'
        elif tomorrow.strftime('%A')=='Monday':
            day='Понедельник'
        elif tomorrow.strftime('%A')=='Tuesday':
            day='Вторник'
        elif tomorrow.strftime('%A')=='Wensday':
            day='Среда'
        elif tomorrow.strftime('%A')=='Thursday':
            day='Четверг'
        elif tomorrow.strftime('%A')=='Friday':
            day='Пятница'
        if tomorrow.strftime('%B')=='September':
            mouth='Сентября'
        elif tomorrow.strftime('%B')=='Octember':
            mouth='Октября'
        elif tomorrow.strftime('%B')=='November':
            mouth='Ноября'
        elif tomorrow.strftime('%B')=='December':
            mouth='Декабря'
        elif tomorrow.strftime('%B')=='January':
            mouth='Января'
        elif tomorrow.strftime('%B')=='February':
            mouth='Февраля'
        elif tomorrow.strftime('%B')=='March':
            mouth='Марта'
        elif tomorrow.strftime('%B')=='April':
            mouth='Апреля'
        elif tomorrow.strftime('%B')=='May':
            mouth='Мая'
        elif tomorrow.strftime('%B')=='June':
            mouth='Июня'
        elif tomorrow.strftime('%B')=='July':
            mouth='Июля'
        elif tomorrow.strftime('%B')=='August':
            mouth='Августа'
        time=tomorrow.strftime(f"%d {mouth},{day}")
        return time

    def Like(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        window.prokrutka+=1
        if window.prokrutka==1:
            for value in cur.execute(f"SELECT Food_voites FROM food WHERE food_name='{spisok[3]}'"):
                self.voit=value[0]
    
            cur.execute(f"""Update food set Food_voites = Food_voites+1 where food_name = '{spisok[1]}'""")
            db.commit()

            db.commit()
            im=images[1]
            self.label.setPixmap(im)
            self.voites.setText('Количество голосов:'+ str(self.voit))

        elif window.prokrutka==2:
            for value in cur.execute(f"SELECT Food_voites FROM food WHERE food_name='{spisok[5]}'"):
                self.voit=value[0]
    
            cur.execute(f"""Update food set Food_voites = Food_voites+1 where food_name = '{spisok[3]}'""")
            db.commit()

            im=images[2]
            self.label.setPixmap(im)
            self.voites.setText('Количество голосов:'+ str(self.voit))


        elif window.prokrutka==3:
            cur.execute(f"""Update food set Food_voites = Food_voites+1 where food_name = '{spisok[5]}'""")
            db.commit()
            self.finish_voit()

        db.close()

    def finish_voit(self):
            db=sqlite3.connect('base.db')
            cur=db.cursor()
            cur.execute(f"UPDATE user SET key=0 WHERE Login = '{user_login}'")
            db.commit()
            cur.execute(f"SELECT key FROM user WHERE Login = '{user_login}'")
            
            db.close()
            self.label.hide()
            self.voites.hide()
            self.but_dislike.hide()
            self.but_like.hide()
            self.label=QLabel('Спасибо за голос')
            self.label.setFont(QFont("Arial",35))
            self.second_layout.addWidget(self.label,alignment=Qt.AlignmentFlag.AlignCenter)




    def Dilike(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        window.prokrutka+=1
        if window.prokrutka==1:
            for value in cur.execute(f"SELECT Food_voites FROM food WHERE food_name='{spisok[3]}'"):
                self.voit=value[0]
    
            cur.execute(f"""Update food set Food_voites = Food_voites-1 where food_name = '{spisok[1]}'""")
            db.commit()
            im=images[1]
            self.label.setPixmap(im)
            self.voites.setText('Количество голосов:'+ str(self.voit))

        elif window.prokrutka==2:
            for value in cur.execute(f"SELECT Food_voites FROM food WHERE food_name='{spisok[5]}'"):
                self.voit=value[0]
    
            cur.execute(f"""Update food set Food_voites = Food_voites-1 where food_name = '{spisok[3]}'""")
            db.commit()
            im=images[2]
            self.label.setPixmap(im)
            self.voites.setText('Количество голосов:'+ str(self.voit))


        elif window.prokrutka==3:
            cur.execute(f"""Update food set Food_voites = Food_voites-1 where food_name = '{spisok[5]}'""")
            db.commit()
            self.finish_voit()
        db.close()

    def go_toregest(self):
        window.window2.close()
        window.show()
        window.main_groupbox.show()

    def go_to_list(self):
        window.window2.close()
        window4.show()
    
    def go_to_adminWin(self):
        window.window2.close()
        window.close()
        window3.show()



class AdminWin(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()


    def init_ui(self):

        self.setWindowTitle('Школьная Столовая')
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("""background-color: #bdccccff;""")

        self.Hlayout=QHBoxLayout()
        self.Hlayout2=QHBoxLayout()
        self.Hlayout3=QHBoxLayout()
        self.mainLayout=QVBoxLayout()

        self.text1=QLabel('Выберите 3 блюда для детей')
        self.text1.setFont(QFont("Arial",20))
        self.stroka=''
        self.but = QPushButton()
        self.but2 = QPushButton()
        self.but3=QPushButton()
        self.but4=QPushButton()
        self.but5=QPushButton()
        self.but6=QPushButton()
        self.but7=QPushButton()
        self.but8=QPushButton()
        self.but9=QPushButton()
        self.but10=QPushButton()


        self.but_ex=QPushButton('Выход')
        self.but_back=QPushButton('Назад')
        self.but.setIcon(QIcon('ImagesNPK/blini.jpg'))
        self.but.setIconSize(QSize(200,200))
        self.but2.setIcon(QIcon('ImagesNPK/borch.jpg'))
        self.but2.setIconSize(QSize(200,200))
        self.but3.setIcon(QIcon('ImagesNPK/grechka.jpg'))
        self.but3.setIconSize(QSize(200,200))
        self.but4.setIcon(QIcon('ImagesNPK/kasha.jpg'))
        self.but4.setIconSize(QSize(200,200))
        self.but5.setIcon(QIcon('ImagesNPK/kotletka_s_pureshkoy.jpg'))
        self.but5.setIconSize(QSize(200,200))

        self.but6.setIcon(QIcon('ImagesNPK/makaroni.jpg'))
        self.but6.setIconSize(QSize(200,200))
        self.but7.setIcon(QIcon('ImagesNPK/pelmeni.jpg'))
        self.but7.setIconSize(QSize(200,200))
        self.but8.setIcon(QIcon('ImagesNPK/perlovka.jpg'))
        self.but8.setIconSize(QSize(200,200))
        self.but9.setIcon(QIcon('ImagesNPK/sasuges.jpg'))
        self.but9.setIconSize(QSize(200,200))
        self.but10.setIcon(QIcon('ImagesNPK/zapikanka.jpg'))
        self.but10.setIconSize(QSize(200,200))

        
        self.Hlayout.addWidget(self.but,alignment=Qt.AlignmentFlag.AlignTop)
        self.Hlayout.addWidget(self.but2,alignment=Qt.AlignmentFlag.AlignTop)
        self.Hlayout.addWidget(self.but3,alignment=Qt.AlignmentFlag.AlignTop)
        self.Hlayout.addWidget(self.but4,alignment=Qt.AlignmentFlag.AlignTop)
        self.Hlayout.addWidget(self.but5,alignment=Qt.AlignmentFlag.AlignTop)
        self.Hlayout2.addWidget(self.but6,alignment=Qt.AlignmentFlag.AlignBottom)
        self.Hlayout2.addWidget(self.but7,alignment=Qt.AlignmentFlag.AlignBottom)
        self.Hlayout2.addWidget(self.but8,alignment=Qt.AlignmentFlag.AlignBottom)
        self.Hlayout2.addWidget(self.but9,alignment=Qt.AlignmentFlag.AlignBottom)
        self.Hlayout2.addWidget(self.but10,alignment=Qt.AlignmentFlag.AlignBottom)
        self.Hlayout3.addWidget(self.but_ex,alignment=Qt.AlignmentFlag.AlignLeft)
        self.Hlayout3.addWidget(self.text1,alignment=Qt.AlignmentFlag.AlignCenter)
        self.Hlayout3.addWidget(self.but_back,alignment=Qt.AlignmentFlag.AlignRight)
    

        self.mainLayout.addLayout(self.Hlayout)
        self.mainLayout.addLayout(self.Hlayout3)
        self.mainLayout.addLayout(self.Hlayout2)

        self.setLayout(self.mainLayout)
        
        self.but_back.clicked.connect(self.go_to_main)
        self.but_ex.clicked.connect(self.go_to_registration)

        self.but.clicked.connect(self.hide_b)
        self.but2.clicked.connect(self.hide_b2)
        self.but3.clicked.connect(self.hide_b3)
        self.but4.clicked.connect(self.hide_b4)
        self.but5.clicked.connect(self.hide_b5)
        self.but6.clicked.connect(self.hide_b6)
        self.but7.clicked.connect(self.hide_b7)
        self.but8.clicked.connect(self.hide_b8)
        self.but9.clicked.connect(self.hide_b9)
        self.but10.clicked.connect(self.hide_b10)
        
    def thanks_for_work(self):
            db=sqlite3.connect('base.db')
            cur=db.cursor()
            for i in range(len(admin_choose)):
                self.stroka+=admin_choose[i]+' '
            cur.execute(f"INSERT INTO admin VALUES (?)",(self.stroka,))
            db.commit()
            db.close()
            box=QMessageBox()
            box.setText("Спасибо за выбор заходите завтра")
            box.exec_()
            window.show()
            self.go_to_registration()
            window3.close()



    def go_to_main(self):
        window3.hide()
        window.window2.show()

    def go_to_registration(self):
        window3.hide()
        window.show()
        window.main_groupbox.show()

    def hide_b(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'blini'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        if len(admin_choose)==6:
            self.thanks_for_work()
        db.close()
        self.but.hide()
       

    def hide_b2(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'borch'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        self.but2.hide()
        if len(admin_choose)==6:
            self.thanks_for_work()
        


    def hide_b3(self):

        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'grechka'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        self.but3.hide()
        if len(admin_choose)==6:
            self.thanks_for_work()
        

    def hide_b4(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'kasha'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        self.but4.hide()
        if len(admin_choose)==6:
            self.thanks_for_work()
        


    def hide_b5(self):

        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'kotletka_s_pureshkoy'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        self.but5.hide()
        if len(admin_choose)==6:
            self.thanks_for_work()
        


    def hide_b6(self):

        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'makaroni'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        self.but6.hide()
        if len(admin_choose)==6:
            self.thanks_for_work()
        

    def hide_b7(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'pelmeni'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        self.but7.hide()
        if len(admin_choose)==6:
            self.thanks_for_work()
        


    def hide_b8(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'perlovka'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        self.but8.hide()
        if len(admin_choose)==6:
            self.thanks_for_work()
        

    def hide_b9(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'sasuges'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        self.but9.hide()
        if len(admin_choose)==6:
            self.thanks_for_work()
        

    def hide_b10(self):

        db=sqlite3.connect('base.db')
        cur=db.cursor()
        for value in cur.execute(f"SELECT food_name from food WHERE food_name='{'zapikanka'}'"):
            
            admin_choose.append(f"ImagesNPK/{value[0]}.jpg")
            admin_choose.append(f'{value[0]}')
        db.close()
        if len(admin_choose)==6:
            self.thanks_for_work()
        self.but10.hide()


        


class class_lists(QWidget):
    def __init__(self):

        super().__init__()
        self.init_ui()
        self.fetch_class_data()
    def init_ui(self):
        self.setGeometry(100,100,800,800)

        self.tableWidget = QTableWidget()
        self.button_back=QPushButton('Назад')
        self.button_update=QPushButton('Обновить')
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Класс", "Количество плантов", "Количество бесплатников"])


        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.button_back)
        layout.addWidget(self.button_update)
        self.setLayout(layout)
    
        
        self.button_back.clicked.connect(self.go_to_main)
        self.button_update.clicked.connect(self.update)




    def fetch_class_data(self):
            self.tableWidget.setRowCount(0)
            conn = sqlite3.connect('base.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM user")



            # Получаем уникальные классы
            cur.execute("SELECT DISTINCT Class_Number FROM user")

            classes = cur.fetchall()
            #print(classes)

            class_data = []
            
            for class_number in classes:
                class_number=class_number[0]
                # Для каждого класса подсчитываем количество пользователей с разными ролями
                cur.execute("SELECT COUNT(*) FROM user_eat LEFT JOIN user ON user_eat.Login=user.Login WHERE Class_Number=? AND Role=?", (class_number, 'platnoe'))
                plat_count = cur.fetchone()[0]


                cur.execute("SELECT COUNT(*)  FROM user_eat LEFT JOIN user ON user_eat.Login=user.Login WHERE Class_Number=? AND Role=?", (class_number, 'besplat'))
                besplat_count = cur.fetchone()[0]


                class_data.append((class_number,plat_count, besplat_count))

            conn.close()

            for row, row_data in enumerate(class_data):
                self.tableWidget.insertRow(row)
                for col, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.tableWidget.setItem(row, col, item)

    def go_to_main(self):
        self.fetch_class_data()
        window4.hide()
        window.window2.show()
    def update(self):
        self.fetch_class_data()

class Results(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        db=sqlite3.connect('base.db')
        cur=db.cursor()
        spisok=[]
        for value in cur.execute("SELECT admin_choose from admin"):
            spisok=str(value[0]).split()
 

        self.setGeometry(100,100,1200,800)
        self.but_update=QPushButton('Обновить')
        self.lineH1=QHBoxLayout()
        self.lineH2=QHBoxLayout()
        self.lineH3=QHBoxLayout()
        self.Mainline=QVBoxLayout()
        

        self.label1=QLabel()
        self.label2=QLabel()
        self.label3=QLabel()
        self.text1=QLabel()
        self.text2=QLabel()
        self.text3=QLabel()



        if len(spisok)>0:
            for value in cur.execute(f"SELECT Food_voites from food WHERE food_name = '{spisok[1]}'"): text1=value[0]
            for value in cur.execute(f"SELECT Food_voites from food WHERE food_name = '{spisok[3]}'"): text2=value[0]
            for value in cur.execute(f"SELECT Food_voites from food WHERE food_name = '{spisok[5]}'"): text3=value[0]
            self.text1.setText(f'        {text1} Голосов')
            self.text2.setText(f'{text2} Голосов  ')
            self.text3.setText(f'{text3} Голосов       ')
            self.label1.setPixmap(QPixmap(spisok[0]).scaled(370,350))
            self.label2.setPixmap(QPixmap(spisok[2]).scaled(370,350))
            self.label3.setPixmap(QPixmap(spisok[4]).scaled(370,350))
            self.text1.setFont(QFont("Arial",25))
            self.text2.setFont(QFont("Arial",25))
            self.text3.setFont(QFont("Arial",25))


        #images
        self.lineH1.addWidget(self.label1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.lineH1.addWidget(self.label2,alignment=Qt.AlignmentFlag.AlignCenter)
        self.lineH1.addWidget(self.label3,alignment=Qt.AlignmentFlag.AlignRight)

        #Texts
        self.lineH2.addWidget(self.text1,alignment=Qt.AlignmentFlag.AlignLeft)
        self.lineH2.addWidget(self.text2,alignment=Qt.AlignmentFlag.AlignCenter)
        self.lineH2.addWidget(self.text3,alignment=Qt.AlignmentFlag.AlignRight)
        self.lineH3.addWidget(self.but_update,alignment=Qt.AlignmentFlag.AlignLeft)

        

        self.but_back=QPushButton('Назад')
        self.but_back.setMinimumSize(65,45)
        self.lineH3.addWidget(self.but_back,alignment=Qt.AlignmentFlag.AlignHCenter)
        self.Mainline.addLayout(self.lineH1)
        self.Mainline.addLayout(self.lineH2)
        self.Mainline.addLayout(self.lineH3)
        self.setLayout(self.Mainline)


        self.but_update.clicked.connect(self.update)
        self.but_back.clicked.connect(self.go_to_MainWin)
        db.close()

    def go_to_MainWin(self):
        window5.hide()
        window.window2.show()
    
    def update(self):
        if len(spisok)>0:
            db=sqlite3.connect('base.db')
            cur=db.cursor()
            for value in cur.execute(f"SELECT Food_voites from food WHERE food_name = '{spisok[1]}'"): text1=value[0]
            for value in cur.execute(f"SELECT Food_voites from food WHERE food_name = '{spisok[3]}'"): text2=value[0]
            for value in cur.execute(f"SELECT Food_voites from food WHERE food_name = '{spisok[5]}'"): text3=value[0]
            self.text1.setText(f'        {text1} Голосов')
            self.text2.setText(f'{text2} Голосов  ')
            self.text3.setText(f'{text3} Голосов       ')
            db.close()


    

"""conn = ps.connect(database='base.sql')
cursor = conn.cursor()
cursor.execute("INSERT INTO people (last_name, first_name) VALUES ('Tom', 38)")"""




if __name__ == '__main__':
    keys=[]
    user_login_now=[]
    admin_choose=[]
    spisok=[]
    app = QApplication([])
    app.setStyle('Breeze')
    db=sqlite3.connect('base.db')
    cur=db.cursor()
    
    for value in cur.execute("SELECT admin_choose FROM admin"):
        spisok=str(value[0]).split()
    if len(spisok)>0:
        a='ImagesNPK/blini.jpg'

        images=[
        QPixmap(spisok[0]).scaled(450,400),
        QPixmap(spisok[2]).scaled(450,400),
        QPixmap(spisok[4]).scaled(450,400),
        ]

        im=images[0]
    else:
        images=[]

    besplat_pit1A=0



    window = AuthWindow()
    #self.window2=MainWin(images)
    window3=AdminWin()
    window4=class_lists()
    window5=Results()
    db.close()
    window.show()
    app.exec_()



