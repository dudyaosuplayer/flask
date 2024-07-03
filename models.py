import datetime
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base, str_256


class ExampleNames(Base):
    __tablename__ = 'example_names'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str_256]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at
        }
