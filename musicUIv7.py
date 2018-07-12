#! /usr/bin/env python

from mp3_tagger import MP3File, VERSION_1, VERSION_2, VERSION_BOTH
import sys
import time
import glob
import pygame.mixer
import os
#import sys
import pickle
from tkinter import messagebox
from tkinter import font as Font
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

#import musicUI_support
import random
def __hash__(self):
    value = 0x345678
    x = random.randint(1,1000)
    for item in self:
        value = c_mul(1000003*x, value) ^ hash(item)
    value = value ^ len(self)
    if value == -1:
        value = -2
    return value

def c_mul(a, b):
    return eval(hex((a * b) & 0xFFFFFFFF)[:-1])

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val,time1, w, root, top, labelSong, labelArtist, labelAlbum, labelGenre
    root = Tk()
    time1 = ''
    labelSong=StringVar()
    labelSong.set('<Song Name>')
    labelGenre=StringVar()
    labelGenre.set('<Genre>')
    labelAlbum=StringVar()
    labelAlbum.set('<Album>')
    labelArtist=StringVar()
    labelArtist.set('<Artist>')
    #labelTime=StringVar()
    top = New_Toplevel (root)
    maininit(top)
#    musicUI_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, tp
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    musicUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font11 = "-family {Century Gothic} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x390+405+118")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Search",
                command=onsearchClick)
