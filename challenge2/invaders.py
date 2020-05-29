from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
class MainApp(App):
    def build(self):
        self.lista = ["apple", "anaconda", "answer", "alley"]
        self.listb = ["banana", "bowl", "brawl", "bonanza"]
        self.arrows = ["<", ">"]
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55
        )
        main_layout.add_widget(self.solution)

        left_button = Button(
            text="<",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        right_button = Button(
            text=">",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        layoutb = BoxLayout(orientation='horizontal')
        layoutb.add_widget(left_button)
        layoutb.add_widget(right_button)
        layout = AnchorLayout(anchor_x='right', anchor_y='bottom')
        layout.add_widget(layoutb)
        main_layout.add_widget(layout)

        return main_layout

    def on_right(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_left(self, instance):
        current = self.solution.text
        button_text = instance.text


if __name__ == "__main__":
    app = MainApp()
    app.run()
