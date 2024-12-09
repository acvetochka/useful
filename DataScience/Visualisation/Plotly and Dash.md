# Cheat Sheet: Plotly and Dash


## Plotly Express 
| Function | Description | Syntax | Example |
| -------- | ----------- | -------| ------- |
| scatter |	Create a scatter plot |	px.scatter(dataframe, x=x_column, y=y_column) |	px.scatter(df, x=age_array, y=income_array) |
| line	  | Create a line plot	  | px.line( x=x_column, y=y_column,'title')	     | px.line(x=months_array, y=no_bicycle_sold_array) |
| bar     | Create a bar plot	    | px.bar( x=x_column, y=y_column,title='title')  |	px.bar( x=grade_array, y=score_array, title='Pass Percentage') |
| sunburst|	Create a sunbust plot |	px.sunburst(dataframe, path=[col1,col2..], </br>values='column',title='title')	| px.sunburst(data, path=['Month', 'DestStateName'], values='Flights',title='Flight Distribution Hierarchy') |
| histogram	| Create a histogram	| px.histogram(x=x,title="title")                |	px.histogram(x=heights_array,title="Distribution of Heights") |
| bubble |	Create a bubble chart |	px.scatter(dataframe, x=x,y=y,size=size,title="title") |	px.scatter(bub_data, x="City", y="Numberofcrimes", size="Numberofcrimes",hover_name="City", title='Crime Statistics') |
| pie |	Create a pie chart	 |px.pie(values=x,names=y,title="title")	| px.pie(values=exp_percent, names=house_holdcategories, title='Household Expenditure') |

## Plotly Graph Objects
| Function | Description | Syntax | Example |
| -------- | ----------- | -------| ------- |
| Scatter |	Create a scatter	| go.Scatter(x=x, y=y, mode='markers')	| go.Scatter(x=age_array, y=income_array, mode='markers') |
| | Create a line plot	| go.Scatter(x=x, y=y, mode='lines')	| go.Bar(x=months_array, y=no_bicycle_sold_array,mode='lines') |
| add_trace| 	Add additional traces to an existing figure	| fig.add_trace(trace_object)	| fig.add_trace(go.Scatter(x=months_array, y=no_bicycle_sold_array))| 
| update_layout	| Update the layout of a figure, such as title, axis labels, and annotations.	| fig.update_layout(layout_object)	| fig.update_layout(title='Bicycle Sales', xaxis_title='Months', yaxis_title='Number of Bicycles Sold')|

## Dash
| Function | Description | Syntax | Example |
| -------- | ----------- | -------| ------- |
| dash_core_components.Input |	Create an input component |	dcc.Input(value='', type='text') |	dcc.Input(value='Hello', type='text') |
| dash_core_components.Graph |	Create a graph component |	dcc.Graph(figure=fig)	| dcc.Graph(figure=fig) |
| dash_html_components.Div |	Create a div element	| html.Div(children=component_list)	| html.Div(children=[html.H1('Hello Dash'), html.P('Welcome to Dash')]) |
| dash_core_components.Dropdown	| Create a dropdown component |	dcc.Dropdown(options=options_list, value=default_value)	| dcc.Dropdown(options=[{'label': 'Option 1', 'value': '1'}, {'label': 'Option 2', 'value': '2'}], value='1') |

Dash - це бібліотека інтерфейсів користувача з відкритим вихідним кодом на мові Python для створення реактивних веб-додатків.

За допомогою Dash легко створювати графічні інтерфейси користувача, оскільки вона абстрагує всі технології, необхідні для створення додатків.

Dash складається з двох компонентів: Ядро та HTML-компоненти.

Dash_core_components описують інтерактивні компоненти вищого рівня, що генеруються за допомогою JavaScript, HTML та CSS через бібліотеку React.js.

Бібліотека dash_html_components має компонент для кожного тегу HTML.

Функція зворотного виклику - це функція python, яка автоматично викликається Dash щоразу, коли змінюється властивість вхідного компонента.

Декоратор @app.callback прикрашає функцію зворотного виклику, щоб вказати Dash викликати її щоразу, коли змінюється значення вхідного компонента.

Функція зворотного виклику приймає вхідний і вихідний компоненти як параметри і виконує операції, щоб повернути бажаний результат для вихідного компонента.
