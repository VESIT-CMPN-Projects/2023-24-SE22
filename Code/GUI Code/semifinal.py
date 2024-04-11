from cProfile import label
import glob
from optparse import Option
import tkinter as tk
from tkinter import ttk
from display_note import plot_piano_roll
import csv_Play
from tkinter import filedialog, Toplevel
import la
import convo_
import getfreq
import consec
import mixing
import M_random
import succesive
import mix_random
import band_mix
import getlist2
import mix_fr
import play_notes
import heal as he
from tonotes import midi_to_notes 
from keras.models import load_model
from play_generated import play_gen,play_gen2
from audiogen import play_generated_notes
from midi_input import midi_to_notes
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("7500x6400")



def deleteframes():
    for frame in main_frame.winfo_children():
        frame.destroy()


##############
def no():
    def p():
        play_notes.play_music(e.get())
    deleteframes()
    e=tk.Entry(main_frame,text="hello")
    e.grid(row=1,column=2)
    e.insert(0,"enter notes")
    bt1 = tk.Button(main_frame, text="PLay", command=p)
    bt1.grid(row=2, column=2, padx=60)

def mi():
    deleteframes()
    l2 = tk.Label(main_frame, text="Mixing", anchor="center", borderwidth=3, bg="#ffb6c1",justify="center",font= ("Lucida Calligraphy", 70, "bold"))
    l2.grid(row=0, column=0, padx=(400,0),pady=15)

    def mix():
        # mi()
        mixing.mix(fl1.cget("text"), fl2.cget("text"))

    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
            ("WAV files", "*.wav"), ("MP3 files", "*.mp3"), ("All files", "*.*")))
        if file_path:
            # Self.text="{}",file_path
            fl.config(text="" + file_path)

    fl1 = tk.Label(main_frame, text="")
    fl2 = tk.Label(main_frame, text="")

    ##
    def up1():
        global n1,var2
        opt2 = getlist2.s(var.get())
        n1.destroy()
        var2 = tk.StringVar()
        var2.set("select")
       
        n1 = tk.OptionMenu(main_frame, var2, *opt2)
        
        n1.grid(row=6, column=0)
    def up2():
        global n2,var3
        opt3 = getlist2.s(var1.get())
        n2.destroy()
        var3 = tk.StringVar()
        var3.set("select")
        
        n2 = tk.OptionMenu(main_frame, var3, *opt3)
        n2.grid(row=6, column=1)
    def up(n1,n2):
       up1()
       up2()
    def mbf():
        global var2,var3
        mix_fr.play_mixed_audio(var2.get(),var3.get())

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=0, padx=(0,0))
    bt2 = tk.Button(main_frame, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=1, column=1, padx=(50,50))
    #
    bt4 = tk.Button(main_frame, text="play mixed signal", command=mix)
    bt4.grid(row=1, column=4, padx=60)

    l12 = tk.Label(main_frame, text="Random Mixing", anchor="center", borderwidth=3, bg="#ffb6c1",font= ("Lucida Calligraphy", 15, "bold"))
    l12.grid(row=2, column=0, padx=(400,0),pady=(70,0))

    #
    bt5 = tk.Button(main_frame,text="mix randomly",command=band_mix.r)
    bt5.grid(row=3,column=0,padx=(350,0))
    # ye itna ho gaya ki 10 min mein video start karte hai

    # l13 = tk.Label(main_frame, text="Mix Selected", anchor="center", borderwidth=3, bg="#ffb6c1",justify="center",font= ("Lucida Calligraphy", 40, "bold"))
    # l13.grid(row=4, column=1, pady=15)

    
    bt6 = tk.Button(main_frame,text="get frequency",command= lambda:up(n1,n2))
    bt6.grid(row=6,column=0,padx=(500,0),pady=(10,10))
    bt7 = tk.Button(main_frame,text="mix selected frequency",command= mbf)
    bt7.grid(row=8,column=0,padx=(500,0),pady=(10,0))
    #bohot scattered lag raha hai konse buttons kiske kiye hai saamajh nahi aa raha
    ##ye page  me aur kya chane kar sakte?? bas thik hai vido chalu karte hai?? rehne de abhi time nahi hai
    #kal mujhe subah viva dene jaana hai?? mp ka ,ok
    # 10 min mein meet pe milte hai wait,

    

    l = tk.Label(main_frame, text="mix the band freq by selecting them from the dropdown list", bg="#ffb6c1", anchor="nw", borderwidth=3,font= ("Lucida Calligraphy", 15, "bold"))
    l.grid(row=4, column=0, padx=(200,0), pady=(120,0))
    opt = [
        "A_band",
        "B_band",
        "C_band",
        "D_band",
        "E_band",
        "F_band"
    ]

    var = tk.StringVar()
    var.set(opt[0])
    o = tk.OptionMenu(main_frame, var, *opt)
    o.grid(row=5, column=0)
    #up1()
    opt2 = getlist2.s(var.get())
    global var2
    var2 = tk.StringVar()
    var2.set("select")
    global n1
    n1= tk.OptionMenu(main_frame, var2, *opt2)
    n1.grid(row=7, column=0)
    
