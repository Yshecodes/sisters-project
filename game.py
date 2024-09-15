from random import choice
from time import sleep
import re
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import BooleanProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from game_state import GameState

class MainScreen(Screen):
    def on_button_press(self):
        self.manager.current = 'name_input'

class NameInputScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_state = None

    def on_enter(self, *args):
        self.game_state = App.get_running_app().game_state
        self.ids.name_input.bind(on_text_validate=self.set_player_name)
    
    def set_player_name(self, *args):
        name = self.ids.name_input.text
        if name:
            self.game_state.set_player_name('player1', name)
            self.ids.name_input.text = ''
            self.ids.name_input.opacity = 0
            self.ids.name_input.disabled = True
            self.game_state.reset_players_attributes()
            self.game_state.gen_starting_player()
            self.manager.current = 'game_throw'

class GameThrow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.game_state = None
    
    def on_enter(self, *args):
        self.game_state = App.get_running_app().game_state
        self.ids.throw.text = ''
        player2_throw = self.game_state.get_machine_throw('player2')
        self.game_state.set_machine_throw('player2', player2_throw)
        player3_throw = self.game_state.get_machine_throw('player3')
        self.game_state.set_machine_throw('player3', player3_throw)
        self.ids.throw.bind(on_text_validate=self.process_throw_input)
        
    def process_throw_input(self, *args):
        throw = self.ids.throw.text

        if throw:
            throw = int(throw)
            self.game_state.set_player_throw('player1', throw)
            self.ids.throw.text = ''
            self.ids.throw.opacity = 0
            self.ids.throw.disabled = True
            self.manager.current = 'starting_player'
        else:
            self.show_popup("Invalid input! Please try again.")
    
    def show_popup(self, message):
        popup = Popup(title='Game Update',
                    content=Label(text=message),
                    size_hint=(None, None), size=(400, 200))
        popup.open()

class StartingPlayer(Screen):
    def on_enter(self):
        self.current_player_key = self.gen_starting_player(self.players)
        if self.current_player_key == "player1":
            self.manager.current = 'user_guess'
        else:
            self.manager.current = 'machine_guess'

class UserGuess(Screen):
    def on_enter(self):
        self.ids.guess.opacity = 1
        guess_value = self.ids.guess.text
        if guess_value.isdigit():
            guess_value = int(guess_value)
            
            if guess_value not in game_state.existing_guesses:
                game_state.players['player1']['guess'] = guess_value
                game_state.existing_guesses.append(guess_value)
            else:
                self.show_popup("This guess has been taken.\nPlease choose a different one.")
        else:
            self.show_popup("Please enter a valid number.")

    def show_popup(self, message):
        close_button = Button(text='Close', size_hint=(None, None), size=(100, 50))
        
        content = BoxLayout(orientation='vertical')
        content.add_widget(Label(text=message))
        content.add_widget(close_button)
        
        popup = Popup(title='Game Update',
                    content=content,
                    size_hint=(None, None), size=(400, 200))
        
        close_button.bind(on_release=popup.dismiss)
        
        popup.open()

class MachineGuess(Screen):
    def on_enter(self):
        if game_state.current_player_key == 'player2':
            game_state.get_player2_guess(game_state.players['player2']['throw'], game_state.existing_guesses)
            self.show_popup(f"{game_state.players['player2']['name']} guessed {game_state.players['player2']['guess']}!")
            game_state.rotate_turns(game_state.player_keys, game_state.current_index)
            self.manager.current = 'machine_guess'
        elif game_state.current_player_key == 'player3':
            game_state.get_player3_guess(game_state.players['player3']['throw'], game_state.existing_guesses)
            self.show_popup(f"{game_state.players['player3']['name']} guessed {game_state.players['player3']['guess']}!")
            game_state.rotate_turns(game_state.player_keys, game_state.current_index)
        else:
            self.manager.current = 'user_guess'

class Winner(Screen):
    def on_enter(self):
        self.manager.current = 'game_over'

class Score(Screen):
    def on_enter(self):
        self.manager.current = 'game_throw'

class GameOver(Screen):
    def on_enter(self):
        play_again = ("Play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("See you next time!") 
            self.manager.current = 'goodbye'
        else:
            game_state.reset_players_attributes(game_state.players)
            game_state.gen_starting_player(game_state.players)
            self.manager.current = 'game_throw'
class GuessingGameApp(App):
    def build(self):
        self.game_state = GameState()
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(NameInputScreen(name='name_input'))
        sm.add_widget(GameThrow(name='game_throw'))
        sm.add_widget(StartingPlayer(name='starting_player'))
        sm.add_widget(UserGuess(name='user_guess'))
        sm.add_widget(MachineGuess(name='machine_guess'))
        sm.add_widget(Winner(name='winner'))
        sm.add_widget(Score(name='score'))
        sm.add_widget(GameOver(name='game_over'))
        return sm

if __name__ == '__main__':
    GuessingGameApp().run()