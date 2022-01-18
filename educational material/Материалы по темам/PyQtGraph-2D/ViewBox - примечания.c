У viewBox есть ряд методов:
	# при изменении масштаба - изменяется масштаб и по X, и по Y с сохранением пропорций
	.setAspectLocked(1.0)
	
	# ограничение поля графика
	# в текущем - по полю по оси X разрешено передвигаться в промежутке от xMin=-100 до xMax=1100
	# и изменять масштаб так, чтобы по оси X на view умещалось от 20 до 500 единиц по X
	.setLimits(xMin=-100, xMax=1100, 
             minXRange=20, maxXRange=500)
	
	# текущий отображаемый диапазон
	# (отобразится и растянется на весь view)
	.setXRange(300, 450)
	
	# убрать оси координат
	.setAutoVisible(x=False, y=False)
	
	# убрать стандартные контекстные меню и реакцию на мышь от pyqtgraph
	.setMouseEnabled(x=False, y=False)
	
	# подгонять ли автоматом отображаемый диапазон под отображаемый объект
	# т.е. чтобы автоматом показывался только тот отрезок, который заполнен (график или еще что)
	# --отключение
	.enableAutoRange(x=False, y=False)
	.enableAutoRange('xy', False)
	
	
	см.:
		https://pyqtgraph.readthedocs.io/en/latest/graphicsItems/viewbox.html#pyqtgraph.ViewBox
		пример PyQtGraph - 2D \ ViewBox-features.py