###############################
    #l = tk.Label(main_frame, text="Play the bands by selecting them from the dropdown list", anchor="nw", borderwidth=3)
    #l.grid(row=1, column=0, padx=90, pady=3)
    opt1 = [
        "A_band",
        "B_band",
        "C_band",
        "D_band",
        "E_band",
        "F_band"
    ]

    var1 = tk.StringVar()
    var1.set((opt1[0]))
    o2 = tk.OptionMenu(main_frame, var1, *opt1)
    o2.grid(row=5, column=1)
##
    #up2()
    opt3 = getlist2.s(var1.get())
    global var3
    var3 = tk.StringVar()
    var3.set("select")
    global n2
    n2 = tk.OptionMenu(main_frame, var3, *opt3)
    n2.grid(row=7, column=1)
####################
def con():
    deleteframes()
    l2 = tk.Label(main_frame, text="Convolution", anchor="center", borderwidth=3, bg="#ffb6c1",justify="center",font= ("Lucida Calligraphy", 56, "bold"))
    l2.grid(row=0, column=4, pady=15)

    def pcon():
        convo_.con(getfreq.get_audio_frequency(fl1.cget("text")), getfreq.get_audio_frequency(fl2.cget("text")))

    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
          ("WAV files", "*.wav"),("MP3 files", "*.mp3"),  ("All files", "*.*")))
        if file_path:
            # Self.text="{}",file_path
            fl.config(text="" + file_path)

    fl1 = tk.Label(main_frame, text="")
    fl2 = tk.Label(main_frame, text="")

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=4, padx=60)
    bt2 = tk.Button(main_frame, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=3, column=4, padx=60)
    # 
    bt3 = tk.Button(main_frame, text="play convolved signal", command=pcon)
    bt3.grid(row=5, column=4, padx=60)


