from selene import have
from selene.support.shared import browser
import pytest


# Добавляем новую запись в таблицу
def test_add_new_entry_to_webtable():
    # Открываем форму, которую будем тестировать
    browser.open_url('https://demoqa.com/webtables')
    # Жмем кнопку добавление записи в таблицу
    browser.element('#addNewRecordButton').click()
    # Проверяем, что открылась форма "Registration Form"
    browser.element('#registration-form-modal').should(have.text('Registration Form'))
    # Заполняем элементы формы и закрываем ее
    browser.element('#firstName').type('Joe')
    browser.element('#lastName').type('Black')
    browser.element('#userEmail').type('JoeBlack@gmail.com')
    browser.element('#age').type('26')
    browser.element('#salary').type('13000')
    browser.element('#department').type('Cryptology')
    browser.element('#submit').click()
    # Проверяем, что данные добавились в таблицу
    browser.element('.rt-tbody').should(have.text('Joe'))
    browser.element('.rt-tbody').should(have.text('Black'))


# Редактируем вторую запись в таблице
def test_edit_entry():
    browser.open_url('https://demoqa.com/webtables')
    # Открываем форму редактирования второй строки
    browser.element('#edit-record-2').click()
    # Очищаем поля FirstName и LastName и вводим новые значеия
    browser.element('#firstName').clear().type('Leo')
    browser.element('#lastName').clear().type('Smith')
    browser.element('#userEmail').clear().type('LeoSmith@gmail.com')
    browser.element('#age').clear().type('33')
    browser.element('#salary').clear().type('9000')
    browser.element('#department').clear().type('Design')
    browser.element('#submit').click()
    # Проверяем, что в таблице поменялись значения
    browser.element('.rt-tbody').should(have.text('Leo'))
    browser.element('.rt-tbody').should(have.text('Smith'))
    browser.element('.rt-tbody').should(have.text('LeoSmith@gmail.com'))
    browser.element('.rt-tbody').should(have.text('33'))
    browser.element('.rt-tbody').should(have.text('9000'))


# Удаляем третью строку в таблице
def test_delete_entry():
    browser.open_url('https://demoqa.com/webtables')
    browser.element('#delete-record-3').click()
    browser.element('.rt-tbody').should(have.no.text('Kierra'))
    browser.element('.rt-tbody').should(have.no.text("Gentry"))
    browser.element('.rt-tbody').should(have.no.text('kierra@example.com'))