#        self.menubar.add_command(
#                activebackground="#d8d8d8",
#                activeforeground="#000000",
#                background="#d9d9d9",
#                font="TkMenuFont",
#                foreground="#000000",
#                label="Create Playlist",
#                command=onplaylcClick)
        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Modify",
                command=onmodClick)
        self.menubar.add_command(
                activebackground="#d8d8d8",
                activeforeground="#000000",
                background="#d9d9d9",
                font="TkMenuFont",
                foreground="#000000",
                label="Export",
                command=onexpClick)


        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.5, rely=0.0, relheight=1.14, relwidth=0.51)
        self.TNotebook1.configure(width=304)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="All Songs", compound="left", underline="-1"
                ,)
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="Playlists", compound="left", underline="-1"
                ,)
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")

        self.Scrolledlistbox1 = ScrolledListBox(self.TNotebook1_t0)
        self.Scrolledlistbox1.place(relx=0.07, rely=0.02, relheight=0.82
                , relwidth=0.84)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        self.Scrolledlistbox1.bind("<<ListboxSelect>>",lselect2)
        self.Scrolledlistbox1.bind("<Enter>",lfocus)

        self.Scrolledlistbox2 = ScrolledListBox(self.TNotebook1_t1)
        self.Scrolledlistbox2.place(relx=0.03, rely=0.02, relheight=0.67
                , relwidth=0.9)
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(foreground="black")
        self.Scrolledlistbox2.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox2.configure(selectforeground="black")
        self.Scrolledlistbox2.configure(width=10)
        self.Scrolledlistbox2.bind("<<ListboxSelect>>",lselect2)
        self.Scrolledlistbox2.bind("<Enter>",lfocus2)

        self.Entry1 = Entry(self.TNotebook1_t1)
        self.Entry1.place(relx=0.0, rely=0.81,height=20, relwidth=0.55)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Button6 = Button(self.TNotebook1_t1)
        self.Button6.place(relx=0.67, rely=0.81, height=24, width=57)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Go''')
        self.Button6.configure(command=goPlay)
        
        self.Label3 = Label(self.TNotebook1_t1)
        self.Label3.place(relx=0.0, rely=0.74, height=21, width=95)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Choose a Playlist''')
        
        
        self.Button7 = Button(self.TNotebook1_t1)
        self.Button7.place(relx=0.67, rely=0.74, height=24, width=57)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Back''', command=gback)
#        self.Label1 = Label(top)
#        self.Label1.place(relx=0.03, rely=0.18, height=51, width=244)
#        self.Label1.configure(activebackground="#f9f9f9")
#        self.Label1.configure(activeforeground="black")
#        self.Label1.configure(background="#d9d9d9")
#        self.Label1.configure(disabledforeground="#a3a3a3")
#        self.Label1.configure(font=font11)
#        self.Label1.configure(foreground="#000000")
#        self.Label1.configure(highlightbackground="#d9d9d9")
#        self.Label1.configure(highlightcolor="black")
#        self.Label1.configure(text='''Song Name''')
#
#        self.Label2 = Label(top)
#        self.Label2.place(relx=0.17, rely=0.33, height=31, width=84)
#        self.Label2.configure(activebackground="#f9f9f9")
#        self.Label2.configure(activeforeground="black")
#        self.Label2.configure(background="#d9d9d9")
#        self.Label2.configure(disabledforeground="#a3a3a3")
#        self.Label2.configure(foreground="#000000")
#        self.Label2.configure(highlightbackground="#d9d9d9")
#        self.Label2.configure(highlightcolor="black")
#        self.Label2.configure(text='''Time-1:12/3:12''')
        self.Label1 = Label(top)
        self.Label1.place(relx=0.03, rely=0.05, height=51, width=250)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(textvariable=labelSong)
        lbsong_tooltip = CreateToolTip(self.Label1, labelSong, 'Song Name:\n')
        
        self.Label2 = Label(top)
        self.Label2.place(relx=0.17, rely=0.46, height=31, width=84)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
       # self.Label2.configure(textvariable=labelTime)

        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.05, rely=0.59, relheight=0.17, relwidth=0.41)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=245)

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.04, rely=0.15, height=44, width=87)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Play''')
        self.Button1.configure(command=playcmd)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.57, rely=0.15, height=44, width=87)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Add to Playlist''')
        self.Button2.configure(command=onplayaddClick)

        self.Frame2 = Frame(top)
        self.Frame2.place(relx=0.05, rely=0.82, relheight=0.19, relwidth=0.41)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=245)

        self.Button3 = Button(self.Frame2)
        self.Button3.place(relx=0.37, rely=0.27, height=24, width=69)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Play/Pause''',command=play_pause)

        self.Button4 = Button(self.Frame2)
        self.Button4.place(relx=0.73, rely=0.27, height=24, width=35)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Next''',command=nextsong)

        self.Button5 = Button(self.Frame2)
        self.Button5.place(relx=0.04, rely=0.27, height=24, width=56)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Previous''',command=previoussong)
        
        self.Label4 = Label(top)
        self.Label4.place(relx=0.03, rely=0.21, height=21, width=250)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(textvariable=labelArtist)
        self.Label4.configure(width=132)
        lbartist_tooltip = CreateToolTip(self.Label4, labelArtist, 'Artist:\n')
        
        self.Label5 = Label(top)
        self.Label5.place(relx=0.03, rely=0.28, height=21, width=250)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(textvariable=labelAlbum)
        self.Label5.configure(width=34)
        lbalbum_tooltip = CreateToolTip(self.Label5, labelAlbum, 'Album:\n')

        self.Label6 = Label(top)
        self.Label6.place(relx=0.03, rely=0.36, height=21, width=250)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(textvariable=labelGenre)
        lbgenre_tooltip = CreateToolTip(self.Label6,labelGenre,'Genre:\n')

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, tvar, text='widget info',
                 bg='#FFFFD4',
                 pad=(5, 3, 5, 3),
                 waittime=400,
                 wraplength=250
                 ):
        self.waittime = waittime  # in miliseconds, originally 500
        self.wraplength = wraplength  # in pixels, originally 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.onEnter)
        self.widget.bind("<Leave>", self.onLeave)
        self.widget.bind("<ButtonPress>", self.onLeave)
        self.bg = bg
        self.pad = pad
        self.id = None
        self.tw = None
        self.tvar = tvar

    def onEnter(self, event=None):
        self.schedule()

    def onLeave(self, event=None):
        self.unschedule()
        self.hide()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.show)

    def unschedule(self):
        id_ = self.id
        self.id = None
        if id_:
            self.widget.after_cancel(id_)

    def show(self):
        def tip_pos_calculator(widget, label,
                               *,
                               tip_delta=(10, 5), pad=(5, 3, 5, 3)):

            w = widget

            s_width, s_height = w.winfo_screenwidth(), w.winfo_screenheight()

            width, height = (pad[0] + label.winfo_reqwidth() + pad[2],
                             pad[1] + label.winfo_reqheight() + pad[3])

            mouse_x, mouse_y = w.winfo_pointerxy()

            x1, y1 = mouse_x + tip_delta[0], mouse_y + tip_delta[1]
            x2, y2 = x1 + width, y1 + height

            x_delta = x2 - s_width
            if x_delta < 0:
                x_delta = 0
            y_delta = y2 - s_height
            if y_delta < 0:
                y_delta = 0

            offscreen = (x_delta, y_delta) != (0, 0)

            if offscreen:

                if x_delta:
                    x1 = mouse_x - tip_delta[0] - width

                if y_delta:
                    y1 = mouse_y - tip_delta[1] - height

            offscreen_again = y1 < 0  # out on the top

            if offscreen_again:
                # No further checks will be done.

                # TIP:
                # A further mod might automagically augment the
                # wraplength when the tooltip is too high to be
                # kept inside the screen.
                y1 = 0

            return x1, y1

        bg = self.bg
        pad = self.pad
        widget = self.widget

        # creates a toplevel window
        self.tw = Toplevel(widget)

        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tx =StringVar()
        self.tx.set(self.text+self.tvar.get())
        win = Frame(self.tw,
                       background=bg,
                       borderwidth=0)
        label = ttk.Label(win,
                          textvariable=self.tx,
                          justify=LEFT,
                          background=bg,
                          relief=SUNKEN,
                          borderwidth=0,
                          wraplength=self.wraplength)

        label.grid(padx=(pad[0], pad[2]),
                   pady=(pad[1], pad[3]),
                   sticky=NSEW)
        win.grid()

        x, y = tip_pos_calculator(widget, label)

        self.tw.wm_geometry("+%d+%d" % (x, y))

    def hide(self):
        tw = self.tw
        if tw:
            tw.destroy()
        self.tw = None


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


class ModifyDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+502+146")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.protocol("WM_DELETE_WINDOW",  self.on_close)

        mp = MP3File(cpath)
        self.oldt = mp.song   #to delete old tags from the index file these variables are used
        self.oldart = mp.artist
        self.oldalb = mp.album
        self.olgenre = mp.genre

        self.Label1 = Label(top)
        self.Label1.place(relx=0.12, rely=0.11, height=31, width=254)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Enter the field to be modified''')
        self.Label1.configure(width=254)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.15, rely=0.24, height=27, width=88)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Song Name''')

        self.Label3 = Label(top)
        self.Label3.place(relx=0.15, rely=0.33, height=27, width=43)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Artist''')

        self.Label4 = Label(top)
        self.Label4.place(relx=0.15, rely=0.42, height=27, width=52)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font10)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Album''')

        self.Label5 = Label(top)
        self.Label5.place(relx=0.15, rely=0.51, height=27, width=48)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font10)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Genre''')

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.35, rely=0.27,height=20, relwidth=0.27)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry2 = Entry(top)
        self.Entry2.place(relx=0.35, rely=0.36,height=20, relwidth=0.27)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = Entry(top)
        self.Entry3.place(relx=0.35, rely=0.44,height=20, relwidth=0.27)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Entry4 = Entry(top)
        self.Entry4.place(relx=0.35, rely=0.53,height=20, relwidth=0.27)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.7, rely=0.27, height=24, width=90)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Modify Name''',command = self.modifyname)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.7, rely=0.36, height=24, width=90)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Modify Artist''',command = self.modifyartist)
        self.Button2.configure(width=90)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.7, rely=0.44, height=24, width=90)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Modify Album''',command = self.modifyalbum)
        self.Button3.configure(width=88)

        self.Button4 = Button(top)
        self.Button4.place(relx=0.7, rely=0.53, height=24, width=90)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Modify Genre''',command = self.modifygenre)

    def modifyname(self):
        global d
        name = self.Entry1.get()
        mp = MP3File(cpath)
        self.oldt = mp.song
        mp.song = name
        print(mp.song)
        mp.save()
        del d[self.oldt, self.oldart, self.oldalb, self.olgenre]
        d[mp.song, mp.artist, mp.album, mp.genre] = cpath

    def modifyartist(self):
        global d
        artist = self.Entry2.get()
        mp = MP3File(cpath)
        self.oldart = mp.artist
        mp.artist = artist
        print(mp.artist)
        mp.save()
        del d[self.oldt, self.oldart, self.oldalb, self.olgenre]
        d[mp.song, mp.artist, mp.album, mp.genre] = cpath

    def modifyalbum(self):
        global d
        album = self.Entry3.get()
        mp = MP3File(cpath)
        self.oldalb = mp.album
        mp.album = album
        print(mp.album)
        mp.save()
        del d[self.oldt, self.oldart, self.oldalb, self.olgenre] #delete the old tags from the dictionary
        d[mp.song, mp.artist, mp.album, mp.genre] = cpath #add new element to the dictionary which has modified values

    def modifygenre(self):
        global d
        genre = self.Entry4.get()
        mp = MP3File(cpath)
        self.olgenre = mp.genre
        mp.genre = genre
        print(mp.genre)
        mp.save()
        del d[self.oldt, self.oldart, self.oldalb, self.olgenre]
        d[mp.song, mp.artist, mp.album, mp.genre] = cpath
    def on_close(self):
        close = messagebox.askokcancel("Close", "Would you like to close the window?")
        if close:
            self.top.destroy()
            mp = MP3File(cpath)
            labelSong.set(mp.song)
            labelAlbum.set(mp.album)
            labelArtist.set(mp.artist)
            labelGenre.set(mp.genre)
            # root.destroy()
            # vp_start_gui()
                        

def onmodClick():
    inputDialog = ModifyDialog(root)
    root.wait_window(inputDialog.top)

class SearchDialog:

    def __init__(self, parent):
        top = self.top = Toplevel(parent)
#        self.myLabel = Label(top, text='Enter your username below')
#        self.myLabel.pack()
#        self.myEntryBox = Entry(top)
#        self.myEntryBox.pack()
#        self.mySubmitButton = Button(top, text='Submit', command=self.send)
#        self.mySubmitButton.pack()
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+493+144")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.03, rely=0.04, relheight=0.07, relwidth=0.68)
        self.TEntry1.configure(width=406)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.button1 = Button(top)
        self.button1.place(relx=0.75, rely=0.04, height=31, width=125)
        self.button1.configure(activebackground="#d9d9d9")
        self.button1.configure(activeforeground="#000000")
        self.button1.configure(background="#d9d9d9")
        self.button1.configure(disabledforeground="#a3a3a3")
        self.button1.configure(foreground="#000000")
        self.button1.configure(highlightbackground="#d9d9d9")
        self.button1.configure(highlightcolor="black")
        self.button1.configure(pady="0")
        self.button1.configure(text='''Search''')
        self.button1.configure(width=107)
        self.button1.configure(command=self.search)

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.03, rely=0.16, relheight=0.8, relwidth=0.67)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="#000000")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        self.Scrolledlistbox1.bind("<<ListboxSelect>>",lselect)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.75, rely=0.18, height=74, width=127)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Modify''',command=onmodClick)
        self.Button2.configure(width=127)

        self.Button3 = Button(top)
        self.Button3.place(relx=0.75, rely=0.42, height=84, width=127)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Add To Playlist''',command=onplayaddClick)
        self.Button3.configure(width=127)
    def search(self):
        global d
        self.Scrolledlistbox1.delete(0,END)
        name = self.TEntry1.get()
        # with open('index.p', 'rb') as fp:
        #     data = pickle.load(fp)
        l = []
        for k,v in d.items():
            #some songs have names with null character padding-'\x00'.So we do rstrip
            if name in (x.rstrip('\x00') for x in k):
                l.append(v)
        for i in l:
            self.Scrolledlistbox1.insert(END, i)
    def send(self):
#        self.username = self.myEntryBox.get()
        self.top.destroy()
        root.update()

def onsearchClick():
    inputDialog = SearchDialog(root)
    inputDialog.TEntry1.insert(END, 'Enter Song Name,album,artist or genre')
    root.wait_window(inputDialog.top)

class PlaylistDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("342x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        self.spath = ""
        

        self.Button1 = Button(top)
        self.Button1.place(relx=0.29, rely=0.16, height=44, width=136)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''AddToNewPlaylist''', command=self.createpl)
        self.Button1.configure(width=136)

        self.Button2 = Button(top)
        self.Button2.place(relx=0.29, rely=0.84, height=44, width=137)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''AddToExistingPlaylist''', command=self.addexpl)
        self.Button2.configure(width=137)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.12, rely=0.04,height=40, relwidth=0.74)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=254)

        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.12, rely=0.31, relheight=0.48
                , relwidth=0.73)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        self.Scrolledlistbox1.bind("<<ListboxSelect>>",lselect)
        #self.Scrolledlistbox1.bind("<Enter>",self.lbinit)
    def createpl(self):
        global p, w
        name = self.Entry1.get()
        if name in p:
            return
        else:
            dp = []
            p.append(name)
            mp3 = MP3File(cpath)
            dp.append(cpath)
            dp=tuple(dp)
            with open(name+".p", 'wb') as fp:
                pickle.dump(dp, fp, protocol=pickle.HIGHEST_PROTOCOL)
            self.top.destroy()
#            print(w)
            root.destroy()
            vp_start_gui()
    def addexpl(self):
        dp = ()
        mp3 = MP3File(self.spath)
        dp += (self.spath,)
        with open(cpath+".p", 'ab') as fp:
            pickle.dump(dp, fp, protocol=pickle.HIGHEST_PROTOCOL)
        self.top.destroy()
        root.destroy()
        vp_start_gui()


def onplayaddClick():
    inputDialog = PlaylistDialog(root)
    inputDialog.spath = cpath
    print(inputDialog.spath)
    for i in p:
            inputDialog.Scrolledlistbox1.insert(END,i)
    root.wait_window(inputDialog.top)

        
class ExpDialog:
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("358x450+466+158")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Scrolledlistbox1 = ScrolledListBox(top)
        self.Scrolledlistbox1.place(relx=0.11, rely=0.04, relheight=0.66
                , relwidth=0.78)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font=font10)
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        self.Scrolledlistbox1.configure(width=10)
        self.Scrolledlistbox1.bind("<<ListboxSelect>>",lselect)

        self.Button1 = Button(top)
        self.Button1.place(relx=0.28, rely=0.76, height=44, width=157)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Export''')
        self.Button1.configure(width=157, command=self.exportpl)
    
    def exportpl(self):
        dpx = []
        with open(cpath+'.p', 'rb') as fp:
            while True:
                try:
                    x = pickle.load(fp)
                except EOFError:
                    break
                dpx.append(x[0])
        os.makedirs('xport', exist_ok=True)
        with open('xport\\'+cpath+'.m3u', 'w') as fp:
            for song in dpx:
                fp.write(song+'\n')
        self.top.destroy()
        
