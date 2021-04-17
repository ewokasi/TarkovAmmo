# -*- coding: UTF-8 -*-
from tkinter import *

import tk as tk
boole=0

def clicked():
    search()

def switchStayOnTop():
    global boole
    if boole==0:

        boole=1

    else:

        boole = 0
    root.attributes('-topmost', boole)
    print(boole)


def search ():
    x = str(entry.get())
    flag = False
    sovpadeni = 0
    for i in range(0, len(allData)):

        if x.upper() in str(allData[i][0:len(allData[i])-18]).upper() or x.lower() in str(allData[i][0:len(allData[i])-18]).lower():

                        #####Названия параметров#####
            sovpadeni = sovpadeni+1
            po6klassy=allData[i][len(allData[i])-1]
            po5klassy=allData[i][len(allData[i])-2]
            po4klassy=allData[i][len(allData[i])-3]
            po3klassy=allData[i][len(allData[i])-4]
            po2klassy=allData[i][len(allData[i])-5]
            po1klassy=allData[i][len(allData[i])-6]

            isTrasser = allData[i][len(allData[i])-7]
            if isTrasser =='—':
                isTrasser= 'Not trasser'
            else: isTrasser = 'Is trasser'
            rikoshet = allData[i][len(allData[i])-8]

            lightBleeding = allData[i][len(allData[i])-9]
            if lightBleeding == '—':
                lightBleeding = 'none'
            hardBleeding = allData[i][len(allData[i])-10]
            if hardBleeding == '—':
                hardBleeding = 'none'

            fragmentation = allData[i][len(allData[i])-11]
            recoil = allData[i][len(allData[i])-12]
            tochnost = allData[i][len(allData[i])-13]

            kolvoOfObj =allData[i][len(allData[i])-14]
            speed =allData[i][len(allData[i])-15]
            armorDamageEqu = allData[i][len(allData[i])-16]
            armorD = allData[i][len(allData[i]) - 17]
            penetr = allData[i][len(allData[i])-18]
            damage =allData[i][len(allData[i])-19]

            calibr = allData[i][0]
            nameingPatrona = str(allData[i][1])

            flag = True

                            #####Вывод#####

            print('\n'+calibr+'', nameingPatrona+':', isTrasser)
            print('     Урон:', damage+',', 'Пробитие:', penetr,'\n','\t'+" "+ speed+' m/s,','Фрагментов:'+kolvoOfObj, ", Урон броне%:", armorD)
            print('     Сильное кровотечеине%: '+hardBleeding,'\n',"    Слаьое кровотечение%: "+lightBleeding)
            print('     Extra props:','\n', '    Отдача:', recoil, ", Точность:", tochnost, ', Шанс фрагментации', fragmentation)

            if sovpadeni==1:
                outp.configure(text=calibr+" "+nameingPatrona+': '+isTrasser +'\n' 'Урон:' + damage+', '+ 'Пробитие:'+ penetr+'\n'+ speed+' м/с, '+'Фрагментов:'+kolvoOfObj+ ", Урон броне%:"+ armorD +  '\n'  'Отдача: '+ recoil+ ", Точность:"+ tochnost+ ', Шанс фрагм '+ fragmentation)
                lbl21.configure(text=po1klassy)
                lbl22.configure(text=po2klassy)
                lbl23.configure(text=po3klassy)
                lbl24.configure(text=po4klassy)
                lbl25.configure(text=po5klassy)
                lbl26.configure(text=po6klassy)
                            #####Ошибка#####
            elif sovpadeni==2:
                outp2.configure(text=calibr+" "+nameingPatrona+': '+isTrasser +'\n' 'Урон:' + damage+', '+ 'Пробитие:'+ penetr+'\n'+ speed+' м/с, '+'Фрагментов:'+kolvoOfObj+ ", Урон броне%:"+ armorD +  '\n'  'Отдача: '+ recoil+ ", Точность:"+ tochnost+ ', Шанс фрагм '+ fragmentation)
            elif sovpadeni==3:
                outp3.configure(text=calibr+" "+nameingPatrona+': '+isTrasser +'\n' 'Урон:' + damage+', '+ 'Пробитие:'+ penetr+'\n'+ speed+' м/с, '+'Фрагментов:'+kolvoOfObj+ ", Урон броне%:"+ armorD +  '\n'  'Отдача: '+ recoil+ ", Точность:"+ tochnost+ ', Шанс фрагм '+ fragmentation)

        elif i ==len(allData)-1 and not flag:
            print("Not found. Try again with another name")
            break


