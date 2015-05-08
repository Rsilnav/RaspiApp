#!/usr/bin/env python
import signal
import json

from urllib2 import Request, urlopen, URLError

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify


APPINDICATOR_ID = 'myappindicator'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, '/home/rafsill/bin/tempAlert/icon.png', appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_temp = gtk.MenuItem('Temperatura')
    item_temp.connect('activate', temp)
    menu.append(item_temp)

    sep = gtk.SeparatorMenuItem()
    menu.append(sep)

    item_quit = gtk.MenuItem('Salir')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()

    return menu

def fetch_temp():
    request = Request('http://raspi:3000')
    response = urlopen(request)
    return response.read()

def temp(_):
    notify.Notification.new("<b>Temperatura</b>", fetch_temp(), None).show()

def quit(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
