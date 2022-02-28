"""
MVC Controller
"""

from model import Model
from view import View


class Controller:
    """
    MVC Controller Class
    """

    def __init__(self):
        """
        Constructor
        """
        self.model = Model()
        self.view = View(self)

    def main(self):
        """
        main View entry
        """
        self.view.main()

    def on_button_click(self, caption):
        """
        Button click callback
        """


if __name__ == "__main__":
    controller = Controller()
    controller.main()
