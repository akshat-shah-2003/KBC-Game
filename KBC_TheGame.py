import os,sys
import random
import kivy
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.core.audio import Sound
from kivy.uix.progressbar import ProgressBar
from kivy.uix.togglebutton import ToggleButton

ques={1: "Who was the first to discover India?",
   2: "Who is known as the Iron Man of India?",
   3: "What is the Capital of India?",
   4: "Which state is also known as the fruit bowl of India?",
   5: "Which is the national sport of India?",
   6: "Which state is also known as the land of rising sun?",
   7: "Where is the Taj Mahal located?",
   8: "Which Indian state has the smallest coastline?",
   9: "What is the national heritage animal of India?",
   10: "In which state is the International Kite Festival celebrated?",
   11: "Which state in India has the highest population?",
   12: "Name the national bird of India.",
   13: "How many states are there in India?",
   14: "Which is the national animal of India?",
   15: "Who is considered the ‘Father of the Nation’?"
   }
ans={
    1: "Vasco da Gama",
    2: "Sardar Vallabhbhai Patel",
    3: "New Delhi",
    4: "Himachal Pradesh",
    5: "Hockey",
    6: "Arunachal Pradesh",
    7: "Agra",
    8: "Goa",
    9: "Elephant",
    10: "Gujarat",
    11: "Uttar Pradesh",
    12: "Peacock",
    13: "29",
    14: "Tiger",
    15: "Mahatma Gandhi",
}
d = {
    1: 1000,
    2: 2000,
    3: 5000,
    4: 10000,
    5: 20000,
    6: 40000,
    7: 80000,
    8: 160000,
    9: 320000,
    10: 640000,
    11: 1250000,
    12: 2500000,
    13: 5000000,
    14: 10000000,
    15: 70000000
}
options=[["Charles Darwin", "Napolean Bonaparte", "Vasco da Gama", "Gautam Buddha"],
        ["Tony Stark", "Sardar Vallabhbhai Patel", "Mahatma Gandhi", "Atal Bihari Vajpayee"],
        ["New Delhi", "Mumbai", "Bhopal", "Bangalore"],
        ["Himachal Pradesh", "Madhya Pradesh", "Maharashtra", "Hyderabad"],
        ["Cricket", "Hockey", "Badminton", "Football"],
        ["Uttarakhand", "Rajasthan", "Goa", "Arunachal Pradesh"],
        ["Delhi", "Ujjain", "Mumbai", "Agra"],
        ["Maharashtra", "Goa", "Tripura", "Nagaland"],
        ["Tiger", "Peacock", "Elephant", "Camel"],
        ["Mumbai", "Rajasthan", "Gujarat", "Delhi"],
        ["Uttar Pradesh", "Madhya Pradesh", "Maharashtra", "Karnataka"],
        ["Kiwi", "Kingfisher", "Peacock", "Sparrow"],
        [28,29,7,30],
        ["Tiger", "Dog", "Gorilla", "Elephant"],
        ["Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Mahatma Gandhi", "Subhash Chandra Bose"]]
