from __future__ import annotations

from typing import Any, List, Optional, Union, Literal, Mapping, Tuple, Callable

from pydantic import BaseModel, Field, field_serializer, model_serializer

from .generic import ColorScheme, Modifiers, ColorType, CurveType

class Point(BaseModel):
    enablePoints: Optional[bool] = True
    pointSymbol: Optional[Callable] = None
    pointSize: Optional[float] = 10
    pointColor: Optional[ColorType] = None
    pointBorderWidth: Optional[float] = 2
    pointBorderColor: Optional[ColorType] = None
    enablePointLabel: Optional[bool] = False
    pointLabel: Optional[str] = None
    pointLabelYOffset: Optional[float] = -12