file = open('data.txt', encoding="utf8")
stroks = file.readlines()

allData = []

for i in range(len(stroks)):
    allData.append(stroks[i].split())


                        #####Интерфейс######
 #### цвета #1c1c1b - черный, #877c61 - хаки, #b5b1b1 - белый
black = '#1c1c1b'
hacki='#877c61'
white='#b5b1b1'

root = Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2 # середина экрана
h = h//2
w = w + 200 # смещение от середины
h = h + 100

root.title('TarkovAmmo')
root.geometry('550x300+{}+{}'.format(w, h))
root.configure(bg=black)
root.resizable(width=True, height=True)


#polzyn = Scrollbar(root)
#polzyn.place(relx=0.95, rely=0.1)

stayFrame=Frame(root)
stayFrame.configure(width=100, height = 20, bg=black)
stayFrame.place(relx=0,rely=0)


stayTopBool= 0

stayOnTop=Checkbutton(stayFrame, command=switchStayOnTop)
stayOnTop.configure(bg=black, text="Stay on top", fg=white)
stayOnTop.grid(column=0, row=0)


entry = Entry(root)
entry.focus()
entry.place(relx=0.10, rely=0.15)
entry.configure(bg=hacki, bd=0,fg=white, highlightcolor=white)

armorFrame=Frame(root)
armorFrame.configure(width=230, height = 60, bg=black)

armorFrame.place(relx=0.5, rely=0.32)

btn = Button(root, text='Search', command=clicked, bg=black, bd=3, fg=white, highlightcolor=hacki)
btn.place(relx=0.5, rely=0.14)

outp = Label(root, text="",bg=black, fg=hacki, justify = 'left')
outp.place(relx=0.0, rely=0.3)
outp2 = Label(root, text="",bg=black, fg=hacki, justify = 'left')
outp2.place(relx=0.0, rely=0.6)
outp3 = Label(root, text="",bg=black, fg=hacki, justify = 'left')
outp3.place(relx=0.0, rely=0.9)

dopLbl1= Label(root, text='Enter the type of ammo:', bg = black, fg=white)
dopLbl1.place(relx=0.08, rely=0.08)

lbl11=Label(armorFrame, text= '|1 кл|')
lbl12=Label(armorFrame, text= '|2 кл|')
lbl13=Label(armorFrame, text= '|3 кл|')
lbl14=Label(armorFrame, text= '|4 кл|')
lbl15=Label(armorFrame, text= '|5 кл|')
lbl16=Label(armorFrame, text= '|6 кл|')
lbl11.grid(column=0, row=1)
lbl12.grid(column=1, row=1)
lbl13.grid(column=2, row=1)
lbl14.grid(column=3, row=1)
lbl15.grid(column=4, row=1)
lbl16.grid(column=5, row=1)
lbl11.configure(bg=black,fg=hacki)
lbl12.configure(bg=black,fg=hacki)
lbl13.configure(bg=black,fg=hacki)
lbl14.configure(bg=black,fg=hacki)
lbl15.configure(bg=black,fg=hacki)
lbl16.configure(bg=black,fg=hacki)

lbl21=Label(armorFrame, text= '')
lbl22=Label(armorFrame, text= '')
lbl23=Label(armorFrame, text= '')
lbl24=Label(armorFrame, text= '')
lbl25=Label(armorFrame, text= '')
lbl26=Label(armorFrame, text= '')
lbl21.grid(column=0, row=2)
lbl22.grid(column=1, row=2)
lbl23.grid(column=2, row=2)
lbl24.grid(column=3, row=2)
lbl25.grid(column=4, row=2)
lbl26.grid(column=5, row=2)
lbl21.configure(bg=black,fg=hacki)
lbl22.configure(bg=black,fg=hacki)
lbl23.configure(bg=black,fg=hacki)
lbl24.configure(bg=black,fg=hacki)
lbl25.configure(bg=black,fg=hacki)
lbl26.configure(bg=black,fg=hacki)
lbl00=Label(armorFrame,text="Эффективность по 8-ми балльной шкале", bg=black, fg=hacki)
lbl00.grid(column=0, row=0, columnspan=6)





root.mainloop()


