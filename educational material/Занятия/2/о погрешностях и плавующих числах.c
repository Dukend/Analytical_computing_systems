Про float ("What Every Computer Scientist Should Know About Floating-Point Arithmetic")
	S0ER - Виновата математика или компьютер?
		https://www.youtube.com/watch?v=SbG7wF0bPgo
		системы счисления и дроби
		почему 0.2 - 0.1 != 0.1
	
	S0ER - Почему этот код крутится в бесконечном цикле?
		https://www.youtube.com/watch?v=5zSR7FfaLCY
		о стандарте IEEE-754
		как хранятся дробные числа в двоичной системе счисления в компьютере
		-- это продолжение того видео, что выше
		
	================================
	Floating Point Arithmetic: Issues and Limitations
		https://docs.python.org/3/tutorial/floatingpoint.html
		
		>>> .1 + .1 + .1 == .3
		False
		
		>>> round(.1, 1) + round(.1, 1) + round(.1, 1) == round(.3, 1)
		False
	
	Адаптация статьи(книги) ниже:
		https://habr.com/ru/post/112953/
		
	What Every Computer Scientist Should Know About Floating-Point Arithmetic
		https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
		
Про float и мало отличающиеся друг от друга числа
	https://en.wikipedia.org/wiki/Loss_of_significance
	