def onexpClick():
    inputDialog = ExpDialog(root)
    for i in p:
            inputDialog.Scrolledlistbox1.insert(END,i)
    root.wait_window(inputDialog.top)
        
focs=""
def lfocus(self):
    global focs
    focs="lb1"

def lfocus2(self):
    global focs
    focs="lb2"


currentlb="lb1"
def lselect(evt):
    global cindex,cpath,top, root, focs, currentlb
    try:
        w=evt.widget
#        print(w)
        cindex = int(w.curselection()[0])

        cpath = (w.get(ANCHOR))
##        if focs == "lb1":
##            currentlb = "lb1"
##        elif focs == "lb2":
##            currentlb = "lb2"
#        print(currentlb)
    except:
        pass

def lselect2(evt):
    global cindex,cpath,top, root, focs, currentlb
    try:
        w=evt.widget
#        print(w)
        cindex = int(w.curselection()[0])
        cpath = (w.get(ANCHOR))
        if focs == "lb1":
            currentlb = "lb1"
        elif focs == "lb2":
            currentlb = "lb2"
        if cpath.endswith('.mp3'):
            mp3 = MP3File(cpath)
            labelSong.set(mp3.song)
            labelAlbum.set(mp3.album)
            labelArtist.set(mp3.artist)
            labelGenre.set(mp3.genre)
