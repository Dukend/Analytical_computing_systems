http://www.pyqtgraph.org/documentation/graphicsItems/axisitem.html

def onSigRangeChanged(r):
    w1.sigRangeChanged.disconnect(onSigRangeChanged)
    w2.sigRangeChanged.disconnect(onSigRangeChanged)
    if w1==r:
        w2.setRange(xRange=r.getAxis('bottom').range)
    elif w2 == r:
        w1.setRange(xRange=r.getAxis('bottom').range)

    w1.sigRangeChanged.connect(onSigRangeChanged)
    w2.sigRangeChanged.connect(onSigRangeChanged)
	
статика - AxisItem.setTicks()
динамика - нужно создать AxisItem подкласс, который переопределяет tickValues и tickStrings
	https://github.com/pyqtgraph/pyqtgraph/blob/develop/pyqtgraph/graphicsItems/AxisItem.py#L661
	
setTicks(ticks)[source]
	Explicitly determine which ticks to display. 
	This overrides the behavior specified by tickSpacing(), tickValues(), and tickStrings() 
	The format for ticks looks like:
	[
		[ (majorTickValue1, majorTickString1), (majorTickValue2, majorTickString2), ... ],
		[ (minorTickValue1, minorTickString1), (minorTickValue2, minorTickString2), ... ],
		...
	]
setWidth(w=None)[source]
	Set the width of this axis reserved for ticks and tick labels. The width of the axis label is automatically added.
	If width is None, then the value will be determined automatically based on the size of the tick text.
	
setTickSpacing(major=None, minor=None, levels=None)[source]
	Explicitly determine the spacing of major and minor ticks. 
	This overrides the default behavior of the tickSpacing method, and disables the effect of setTicks(). 
	Arguments may be either major and minor, or levels which is a list of (spacing, offset) tuples for each tick level desired.

	If no arguments are given, then the default behavior of tickSpacing is enabled.

	Examples:
		# two levels, all offsets = 0
		axis.setTickSpacing(5, 1)
		# three levels, all offsets = 0
		axis.setTickSpacing([(3, 0), (1, 0), (0.25, 0)])
		# reset to default
		axis.setTickSpacing()
		
setPen(*args, **kwargs)[source]
	Set the pen used for drawing text, axes, ticks, and grid lines. If no arguments are given, the default foreground color will be used (see setConfigOption).
	http://www.pyqtgraph.org/documentation/_modules/pyqtgraph/graphicsItems/AxisItem.html#AxisItem.setPen
	
PlotItem.showGrid(x=None, y=None, alpha=None)
PlotItem.setMenuEnabled(self, enableMenu=True, enableViewBoxMenu='same'):
        """
        Enable or disable the context menu for this PlotItem.
        By default, the ViewBox's context menu will also be affected.
        (use enableViewBoxMenu=None to leave the ViewBox unchanged)
        """
================================
AxisItem.setPen(self, *args, **kwargs):
        """
        Set the pen used for drawing text, axes, ticks, and grid lines.
        If no arguments are given, the default foreground color will be used 
        (see :func:`setConfigOption <pyqtgraph.setConfigOption>`).
        """
        self.picture = None
        if args or kwargs:
            self._pen = fn.mkPen(*args, **kwargs)
        else:
            self._pen = fn.mkPen(getConfigOption('foreground'))
        self.labelStyle['color'] = '#' + fn.colorStr(self._pen.color())[:6]
        self.setLabel()
        self.update()
		
ef setScale(self, scale=None):
        """
        Set the value scaling for this axis. 
        
        Setting this value causes the axis to draw ticks and tick labels as if
        the view coordinate system were scaled. By default, the axis scaling is 
        1.0.
        """
        # Deprecated usage, kept for backward compatibility
        if scale is None:  
            scale = 1.0
            self.enableAutoSIPrefix(True)
            
        if scale != self.scale:
            self.scale = scale
            self.setLabel()
            self.picture = None
            self.update()

        
enableAutoSIPrefix(self, enable=True):
setRange(self, mn, mx):
setTicks(self, ticks):
	"""Explicitly determine which ticks to display.
	This overrides the behavior specified by tickSpacing(), tickValues(), and tickStrings()
	The format for *ticks* looks like::

		[
			[ (majorTickValue1, majorTickString1), (majorTickValue2, majorTickString2), ... ],
			[ (minorTickValue1, minorTickString1), (minorTickValue2, minorTickString2), ... ],
			...
		]
	
	If *ticks* is None, then the default tick system will be used instead.
	"""
	self._tickLevels = ticks
	self.picture = None
	self.update()
	
def setTickSpacing(self, major=None, minor=None, levels=None):
	"""
	Explicitly determine the spacing of major and minor ticks. This 
	overrides the default behavior of the tickSpacing method, and disables
	the effect of setTicks(). Arguments may be either *major* and *minor*, 
	or *levels* which is a list of (spacing, offset) tuples for each 
	tick level desired.
	
	If no arguments are given, then the default behavior of tickSpacing
	is enabled.
	
	Examples::
	
		# two levels, all offsets = 0
		axis.setTickSpacing(5, 1)
		# three levels, all offsets = 0
		axis.setTickSpacing([(3, 0), (1, 0), (0.25, 0)])
		# reset to default
		axis.setTickSpacing()
	"""
	
	if levels is None:
		if major is None:
			levels = None
		else:
			levels = [(major, 0), (minor, 0)]
	self._tickSpacing = levels
	self.picture = None
	self.update()
	
tickValues(self, minVal, maxVal, size):
tickStrings(self, values, scale, spacing):
mouseClickEvent(self, event)

=======================
viewBox:
setLimits(**kwds)[source]
	Set limits that constrain the possible view ranges.

	Panning limits. The following arguments define the region within the viewbox coordinate system that may be accessed by panning the view.
		xMin	Minimum allowed x-axis value
		xMax	Maximum allowed x-axis value
		yMin	Minimum allowed y-axis value
		yMax	Maximum allowed y-axis value
		
	Scaling limits. These arguments prevent the view being zoomed in or out too far.
		minXRange	Minimum allowed left-to-right span across the view.
		maxXRange	Maximum allowed left-to-right span across the view.
		minYRange	Minimum allowed top-to-bottom span across the view.
		maxYRange	Maximum allowed top-to-bottom span across the view.
		
	plt.centralWidget.vb.setLimits(xMin=-20, xMax=120, minXRange=5, maxXRange=100)