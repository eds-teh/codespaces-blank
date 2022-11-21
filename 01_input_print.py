#!/usr/bin/env python3

name = input("Как тебя зовут? ")
print(f"Привет, {name}!")
lastname = input("Как твоя фамилия? ")
print(f"Спасибо за информацию, {name}!")
last_question = input('''Последний вопрос: 
Что ты ел на завтрак? ''')

print(f"Ваши ответы: " + name + ' ' + lastname + ' ' +  last_question)