#        print(currentlb)
    except:
        pass
    

def gback():
    global top, p, data, playlist
    w = top.Scrolledlistbox2
    w.delete(0, END)
    for plname in p:
        w.insert(END, plname)

data={}
def goPlay():
    global top,p,data, playlist, pl
#    try:
    if str(top.Entry1.get()) in p:
        pl = []
        dpx=[]
        w=top.Scrolledlistbox2
        w.delete(0, END)
        with open(r'C:\Python\\'+str(top.Entry1.get())+'.p', 'rb') as fp:
            while True:
                try:
                    x = pickle.load(fp)
                except EOFError:
                    break
                dpx.append(x[0])
                print(dpx)
        for val in dpx:
            w.insert(END,val)
            pl.append(val)
#    except:
#          pass  

def tagdefn(mp3,i):
    mp3.set_version(VERSION_2)
    tags = mp3.get_tags()
    mp3.song = tags.get('song','Invalid'+str(i))
    mp3.artist = tags.get('artist','Invalid'+str(i))
    mp3.album = tags.get('album','Invalid'+str(i))
    mp3.genre = tags.get('genre','Invalid'+str(i))
    mp3.save()

def playcmd():
    global paused
    pygame.mixer.music.load(cpath)
    pygame.mixer.music.play()
    tick()
    paused=False

