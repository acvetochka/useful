# Cheat Sheet : Plotting with Matplotlib using Pandas

| Plot Type | Description | Pandas Function | Example | Visual |
| ---------- | ---------- | --------------- | -------- | ------ |
| Line Plot	| Shows trends and changes over time	| DataFrame.plot.line() <br/> DataFrame.plot(kind = ‘line’)	| df.plot(x=’year’, y=’sales’, kind=’line’)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/line_plot.png"/> |
| Area Plot |	Displays data series as filled areas, showing the relationship between them |	DataFrame.plot.area() <br/> DataFrame.plot(kind = ‘area’)	| df.plot(kind='area')	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/area_plot.png"/> |
| Histogram	| Displays bars representing the data count in each interval/bin	| Series.plot.hist() <br/> Series.plot(kind = ‘hist’, bins = n) |	s.plot(kind='hist', bins=10) <br/> df[‘age’].plot(kind='hist', bins=10)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/histogram.png"/> | 
| Bar Chart	| Displays data using rectangular bars	| DataFrame.plot.bar() <br/> DataFrame.plot(kind = ‘bar’)	| df.plot(kind='bar')	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/bar_chart.png"/> |
| Pie Chart	| Displays data as a circular plot divided into slices, representing proportions or percentages of a whole |	Series.plot.pie() <br/> Series.plot(kind = ‘pie’) <br/> DataFrame.plot.pie(y, labels) <br/> DataFrame.plot(kind = ‘pie’)	| s.plot(kind='pie’,autopct='%1.1f%%') <br/> df.plot(x='Category',y='Percentage',kind='pie')	 | <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/pie_chart.png"/> |
| Box Plot |	Displays the distribution of a dataset along with key statistical measures |	DataFrame.plot.box() <br/> DataFrame.plot(kind = ‘box’)	| df_can.plot(kind='box')	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/box_plot.png"/> |
| Scatter Plot |	Uses Cartesian coordinates to display values for two variables |	DataFrame.plot.scatter() <br/> DataFrame.plot(x, y, kind = ‘scatter’) |	df.plot(x='Height', y='Weight', kind='scatter')	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/scatter.png"/> |


# Cheat Sheet : Plotting directly with Matplotlib

| Plot Type | Description | Pandas Function | Example | Visual |
| ---------- | ---------- | --------------- | -------- | ------ |
| Line Plot	| Shows trends and changes over time	| plt.plot()	| plt.plot(x, y, color='red', linewidth=2)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/line.png"/> |
| Area Plot	| Display data series as filled areas |	plt.fill_between() |	plt.fill_between(x, y1, y2, color='blue', alpha=0.5)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/area_plot.png"/> |
| Histogram |	Displays bars representing the data count in each interval/bin |	plt.hist() |	plt.hist(data, bins=10, color='orange', edgecolor='black')	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/hist.png"/> |
| Bar Chart |	Displays data using rectangular bars |	plt.bar()	| plt.bar(x, height, color='green', width=0.5)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/bar.png"/> |
| Pie Chart |	Displays data as a circular plot divided into slices, representing proportions or percentages of a whole |	plt.pie() |	plt.pie(sizes, labels=labels, colors=colors, explode=explode)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/pie_chart.png"/> |
| Box Plot |	Displays the distribution of a dataset along with key statistical measures |	plt.boxplot() |	plt.boxplot(data, notch=True)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/box.png"/> |
| Scatter Plot	| Uses Cartesian coordinates to display values for two variables |	plt.scatter() |	plt.scatter(x, y, color='purple', marker='o', s=50)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/scatter_without_out.png"/> |
| Subplotting |	Creating multiple plots on one figure |	plt.subplots() |	fig, axes = plt.subplots(nrows=2, ncols=2)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/Line_Scatter_shareY.png"/> |
| Customization |	Customizing plot: adding labels, title, legend, grid |	Various customization |	plt.title('Title')<br/>plt.xlabel('X Label') <br/>plt.ylabel('Y Label') <br/>plt.legend() <br/>plt.grid(True)	| <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/images/customized.png"/> |