ls=list(d.keys())
ms=list(d.values())
class MyWidget(Widget):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.i=1
        self.j=1
        self.money=0
        self.locked=False
        self.pressed()

    def pressed(self):
        self.image = Image(source='image.png', size_hint=(None, None), size=(500, 500), pos=(150, 50))
        self.add_widget(self.image)
        sound = SoundLoader.load('intro.mp3')
        sound.play()
        sound.bind(on_stop=self.on_stop)
    def next_ques(self,instance):
        self.ques_label.text=''
        self.i+=1
        self.remove_widget(self.nb)
        self.next_stop0(instance)
            
    def after_restart(self,instance):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def after_lock(self,instance):
        self.locked=True
        if self.i<16:
            if self.toggle_button1.text[3:]==ans[self.t] and self.toggle_button1.state=='down':
                self.correct=True
                self.label.color='green'
                self.toggle_button1.background_down='green.png'
                self.toggle_button2.background_down='red.png'
                self.toggle_button3.background_down='red.png'
                self.toggle_button4.background_down='red.png'
            elif self.toggle_button1.text[3:]==ans[self.t] and self.toggle_button1.state!='down':
                self.correct=False
                self.label.color='red'
                self.toggle_button1.background_normal='green.png'
                self.toggle_button2.background_down='red.png'
                self.toggle_button3.background_down='red.png'
                self.toggle_button4.background_down='red.png'
            elif self.toggle_button2.text[3:]==ans[self.t] and self.toggle_button2.state=='down':
                self.correct=True
                self.label.color='green'
                self.toggle_button2.background_down='green.png'
                self.toggle_button1.background_down='red.png'
                self.toggle_button3.background_down='red.png'
                self.toggle_button4.background_down='red.png'
            elif self.toggle_button2.text[3:]==ans[self.t] and self.toggle_button2.state!='down':
                self.correct=False  
                self.label.color='red'
                self.toggle_button2.background_normal='green.png'
                self.toggle_button1.background_down='red.png'
                self.toggle_button3.background_down='red.png'
                self.toggle_button4.background_down='red.png'
            elif self.toggle_button3.text[3:]==ans[self.t] and self.toggle_button3.state=='down':
                self.correct=True
                self.label.color='green'
                self.toggle_button3.background_down='green.png'
                self.toggle_button2.background_down='red.png'
                self.toggle_button1.background_down='red.png'
                self.toggle_button4.background_down='red.png'
            elif self.toggle_button3.text[3:]==ans[self.t] and self.toggle_button3.state!='down':
                self.correct=False  
                self.label.color='red'
                self.toggle_button3.background_normal='green.png'
                self.toggle_button2.background_down='red.png'
                self.toggle_button1.background_down='red.png'
                self.toggle_button4.background_down='red.png'
            elif self.toggle_button4.text[3:]==ans[self.t] and self.toggle_button4.state=='down':
                self.money=ms[self.i+1]
                self.correct=True
                self.label.color='green'
                self.toggle_button4.background_down='green.png'
                self.toggle_button2.background_down='red.png'
                self.toggle_button3.background_down='red.png'
                self.toggle_button1.background_down='red.png'
            elif self.toggle_button4.text[3:]==ans[self.t] and self.toggle_button4.state!='down':
                self.correct=False
                self.label.color='red'
                self.toggle_button4.background_normal='green.png'
                self.toggle_button2.background_down='red.png'
                self.toggle_button3.background_down='red.png'
                self.toggle_button1.background_down='red.png'
        if self.correct==True:
            if self.i<15:
                self.money=ms[self.i-1]
                self.nb=Button(text='NEXT',pos=(250,100),on_press=self.next_ques,size=(80,70))
                self.add_widget(self.nb)
            else:
                self.win=Label(text="YOU WIN ₹70000000",font_size=30,pos=(300,220))
                self.add_widget(self.win)
                self.restart=Button(text='RESTART',size=(80,70),pos=(250,100),on_press=self.after_restart)
                self.add_widget(self.restart)
                #self.remove_widget(self.ques_label)
        else:
            if self.toggle_button1.state=='down' or self.toggle_button2.state=='down' or self.toggle_button3.state=='down' or self.toggle_button4.state=='down':
                if self.money<10000:
                    self.money=0
                elif self.money>=10000 and self.money<320000:
                    self.money=10000
                elif self.money>=320000 and self.money<=10000000:
                    self.money=320000
            self.remove_widget(self.lock_button)
            self.lose=Label(text=f"YOU LOSE! Money Earned ₹ {self.money}.",font_size=30,pos=(300,220))
            self.add_widget(self.lose)
            self.restart=Button(text='RESTART',size=(80,70),pos=(250,100),on_press=self.after_restart)
            self.add_widget(self.restart)


    def on_stop(self, sound):
        self.start=Button(text='START',size=(60,50),pos=(650,10),on_press=self.next_stop0)
        self.add_widget(self.start)
    
    def next_stop0(self,instance):
        self.ques_label=Label(font_size=25,pos=(330,500))
        self.add_widget(self.ques_label)
        self.toggle_button1 = ToggleButton(size=(200, 50), pos=(100, 400),background_normal='white.png',color='black')
        self.add_widget(self.toggle_button1)
        self.toggle_button2 = ToggleButton(size=(200, 50), pos=(350, 400),background_normal='white.png',color='black')
        self.add_widget(self.toggle_button2)
        self.toggle_button3 = ToggleButton(size=(200, 50), pos=(100, 300),background_normal='white.png',color='black')
        self.add_widget(self.toggle_button3)
        self.toggle_button4 = ToggleButton(size=(200, 50), pos=(350, 300),background_normal='white.png',color='black')
        self.add_widget(self.toggle_button4)
        self.lock_button = Button(text="SUBMIT", on_press=self.after_lock,size=(80,70))
        self.lock_button.pos = (100, 100)
        #self.balance=Label(pos=(165,165),font_size=30,text='')
        #self.add_widget(self.balance)
        self.next_stop1(instance)

    def next_stop1(self,instance):
        self.remove_widget(self.start)
        self.remove_widget(self.image)
        
        if self.i < 16:
            self.locked=False
            self.label = Label(text=f"  {self.i}    ₹{d[self.i]}\n")
            self.label.pos = (650, 10 + self.i*30)
            self.add_widget(self.label)
            self.t = random.choice(ls)
            ls.remove(self.t)

            self.ques_label.text = f"{self.i}. {ques[self.t]}"
            self.toggle_button1.text=f"A. {options[self.t-1][0]}"
            self.toggle_button2.text=f"B. {options[self.t-1][1]}"
            self.toggle_button3.text=f"C. {options[self.t-1][2]}"
            self.toggle_button4.text=f"D. {options[self.t-1][3]}"
            self.add_widget(self.lock_button)
                      
class MyApp(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Window.fullscreen = True
    MyApp().run()
