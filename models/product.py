from ..core.database import Base
from sqlalchemy.orm import mapped_column, Mapped


class ProductTag(Base):
    __tablename__ = 'product_tag'

    tag_id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(primary_key=True)


class Product(Base):
    __tablename__ = 'products'

    product_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    image_filename: Mapped[str] = mapped_column()
    
    size: Mapped[int] = mapped_column(nullable=False)
