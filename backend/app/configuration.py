from typing import Any

from configuration.common import ConfigurationBuilder
from configuration.env import EnvironmentVariables
from configuration.yaml import YAMLFile


def load_configuration() -> Any:
    builder = ConfigurationBuilder()

    builder.add_source(YAMLFile("settings.yaml"))
    builder.add_source(EnvironmentVariables())

    config = builder.build()

    return config
