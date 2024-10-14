from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="BOT__",
    )
    token: str
    admin_ids: frozenset[int] = frozenset(
        {
            850328937,  # @jase_go
            815114488,  # @greitt
        }
    )


settings = BotSettings()
