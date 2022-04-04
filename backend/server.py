try:
    import uvloop
except ModuleNotFoundError:
    print("[*] Running without `uvloop`")
    uvloop = ...
from app.configuration import load_configuration
from app.program import configure_application
from app.services import configure_services

if uvloop is not ...:
    uvloop.install()

app = configure_application(*configure_services(load_configuration()))
