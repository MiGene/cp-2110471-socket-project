from textual import on, events
from textual.app import App, ComposeResult
from textual.reactive import reactive
from textual.containers import ScrollableContainer
from textual.widgets import Footer, Header, Button, Static, Placeholder, Input, Pretty, Label
from textual.color import Color

# class ModeSwitchingButton(Static):
#     def compose(self) :
#         yield Button("Switch Mode", variant='primary')
#         yield Button("Switch Mode", variant='error')

#* message box
#TODO fetch and create new message box
class MessageBox(Static) :
    def compose(self) :
        yield Label('hi',classes='message')


#* Input message and send Button div
#TODO apply send message function
class InputText(Static) :
    def compose(self) :
        yield Input(placeholder='text something...', id='textBox')
        yield Button('send', variant='primary', id='sendButton')
        yield Pretty([])
        

    @on(Input.Changed)
    def show_invalid_reasons(self, event: Input.Changed) -> None:
        # Updating the UI to show the reasons why validation failed
        # if not event.validation_result.is_valid:  
        #     self.query_one(Pretty).update(event.validation_result.failure_descriptions)
        # else:
        self.query_one(Pretty).update([])



class ChatApp(App) :
    # BINDINGS = [
    #     ('d', 'toggle_dark_mode', 'Toggle dark mode'),
    # ]

    CSS_PATH = "chat_room.tcss"

    def compose(self):
        yield Header()
        yield Footer()
        yield Button('switch', id='switch')
        with ScrollableContainer(id='chats') :
            yield MessageBox()
            yield MessageBox()
        yield InputText()
        yield Label(id='label1')
        # with ScrollableContainer(id="Buttons"):
        #     yield ModeSwitchingButton()
        #     yield ModeSwitchingButton()
        # self.dark = False
    
    #TODO give Title of chatroom
    def on_mount(self) -> None:
        self.title = "Group/Person name"
        self.sub_title = "group chat / personal chat"

    #* switch mode (dark-light)
    @on(Button.Pressed, '#switch')
    def switch(self):
        self.dark = not self.dark
        # self.dark = event.is_on
    # def action_toggle_dark_mode(self) :
    #     self.dark = not self.dark

if __name__ == "__main__" :
    ChatApp().run()