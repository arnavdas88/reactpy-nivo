from __future__ import annotations

from typing import Any, List, Optional, Union, Literal

from pydantic import BaseModel, Field

class Margin(BaseModel):
    top: float
    right: float
    bottom: float
    left: float

class ValueScale(BaseModel):
    type: Literal['linear', 'symlog']

class IndexScale(BaseModel):
    type: Literal['band']
    round: bool

class Base(BaseModel):
    data: Any
    keys: List[str] = ['value']
    indexBy: Union[str, int] = 'id'
    groupMode: Literal['grouped', 'stacked'] = 'stacked'
    layout: Literal['horizontal', 'vertical'] = 'vertical'
    reverse: bool = False
    minValue: Union[float, str] = 'auto'
    maxValue: Union[float, str] = 'auto'
    height: Optional[float] = None
    width: Optional[float] = None
    pixelRatio: Optional[float] = None
    margin: Optional[Margin]
    padding: Optional[float]
    valueScale: Optional[ValueScale]
    indexScale: Optional[IndexScale]