def contactus():
    deleteframes()    
    
    def create_contact_us_page(root):
        # root.title("Contact Us")
        
        # Create labels for team members
        team_members = [
            {"name": "Mrunal Mahajan", "number": "+91 70581 12289", "email": "2022.mrunal.mahajan@ves.ac.in", "photo": r"C:\Users\mruna\Documents\final_mini\tarangAI\m.png"},
            {"name": "Ayush Verma", "number": "+91 91362 24186", "email": "2022.ayush.verma@ves.ac.in", "photo": r"C:\Users\mruna\Documents\final_mini\tarangAI\a.png"},
            {"name": "Latish Adwani", "number": "+91 93224 45108", "email": "2022.latish.adwani@ves.ac.in", "photo": r"C:\Users\mruna\Documents\final_mini\tarangAI\l.png"},
            {"name": "vineet chelani", "number": "+91 91720 71820", "email": "2022.vineet.chelani@ves.ac.in", "photo": r"C:\Users\mruna\Documents\final_mini\tarangAI\v.png"}
        ]
        
        for idx, member in enumerate(team_members):
            frame = tk.Frame(root, bg="#ffb6c1")
            frame.grid(row=idx//2, column=idx%2, padx=50, pady=50)  # Calculate row and column based on idx
            
            # Load and resize member's photo
            image = Image.open(member["photo"])
            image = image.resize((120, 150))  # Resize to 100x100 pixels
            photo = ImageTk.PhotoImage(image)
            
            # Create label with resized image
            photo_label = ttk.Label(frame, image=photo, background="#ffb6c1")
            photo_label.image = photo  # To prevent image from being garbage collected
            photo_label.pack()
            
            # Display member's information
            info_label = tk.Label(frame,text=f"Name: {member['name']}\nNumber: {member['number']}\nEmail: {member['email']}",font=56,fg="red",bg="#ffb6c1")
            info_label.pack()
    create_contact_us_page(main_frame)


def autoplay2():
    deleteframes()
    l2 = tk.Label(main_frame, text="midi", anchor="center", borderwidth=3, bg="#ffb6c1",justify="center",font= ("Lucida Calligraphy", 70, "bold"))
    l2.grid(row=0, column=2, pady=15)
    def display_generated_notes(generated_notes, parent_frame):
        tree = ttk.Treeview(parent_frame)
        tree["columns"] = list(generated_notes.columns)
        tree["show"] = "headings"
        for column in generated_notes.columns:
            tree.heading(column, text=column)

        for index, row in generated_notes.iterrows():
            tree.insert("", "end", values=list(row))

        tree.grid(row=2, column=2, sticky="nsew")

    def load_graph_image():
        plot_image = tk.PhotoImage(file='piano_roll.png')
        label_plot = ttk.Label(main_frame, image=plot_image )
        label_plot.image = plot_image  # To prevent image from being garbage collected
        label_plot.grid(row=5, column=2,padx=10,pady=10)


    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
            ("midi files", "*.mid"), ("midi file", "*.midi"), ("All files", "*.*")))
        if file_path:
            # Self.text="{}",file_path
            fl.config(text="" + file_path)

    mfl1 = tk.Label(main_frame, text="")
    def ap():
        play_generated_notes(generated_notes)
    def mg():
        global var2,var3,generated_notes
        notes=midi_to_notes(mfl1.cget("text"))
        # print(notes)
        generated_notes=play_gen2(notes)
        display_generated_notes(generated_notes,main_frame)
        load_graph_image()

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(mfl1))
    bt1.grid(row=1, column=1, padx=60)

    bt7 = tk.Button(main_frame,text="generate from midi",command= mg)
    bt7.grid(row=2,column=1,padx=60)

    apb2=tk.Button(main_frame,text='Play Genereted notes',command=ap)
    apb2.grid(row=1,column=3)

    


def autoplay():
    deleteframes()
    def display_generated_notes(generated_notes, parent_frame):
        tree = ttk.Treeview(parent_frame)
        tree["columns"] = list(generated_notes.columns)
        tree["show"] = "headings"
        for column in generated_notes.columns:
            tree.heading(column, text=column)

        for index, row in generated_notes.iterrows():
            tree.insert("", "end", values=list(row))

        tree.grid(row=5, column=2, sticky="nsew")

    def load_graph_image():
        plot_image = tk.PhotoImage(file='piano_roll.png')
        label_plot = ttk.Label(main_frame, image=plot_image )
        label_plot.image = plot_image  # To prevent image from being garbage collected
        label_plot.grid(row=9, column=2,padx=10,pady=10)
        
    def auto():
        global notes
        pitch=int(e1.get())
        step=float(e2.get())
        duration=float(e3.get())
        print(pitch,step,duration)
        notes=play_gen(pitch,step,duration)
        display_generated_notes(notes,main_frame)
        plot_piano_roll(notes)
        load_graph_image()

    def ap():
        play_generated_notes(notes)

    e1=tk.Entry(main_frame,text="pitch")
    e1.grid(row=2,column=1)
    e1.insert(0,"enter pitch")
    
    
    e2=tk.Entry(main_frame,text="step")
    e2.grid(row=2,column=3)
    e2.insert(0,"enter step")
    
    e3=tk.Entry(main_frame,text="duration")
    e3.grid(row=2,column=5)
    e3.insert(0,"enter duration")


    apb=tk.Button(main_frame,text='Generate Notes',command=auto)
    apb.grid(row=3,column=3)

    apb2=tk.Button(main_frame,text='Play Genereted notes',command=ap)
    apb2.grid(row=4,column=3)

