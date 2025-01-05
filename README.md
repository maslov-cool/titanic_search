# titanic_search
программу с графическим пользовательским интерфейсом на PyQT, которая отображает информацию о пассажирах Титаника из csv-файла, раскрашивая строки, содержащие информацию о выживших одним цветом, а о погибших — другим.
Добавьте строку поиска по имени пассажира, которая должна работать следующим образом:

Если в строке поиска менее трех символов, поиск не производится и отображается информация обо всех пассажирах
Если в строке поиска три и более символов, отображаются данные только тех пассажиров, имя которых содержит введенную подстроку (вне зависимости от регистра)

Класс, реализующий окно приложения, назовите TitanicSearch. Объект содержащий таблицу назовите resultTable. Строку поиска назовите searchEdit. Цвет для погибших #FF0000, для выживших #00FF00.
