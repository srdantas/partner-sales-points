from flask import Flask

app = Flask(__name__)

import partners.controllers
import partners.controllers_handlers
