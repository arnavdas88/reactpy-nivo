from __future__ import annotations

from typing import Any, List, Optional, Union, Literal, Mapping, Tuple

from pydantic import BaseModel, Field, field_serializer, model_serializer

from .generic import ColorScheme, Modifiers, ColorType, CurveType, BlendMode

class Colors(BaseModel):
    scheme: ColorScheme

class Def(BaseModel):
    id: str
    type: str
    background: str
    color: str
    size: Optional[int] = None
    padding: Optional[int] = None
    stagger: Optional[bool] = None
    rotation: Optional[int] = None
    lineWidth: Optional[int] = None
    spacing: Optional[int] = None

class FillItem(BaseModel):
    match: Any
    id: Union[Literal['dots', 'squares', 'lines'], str]

class Style(BaseModel):
    curve: Optional[CurveType] = 'linear'
    theme: Any = None
    colors: Colors
    lineWidth: Optional[float] = 2.0
    enableArea: Optional[bool] = True
    areaBaselineValue: Optional[Any] = None
    areaOpacity: Optional[float] = .02
    areaBlendMode: Optional[BlendMode] = "normal"
    defs: Optional[List[Def]] = None
    fill: Optional[List[FillItem]] = None