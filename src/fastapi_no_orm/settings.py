from pydantic import BaseModel, computed_field
from pydantic_core import MultiHostUrl
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class PostgresConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str
    db_name: str
    db_schema: str

    @computed_field  # type: ignore[prop-decorator]
    @property
    def alembic_postgres_url(self) -> str:
        return MultiHostUrl.build(
            scheme="postgresql+asyncpg",
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            path=self.db_name,
        ).unicode_string()

    @computed_field  # type: ignore[prop-decorator]
    @property
    def postgres_url(self) -> str:
        return MultiHostUrl.build(
            scheme="postgresql",
            host=self.host,
            port=self.port,
            username=self.user,
            password=self.password,
            path=self.db_name,
        ).unicode_string()


class Settings(BaseSettings):
    postgres: PostgresConfig

    model_config = SettingsConfigDict(toml_file="config.toml")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)


settings = Settings()  # type: ignore[call-arg]
