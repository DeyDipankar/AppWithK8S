from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    SERVICE_NAME : str =  "Service 2"
    APP2_SECRET_KEY : str

    # inter namespace communication test
    APP1_HOST : str



settings = Settings()