Option_frame = tk.Frame(root, bg="#ADD8E6", relief="sunken", borderwidth=2)

#################
def healing():
    deleteframes()

    # def randomsound():
    #     M_random.play(var.get())

    # def conse():
    #     consec.play(var.get())

    # def s():
    #     succesive.successive(var.get())

    def h():
        t=int(get_key_from_value(frequencies_info,(var.get())))
        he.play_frequency(t,6)
        # he.play_frequency()

    def get_key_from_value(dictionary, target_value):
        for key, value in dictionary.items():
            if value == target_value:
                return key
        return None  
    new_windoe = tk.Button(main_frame, text="Play", command=h)

    l = tk.Label(main_frame, text="select healing frequency", anchor="center", borderwidth=3, bg="#ffb6c1",justify="center",font= ("Lucida Calligraphy", 12, "bold"))
    l.grid(row=1, column=2, padx=90, pady=3)


    frequencies_info = {
            "174": "Pain Reduction, Healing",
            "285": "Energy Fields, Healing",
            "396": "Emotional Healing, Liberation from Fear",
            "528": "DNA Repair, Overall Healing",
            "639": "Relationships, Interpersonal Connection",
            "741": "Problem-Solving, Intuitive Thinking",
            "852": "Awakens Intuition, Spiritual Development",
            "963": "Spiritual Connections, Oneness with the Universe"
        }

    frequencies = list(frequencies_info.keys())



    # opt = [
    #     417,
    #     528,
    #     639,
    #     741,
    #     852,
    #     963,
    # ]
    opt =list(frequencies_info.values())
    var = tk.StringVar()
    var.set(opt[0])
    o = tk.OptionMenu(main_frame, var, *opt)
    o.grid(row=2, column=2)
    new_windoe.grid(row=3, column=2)
    # consecutive = tk.Button(main_frame, text="Play consecutive", command=conse, padx=15, pady=10)
    # consecutive.grid(row=3, column=0)
    # succes = tk.Button(main_frame, text="Play Successive", padx=15, pady=10,command=s)
    # succes.grid(row=3, column=1)
    # ra = tk.Button(main_frame, text="Play Random", padx=15, pady=10,command=randomsound)
    # ra.grid(row=3, column=2)


Option_frame = tk.Frame(root, bg="#ADD8E6", relief="sunken", borderwidth=2)

###################
def band():
    deleteframes()

    def randomsound():
        M_random.play(var.get())

    def conse():
        consec.play(var.get())

    def s():
        succesive.successive(var.get())

    def dropd():
        csv_Play.inn(var.get())

    new_windoe = tk.Button(main_frame, text="Play selected band", command=dropd)

    l = tk.Label(main_frame, text="Play the bands by selecting them from the dropdown list", anchor="center", borderwidth=3, bg="#ffb6c1",justify="center",font= ("Lucida Calligraphy", 40, "bold"))
    l.grid(row=1, column=0, pady=3, columnspan=2)
    opt = [
        "A_band",
        "B_band",
        "C_band",
        "D_band",
        "E_band",
        "F_band"
    ]

    var = tk.StringVar()
    var.set(opt[0])
    o = tk.OptionMenu(main_frame, var, *opt)
    o.grid(row=2, column=0)
    new_windoe.grid(row=2, column=1)
    consecutive = tk.Button(main_frame, text="Play consecutive", command=conse, padx=15, pady=10)
    consecutive.grid(row=3, column=0)
    succes = tk.Button(main_frame, text="Play Successive", padx=15, pady=10,command=s)
    succes.grid(row=3, column=1)
    ra = tk.Button(main_frame, text="Play Random", padx=15, pady=10,command=randomsound)
    ra.grid(row=3, column=2)


