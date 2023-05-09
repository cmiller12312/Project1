from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (QComboBox, QLabel, QLineEdit,QPushButton, QSlider)
import tele
import csv

class Ui_Widget(object):
    def setupUi(self, Widget) -> None:
        """
        sets up all the buttins and everything
        :param Widget: the screen
        """
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 400)
        Widget.setMinimumSize(QSize(400, 400))
        Widget.setMaximumSize(QSize(400, 400))
        self.label_title = QLabel(Widget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(20, 10, 360, 40))
        font = QFont()
        font.setPointSize(26)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)
        self.options = QComboBox(Widget)
        self.options.setObjectName(u"options")
        self.options.setGeometry(QRect(20, 70, 240, 30))
        self.options.addItems(self.startup())
        self.button_select = QPushButton(Widget, clicked=self.select)
        self.button_select.setObjectName(u"button_select")
        self.button_select.setGeometry(QRect(280, 70, 80, 30))
        self.label_name = QLabel(Widget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(25, 140, 60, 20))
        self.in_name = QLineEdit(Widget)
        self.in_name.setObjectName(u"lineEdit")
        self.in_name.setGeometry(QRect(90, 140, 240, 20))
        #volume slider and label
        self.volume_slider = QSlider(Qt.Horizontal, Widget)
        self.volume_slider.setGeometry(225, 325, 150, 30)
        self.vol_slider_label = QLabel(Widget)
        self.volume_slider.setMaximum(10)
        self.volume_slider.setDisabled(True)
        try:
            self.volume_slider.setValue(self.tvs[self.options.currentIndex() - 1].get_volume())
        except (IndexError):
            self.volume_slider.setValue(0)
        self.vol_slider_label.setGeometry((225 + (self.volume_slider.value() * 15) - (1 * self.volume_slider.value())), 350, 25, 25)
        self.label_vol = QLabel(Widget)
        self.label_vol.setObjectName(u"label_vol")
        self.label_vol.setGeometry(QRect(60, 130, 60, 30))
        self.label_vol.setAlignment(Qt.AlignCenter)
        self.channel_up = QPushButton(Widget, clicked=self.change_channel_up)
        #channel buttons
        self.channel_up.setObjectName(u"channel_up")
        self.channel_up.setGeometry(QRect(340, 130, 30, 30))
        self.channel_down = QPushButton(Widget, clicked=self.change_channel_down)
        self.channel_down.setObjectName(u"channel_down")
        self.channel_down.setGeometry(QRect(250, 130, 30, 30))
        #volume buttons
        self.volume_up = QPushButton(Widget, clicked=self.change_vol_up)
        self.volume_down = QPushButton(Widget, clicked=self.change_vol_down)
        self.volume_up.setGeometry(30,130,30,30)
        self.volume_down.setGeometry(120,130,30,30)
        #power buttons
        self.button_power = QPushButton(Widget, clicked=self.change_power)
        self.button_power.setObjectName(u"button_power")
        self.button_power.setGeometry(QRect(230, 95, 60, 30))
        #mute button
        self.button_mute = QPushButton(Widget, clicked=self.change_mute)
        self.button_mute.setObjectName(u"button_power")
        self.button_mute.setGeometry(QRect(300,95,60,30))
        #channel label
        self.label_channel = QLabel(Widget)
        self.label_channel.setObjectName(u"label_channel")
        self.label_channel.setGeometry(QRect(280, 130, 60, 30))
        self.label_channel.setAlignment(Qt.AlignCenter)
        #create button
        self.button_create = QPushButton(Widget, clicked=self.create)
        self.button_create.setObjectName(u"button_create")
        self.button_create.setGeometry(QRect(160, 190, 80, 30))
        #delete button
        self.button_del = QPushButton(Widget, clicked=self.delete)
        self.button_del.setObjectName(u"button_del")
        self.button_del.setGeometry(QRect(160,95,60,30))

        self.channel_image = QLabel(Widget)
        self.images = [QPixmap('channel_images/weatherCat.jpeg'),QPixmap('channel_images/sportsCat.jpeg'),QPixmap('channel_images/CatCat.jpeg')]
        for i in range(0, len(self.images)):
            self.images[i] = self.images[i].scaled(150,150)
        self.channel_image.setGeometry(QRect(225,170,150,150))
        self.retranslateUi(Widget)
        QMetaObject.connectSlotsByName(Widget)
        self.channel_image.setPixmap(self.images[self.tvs[self.options.currentIndex() - 1].get_channel()])
    # setupUi

    def startup(self) -> list:
        """
        creates self.tvs
        reads data.csv
        :return: first column of data.csv
        """
        self.tvs = []
        ending = ["New"]
        with open("data.csv", "r") as input_file:
            temp = []
            i = 0
            con = csv.reader(input_file,delimiter=",")
            for row in con:
                temp.append(row)
                inside = temp[i]
                self.tvs.append(
                    tele.Television(inside[0], self.change(inside[1]), self.change(inside[2]), int(inside[3]), int(inside[4])))
                ending.append(inside[0])
                i += 1
        return ending

    def change(self, inside: str) -> bool:
        """
        converts a str into a bool
        :param inside: a str that should be "True" or "False"
        :return: "True" or "False" if string is a bool
        """
        if inside == "True":
            return True
        elif inside == "False":
            return False
        else:
            raise TypeError

    def select(self) -> None:
        """
        hides and shows objects in Widget
        :return: None
        """
        choice = self.options.currentText()
        self.in_name.clear()
        if choice == "New":
            self.button_power.hide()
            self.button_mute.hide()
            self.label_name.show()
            self.in_name.show()
            self.button_create.show()
            self.label_channel.hide()
            self.label_vol.hide()
            self.channel_down.hide()
            self.channel_up.hide()
            self.volume_slider.hide()
            self.button_del.hide()
            self.channel_image.hide()
            self.vol_slider_label.hide()
            self.volume_down.hide()
            self.volume_up.hide()
        else:
            self.tv = self.tvs[self.options.currentIndex() - 1]
            self.button_power.show()
            self.button_mute.show()
            self.label_name.hide()
            self.in_name.hide()
            self.button_create.hide()
            self.label_channel.show()
            self.label_vol.show()
            self.channel_down.show()
            self.channel_up.show()
            self.volume_slider.show()
            self.button_del.show()
            if self.tv.get_status():
                self.channel_image.show()
            self.vol_slider_label.show()
            self.volume_down.show()
            self.volume_up.show()
            if self.tv.get_muted():
                self.volume_slider.setValue(0)
                self.vol_slider_label.setGeometry((225 + (0 * 15) - (1 * 0)), 350, 25, 25)
                self.vol_slider_label.setText(str(0))
            else:
                self.volume_slider.setValue(self.tv.get_volume())
                self.vol_slider_label.setGeometry((225 + (self.volume_slider.value() * 15) - (1 * self.volume_slider.value())), 350, 25, 25)
                self.vol_slider_label.setText(str(self.tv.get_volume()))
            if self.tv.get_status():
                self.channel_image.show()
                self.channel_image.setPixmap(self.images[self.tv.get_channel()])
            else:
                self.channel_image.hide()
    def change_power(self) -> None:
        """
        changes status of selected tv
        :return: None
        """
        self.tv.power()
        if self.tv.get_status():
            self.channel_image.show()
        else:
            self.channel_image.hide()
        self.tv.mute()
        self.save()
        if not self.tv.get_status():
            self.volume_slider.setValue(0)
            self.vol_slider_label.setGeometry((225 + (0 * 15) - (1 * 0)), 350, 25, 25)
            self.vol_slider_label.setText(str(0))
        else:
            self.volume_slider.setValue(self.tv.get_volume())
            self.vol_slider_label.setGeometry((225 + (self.volume_slider.value() * 15) - (1 * self.volume_slider.value())), 350, 25, 25)
            self.vol_slider_label.setText(str(self.tv.get_volume()))
        self.save()

    def change_mute(self) -> None:
        """
        changes mute of selected tv
        :return: None
        """
        if self.tv.get_status():
            self.tv.mute()
            if self.tv.get_muted():
                self.volume_slider.setValue(0)
                self.vol_slider_label.setGeometry((225 + (0 * 15) - (1 * 0)),350, 25, 25)
                self.vol_slider_label.setText(str(0))
            else:
                self.volume_slider.setValue(self.tv.get_volume())
                self.vol_slider_label.setGeometry((225 + (self.volume_slider.value() * 15) - (1 * self.volume_slider.value())), 350, 25, 25)
                self.vol_slider_label.setText(str(self.tv.get_volume()))
            self.save()

    def change_vol_up(self) -> None:
        """
        increases volume of selected tv
        :return:
        """
        if self.tv.get_status():
            self.tv.volume_up()
            self.volume_slider.setValue(self.tv.get_volume())
            self.vol_slider_label.setGeometry((225 + (self.volume_slider.value() * 15) - (1 * self.volume_slider.value())), 350, 25, 25)
            self.vol_slider_label.setText(str(self.tv.get_volume()))
            self.save()

    def change_vol_down(self) -> None:
        """
        decreases volume of selected tv
        :return: None
        """
        if self.tv.get_status():
            self.tv.volume_down()
            self.volume_slider.setValue(self.tv.get_volume())
            self.vol_slider_label.setGeometry((225 + (self.volume_slider.value() * 15) - (1 * self.volume_slider.value())), 350, 25, 25)
            self.vol_slider_label.setText(str(self.tv.get_volume()))
            self.save()

    def change_channel_up(self) -> None:
        """
        increases the channel of selected tv
        :return: None
        """
        self.tvs[self.options.currentIndex()-1].channel_up()
        self.channel_image.setPixmap(self.images[self.tv.get_channel()])
        self.save()

    def change_channel_down(self) -> None:
        """
        decreases the channel of selected tv
        :return: None
        """
        self.tvs[self.options.currentIndex()-1].channel_down()
        self.channel_image.setPixmap(self.images[self.tv.get_channel()])
        self.save()

    def save(self) -> None:
        """
        saves the data within self.tvs
        :return: None
        """
        with open("data.csv", "w") as output_file:
            con = csv.writer(output_file)
            for line in range(0,len(self.tvs)):
                con.writerow(self.tvs[line].get_storage())

    def create(self) -> None:
        """
        creates a new tv with the str inside of in_name
        :return: None
        """
        name = self.in_name.text()
        self.in_name.clear()
        self.tvs.append(tele.Television(name))
        self.options.addItems([name])
        self.save()

    def delete(self) -> None:
        """
        deletes the selected tv
        :return: None
        """
        self.tvs.pop(self.options.currentIndex()-1)
        self.options.removeItem(self.options.currentIndex())
        self.save()
        self.select()

    def retranslateUi(self, Widget) -> None:
        """
        Sets the text for startup and hides certain things
        :param Widget: The frame it is going on
        :return: None
        """
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"TV Manager", None))
        self.label_title.setText(QCoreApplication.translate("Widget", u"Television Manager", None))
        self.button_select.setText(QCoreApplication.translate("Widget", u"Select", None))
        self.label_name.setText(QCoreApplication.translate("Widget", u"Name:", None))
        self.label_vol.setText(QCoreApplication.translate("Widget", u"Volume", None))
        self.channel_up.setText(QCoreApplication.translate("Widget", u"+", None))
        self.channel_down.setText(QCoreApplication.translate("Widget", u"-", None))
        self.volume_up.setText(QCoreApplication.translate("Widget", u"+", None))
        self.volume_down.setText(QCoreApplication.translate("Widget", u"-", None))
        self.label_channel.setText(QCoreApplication.translate("Widget", u"Channel", None))
        self.button_create.setText(QCoreApplication.translate("Widget", u"Create", None))
        self.button_power.setText(QCoreApplication.translate("Widget",u"Power",None))
        self.button_mute.setText(QCoreApplication.translate("Widget",u"Mute",None))
        self.button_del.setText(QCoreApplication.translate("Widget",u"Delete",None))
        self.vol_slider_label.setText(QCoreApplication.translate("Widget",str(self.tvs[self.options.currentIndex() - 1]) , None))
        self.button_power.hide()
        self.button_mute.hide()
        self.volume_slider.hide()
        self.channel_down.hide()
        self.channel_up.hide()
        self.label_channel.hide()
        self.label_vol.hide()
        self.button_del.hide()
        self.channel_image.hide()
        self.vol_slider_label.hide()
        self.volume_up.hide()
        self.volume_down.hide()
