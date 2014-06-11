#!/usr/bin/env python3
#-*-coding:utf-8-*-

from gi.repository import Gtk,Gdk,GObject
import cairo
import math
from collections import *
from datetime import datetime

print('''
这是一个简单的动态显示时钟程序。
''')

point=namedtuple('point',['x','y'])

polar=namedtuple('polar',['angle','radius'])

def topoint(polar):
    p=point
    point.x=math.cos(math.radians(-polar.angle))*polar.radius
    point.y=math.sin(math.radians(-polar.angle))*polar.radius
    return p

class Clock(Gtk.DrawingArea):
    def __init__(self,parent):
        super(Clock, self).__init__()


        # make it private
        self._time = None
        self.update()
        self.connect("draw", self.draw)

        GObject.timeout_add(1000, self.update)

    def draw(self, wid, cr):
        cr.set_source_rgb(0, 0, 0)
        cr.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL)

        #rect = self.get_allocation()
        #w, h = rect.x + rect.width ,rect.y + rect.height
        w, h = 400,350
        cr.translate(w/2, h/2)
        cr.set_line_width(3*3)
        cr.arc(0, 0, 170, 0, 2*math.pi)
        cr.stroke_preserve()
        cr.set_source_rgb(1, 0.973, 0.827)
        cr.fill()

        for (angle,label) in [(0,3),(30,2),(60,1),(90,12),(120,11),(150,10),(180,9),(210,8),(240,7),(270,6),(300,5),(330,4)]:
            if angle in[0,90,180,270]:
                cr.set_line_width(6)
                cr.set_source_rgb(0, 0, 0)
                cr.move_to(topoint(polar(angle,136)).x,topoint(polar(angle,136)).y)
                cr.line_to(topoint(polar(angle,170)).x,topoint(polar(angle,170)).y)
                cr.stroke()
            cr.set_line_width(3*1)
            cr.set_source_rgb(0, 0, 0)
            cr.move_to(topoint(polar(angle,154)).x,topoint(polar(angle,154)).y)
            cr.line_to(topoint(polar(angle,170)).x,topoint(polar(angle,170)).y)
            cr.stroke()

            cr.set_font_size(20)
            cr.move_to(topoint(polar(angle,120)).x,topoint(polar(angle,120)).y)
            cr.show_text(str(label))

        cr.move_to(0,0)
        cr.set_source_rgb(0, 0, 0)
        cr.set_line_width(6)
        cr.line_to(topoint(polar(-self.hour*30+90-self.minute*30/60,60)).x,topoint(polar(-self.hour*30+90-self.minute*30/60,60)).y)
        cr.stroke()

        cr.set_source_rgb(0, 0, 0)
        cr.set_line_width(4.5)
        cr.move_to(0,0)
        cr.line_to(topoint(polar(-self.minute*6+90,85)).x,topoint(polar(-self.minute*6+90,85)).y)
        cr.stroke()

        cr.set_source_rgb(1, 0, 0)
        cr.set_line_width(1.8)
        cr.move_to(0,0)
        cr.line_to(topoint(polar(-self.second*6+90,110)).x,topoint(polar(-self.second*6+90,110)).y)
        cr.stroke()


        cr.set_source_rgb(0, 0, 0)
        cr.arc(0, 0, 5, 0, 2*math.pi)
        cr.fill()




    def update(self):
        # update the time
        self.time = datetime.now()
        self.hour=self.time.hour
        self.minute=self.time.minute
        self.second=self.time.second

        return True # keep running this event

    def redraw_canvas(self):
        if self.update:
            self.queue_draw()

    # public access to the time member
    def _get_time(self):
        return self._time
    def _set_time(self, datetime):
        self._time = datetime
        self.redraw_canvas()
    time = property(_get_time, _set_time)

class PyApp(Gtk.Window):
    def __init__(self):
        super(PyApp,self).__init__()
        self.set_title("我的闹钟")
        self.resize(400, 350)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("destroy", Gtk.main_quit)

        self.clock = Clock(self)
        self.add(self.clock)

        self.show_all()


def main():
    PyApp()
    Gtk.main()


if __name__ == "__main__":#if run as script
    main()



















