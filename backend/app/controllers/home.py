import os

from configuration.common import Configuration

from blacksheep import Application
from blacksheep.server.controllers import Controller, get
from blacksheep.messages import Response


app = Application()


class Home(Controller):
    @get()
    def index(self):
        # Since the @get() decorator is used without arguments, the URL path
        # is by default "/"
        return "welcome to news api"
