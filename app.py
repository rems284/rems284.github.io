import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import json
import plotly.express as px
import numpy as np

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#cagar data
df_ocupacion = pd.read_csv('data/ocupacion.csv')
df_experiencia = pd.read_csv('data/experiencia.csv')
df_salario = pd.read_csv('data/salario.csv')
df_educacion = pd.read_csv("data/educacion.csv")
df_indicadores = pd.read_csv("data/indicadores.csv")
df_indicadores_porcen = pd.read_csv("data/indicador_porcentaje.csv")


ocup_depart= df_ocupacion['departamento'].unique()
ocup_anio= df_ocupacion['anio'].unique()


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#F3E7CC",
   
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
STYLE_LOGO = {
    "margin-left": "-37px",
}
image_filename = 'logo.png' 

sidebar = html.Div(
    [
        html.Div(html.Img(src=app.get_asset_url(image_filename)),style=STYLE_LOGO),
        html.Hr(),
       
        dbc.Nav(
            [
                dbc.NavLink("Introducción", href="/", active="exact",style={"color":"#000"}),
                dbc.NavLink("Exploración Datos", href="/datos", active="exact",style={"color":"#000"}),
                dbc.NavLink("Indicadores", href="/indicadores", active="exact",style={"color":"#000"}),
                dbc.NavLink("Dash interactivo", href="/dash", active="exact",style={"color":"#000"}),
                dbc.NavLink("Conclusiones", href="/conclusiones", active="exact",style={"color":"#000"}),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")],)
def render_page_content(pathname):
    if pathname == "/":

        page_1 = html.Div(
            [
                html.H2("Demanda Laboral en Colombia 2015 / 2020", className="display-5"),
                html.Br(),
                html.P("De acuerdo con la contingencia de salud que se presentó a nivel mundial, quisimos saber, cómo impactó a Colombia esta situación respecto a la oferta laboral para el año 2020, por tal razón, nos vimos motivados a consultar en las páginas adscritas al Ministerio del Trabajo que brindan información sobre las oportunidades de trabajo a nivel nacional, teniendo en cuenta variables como nivel de educación, salarios, experiencia laboral, sectores económicos y ocupación, distribuido por departamentos. De acuerdo con esta inquietud, nos apoyamos en la Unidad del Servicio Público de Empleo, la cual tiene como objetivo brindar información pública sobre ofertas laborales tanto en el sector público como privado. Esta entidad ofrece datos abiertos de estudios e investigación por periodos y departamentos que pueden ser descargados para su uso."),
                html.P("Fuente de información: Unidad del servicio de Empleo"),
                html.P("Este proyecto tiene como finalidad analizar las tendencias y características que más son buscadas por los prestadores de servicios de empleo durante el año 2020, teniendo en cuenta que este año, corresponde a un hito histórico a nivel mundial que afectó al sector productivo en diferentes ámbitos tanto negativa como positivamente:"),
                html.Span("Educación"),
                html.Br(),
                html.Span("Ocupación"),
                html.Br(),
                html.Span("Salario"),
                html.Br(),
                html.Span("Experiencia"),
            ],
        )
       
        return page_1
    elif pathname == "/datos":
        page = html.Div(
            [
                html.H2("Exploración de los datos", className="display-5"),
                html.Br(),
                html.P("El análisis exploratorio permite tener un primer acercamiento a la distribución de los datos, ganar un primer entendimiento y poder identificar patrones visualmente"),
                
                'Departamento',
                dcc.Dropdown(
                    id='clientside-graph-country-px',
                    options=[
                        {'label': country, 'value': country}
                        for country in ocup_depart
                    ],
                    value='Amazonas'
                ),
                'Año',
                dcc.Dropdown(
                    id='clientside-graph-anio-px',
                    options=[
                        {'label': anio, 'value': anio}
                        for anio in ocup_anio
                    ],
                    value=2020
                ),
                html.H3("Ocupación", className="display-5"),
                dcc.Graph(
                    id='clientside-graph-px'
                ),
                dcc.Store(
                    id='clientside-figure-store-px'
                ),
                html.H3("Experiencia", className="display-5"),
                 dcc.Graph(
                    id='clientside-graph-px2'
                ),
                dcc.Store(
                    id='clientside-figure-store-px2'
                ),
                html.H3("Salario", className="display-5"),
                dcc.Graph(
                    id='clientside-graph-px3'
                ),
                dcc.Store(
                    id='clientside-figure-store-px3'
                ),
                html.Hr(),
                html.H3("Educación", className="display-5"),
                dcc.Graph(
                    id='clientside-graph-px4'
                ),
                dcc.Store(
                    id='clientside-figure-store-px4'
                ),
            ],
        )
       
        return page
        
    elif pathname == "/indicadores":

        page_1 = html.Div(
            [
                html.Div(
                 [
                html.H2("Tasa de desempleo en Colombia", className="display-5"),
                html.Br(),
                html.Li("Para el mes de marzo de 2021, la tasa de desempleo fue 14,2%, lo que representó un aumento de 1,6 puntos porcentuales comparado con el mismo mes del 2020 (12,6%)."),
                html.Br(),
               
                'Departamento',
                dcc.Dropdown(
                    id='clientside-graph-country-px',
                    options=[
                        {'label': country, 'value': country}
                        for country in ocup_depart
                    ],
                    value='Amazonas'
                ),
                'Año',
                dcc.Dropdown(
                    id='clientside-graph-anio-px',
                    options=[
                        {'label': anio, 'value': anio}
                        for anio in ocup_anio
                    ],
                    value=2020
                ),
                ],
                style={'width': '40%','height':'150px','float':'left'}),
                
                html.Div(

                   html.Div(
                    dcc.Graph(
                     id='clientside-graph-px5',
                     style={'height':'200px','font-size':"60px"}
                    ),
                    style={'font-size':"60px",'margin': 'auto','width': '50%','border': '3px solid green'}),
                    
                style={'width': '60%','float':'left','font-size':"60px"}),
                dcc.Store(
                        id='clientside-figure-store-px5'
                ),
                html.Div(
                    html.Hr(
                    
                    ),
                    style={'float':'left'}
                ),
                html.Div(
                 [
                html.H3("% de vacantes ofrecidas por población", className="display-5"),
                html.Li("Para el acumulado de vacantes en los 6 años por cada departamento y de acuerdo a la población proyectada según el DANE, la relación de vacantes por departamento corresponde a :"),
                'Departamento',
                dcc.Dropdown(
                    id='clientside-graph-country-px2',
                    options=[
                        {'label': country, 'value': country}
                        for country in ocup_depart
                    ],
                    value='Amazonas'
                ),
                
                ],
                style={'width': '40%','height':'150px','float':'left',"margin-top":'160px'}),
                html.Div(
                    html.Div(
                    dcc.Graph(
                     id='clientside-graph-px6',
                     style={'height':'200px','font-size':"60px"}
                    ),
                    style={'font-size':"60px",'margin': 'auto','width': '50%','border': '3px solid green'}),
                    
                 style={'width': '60%','float':'left','font-size':"60px","margin-top":'160px'}),
                dcc.Store(
                    id='clientside-figure-store-px6'
                ),
            ],
        )
       
        return page_1
    elif pathname == "/dash":

        page_1 = html.Div(
            [
                html.H2("Interactivo", className="display-5"),
                html.Br(),
                html.Li("Esta sección le permite interactuar e identificar el comportamiento"),
                'Departamento',
                dcc.Dropdown(
                    id='clientside-graph-country-px',
                    options=[
                        {'label': country, 'value': country}
                        for country in ocup_depart
                    ],
                    value='Amazonas'
                ),
                 dcc.Graph(
                    id='clientside-graph-px7'
                ),
                dcc.Store(
                    id='clientside-figure-store-px7'
                ),
                html.H3("Vacantes por departamentos", className="display-5"),
                'Año',
                dcc.Dropdown(
                    id='clientside-graph-anio-px',
                    options=[
                        {'label': anio, 'value': anio}
                        for anio in ocup_anio
                    ],
                    value=2020
                ),
                 dcc.Graph(
                    id='clientside-graph-px8'
                ),
                dcc.Store(
                    id='clientside-figure-store-px8'
                ),
            ],
        )
       
        return page_1

    elif pathname == "/conclusiones":

        page_1 = html.Div(
            [
                html.H2("Conclusiones", className="display-5"),
                html.Div(
                    [
                        html.Img(src=app.get_asset_url("empleo.png"),height=96,width=128),
                    ],
                    style={'witdh':"150px",'heigth':"150px",'margin-left':'40%'}),
                html.Br(),
                html.Li("De acuerdo con los resultados obtenidos por cada aspecto analizado, se identificó que las ofertas laborales para el año 2020, disminuyeron respecto al año 2019, lo que indica que si se vio impactado el sector laboral debido a la contingencia de salud que se vive a nivel mundial."),
                html.Br(),
                html.Li("Se identificó que Casanare un comportamiento especial, por ser un departamento que proporcional a su población cuenta con un alto número de vacantes y el sector más relevante es la explotación de minas y canteras."),
                html.Br(),
                html.Li("Los departamentos que más requieren vacantes con estudios de maestría corresponden Bogotá D.C, Antioquia, Santander y Valle del Cauca."),
                html.Br(),
                html.Li("El departamento de Archipiélago San Andrés presenta las mayores ofertas en Alojamiento y servicios de comida comparado con los demás departamentos."),
                html.Br(),
                html.Li("Casanare es el departamento que más solicita meses de experiencia en sus ofertas (más de 60 meses) laborales y la remuneración económica es asignada a convenir, no especifica los estudios económicos y sus ofertas dirigidas a la explotación de minas y canteras, la construcción y agricultura son las de mayor porcentaje comparado con los demás departamentos."),
                html.Br(),
                
                html.Br(),
                html.Div(
                    [
                        html.Img(src=app.get_asset_url("cv.png"),height=96,width=128),
                    ],
                    style={'witdh':"150px",'heigth':"150px",'margin-left':'40%'}),
                    
            ],
        )
       
        return page_1
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(
    Output('clientside-figure-store-px', 'data'),
    Input('clientside-graph-country-px', 'value'),
    Input('clientside-graph-anio-px', 'value')
)
def update_store_data( country,anio):
    dff = df_ocupacion 
    if country != None :
        dff = df_ocupacion[df_ocupacion['departamento'] == country]
    
    if anio != None:
        dff = dff[dff['anio'] == anio]

    deff = dff[['ocupacion','cant_ocupac']].groupby(['ocupacion']).sum()
    deff = deff.sort_values(by='cant_ocupac', ascending=True)

    return px.bar(deff,orientation='h')

@app.callback(
    Output('clientside-figure-store-px2', 'data'),
    Input('clientside-graph-country-px', 'value'),
    Input('clientside-graph-anio-px', 'value')
)
def update_store_data( country,anio):
    dff = df_experiencia 
    if country != None :
        dff = df_experiencia[df_experiencia['departamento'] == country]
    
    if anio != None:
        dff = dff[dff['anio'] == anio]

    deff = dff[['experiencia','cant_exp']].groupby(['experiencia']).sum()
    deff = deff.sort_values(by='cant_exp', ascending=False)

    return px.bar(deff)

@app.callback(
    Output('clientside-figure-store-px3', 'data'),
    Input('clientside-graph-country-px', 'value'),
    Input('clientside-graph-anio-px', 'value')
)
def update_store_data( country,anio):

    dff = df_salario 
    if country != None :
        dff = df_salario[df_salario['departamento'] == country]
    
    if anio != None:
        dff = dff[dff['anio'] == anio]
    

    deff = dff[['salario','cant_salario']].groupby(['salario']).sum()
    return px.scatter(deff)


@app.callback(
    Output('clientside-figure-store-px4', 'data'),
    Input('clientside-graph-country-px', 'value'),
    Input('clientside-graph-anio-px', 'value')
)
def update_store_data( country,anio):
    dff = df_educacion 
    if country != None :
        dff = df_educacion[df_educacion['departamento'] == country]
    
    if anio != None:
        dff = dff[dff['anio'] == anio] 

    return px.pie(dff,values='cant_edu', names='educacion')

@app.callback(
    Output('clientside-figure-store-px5', 'data'),
    Input('clientside-graph-country-px', 'value'),
    Input('clientside-graph-anio-px', 'value')
)
def update_store_data( country,anio):
    dff = df_indicadores
    if country != None :
        dff = df_indicadores[df_indicadores['departamento'] == country]
    
    if anio != None:
        dff = dff[dff['anio'] == anio] 

    
    number = dff[['vacantes']].sum()[0]

    fig =  go.Figure(go.Indicator(mode = "number+delta",number={"font":{"size":60}},
    value = number,title = {'text': 'Total ofertas empleo'},))
    return fig.update_layout(paper_bgcolor = "lightgray")

@app.callback(
    Output('clientside-figure-store-px6', 'data'),
    Input('clientside-graph-country-px2', 'value'),
)
def update_store_data( country):
    dff = df_indicadores_porcen
    if country != None :
        dff = df_indicadores_porcen[df_indicadores_porcen['departamento'] == country]
    

    
    number = dff[['porcentaje']].sum()[0]*100
     
    fig = go.Figure(go.Indicator(mode = "number+delta",number={"font":{"size":60}},value = number,title = {'text': 'Porcentaje'}))
    return fig.update_layout(paper_bgcolor = "lightgray")


@app.callback(
    Output('clientside-figure-store-px7', 'data'),
    Input('clientside-graph-country-px', 'value'),
)
def update_store_data( country):
    dff = df_indicadores
    if country != None :
        dff = df_indicadores[df_indicadores['departamento'] == country]
    
    
    deff = dff[['departamento','vacantes','anio']].groupby(['anio']).sum()
    

    return px.line(deff)

@app.callback(
    Output('clientside-figure-store-px8', 'data'),
    Input('clientside-graph-anio-px', 'value'),
)
def update_store_data( anio):
    dff = df_indicadores
    if anio != None:
        dff = dff[dff['anio'] == anio]     

    deff = dff[['departamento','vacantes']].groupby(['departamento']).sum()
    deff = deff.sort_values(by='vacantes', ascending=True)

    return px.bar(deff,orientation='h')



app.clientside_callback(
    """
    function(figure) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px', 'figure'),
    Input('clientside-figure-store-px', 'data')
)

app.clientside_callback(
    """
    function(figure) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px2', 'figure'),
    Input('clientside-figure-store-px2', 'data')
)
app.clientside_callback(
    """
    function(figure) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px3', 'figure'),
    Input('clientside-figure-store-px3', 'data')
)
app.clientside_callback(
    """
    function(figure) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px4', 'figure'),
    Input('clientside-figure-store-px4', 'data')
)

app.clientside_callback(
    """
    function(figure) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px5', 'figure'),
    Input('clientside-figure-store-px5', 'data')
)

app.clientside_callback(
    """
    function(figure) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px6', 'figure'),
    Input('clientside-figure-store-px6', 'data')
)
app.clientside_callback(
    """
    function(figure) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px7', 'figure'),
    Input('clientside-figure-store-px7', 'data')
)

app.clientside_callback(
    """
    function(figure) {
        if(figure === undefined) {
            return {'data': [], 'layout': {}};
        }
        const fig = Object.assign({}, figure, {
            'layout': {
                ...figure.layout,
                'yaxis': {
                    ...figure.layout.yaxis
                }
             }
        });
        return fig;
    }
    """,
    Output('clientside-graph-px8', 'figure'),
    Input('clientside-figure-store-px8', 'data')
)
if __name__ == "__main__":
    app.run_server(port=8888)