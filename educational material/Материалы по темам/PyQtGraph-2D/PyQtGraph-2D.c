{|/pyqtgraph - базовое и разное
	http://www.pyqtgraph.org/documentation/
	http://www.pyqtgraph.org/documentation/apireference.html
	
	Для работы нужен сам пакет pyqtgraph + PyQt5 + numphy
	Все устанавливается через pip install
	
	Примеры:
		import pyqtgraph.examples
		pyqtgraph.examples.run()
		> Преломление, отражение света - примеры pyqtgraph (Demos -> Optics)
	Отключить контекстное меню от pyqtgraph на холсте		
		pyqtgraph.setConfigOption('leftButtonPan', False)	
}
{|/База 2D отрисовки Qt:
	QGraphicsView
		уровень представления данных (паттерн MVC - роль View)
		виджет для отображения объектов графической сцены на экран
		
	QGraphicsScene
		уровень данных (паттерн MVC - роль Data)
		графическая сцена
		интерфейс для:
			отслеживания пересечений объектов
			, их положения
			, вызова отрисовки
			, и т.д.
		
	QGraphicsItems
		базовый класс объекта графической сцены
}
{|/Иерархия pyqtgraph 2D:
	QObject, QPaintDevice
		QWidget
			QFrame
				QAbstractScrollArea
					QGraphicsView (pyqt: QtGui.QGraphicsView)
						: provides a widget for displaying the contents of a QGraphicsScene
						
						-> pg.GraphicsView
							--> pg.PlotWidget
								: содержит pg.PlotItem (является центральным виджетом у PlotWidget)
								---> pg.PlotWindow

	QObject
		QGraphicsScene
			: provides a surface for managing a large number of 2D graphical items
	
	pg.GraphicsItem, QtGui.QGraphicsWidget
		-> pg.GraphicsWidget
			--> pg.PlotItem
				: implementing a standard 2D plotting area with axes
				- Manage placement of ViewBox, AxisItems, and LabelItems
				- Create and manage a list of PlotDataItems displayed inside the ViewBox
				- Implement a context menu with commonly used display and analysis options
				- содержит pg.ViewBox (поле self.vb)
				
			--> pg.ViewBox
	
	Python object
		-> pg.GraphicsItem
			http://www.pyqtgraph.org/documentation/graphicsItems/graphicsitem.html
			getViewBox()
			mapToDevice()
			pos()
			..etc
			
	QObject, QGraphicsItem --> QGraphicsObject
		QGraphicsObject, QGraphicsLayoutItem
			QGraphicsWidget
				: виджет, который можно добавлять в QGraphicsScene и QGraphicsLayout
				
}		
{|/Создание графика 2D
	
	http://www.pyqtgraph.org/documentation/how_to_use.html
	http://www.pyqtgraph.org/documentation/plotting.html
	
	{|/Типичные функции
		pyqtgraph.plot()
			создать новое окно с графиком
			возвращает pg.PlotWindow // pg.GraphicsView -> pg.PlotWidget -> pg.PlotWindow
				
		pg.PlotWidget.plot()	
			- добавить новый график(PlotItem) на холст PlotWidget
			
		PlotItem.plot()	
			- новый график(PlotDataItem) в существующий widget холста графика
			
		GraphicsLayout.addPlot()	
			- новый график в новую ячейку GridLayout
	}
	
	{|/Уровни работы с графиками (иерархия объектов и т.д.)
		{|/Уровень "Данные" (Data)
			Массив точек и тип представления массива точек на полотне pyqtgraph
			Наследование: 
				Python object
					-> pg.GraphicsItem
						http://www.pyqtgraph.org/documentation/graphicsItems/graphicsitem.html
						getViewBox()
						mapToDevice()
						pos()
						..etc
						
				QGraphicsItem
					: базовый класс объектов, которые отрисовываются через QGraphicsView
					системы координат
					масшитабирование
					трансформация
					обработка событий
					
				QObject, QGraphicsItem 
					-> QGraphicsObject
					Добавляет сигналы и свойства\поля
				
				pg.GraphicsItem, QtGui.QGraphicsObject
					-> pg.GraphicsObject
						-> pg.PlotCurveItem
						-> pg.ScatterPlotItem
						-> pg.PlotDataItem
			
			PlotCurveItem
				: линейный график. Состоит из отрезков, соединяющих заданные точки.
				
			ScatterPlotItem
				: отображает диаграмму рассеяния 
					Т.е. график состоит из отдельных(не соединенных) точек.
					Каждая точка отмечена выбранным маркером (кружок по умолчанию).
					
			PlotDataItem
				: комбинация предыдущих двух.
				Т.е. может отображать и линейный график из отрезков, и точечный график, и оба сразу.
				Реализовано через агрегирование. Т.е. в конструкторе класса прописано:
					self.curve = PlotCurveItem()
					self.scatter = ScatterPlotItem()
		}
		{|/Уровень "Контейнер" (Container)
			http://www.pyqtgraph.org/documentation/graphicsItems/index.html
			http://www.pyqtgraph.org/documentation/graphicsItems/plotitem.html
			Наследование:
				pg.GraphicsItem, QtGui.QGraphicsWidget
				-> pg.GraphicsWidget
					--> pg.PlotItem
						: implementing a standard 2D plotting area with axes
						- Manage placement of ViewBox, AxisItems, and LabelItems
						- Create and manage a list of PlotDataItems displayed inside the ViewBox
						- Implement a context menu with commonly used display and analysis options
						- содержит pg.ViewBox (поле self.vb)
					--> pg.GraphicsLayout
					
					--> pg.ViewBox
					--> pg.AxisItem
					
			Т.е. это графические виджеты, которые можно добавлять в менеджеры размещения, отображать посредством View и т.д.
			И в которые добавляются графики - объекты уровня "Data"
			В конечном счете, такой объект ДОЛЖЕН быть отображен посредством pg.GraphicsView
					
			PlotItem
				Содержит:
					ViewBox для отображения данных.
					график
					, оси координат (pg.AxisItem)
					, подписей к ним и т.д.
					
			GraphicsLayout
				реализует QGridLayout
				Т.е. это менеджер размещения, который позволяет на одном полотне (в армках одного виджета)
				расположить несколько графиков, каждый в своей ячейке и со своими координатными осями.
				
			ViewBox
				Отвечает за отображение данных.
				Более конкретно:
					обработка сигналов и событий:
						масштабирование по скроллу мыши
						перемещение по холсту перетаскиванием мыши
						стандартное меню по правому клику мыши по холсту
						+ некоторые сигналы от самих графиков
						и синхронизация связанных графиков. Т.е. когда есть, например, 
							график в одной ячейке 
							и текущая  выделенная в ROI область отображается в другом масштабе в другой ячейке
					и обычно объекты уровня "Данные" отображаются как раз посредством ViewBox
				
			AxisItem
				Отображение координатных осей.
				Настройки координатных осей (подписи, метки, используемые перья отрисовки и т.д.)
		}
		{|/Уровень "Представление" (View)
			// в документации: "Container Classes (subclasses of QWidget; may be embedded in PyQt GUIs)"
			Можно добавлять напрямую в объекты PyQt GUI
			Наследование:
				QObject, QPaintDevice
					QWidget
						QFrame
							QAbstractScrollArea
								QGraphicsView (pyqt: QtGui.QGraphicsView)
									: provides a widget for displaying the contents of a QGraphicsScene
									
									-> pg.GraphicsView
										--> pg.PlotWidget
										--> pg.GraphicsLayoutWidget
											---> pg.GraphicsWindow 
												[!: deprecated]
			
			PlotWidget
				содержит(агрегирует) и отображает одиночный холст графика (PlotItem)
				большинство методов PlotItem доступны и через PlotWidget
				
			GraphicsLayoutWidget
				отображает одиночный GraphicsLayoutItem
				(экземпляр GraphicsLayoutItem является центральным виджетом у GraphicsLayoutWidget)
				, т.е. служит менеджером размещения холстов графиков и пр. объектов уровня GraphicsItem
				--например, распределение разных графиков в разных частях холста
				большинство методов GraphicsLayoutItem доступны и через GraphicsLayoutWidget
		}
	}
}