from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup,QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import *
app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle("Memory Card")
question = QLabel('Сколько Джоунси открыл порталов в 15 сезоне Fortnite?')
RadioGroupBox = QGroupBox('Варианты ответов')

line = QVBoxLayout()

rbth_1 = QRadioButton('9')
rbth_2 = QRadioButton('5')
rbth_3 = QRadioButton('15')
rbth_4 = QRadioButton('12')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbth_1)
layout_ans2.addWidget(rbth_2)
layout_ans3.addWidget(rbth_3)
layout_ans3.addWidget(rbth_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout1 = QVBoxLayout()

AnswerGroupBox = QGroupBox('Результат теста')
l1 = QLabel('Правильно/Неправильно')
l2 = QLabel('Правильный ответ')
layout1.addWidget(l1)
layout1.addWidget(l2)
AnswerGroupBox.setLayout(layout1)

button = QPushButton('Ответить')

line.addWidget(question, alignment = Qt.AlignCenter)
line.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
line.addWidget(AnswerGroupBox, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbth_1)
RadioGroup.addButton(rbth_2)
RadioGroup.addButton(rbth_3)
RadioGroup.addButton(rbth_4)

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    button.setText('Следующий вопрос')
def show_question():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbth_1.setChecked(False)
    rbth_2.setChecked(False)
    rbth_3.setChecked(False)
    rbth_4.setChecked(False)
    RadioGroup.setExclusive(True)
    

def start_test():
    if button.text() == 'Следующий вопрос':
        show_question()
    elif button.text() == 'Ответить':
        show_result()

class Question():
    def __init__(self, question, righ_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.righ_answer = righ_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
question_list = []
q1 = Question('Сколько Джоунси открыл порталов в 15 сезоне Fortnite?',"9","15","5","12")
q2 = Question('Сколько минут длится ивент в игре Fortnite?', "15","6","8","4")

question_list.append(q1)
question_list.append(q2)

q3 = Question('Сколько частей мультфильма Toy Story?', "4","1","2","3")
q4 = Question('Сколько лет потратили на создание Cuberpunk?', "10","3","7","5")

question_list.append(q3)
question_list.append(q4)

q5 = Question('В каком году придумали мультфильм Том и Джерии?', "1940","1935","1950","1945")
q6 = Question('В каком году придумали мультфильм Губка боб квадратные штаны?', "1999","1987","1990","1985")

question_list.append(q5)
question_list.append(q6)

q7 = Question('Когда появились комиксы Мarvel?', "1939","1931","1935","1937")
q8 = Question('Сколько сезонов в игре Fortnite?', "18","15","19","14")

question_list.append(q7)
question_list.append(q8)

q9 = Question('В каком году вышла игра Five Night at Freddys?', "2014","2010","2016","2012")
q10 = Question('В каком году выйдет игра Marvel Spider man 2?', "2023","2022","2024","2021")

question_list.append(q9)
question_list.append(q10)

answers = [rbth_1, rbth_2, rbth_3, rbth_4]
def ask(q):
    shuffle(answers)
    answers[0].setText(q.righ_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    l2.setText(q.righ_answer)
    show_question()

def show_correct(res):
    l1.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        main_win.score =+ 1
        show_correct('Правильно!')
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    
    cur_question = randint(0, len(question_list) - 1)
    if cur_question >= len(question_list):
        
        cur_question = 0
    q = question_list [cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

AnswerGroupBox.hide()



button.clicked.connect(click_OK)

main_win.show()
app.exec_()