{|/Общая информация
	Движок LaTeX:
		MikTex
			https://miktex.org/download
			! устанавливается быстрее, чем TexLive
		LaTex для Windows и Linux — Tex Live
			https://www.tug.org/texlive/
		LaTex для MacOS — MacTeX
			http://www.tug.org/mactex/ 

	Кроссплатформенный редактор LaTex документов — TeXstudio:
		https://www.texstudio.org/
		
	Онлайн редакторы LaTeX:
		https://www.overleaf.com/
		https://papeeria.com/
		https://www.authorea.com/

	Онлайн редактор LaTex с SageTex:
		https://cocalc.com/doc/latex-editor.html
		см. описание: https://cocalc.com/doc/latex-editor.html#a-sagetex

	Книжки:
		Львовский - LaTeX (см. папку материалов "LaTeX")
		
	Ссылки:
		Диджитализируй - LaTeX:
			https://www.youtube.com/watch?v=8dCm1V1XDzw
			вводная: что такое LaTeX, зачем, чем удобен.
			Прим.: не содержательное видео - только вводное.
		
		МКИ - Меркулов - LaTeX для начинающих:
		https://www.youtube.com/watch?v=QzXsE-2ObXs&ab_channel=%D0%9C%D0%9A%D0%98
			более содержательное, упоминается хорошая книжка.
}
{|/1.LaTex чтобы увидел SageTex
	Далее выдержка из:
		complete installation
			http://doc.sagemath.org/html/en/tutorial/sagetex.html#sec-sagetex-install
			
		Make SageTeX known to TeX
			https://doc.sagemath.org/html/en/tutorial/sagetex.html#make-sagetex-known-to-tex
			
	1.Поиск sty-файла
		Для краткости продублирую:
			"Понадобится всего лишь скопировать один файл в директорию поиска TeX.
			Документация по использованию SageTeX находится в $SAGE_ROOT/local/share/texmf/tex/
			latex/sagetex/, где «$SAGE_ROOT» соответствует директории, где установлен сам Sage, например,
			/opt/sage-4.2.1."
			
		Т.е. ищем папку sagetex
			и далее смотрим, чтобы в пути до неё было:
				local/share/texmf/tex/latex/sagetex/
			Например:
				C:\Program Files\SageMath 9.1\runtime\opt\sagemath-9.1\local\share\texmf\tex\latex\sagetex
		Или, можно сразу искать файлик с расширением sty: sagetex.sty
			он такой один на всю систему, потому проблем нет.
		
	2.файл .sty, который надо перекинуть TeX'у, чтобы он увидел Sage
		прямо в папку с TeX проектом
		или
			прописать export TEXINPUTS="SAGE_ROOT/local/share/texmf//:"
		или
			перекинуть *.sty файл по адресу TEXMFHOME
				exapmle.sagetex.sage
}	
{|/2.Как скомпилировать TeX документ с включениями Sage
	Далее идет просто сводка из:
		quick usage introduction 
			http://doc.sagemath.org/html/en/tutorial/sagetex.html 
			> перевод: http://doc.sagemath.org/html/ru/tutorial/sagetex.html

	
	0.Если не установлен LaTeX, то установить. Например, TeXLive (ссылка выше)
		Установить редактор для LaTeX.
		Например, TexMaker.
		Или тот, который идет в комплекте к TexLive(надо отметить соотв. галочку при установке TexLive).
		Проделать, что описано в блоке 1.LaTex чтобы увидел SageTex --в текущем файле выше.
		
	1.файлик example.tex - Его нужно открыть TeX-редактором и попытаться скомпилировать в pdf
		В той же папке, что нашли файлик sagetex.sty или в папке, где локальная документация лежит,
		есть файлик example.tex
	
		Заметьте, что LaTeX будет жаловаться на некоторые вещи, как-то:
			Package sagetex Warning: Graphics file sage-plots-for-example.tex/plot-0.eps on page 1 does not exist. Plot command is on input line 25.

			Package sagetex Warning: There were undefined Sage formulas and/or plots. Run Sage on example.sage, and then run LaTeX on example.tex again.
	
	2.Среди файлов, сгенерированных после запуска LaTeX, есть файл example.sage, являющийся скриптом Sage. Сообщение, показанное выше, предлагало запустить example.sage, поэтому стоит так и сделать.
		Прим.: это значит запустить SageMath Shell (один из трех ярлыков, которые появляются после установки Sage),
			в открывшемся терминале Sage перейти в необх. папку при помощи команды cd
			и выполнить команду
				sage example.sagetex.sage
			Имя файла будет зависеть от имени файла .tex, что вы ранее скомпилировали.
				Т.е. для st_example.tex будет сгенерирован файлик st_example.sagetex.sage
			
	3.Затем будет предложено запустить LaTeX для example.tex еще раз; перед этим будет создан файл example.sout.
		Этот файл содержит результаты вычислений в Sage в формате, удобном для LaTeX.
		Новая папка, содержащая EPS-файл с графиком, также будет создана автоматически.
		Запустите LaTeX еще раз: все, что было вычислено в Sage, теперь включено в Ваш документ.
	============================
	
	Итого:
		1.запустите LaTeX для .tex файла;
			Открыть файл example.tex в TexMaker и запустить сборку.
			Результатом должно быть получение нескольких новых файлов, в том числе и example.sagetex.sage
			В других случаях - значит, где-то в выводе LaTex редактора искать ошибки компиляции файла.
		2.запустите Sage для сгенерированного на шаге 1 .sage файла;
			Запустить SageMath Shell (один из трех ярлыков, которые появляются после установки Sage)
			Выполнить команду: sage example.sagetex.sage
			Снова открыть файл example.tex в TexMaker и запустить сборку.
		3.запустите LaTeX для .tex файла еще раз.
			Теперь уже файл pdf соберется полностью и не будет знаков вопроса вместо формул.
			
		Пункт с запуском Sage можно пропустить, если никакие изменения не были применены к командам Sage в документе.
}
{|/3.Документация по sagetex 
	локальная - в папке:
		C:\Program Files\SageMath 9.1\runtime\opt\sagemath-9.1\local\share\doc\sagetex
		----- проще всего через поиск по "sagetex"
	http://doc.sagemath.org/html/en/tutorial/latex.html
}