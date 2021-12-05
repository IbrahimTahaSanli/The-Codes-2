from tkinter import *

root = Tk()
root.title("Text And Checkboxs")
global k , l 
k = 0 
l = []


class check():
    def __init__( self , text ):
        self.tf    = IntVar()
        self.text  = text
        self.check = ""
    
    def read():
        with open( "Text And Checkboxs.txt" , "r" ) as file :
            for line in file :
                global k
                line = line.split( sep = "  " )
                l.append( check( line[1] ) )
                l[ -1 ].add()
                if line[ 0 ] == "1" :
                    l[ -1 ].check.select()
                

    def add( self ):
        global k 
        self.check = Checkbutton( root , text = self.text , variable = self.tf , onvalue = "1" , offvalue = "0" )
        self.check.place( x = 0 , y = 30 * k + 2 )
        k += 1
        check.place( k )
        
    def dele( text ):
        global k
        del l[ int( text ) - 1 ]
        s  = 0
        k -= 1
        for o in l :
            l[s].check.place( x = 0 , y = 30 * s + 2 )
            s += 1
            check.place( s )

    def save():
        with open( "Text And Checkboxs.txt" , "w" ) as file:
            g = 0
            for u in l :
                text = str( l[g].tf.get() ) + "  " + l[g].text +"\n"
                file.writeline( text )
                g += 1


    def place( k ):
        global texten
        texten.place( x = 0 , y = 32 * k + 2 )
        abutton.place( x = 150 , y = 32 * k + 2 )
        dbutton.place( x = 180 , y = 32 * k + 2 )
        sbutton.place( x = 220 , y = 32 * k + 2 )
        root.geometry( str( 253 ) + "x" + str( 32 * ( k + 1 ) + 2 ) )




def add( text ):
    l.append( check( text ) )
    l[-1].add()

texten  = Entry( root , width = 100 )
abutton = Button( root , text = "Add" , command = lambda:add( texten.get() ) ) 
dbutton = Button( root , text = "Delete" , command = lambda:check.dele( texten.get() ) )
sbutton = Button( root , text = "Save" , command = lambda:check.save() )

try :
    file = open( "Text And Checkboxs.txt" , "r" )

except :
    pass

else :
    file.close()
    check.read()


check.place( k )

root.mainloop()
