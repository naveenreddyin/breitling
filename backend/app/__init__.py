async def resolve_error(error: str) -> str:
    if error == "apiKeyInvalid":
        return "Api key is not valid."
