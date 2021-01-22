#if __name__ == "__main__":
import sys, pyowm
# для погоды
from PyQt5 import QtCore, QtGui, QtWidgets
from test2 import Ui_Dialog
app = QtWidgets.QApplication(sys.argv)
#это создание приложения
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
#Это инициализация , все Это основной цикл приложения


def get_weather_city():
	#создаем функцию. ниже логика приложения
	owm=pyowm.OWM('62c2980e8419f3fad2f1c8f805589918')

	city=ui.lineEdit.text()
	mgr = owm.weather_manager()
	observation	= mgr.weather_at_place( city )
	#w = observation.get_weather()
	w = observation.weather
	temperature = w.temperature( 'celsius' )[ 'temp' ]
	ui.label.setText(f'Температура: {temperature}')
# Выводим в строку лабел в приложение нашц функцию
ui.pushButton.clicked.connect (get_weather_city)
#Метод чтобы при нажатии на кнопку баттно выводмлся текст (функция)
sys.exit(app.exec_())
