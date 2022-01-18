http://www.pyqtgraph.org/documentation/3dgraphics/index.html

		
|/Полигональная сетка (polygon mesh) 
	— это совокупность вершин, рёбер и граней, которые определяют форму многогранного объекта в трёхмерной компьютерной графике и объёмном моделировании. 
	Гранями обычно являются треугольники, четырёхугольники или другие простые выпуклые многоугольники (полигоны), так как это упрощает рендеринг, но сетки могут также состоять и из наиболее общих вогнутых многоугольников, или многоугольников с отверстиями.
	Из: 
	https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BB%D0%B8%D0%B3%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%81%D0%B5%D1%82%D0%BA%D0%B0
	
|/Про глубину и смешивание
	http://www.pyqtgraph.org/documentation/3dgraphics/glgraphicsitem.html#pyqtgraph.opengl.GLGraphicsItem.GLGraphicsItem.setGLOptions
	-- для непрозрачности	


{|/GLViewWidget
	QtOpenGL.QGLWidget -> PyQtGraph GLViewWidget
		http://www.pyqtgraph.org/documentation/_modules/pyqtgraph/opengl/GLViewWidget.html#GLViewWidget
	
	cameraPosition()
	setCameraPosition(distance=15, azimuth=-90)
		текущая позиция камеры: center, dist, elevation, azimuth

	itemsAt(region=None)
		вернуть список объектов, находящихся в прямоугольнике (x, y, w, h) и отображаемые виджетом
		//координаты по СК виджета

	orbit(azim, elev)
		Поворот вокруг центральной точки
		azim, elev - в градусах

	paintGL(region=None, viewport=None, useItemNames=False)
		viewport specifies the arguments to glViewport. 
		If None, then we use self.opts[‘viewport’] region specifies the sub-region of self.opts[‘viewport’] that should be rendered. 
		Note that we may use viewport != self.opts[‘viewport’] when exporting.

	pan(dx, dy, dz, relative=False)
		Moves the center (look-at) position while holding the camera in place.

		If relative=True, then the coordinates are interpreted such that x if in the global xy plane and points to the right side of the view, y is in the global xy plane and orthogonal to x, and z points in the global z direction. Distances are scaled roughly such that a value of 1.0 moves by one pixel on screen.

	pixelSize(pos)
		Return the approximate size of a screen pixel at the location
		Pos may be a Vector or an (N,3) array of locations

	readQImage()
		Read the current buffer pixels out as a QImage.

	setBackgroundColor(*args, **kwds)
		Set the background color of the widget. Accepts the same arguments as pg.mkColor() and pg.glColor().
}
{|/GLGridItem
	http://www.pyqtgraph.org/documentation/3dgraphics/glgriditem.html
	http://www.pyqtgraph.org/documentation/_modules/pyqtgraph/opengl/items/GLGridItem.html#GLGridItem
	
	GLGraphicsItem -> GLGridItem
	
	__init__(size=None, color=None, antialias=True, glOptions='translucent')
	
	setSize(x=None, y=None, z=None, size=None)
		Установить размер осей.
		x,y,z ИЛИ size=QVector3D().

	setSpacing(x=None, y=None, z=None, spacing=None)
		Расстояние между рисками\линиями сетки
		x,y,z ИЛИ spacing=QVector3D().
		
}
{|/GLSurfacePlotItem
	http://www.pyqtgraph.org/documentation/3dgraphics/glsurfaceplotitem.html
	Displays a surface plot on a regular x,y grid
	GLGraphicsItem-> GLMeshItem -> GLSurfacePlotItem
	
	setData(x=None, y=None, z=None, colors=None)
		x,y	1D arrays of values specifying the x,y positions of vertexes in the grid. 
			If these are omitted, then the values will be assumed to be integers.
		z	2D array of height values for each grid vertex.
		colors	(width, height, 4) array of vertex colors.
		
	|/NOTE:
		Note that if vertex positions are updated, the normal vectors for each triangle must be recomputed. This is somewhat expensive if the surface was initialized with smooth=False and very expensive if smooth=True. For faster performance, initialize with computeNormals=False and use per-vertex colors or a normal-independent shader program.
}
{|/GLMeshItem
	http://www.pyqtgraph.org/documentation/3dgraphics/glmeshitem.html
	
}
{|/GLAxisItem
	http://www.pyqtgraph.org/documentation/3dgraphics/glaxisitem.html
	
}
{|/GLGraphicsItem
	http://www.pyqtgraph.org/documentation/3dgraphics/glgraphicsitem.html
	Базовый класс графических объектов
	
}
{|/GLLinePlotItem
	http://www.pyqtgraph.org/documentation/3dgraphics/gllineplotitem.html
	
}
{|/GLScatterPlotItem
	http://www.pyqtgraph.org/documentation/3dgraphics/glscatterplotitem.html
	отрисовать точечный график
}
{|/MeshData
	http://www.pyqtgraph.org/documentation/3dgraphics/meshdata.html
	хранит список объектов 
}
