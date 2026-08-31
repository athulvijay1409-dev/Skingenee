from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from datetime import datetime
import json

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    brand = Column(String(200), nullable=False)

    # Stored as JSON strings for SQLite simplicity in this POC.
    ingredient_tags = Column(Text, nullable=False, default="[]")
    skin_types = Column(Text, nullable=False, default="[]")
    conditions_targeted = Column(Text, nullable=False, default="[]")

    priority = Column(Integer, nullable=False, default=0)  # 0-100
    price = Column(Float, nullable=False, default=0.0)
    affiliate_url = Column(String(1000), nullable=False)
    image_url = Column(String(1000), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def set_ingredient_tags(self, tags: list[str]):
        self.ingredient_tags = json.dumps(tags)

    def get_ingredient_tags(self) -> list[str]:
        return json.loads(self.ingredient_tags or "[]")

    def set_skin_types(self, types_: list[str]):
        self.skin_types = json.dumps(types_)

    def get_skin_types(self) -> list[str]:
        return json.loads(self.skin_types or "[]")

    def set_conditions_targeted(self, conditions: list[str]):
        self.conditions_targeted = json.dumps(conditions)

    def get_conditions_targeted(self) -> list[str]:
        return json.loads(self.conditions_targeted or "[]")


class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(128), nullable=False, index=True)
    image_path = Column(String(1000), nullable=True)

    # JSON string of confidence map
    predictions = Column(Text, nullable=False)

    top_condition = Column(String(64), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class OrderClick(Base):
    __tablename__ = "order_clicks"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(128), nullable=False, index=True)
    product_id = Column(Integer, nullable=False, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
