#module imports
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


# dictionary of home remedies can add more as well
home_remedies = {
    "sore throat": "ginger tea",
    "cough": "honey and lemon",
    "headache": "ibuprofen",
    "fever": "acetaminophen",
    
    
}

# create the app class with the build function
class HomeRemedyApp(App):
    def build(self):
        self.symptom_input = TextInput(text="Enter your symptom here")
        #on input, remove the text
        
        


        # button to search for remedy
        self.search_button = Button(text ="Search",
                   font_size ="20sp",
                   background_color =(255, 255, 255 , 1),
                   color =(255, 255, 255 , 1),
                   size =(30, 50),
                   size_hint =(.2, .2),
                   pos =(300, 250))
       

       #display remedy label 
        self.search_button.bind(on_press=self.display_remedy)
        self.remedy_label = Label()



    #layout of the app vertically 
        self.layout = BoxLayout(orientation="vertical")
        self.layout.add_widget(self.symptom_input)
        self.layout.add_widget(self.search_button)
        self.layout.add_widget(self.remedy_label)



    #return the layout
        return self.layout



    #display remedy function 
    def display_remedy(self, instance):
        symptom = self.symptom_input.text
        remedy = home_remedies.get(symptom, "No remedy found")
        self.remedy_label.text = remedy




#run the app with the name main

if __name__ == "_main_":
    HomeRemedyApp().run()
