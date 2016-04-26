#!/usr/bin/python

import sys, math
from PyQt4 import QtGui, QtCore

class Paraebola(QtGui.QWidget):

	## Init Derp
    
	def __init__(self):
		super(Paraebola, self).__init__()

		self.gravity = 2.9
		self.velocity = 10
		self.air_resistance = 0.01
		self.angle = 45
		self.origin_x = 450
		self.origin_y = 450
		self.initUI()

	## Intialize Dat Shit

	def initUI(self):

		# Main window
		self.window = QtGui.QWidget()

		# Gravity Slider + Counter
		grav_counter = QtGui.QLCDNumber(self)
		grav_slider = QtGui.QSlider(QtCore.Qt.Vertical, self)
		grav_slider.setValue(10)
		grav_slider.setMaximum(1000)
		grav_label = QtGui.QLabel("Gravity")

		gravity_hlayout = QtGui.QHBoxLayout()
		gravity_hlayout.addWidget(grav_counter)
		gravity_hlayout.addWidget(grav_slider)

		# Air Resistance Slider + Counter
		air_counter = QtGui.QLCDNumber(self)
		air_slider = QtGui.QSlider(QtCore.Qt.Vertical, self)
		air_slider.setValue(10)
		air_slider.setMaximum(200)
		air_label = QtGui.QLabel("Air Resistance")

		air_hlayout = QtGui.QHBoxLayout()
		air_hlayout.addWidget(air_counter)
		air_hlayout.addWidget(air_slider)

		# Velocity Slider + Counter
		velocity_counter = QtGui.QLCDNumber(self)
		velocity_slider_label = QtGui.QLabel("Velocity")
		velocity_slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		velocity_slider.setValue(self.velocity)
		velocity_slider.setMaximum(100)

		velocity_vlayout = QtGui.QVBoxLayout()
		velocity_vlayout.addWidget(velocity_slider_label)
		velocity_vlayout.addWidget(velocity_counter)
		velocity_vlayout.addWidget(velocity_slider)

		# Angle Slider + Counter
		angle_counter = QtGui.QLCDNumber(self)
		angle_slider_label = QtGui.QLabel("Angle")
		angle_slider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
		angle_slider.setValue(self.angle)
		angle_slider.setMaximum(180)

		angle_vlayout = QtGui.QVBoxLayout()
		angle_vlayout.addWidget(angle_slider_label)
		angle_vlayout.addWidget(angle_counter)
		angle_vlayout.addWidget(angle_slider)

		# Autobots Assemble
		top_right_vlayout = QtGui.QVBoxLayout()
		top_right_vlayout.addWidget(grav_label)
		top_right_vlayout.addLayout(gravity_hlayout)
		top_right_vlayout.addWidget(air_label)
		top_right_vlayout.addLayout(air_hlayout)

		top_hlayout = QtGui.QHBoxLayout()
		top_hlayout.addWidget(self.window)
		top_hlayout.setStretchFactor(self.window, 10)
		top_hlayout.addLayout(top_right_vlayout)
		top_hlayout.setStretchFactor(top_right_vlayout, 1)

		bottom_hlayout = QtGui.QHBoxLayout()
		bottom_hlayout.addLayout(velocity_vlayout)
		bottom_hlayout.addLayout(angle_vlayout)

		vbox = QtGui.QVBoxLayout()
		vbox.addLayout(top_hlayout)
		vbox.setStretchFactor(top_hlayout, 10)
		vbox.addLayout(bottom_hlayout)
		vbox.setStretchFactor(bottom_hlayout, 1)

		# Slap er up
		self.setLayout(vbox)

		# Plug in all the bells and whistles
		velocity_slider.valueChanged.connect(velocity_counter.display)
		angle_slider.valueChanged.connect(angle_counter.display)
		velocity_slider.valueChanged.connect(self.setvelocity)
		angle_slider.valueChanged.connect(self.setAngle)
		grav_slider.valueChanged.connect(self.setGravity)
		grav_slider.valueChanged.connect(grav_counter.display)
		air_slider.valueChanged.connect(self.setAir)
		air_slider.valueChanged.connect(air_counter.display)

		# Set window settings
		self.setGeometry(300, 300, 2650, 1400)
		self.setWindowTitle('Para ebola')
		self.setWindowOpacity(0.7)
		self.show()


	## Main graph line function

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

	## Setters

	def setvelocity(self, value):
		self.velocity = float(value)

	def setAngle(self, value):
		self.angle = math.radians(float(value))

	def setGravity(self, value):
		self.gravity = float(value) / 100

	def setAir(self, value):
		self.air_resistance = float(value) / 1000

	## Paint Function

	def paintEvent(self, e):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawPoints(qp)
		qp.end()
		self.update()

	## Mouse Event

	def mouseMoveEvent(self, QMouseEvent):
		cursor = QtGui.QCursor()
		self.origin_x =  cursor.pos().x()
		self.origin_y =  cursor.pos().y()


def main():
	app = QtGui.QApplication(sys.argv)
	paraebola = Paraebola()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()


