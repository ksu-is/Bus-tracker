Bus tracker is availabe on IOS and Android, providing real-time alerst to bus drivers when students are within walking distance of their pickup spot.
  #installing
install kivy with pip:
  pip install kivy

from kivy.app import App 

from kivy.uix.boxlayout import BoxLayout 

from kivy.uix.label import Label 

from kivy.uix.textinput import TextInput 

from kivy.uix.button import Button 

from datetime import datetime 

# In-memory user database 

user_database = {} 
# Bus logic 

bus_arrival_time = datetime.strptime("07:30", "%H:%M") 

def get_student_distance(): 

    return 3  # Mocked as always 3 minutes away 

def should_bus_wait(student_distance): 

    if student_distance <= 3: 

        return "The bus is waiting for the student." 

    return "The bus is leaving." 

def time_remaining(bus_time, current_time): 

    remaining_time = bus_time - current_time 

    return remaining_time.total_seconds() / 60 

class BusTrackerLayout(BoxLayout): 

    def __init__(self, **kwargs): 

        super().__init__(orientation='vertical', **kwargs) 

 

        self.status = Label(text="Bus Tracker", font_size=24) 

        self.username_input = TextInput(hint_text='Username') 

        self.password_input = TextInput(hint_text='Password', password=True) 

        self.login_button = Button(text='Login', on_press=self.login) 

        self.create_button = Button(text='Create Account', on_press=self.create_account) 

        self.check_button = Button(text='Check Bus Status', on_press=self.check_status) 

 

        self.add_widget(self.status) 

        self.add_widget(self.username_input) 

        self.add_widget(self.password_input) 

        self.add_widget(self.login_button) 

        self.add_widget(self.create_button) 

        self.add_widget(self.check_button) 

 

    def login(self, instance): 

        username = self.username_input.text 

        password = self.password_input.text 

        if username not in user_database: 

            self.status.text = "Username not found." 

        elif user_database[username] != password: 

            self.status.text = "Incorrect password." 

        else: 

            self.status.text = "Login successful!" 

 

    def create_account(self, instance): 

        username = self.username_input.text 

        password = self.password_input.text 

        if username in user_database: 

            self.status.text = "Username already taken." 

        else: 

            user_database[username] = password 

            self.status.text = "Account successfully created!" 



    def check_status(self, instance): 

        now = datetime.now() 

        minutes_left = time_remaining(bus_arrival_time, now) 

        student_distance = get_student_distance() 

        if minutes_left <= 3: 

            self.status.text = should_bus_wait(student_distance) 

        else: 

            self.status.text = "Bus will arrive in more than 3 minutes." 

class BusTrackerApp(App): 

    def build(self): 

        return BusTrackerLayout() 

if __name__ == '__main__': 

    BusTrackerApp().run() 

 
