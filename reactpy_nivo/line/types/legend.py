from __future__ import annotations

from typing import Any, List, Optional, Union, Literal, Mapping, Tuple, Callable

from pydantic import BaseModel, Field, field_serializer, model_serializer

from .generic import ColorType, InheritColor, ThemeColor, Anchors, Direction, ItemDirection

class EffectStyle(BaseModel):
    itemWidth: Optional[int] = None
    itemHeight: Optional[int] = None
    itemDirection: Optional[ItemDirection] = None
    itemOpacity: Optional[float] = None

class Effect(BaseModel):
    on: str
    style: EffectStyle

class Legend(BaseModel):
    dataFrom: str
    anchor: Optional[Anchors] = None
    direction: Optional[Direction] = None
    justify: Optional[bool] = None
    translateX: Optional[int] = None
    translateY: Optional[int] = None
    itemsSpacing: Optional[int] = None
    itemWidth: int = 100
    itemHeight: int = 20
    itemDirection: Optional[ItemDirection] = None
    itemOpacity: Optional[float] = None
    symbolSize: Optional[int] = None
    effects: Optional[List[Effect]] = None
