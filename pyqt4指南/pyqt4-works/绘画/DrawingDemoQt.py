
#  DrawingDemoQt.py  (c) Kari Laitinen

#  http://www.naturalprogramming.com

#  2009-11-26  File created.
#  2009-11-30  Last modification.

#  This program demonstrates some basic drawing operations.

#  In the Qt drawing system there is a pen and a brush in use:

#    - The pen specifies the color which is used to draw the outlines
#      of graphical objects. Default color is black.
#    - The brush specifies the color which is used to fill graphical
#      objects. (Default is Qt.NoBrush)

#  Drawing methods are explained at
#  http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/qpainter.html

import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DrawingDemoWindow( QWidget ) :

   def __init__( self, parent = None ) :

      QWidget.__init__( self, parent )

      self.setGeometry( 100, 100, 600, 500 )
 
      self.setWindowTitle( "DRAWING OPERATIONS DEMONSTRATED" )


   def paintEvent( self, event ) :
   
      painter = QPainter()
      painter.begin( self )

      window_width  = self.width()
      window_height = self.height()

      painter.drawText( 20, 20, "Window size is %dx%d "  %  \
                                ( window_width, window_height ) )

      painter.drawLine( 0, 100, 500, 100 )
      painter.drawLine( 0, 300, 500, 300 )

      painter.drawLine( window_width / 2, 0,
                        window_width / 2, window_height ) ;

      #  The fillRect() method fills a rectangle without drawing
      #  its outline with the current pen.

      painter.fillRect( 20,  50, 100, 40, Qt.magenta )

      painter.fillRect( 20, 200, 100,  80, Qt.magenta )

      #  The drawRect() method draws a rectangle with the current
      #  pen and fills it with the current brush, which is Qt.NoBrush
      #  in this phase.

      painter.drawRect( 10, 190, 120, 100 )

      #  The corresponding PyGTK and Java programs have a statement
      #  that copies a specified sub-area to another
      #  location on the drawable area. This is left out from this
      #  program as there seems to be no QPainter methods for it.


      #  The 'brush' of the painting system means the color with which
      #  graphical objects are filled.

      painter.setBrush( Qt.darkGreen )

      #  The drawPie() method draws a pie into the specified rectangle.
      #  The second parameter specifies the start angle of the pie,
      #  and the third parameter spcifies the pie arc.
      #  Angles are expressed in 1/16ths of a degree.
      #  45 degrees is thus represented by value 45*16

      painter.drawPie( QRect(  20, 350, 100, 80 ),  45*16, 270*16 )
      painter.drawPie( QRect( 170, 350, 100, 80 ), 315*16,  90*16 )


      painter.drawRect( 350, 50, 100, 40 )

      #  eraseRect() is used to clear a part of the just drawn rectangle.

      painter.eraseRect( QRect( 360, 60,  80, 20 ) )


      #  A polygon can be drawn by giving the polygon points as 
      #  parameters to the drawPolygon() method.

      painter.drawPolygon( QPoint( 400, 150 ), QPoint( 450, 180 ),
                           QPoint( 450, 220 ), QPoint( 400, 250 ),
                           QPoint( 350, 220 ), QPoint( 350, 180 ) )

      #  To draw graphical shapes that are not filled with a color
      #  we must 'destroy' the current brush with the followings statement.

      painter.setBrush( Qt.NoBrush ) 

      painter.drawEllipse( 350, 350, 100, 80 )
      painter.drawRect( 350, 350, 100, 80 )

      painter.drawText( 350, 350, "X" )

      painter.end()

#  Here is the main program:

def main( args ) :

   this_application = QApplication( args )
   application_window = DrawingDemoWindow()
   application_window.show()

   this_application.exec_()
  
if __name__== "__main__" :

   main( sys.argv )
