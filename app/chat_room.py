from textual import on, events
from textual.app import App
from textual.reactive import reactive
from textual.containers import ScrollableContainer
from textual.widgets import Footer, Header, Button, Static, Placeholder

class ModeSwitchingButton(Static):
    def compose(self) :
        yield Button("Switch Mode", variant='primary')
        yield Button("Switch Mode", variant='error')

class chatApp(App) :
    # BINDINGS = [
    #     ('d', 'toggle_dark_mode', 'Toggle dark mode'),
    # ]
    @on(Button.Pressed, '#switch')
    def switch(self):
        self.dark = not self.dark
        # self.dark = event.is_on
        print('pressed')

    CSS_PATH = "chat_room.css"

    def compose(self):
        yield Header()
        yield Footer()
        yield Button("send")
        yield Button('switch', id='switch')
        # yield Placeholder()
        # with ScrollableContainer(id="Buttons"):
        #     yield ModeSwitchingButton()
        #     yield ModeSwitchingButton()
        # self.dark = False
    
    def action_toggle_dark_mode(self) :
        self.dark = not self.dark

if __name__ == "__main__" :
    chatApp().run()