from ..core.database import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class Tag(Base):

    __tablename__ = 'tags'

    tag_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
