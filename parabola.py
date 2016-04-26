#!/usr/bin/python3

import sys, math
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
	def __init__(self):
		super(Example, self).__init__()

		self.gravity = 2.9
		self.velocity = 10
		self.air_resistance = 0.01
		self.angle = 45
		self.origin_x = 450
		self.origin_y = 450
		self.initUI()
        
	def initUI(self):      


		# Main window
		self.window = QtGui.QWidget()

		# Gravity Slider
		grav_counter = QtGui.QLCDNumber(self)
		grav_slider = QtGui.QSlider(QtCore.Qt.Vertical, self)
		grav_slider.setValue(10)
		grav_slider.setMaximum(1000)
		grav_label = QtGui.QLabel("Gravity")

		# Air Resistance Slider
		air_counter = QtGui.QLCDNumber(self)
		air_slider = QtGui.QSlider(QtCore.Qt.Vertical, self)
		air_slider.setValue(10)
		air_slider.setMaximum(200)
		air_label = QtGui.QLabel("Air Resistance")

		# Velocity/Angle Sliders and Counters
		self.counter1 = QtGui.QLCDNumber(self)
		self.counter2 = QtGui.QLCDNumber(self)
		slider1_label = QtGui.QLabel("Velocity")
		slider1 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		slider1.setValue(self.velocity)
		slider1.setMaximum(100)
		slider2_label = QtGui.QLabel("Angle")
		slider2 = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		slider2.setValue(self.angle)
		slider2.setMaximum(180)


		bhbox = QtGui.QHBoxLayout()
		sliderb1 = QtGui.QVBoxLayout()
		sliderb2 = QtGui.QVBoxLayout()

		sliderb1.addWidget(slider1_label)
		sliderb1.addWidget(self.counter1)
		sliderb1.addWidget(slider1)
		sliderb2.addWidget(slider2_label)
		sliderb2.addWidget(self.counter2)
		sliderb2.addWidget(slider2)

		bhbox.addLayout(sliderb1)
		bhbox.addLayout(sliderb2)

		# Autobots Assemble
		thbox = QtGui.QHBoxLayout()
		thbox.addWidget(self.window)
		thbox.setStretchFactor(self.window, 10)

		tvbox = QtGui.QVBoxLayout()
		tvhbox1 = QtGui.QHBoxLayout()
		tvhbox2 = QtGui.QHBoxLayout()

		tvhbox1.addWidget(grav_counter)
		tvhbox1.addWidget(grav_slider)
		tvhbox2.addWidget(air_counter)
		tvhbox2.addWidget(air_slider)

		tvbox.addWidget(grav_label)
		tvbox.addLayout(tvhbox1)
		tvbox.addWidget(air_label)
		tvbox.addLayout(tvhbox2)

		thbox.addLayout(tvbox)
		thbox.setStretchFactor(tvbox, 1)

		vbox = QtGui.QVBoxLayout()
		vbox.addLayout(thbox)
		vbox.setStretchFactor(thbox, 10)
		vbox.addLayout(bhbox)
		vbox.setStretchFactor(bhbox, 1)

		# Slap er up
		self.setLayout(vbox)

		# Plug in all the bells and whistles
		slider1.valueChanged.connect(self.counter1.display)
		slider2.valueChanged.connect(self.counter2.display)
		slider1.valueChanged.connect(self.setvelocity)
		slider2.valueChanged.connect(self.setAngle)
		grav_slider.valueChanged.connect(self.setGravity)
		grav_slider.valueChanged.connect(grav_counter.display)
		air_slider.valueChanged.connect(self.setAir)
		air_slider.valueChanged.connect(air_counter.display)

		self.setGeometry(300, 300, 2650, 1400)
		self.setWindowTitle('Parabola')
		self.setWindowOpacity(0.7)
		self.show()

	def setvelocity(self, value):
		self.velocity = float(value)

	def setAngle(self, value):
		self.angle = math.radians(float(value))

	def setGravity(self, value):
		self.gravity = float(value) / 100

	def setAir(self, value):
		self.air_resistance = float(value) / 1000

	def paintEvent(self, e):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawPoints(qp)
		qp.end()
		self.update()

	def drawPoints(self, qp):

		pen = QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine)
		qp.setPen(pen)
		size = self.size()
 
		adjusted_velocity = self.velocity
		adjusted_gravity = self.gravity + ( 0.00343 * self.velocity )
		old_x = self.origin_x
		old_y = self.origin_y
		# This does the magic yo
		for i in range(0, 100):

			# Calculate Arc
			y = -( (i * adjusted_velocity * math.sin(self.angle)) - (adjusted_gravity * i**2 )/2 )
			x = adjusted_velocity * math.cos(self.angle) * i

			# Draw Arc
			qp.drawLine(old_x, old_y, x + self.origin_x, y + self.origin_y)
			old_x = x + self.origin_x
			old_y = y + self.origin_y

			# Apply air resistance
			adjusted_velocity -= self.air_resistance

		# Draw reticule
		pen = QtGui.QPen(QtCore.Qt.white, 2, QtCore.Qt.SolidLine)
		qp.setPen(pen)
		reticule_offset = 435
		qp.drawLine(self.origin_x - reticule_offset, self.origin_y, self.origin_x + reticule_offset, self.origin_y)
		qp.drawLine(self.origin_x, self.origin_y - reticule_offset, self.origin_x, self.origin_y + reticule_offset)

	def mouseMoveEvent(self, QMouseEvent):
		cursor = QtGui.QCursor()
		self.origin_x =  cursor.pos().x()
		self.origin_y =  cursor.pos().y()

def main():
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()


