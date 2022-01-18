{|/Теор. часть по мат. пакету Sage (http://www.sagemath.org/)
	1. ПО для математических задач: обзор, возможности, задачи.
	2. Дробная степень и отрицательные числа *.
	3. Numpy. Основные функции, применение, задачи.
	4. Графики. Библиотека pyqtgraph.
	5. Графики. Библиотека matplotlib.
	6. Графики Sage. 2D, 3D. Особенности. Возможности. Виды графиков.
	7. Графики Sage. Точки разрыва. Асимптоты и наслоение графиков. Текст на графике.
	8. Графики Sage. Особенности. Изменение пропорций, размера, масштаба. Несколько графиков на одном холсте. Массив графиков на одном холсте.
	9. Производные. Дифференциальные уравнения.
	10. Системы уравнений.
	11. Интегралы. Пределы.
	12. Интерактивные элементы. Автоматизация вычислений.
	13. Работа с формулами. Получение TeX кода формулы. Вывод формулы в формульном виде.
	14. Упрощение - функции группы simplify. Вынесение множителя за скобки, раскрытие скобок. Подставка выражения\значения в формулу вместо переменной формулы.
	15. Получение символьного результата, получение числового значения с указанной точностью.
	16. Функции для нахождения решения уравнений в численном виде.
	17. Оформление документа Sage - работа в режиме markdown, функции print, show, tex.
	18. Оформление документа Sage для web - MathJax и получение html кода формул, отображение.
	19. Оформление TeX документа через Sage. Интеграция в TeX документ. TeX представление объектов Sage.
	20. Пример работы с полиномами. Алгоритм Евклида. Получение НОД по алгоритму Евклида. Функция gcd.
	21. CoCalc Sage online (https://cocalc.com/). Отличия от стационарной версии программы, возможности, преимущества и недостатки.
	22. Отладка. Типичные ошибки и решения.
	
	___________________________
	* - дробная степень:
			f = 4*x/(((9*x-1)**2)**(1/3) - (9*x-1)**(1/3) + 1)
			integrate(f, x, 0, 1)
		Даст результат: 
			4*integrate(x/(((9*x - 1)^2)^(1/3) - (9*x - 1)^(1/3) + 1), x, 0, 1)
		т.е. ответ не может быть получен в Sage в аналитическом виде.
		Необходимо заменить форму описания f (выделенная часть) на:
			f = 4*x/((((9*x-1))**(2/3)) - (9*x-1)**(1/3) + 1)
}
{|/Материалы по Sage
	Официальный туториал на русском
		http://doc.sagemath.org/html/ru/tutorial/tour.html
	Распространенные ошибки, при выполнении скриптов Sage
		http://doc.sagemath.org/html/ru/tutorial/tour_functions.html
	Остальное:
		см. папку материалов.
		
	SageMath - Getting Help With Sage When You're Stuck
		https://www.youtube.com/watch?v=ZD77uTqbg-4
		..?
		..??
		help(..)
		tutorial(..)
		manual(..)
		browse_sage_doc(..)
		python_help()
		cocalc - > Snippets
		wiki.sagemath.org/quickref
		http://sagebook.gforge.inria.fr/english.html
}