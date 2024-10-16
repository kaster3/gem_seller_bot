from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class BotSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="BOT__",
    )
    token: SecretStr
    admin_ids: frozenset[int] = frozenset(
        {
            850328937,  # @jase_go
            7765313456,  # @helperTTDstore
            815114488,  # @greitt
        }
    )


settings = BotSettings()
