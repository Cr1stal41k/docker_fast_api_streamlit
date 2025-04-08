from pydantic import Field

# Project Stuff
from src.core.base_config import MixinSettings


class LinkConfig(MixinSettings):
    fast_api_link: str = Field("http://localhost:8080", env="FAST_API_LINK")


link_config: LinkConfig = LinkConfig()