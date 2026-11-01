from pydantic import AnyUrl

from . import Base


class Url(Base):
    original_url: AnyUrl
    short_code: str
    clicks_count: int
