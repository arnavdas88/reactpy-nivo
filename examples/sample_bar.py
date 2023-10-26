from reactpy import component, html, run
from reactpy.backend.starlette import Options
from reactpy.backend.fastapi import configure

from reactpy_nivo.plot import ResponsiveBar, ResponsiveBarCanvas
from reactpy_nivo.types import Base, Margin, ValueScale, IndexScale
from reactpy_nivo.types import Grid, Axis, AxisLeft, AxisRight, AxisTop, AxisBottom, AxisModel
from reactpy_nivo.types import Style, Colors, Def, FillItem, InheritColor
from reactpy_nivo.types import Label
from reactpy_nivo.types import Legend, Effect, EffectStyle
from reactpy_nivo.types import Accessibility
from fastapi import FastAPI
from reactpy.core.types import VdomDict

import pandas as pd

df = pd.read_json("data/food.json")

@component
def HelloWorld() -> VdomDict:
    base = Base(
        data = df.to_dict(orient='records'),
        keys = [ 'hot dog', 'burger', 'sandwich', 'kebab', 'fries', 'donut'],
        indexBy = "country", 
        layout = "horizontal",

        margin = Margin( top=50, right=130, bottom=50, left=60 ),
        padding = 0.3,
        valueScale = ValueScale(type = 'linear'),
        indexScale = IndexScale( type='band', round=True )
    )
    axis = Axis(
        axisBottom = AxisModel(
            enable = True,
            tickSize = 5,
            tickPadding = 5,
            tickRotation = 0,
            legend = "Country",
            legendPosition = "middle",
            legendOffset = 32,
        ),
        axisLeft = AxisModel(
            enable = True,
            tickSize = 5,
            tickPadding = 5,
            tickRotation = 0,
            legend = "Food",
            legendPosition = "middle",
            legendOffset = -40,
        )
    ) 
    style = Style(
        colors = Colors(scheme = "nivo"), 
        defs = [
            Def(
                id = 'dots',  type = 'patternDots',  background = 'inherit', 
                color = '#38bcb2',  size = 4,  padding = 1,  stagger = True 
            ),
            Def(
                id = 'lines', type = 'patternLines', background = 'inherit', 
                color = '#eed312', rotation = -45, lineWidth = 6, spacing = 10
            )
        ], 
        fill = [
            FillItem( match = { "id": 'fries' }, id = 'dots'),
            FillItem( match = { "id": 'sandwich' }, id = 'lines' ),
        ],
        borderColor = InheritColor(from_ = 'color', modifiers= [ ('darker', 1.6) ])
    )
    label = Label(
        labelSkipWidth = 12,
        labelSkipHeight = 12,
        labelTextColor = InheritColor(from_ = 'color', modifiers= [ ('darker', 1.6) ])
    )
    legend = Legend(
        dataFrom = 'keys',
        anchor = 'top-right',
        direction = 'column',
        justify = False,
        translateX = 120,
        translateY = 0,
        itemsSpacing = 2,
        itemWidth = 100,
        itemHeight = 20,
        itemDirection = 'left-to-right',
        itemOpacity = 0.35,
        symbolSize = 20,
        effects = [
            Effect( on = 'hover', style = EffectStyle(itemOpacity = 1, itemWidth = 60) )
        ]
    )
    accessibility = Accessibility(
        role = "application",
        ariaLabel = "Nivo bar chart demo",
        barAriaLabel = lambda e: e['id']+": "+e['formattedValue']+" in country: "+e['indexValue']
    )
    respbar_obj = ResponsiveBar(
        {
            **base.dict(exclude_none = True, by_alias=True),
            **style.dict(exclude_none = True, by_alias=True),
            **axis.dict(exclude_none = True, by_alias=True),
            **label.dict(exclude_none = True, by_alias=True),
            "legends": [ legend.dict(exclude_none = True, by_alias=True) ],
            **accessibility.dict(exclude_none = True, by_alias=True)
        }
    )
    return html.div(
        {"class": "nivo-plot"},
        respbar_obj
    )

description = """This is an example FastApi application that explains how 
`reactpy-nivo` can be used to create beautiful charts, easily and build 
industry ready dashboards, without actually using any frontend software
stack."""

app = FastAPI(
    title="ReactPy - Nivo",
    description=description,
    summary="A `Nivo Charts` component implemented in `ReactPy`",
    version="0.0.1",
    contact={
        "name": "Arnav Das",
        "url": "about.me/arnav-das",
        "email": "arnav.das88@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "identifier": "MIT",
    },
)

options = Options()
options.head = (*options.head, html.style("div.nivo-plot > div{ height: 400px; width: 800px;  }"))
configure(app, HelloWorld, options=options)