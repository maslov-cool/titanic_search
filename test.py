import io
import sys
import csv

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtGui import QColor

design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Результат олимпиады: фильтрация</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="resultTable">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>70</y>
      <width>801</width>
      <height>521</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Подстрока для поиска</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="searchEdit">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>20</y>
      <width>511</width>
      <height>41</height>
     </rect>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class TitanicSearch(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(design)
        uic.loadUi(f, self)  # Загружаем дизайн

        self.reader = []
        # Чтение CSV файла
        with open('titanic.csv', mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)

            # Добавление данных в список
            for row in csv_reader:
                self.reader.append(row)
        self.resultTable.setRowCount(len(self.reader) - 1)
        self.resultTable.setColumnCount(len(self.reader[0]))

        # Устанавливаем заголовки столбцов
        self.header_labels = self.reader[0]
        self.resultTable.setHorizontalHeaderLabels(self.header_labels)

        self.reader = self.reader[1:]

        for i in range(len(self.reader)):
            for j in range(len(self.reader[i])):
                self.resultTable.setItem(i, j, QTableWidgetItem(self.reader[i][j]))
                if int(self.reader[i][-2]):
                    self.resultTable.item(i, j).setBackground(QColor(0, 255, 0))
                else:
                    self.resultTable.item(i, j).setBackground(QColor(255, 0, 0))
        self.searchEdit.textChanged.connect(self.act)

    def act(self):
        if len(self.searchEdit.text()) > 2:
            text = self.searchEdit.text().lower()
            new_reader = [i for i in self.reader if text.lower() in i[1].lower()]
            self.resultTable.setRowCount(len(new_reader))
            self.resultTable.setColumnCount(len(self.header_labels))

            self.resultTable.setHorizontalHeaderLabels(self.header_labels)

            for i in range(len(new_reader)):
                for j in range(len(new_reader[i])):
                    self.resultTable.setItem(i, j, QTableWidgetItem(new_reader[i][j]))
                    if int(new_reader[i][-2]):
                        self.resultTable.item(i, j).setBackground(QColor(0, 255, 0))
                    else:
                        self.resultTable.item(i, j).setBackground(QColor(255, 0, 0))
        else:
            if self.resultTable.columnCount() < len(self.reader):
                self.resultTable.setRowCount(len(self.reader))
                self.resultTable.setColumnCount(len(self.reader[0]))

                self.resultTable.setHorizontalHeaderLabels(self.header_labels)

                for i in range(len(self.reader)):
                    for j in range(len(self.reader[i])):
                        self.resultTable.setItem(i, j, QTableWidgetItem(self.reader[i][j]))
                        if int(self.reader[i][-2]):
                            self.resultTable.item(i, j).setBackground(QColor(0, 255, 0))
                        else:
                            self.resultTable.item(i, j).setBackground(QColor(255, 0, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    program = TitanicSearch()
    program.show()
    sys.exit(app.exec())
