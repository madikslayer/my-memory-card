from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import shuffle
from random import randint 

class Question():
def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
    self.question = question
    self.right_answer = right_answer
    self.wrong1 = wrong1
    self.wrong2 = wrong2
    self.wrong3 = wrong3

question_list = []
question_list.append(Question(' Как называется еврейский Новый год?', 'Ханука', "Йом Кипур", 'Кванза', 'Рош ха-Шана'))
question_list.append(Question('Сколько синих полос на флаге США?', '6', "7", '13', '0'))
question_list.append(Question('Fe — это символ какого химического элемента?', 'железо', "бром", 'медь', 'серебро'))
question_list.append(Question('сколько людей живут в кз', '20млн', "15млн", '4млн', '30млдр'))
question_list.append(Question('когда умер Болат Назарбаев', '13 ноября 2023', "35 ноября 2020", '13 октября 2023', '20 ноября 2022'))
app = QApplication([])


'''Интерфейс приложения Memory card'''
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году была основана Москва')


RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')



RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)



layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidjet(rbtn_1)
layout_ans2.addWidjet(rbtn_2)
layout_ans3.addWidjet(rbtn_3)
layout_ans3.addWidjet(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLAbel('Прав ли ты или нет?')
lb_Correct = QLAbel('Ответ будет тут!')


layout_res = QHBoxLayout()
layout_res.addWidjet(lb_Result, aligment=(Qt.AlignLeft / Qt.AlignTop))
layout_res.addWidjet(lb_Correct, aligment=Qt.AligHCenter, scretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidjet(lb_Question, aligment=(Qt.AligHCenter / Qt.AligVCenter))
layout_line2.addWidjet(RadioGroupBox)
layout_line2.addWidjet(AnsGroupBox)
AnsGroupBox.hide()



layout_line3.addScretch(1)
layout_line3.addWidjet(btn_OK, scretch=2)
layout_line3.addScretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, scretch=2)
layout_card.addLayout(layout_line2, scretch=8)
layout_card.addScretch(1)
layout_card.addLayout(layout_line3, scretch=1)
layout_card.addScretch(1)
layout_card.setSpacing(5)

def show_result():
RadioGroupBox.hide()
AnsGroupBox.show()
btn_OK.setText('Следующий вопрос')

def show_question():
RadioGroupBox.show()
AnsGroupBox.hide()
btn_OK.setText('Ответить')
RadioGroup.setEXclusive(False)
rbtn_1.set.Checked(False)
rbtn_2.set.Checked(False)
rbtn_3.set.Checked(False)
rbtn_4.set.Checked(False)
RadioGroup.setEXclusive(True)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(res)
    show_result()


def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked()
        show_correct('Правильно')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answera[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг:', (window.score/window.total*100), '%')


def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list) - 1)



    q = questions_list[cur_question]
    ask(q)


def click_OK():
    if btn_OK.Text() == 'Ответить'
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

btn_OK.click.connect(click_OK)


window.score = 0
window.total = 0
next_question()
window.resize(400, 300)
window.show()
app.exec()
































