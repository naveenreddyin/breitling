from configuration.common import Configuration
from rodi import Container

from blacksheep.server import Application
from core.events import ServicesRegistrationContext

from . import controllers  # NoQA

from .errors import configure_error_handlers
from .docs import docs


async def before_start(application: Application) -> None:
    application.services.add_instance(application)
    application.services.add_alias("app", Application)


def configure_application(
    services: Container,
    context: ServicesRegistrationContext,
    configuration: Configuration,
) -> Application:
    app = Application(
        services=services,
        show_error_details=configuration.show_error_details,
        debug=configuration.debug,
    )

    app.on_start += before_start

    app.on_start += context.initialize
    app.on_stop += context.dispose

    configure_error_handlers(app)

    docs.bind_app(app)

    app.use_cors(
        allow_methods="*",
        allow_origins="*",
        allow_headers="* Authorization",
        max_age=300,
    )
    return app
