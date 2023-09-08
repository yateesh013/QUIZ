import tkinter as tk
from tkinter import messagebox
import time
def w1():
    main=tk.Tk()
    main.title("QUIZ APP.")

    main.geometry("500x500")

    l1=tk.LabelFrame(main,text="QUIZ",bg="green")
    l1.place(x=100,y=50)

    l2=tk.Label(l1,bg="blue",text="HELLO WLCOME TO THE ELECTRONICS AND \nCOMMUNICATION QUIZ.")
    l2.pack()


    l3=tk.Label(text="NAME :").place(x=100 ,y=150)

    name=tk.Entry(justify="left")   
    name.place(x=150,y=150)
    def verify_name():
        if name.get()=="":
            messagebox.showerror("NAME ERROR","ENTER YOUR NAME")
        else:
            w2()    
    def clear():
        for item in main.winfo_children():
            item.destroy() 
    def w2():
        name_1=name.get()
        clear()
        l4=tk.Label(text=f"HELLO {name_1.upper()},WELCOME TO THE QUIZ.\nREAD THE BELOW RULES CAREFULLY .")
        l4.place(x=150,y=100)

        l5=tk.LabelFrame(main,bg="red",text="RULES AND REGULATIONS:")
        l5.place(x=100,y=150)
    
        l6=tk.Label(l5,bg="green",text="1.ONE POINT AWARDED FOR CORRECT ANSWER.\n2.NO NEGATIVE MARKING.\n3.CLOSING THE WINDOW IS CONSIDERED AS FAIL.\n4.THERE ARE 5 QUESTIONS IN QUIZ.\n5.EACH CONTAIN 4 OPTIONS & CARRY EQUAL MARKS.\n6.ONLY ONE CHANCE IS ALLOWED TO ANSWER,\nFIRST RESPONSE WILL BE RECORDED.\n\n      ALL THE BEST!")
        l6.pack()

        var1=tk.IntVar()
        b1=tk.Checkbutton(main,variable=var1,onvalue=1,offvalue=0)
        b1.place(x=100,y=400)
    
        l7=tk.Label(main,text="I AGREE TERMS & CONDITIONS.")
        l7.place(x=130,y=400)
    
        def check():
            if var1.get()==0:
                messagebox.showerror("CHECKBOX ERROR","CLICK ON THE CHECK BOX.")
            else:
                i=0
                w3(name_1,i)    
        b2=tk.Button(main,text="CONTINUE",command=check,pady="3",border="5")
        b2.place(x=400,y=400)  
    go1=tk.Button(text="CONTINUE",bg="silver",fg="black",pady="3",border="5",command=verify_name)
    go1.place(x=400,y=400)
    sc=[0]   
    ver_que=[] 
    def w3(name,i):
        num=i
        name_2=name
        clear()
        ques=["1. how a current source is connected to circuit.","2. what is a passive element in below:","3. what is the advantage of ofc","4. in parallel connection which is common parameter","5. which amplifies signal without change \nin frequency or phase of signal"]
        ans=[["1. in series","2. in parallel","3. either in series or parallel","4. all"],["1. transformer","2. transistor","3. diode","4. resistor"],["1. security","2. large bandwidth","3. both a & b","4. no amplifier or repeater needed."],["1. voltage","2. current","3. resistance","4. none"],["1. amplifier","2. rc filters","3. transformer","4. capacitor"]]
        key=[1,4,3,1,3]
        try:
            l8=tk.Label(text=f"HELLO {name.upper()} HERE IS YOUR {num+1} QUESTION.").place(x=100,y=50)
            l9=tk.LabelFrame(main,text=f"{ques[num].upper()}")
            l9.place(x=100,y=100)
            var_2=tk.IntVar()
            l10=tk.Radiobutton(l9,text=f"{ans[num][0].upper()}",variable=var_2,value=1).pack(anchor="w")
            l11=tk.Radiobutton(l9,text=f"{ans[num][1].upper()}",variable=var_2,value=2).pack(anchor="w") 
            l12=tk.Radiobutton(l9,text=f"{ans[num][2].upper()}",variable=var_2,value=3).pack(anchor="w")
            l13=tk.Radiobutton(l9,text=f"{ans[num][3].upper()}",variable=var_2,value=4).pack(anchor="w") 
            l14=tk.Label(main,text=f" ")
            l14.place(x=100,y=300)
        except:
            clear()
            def last():
                main.after(1000,main.destroy())
            l15=tk.Label(main,text=f"{name.upper()} YOUR SCORE IS :{sum(sc)}").place(x=100,y=200)
            exit_button=tk.Button(main,text=f"EXIT",command=last,pady="3",border="5").place(x=400,y=400)
        def check_key():
                if(var_2.get()==key[num] and num+1 not in ver_que):
                    l14.config(text=f"CORRECT ANSWER.")
                    sc.append(1) 
                    ver_que.append(num+1)  
                elif(num+1 in ver_que):
                    l14.config(text="RESPONSE IS ALREADY RECORDED.")    
                elif var_2.get()==0 :
                    messagebox.showwarning("OPTION ERROR","SELECT ANY ONE OPTION.")
                else:
                    l14.config(text=f"WRONG ANSWER.CORRECT OPTION IS {ans[num][(key[num])-1].upper()}")         
                    ver_que.append(num+1)
        def next_call():
            if var_2.get()!=0 and num<len(ques):
                w3(name_2,num+1)
            else:
                messagebox.showwarning("QUESTION ERROR","CANT SKIP THE QUESTION")    
        if(num<len(ques)):
            b3=tk.Button(main,text="VERIFY",command=check_key,pady="3",border="5").place(x=300,y=400)
            b4=tk.Button(main,text="NEXT",command=next_call,pady="3",border="5").place(x=400,y=400)    
    
    main.mainloop()
w1()    