def play_pause():
    global paused
    if paused:
            pygame.mixer.music.unpause()
            paused = False
    elif not paused:
            pygame.mixer.music.pause()
            paused = True

def nextsong():
    global cindex
    if currentlb == 'lb1':
        if cindex == len(mp3_list)-1:
            return
        else:
            cindex +=1
            mp3 = MP3File(mp3_list[cindex])
            labelSong.set(mp3.song)
            labelAlbum.set(mp3.album)
            labelArtist.set(mp3.artist)
            labelGenre.set(mp3.genre)
            pygame.mixer.music.load(mp3_list[cindex])
            pygame.mixer.music.play()
    elif currentlb == 'lb2':
        if cindex == len(pl)-1:
            return
        else:
            cindex +=1
            mp3 = MP3File(pl[cindex])
            labelSong.set(mp3.song)
            labelAlbum.set(mp3.album)
            labelArtist.set(mp3.artist)
            labelGenre.set(mp3.genre)
            pygame.mixer.music.load(pl[cindex])
            pygame.mixer.music.play()


def previoussong():
    global cindex
    if currentlb == 'lb1':
        if cindex == 0:
            return
        else:
            cindex -=1
            mp3 = MP3File(mp3_list[cindex])
            labelSong.set(mp3.song)
            labelAlbum.set(mp3.album)
            labelArtist.set(mp3.artist)
            labelGenre.set(mp3.genre)
            pygame.mixer.music.load(mp3_list[cindex])
            pygame.mixer.music.play()
    elif currentlb == 'lb2':
        if cindex == 0:
            return
        else:
            cindex -=1
            mp3 = MP3File(pl[cindex])
            labelSong.set(mp3.song)
            labelAlbum.set(mp3.album)
            labelArtist.set(mp3.artist)
            labelGenre.set(mp3.genre)
            pygame.mixer.music.load(pl[cindex])
            pygame.mixer.music.play()

d = {}
def maininit(top):
    global mp3_list, p, d
    obj=top.Scrolledlistbox1
    mp3_list=[]
    for file in glob.iglob(r'C:\Users\Siddharth\Music\*.mp3', recursive=True):#r is before path to make it a raw string and ignore escape chars.
        mp3_list.append(file)
        obj.insert(END, file)
    mp3_list=list(mp3_list)
    
    p=[]
    playlist=[]
    for plpath in glob.iglob(r'C:\Python\*.p', recursive=True):
        if plpath.endswith('index.p'):
            continue
        playlist.append(plpath)
    playlist=list(playlist)
    for i in playlist:
        p.append(os.path.basename(i).rstrip('.p'))
        top.Scrolledlistbox2.insert(END,os.path.basename(i).rstrip('.p'))

    i = 0
    for x in mp3_list:
        i+=1
        mp3 = MP3File(x)
        tagdefn(mp3,i)
        d[mp3.song, mp3.artist, mp3.album, mp3.genre] = x


    with open('index.p', 'wb') as fp:
        pickle.dump(d, fp, protocol=pickle.HIGHEST_PROTOCOL)
#    root.protocol("WM_DELETE_WINDOW",  close_main)
    
#def close_main():
#    global top
#    close = messagebox.askokcancel("Close", "Would you like to close the program?")
#    if close:
#        root.destroy()
#        pygame.mixer.quit()
#        sys.exit(0)

def tick():
    global time1, global_index, top

    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2

        time_in_secs = int(pygame.mixer.music.get_pos() / 1000)
        top.Label2.config(text="Time: " + str(int(time_in_secs / 60)) + ":" + str(time_in_secs % 60))

      #  scale2.set((time_in_secs/ global_audio.info.length) * 100) 

    top.Label2.after(200, tick)
        
    

if __name__ == '__main__':
    pygame.mixer.init()
    vp_start_gui()