Option_frame = tk.Frame(root, bg="#ADD8E6", relief="sunken", borderwidth=2)


def about():
    deleteframes()
    tk.Frame(root, bg="#ffb6c1", relief="sunken", borderwidth=2)
    ti=tk.Label(main_frame,text="Tarang AI: AI Based Music Generator\n",fg="red",bg="#ffb6c1",font=80)
    la=tk.Label(main_frame,text="These are following  functions you can do with it:\n\n1.play bands: you can play band(consecutive, succesive, random order)\n2.convolution: you can input two files anf play the concolved signal\n3.Mixing: we have given may options for mixing such as  from file, from bands, and also random mixing\n4.PLay note: you can input notes of any song of music and it will be played.\n5. Heal Yourself: Enhance your well-being by playing customized healing frequencies according to your needsaccording to need.\n6. Autoplay: Generate your own music by providing pitch, step, duration of 1st note.\n7. Generate from midi: Generate notes by using few initial notes of midi file \n\n\n THANK YOU!",font=56,fg="purple",bg="#ffb6c1")
    ti.configure(font=("times",50))
    ti.grid(row=0,column=1,sticky="NW",columnspan=2,padx=80)
    la.grid(row=1,column=1,padx=150)
    #main_frame.label.text         


home_btn = tk.Button(Option_frame, text="ABOUT", fg="#158aff", padx=20, pady=10, command=about)

home_btn.place(x=10, y=50)
home_btn.pack(pady=20)

#aboutus= Label(text="")

playband = tk.Button(Option_frame, text="Play bands", fg="#158aff", padx=20, pady=10, command=band)
playband.place(x=10, y=100)
playband.pack(pady=20)

convobtn = tk.Button(Option_frame, text="Convolution", fg="#158aff", command=con, padx=20, pady=10)
convobtn.place(x=10, y=150)
convobtn.pack(pady=20)

mix = tk.Button(Option_frame, text="Mixing", fg="#158aff", command=mi, padx=20, pady=10)
mix.place(x=10, y=200)
mix.pack(pady=20)

note = tk.Button(Option_frame, text="Play Notes", fg="#158aff", command=no , padx=20, pady=10)
note.place(x=10, y=200)
note.pack(pady=20)

heal = tk.Button(Option_frame, text="heal yourself", fg="#158aff", padx=20, pady=10, command=healing)
heal.place(x=10, y=100)
heal.pack(pady=20)

rec = tk.Button(Option_frame, text="autoplay", fg="#158aff", padx=20, pady=10, command=autoplay)
rec.place(x=10, y=100)
rec.pack(pady=20)

aud = tk.Button(Option_frame, text="Generate from midi", fg="#158aff", padx=20, pady=10, command=autoplay2)
aud.place(x=10, y=100)
aud.pack(pady=20)


ctk = tk.Button(Option_frame, text="Contact Us", fg="#158aff", padx=20, pady=10, command=contactus)
ctk.place(x=10, y=100)
ctk.pack(pady=15)

Option_frame.pack_propagate(False)
Option_frame.configure(width=150, height=400)
Option_frame.pack(side="left", fill="y")

main_frame = tk.Frame(root, bg="#ffb6c1", relief="sunken", borderwidth=2)
main_frame.pack_propagate(False)
main_frame.configure(width=400, height=400)
main_frame.pack(side="left", fill="both", expand=True)
about()
#
# main_frame.pack_propagate(False)
# main_frame.configure(width=400, height=400)
# main_frame.pack(side="top",fill="y")

root.mainloop()