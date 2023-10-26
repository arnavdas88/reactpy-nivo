from __future__ import annotations

from typing import Any, List, Optional, Union, Literal, Mapping, Tuple, Callable

from pydantic import BaseModel, Field, field_serializer, model_serializer

from .generic import ColorType, InheritColor, ThemeColor

class Label(BaseModel):
    enableLabel: Optional[bool] = True
    label : Optional[Union[Callable, str]] = None
    labelSkipWidth : Optional[float] = None
    labelSkipHeight : Optional[float] = None
    labelTextColor: Optional[ColorType] = ThemeColor(theme = "labels.text.fill")

