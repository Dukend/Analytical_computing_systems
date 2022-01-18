## -*- encoding: utf-8 -*-
## This file (lr2.sagetex.sage) was *autogenerated* from lr2.tex with sagetex.sty version 2020/08/12 v3.5.
import sagetex
_st_ = sagetex.SageTeXProcessor('lr2', version='2020/08/12 v3.5', version_check=True)
_st_.current_tex_line = 27
_st_.blockbegin()
try:
 xmin, xmax = -10, 10
 ymin, ymax = -10, 10
 zmin, zmax = -10, 10
except:
 _st_.goboom(31)
_st_.blockend()
_st_.current_tex_line = 33
_st_.blockbegin()
try:
 var("x y z")
 f(x, y, z) = 7*x^2 + 3*y^2 + 3*z^2 +  8*x*y + 8*x*z + 6*y*z + 6*x + y + 7
except:
 _st_.goboom(36)
_st_.blockend()
try:
 _st_.current_tex_line = 39
 _st_.inline(0, latex(f(x, y, z)))
except:
 _st_.goboom(39)
_st_.current_tex_line = 41
_st_.blockbegin()
try:
 p = implicit_plot3d(f(x=x, y=y, z=z), (x, xmin, xmax), (y, ymin, ymax), (z, zmin, zmax))
except:
 _st_.goboom(43)
_st_.blockend()
try:
 _st_.current_tex_line = 46
 _st_.plot(0, format='notprovided', _p_=p)
except:
 _st_.goboom(46)
_st_.current_tex_line = 50
_st_.blockbegin()
try:
 def kanonic_coeffs(fun):
     try:
         var("l l1 l2 l3")
         lvcts = []
         svcts = []
         tmp_fun = fun
         a = vector(RR, 3)
         tmp_vct = vector(RR, 9)
         var_combs_tmp = (x^2, y^2, z^2, x*y, x*z, y*z)
         var_combs_0 = (x^2, x*y, x*z, x*y, y^2, y*z, x*z, y*z, z^2)
         var_combs_1 = (x, y, z)
         for i, var_comb in enumerate(var_combs_0):
             if i == 0 or i == 4 or i == 8:
                 tmp_vct[i] = fun.coefficient(var_comb)
             else:
                 tmp_vct[i] = fun.coefficient(var_comb) / 2
         for var_comb in var_combs_tmp:
             tmp_fun -= fun.coefficient(var_comb)*var_comb
         for i, var_comb in enumerate(var_combs_1):
             a[i] = tmp_fun.coefficient(var_comb) / 2
             tmp_fun -= tmp_fun.coefficient(var_comb)*var_comb
         a0 = tmp_fun.n()
         A = matrix(SR, 3, tmp_vct)
         L = matrix(SR, 3, 3, var('l'))
         E = matrix(SR, 3, 3, 1)
         lvct = vector([l1, l2, l3])
         lambdas = solve([(A-L).determinant() == 0], l)
         for i, el in enumerate(lambdas):
             nums = []
             lhs = (A-el.rhs()*E)*lvct
             res = solve([lhs[0] == 0, lhs[1] == 0, lhs[2] == 0], l1, l2, l3)[0]
             for i in range(len(res)):
                 if len(res[i].rhs().variables()) == 0:
                     nums.append(res[i].rhs())
                 else:
                     nums.append(res[i].rhs()(1))
             lvcts.append(vector(nums))
         for el in lvcts:
             norm_lvct = (el / sqrt((el*el).n())).n()
             svcts.append(norm_lvct)
         ST = matrix(RR, 3)
         for i in range(len(svcts)):
             ST[i] = svcts[i]
         a_ = ST*a
         for i in range(len(lambdas)):
             lambdas[i] = lambdas[i].rhs().n()
         return (lambdas, a_, a0)
     except:
         print("Something gone wrong\n")
         return (None, None, None)
except:
 _st_.goboom(101)
_st_.blockend()
_st_.current_tex_line = 103
_st_.blockbegin()
try:
 (lambdas, a, a0) = kanonic_coeffs(f)
except:
 _st_.goboom(105)
_st_.blockend()
_st_.current_tex_line = 107
_st_.blockbegin()
try:
 print("Lambdas:", tuple(lambdas))
 print("a:", a)
 print("a0:", a0)
except:
 _st_.goboom(111)
_st_.blockend()
try:
 _st_.current_tex_line = 113
 _st_.inline(1, latex(tuple(lambdas)))
except:
 _st_.goboom(113)
try:
 _st_.current_tex_line = 115
 _st_.inline(2, latex(a))
except:
 _st_.goboom(115)
try:
 _st_.current_tex_line = 117
 _st_.inline(3, latex(a0))
except:
 _st_.goboom(117)
_st_.current_tex_line = 119
_st_.blockbegin()
try:
 var("kx ky kz")
 first_part = lambdas[0]*kx^2 + lambdas[1]*ky^2 + lambdas[2]*kz^2
 second_part = 2*a[0]*kx + 2*a[1]*ky + 2*a[2]*kz + a0
 kanonic_func(kx, ky, kz) = first_part + second_part
except:
 _st_.goboom(124)
_st_.blockend()
try:
 _st_.current_tex_line = 127
 _st_.inline(4, latex(kanonic_func(kx, ky, kz)))
except:
 _st_.goboom(127)
_st_.current_tex_line = 129
_st_.blockbegin()
try:
 p = implicit_plot3d(kanonic_func(kx=kx, ky=ky, kz=kz), (kx, xmin, xmax),\
 (ky, ymin, ymax), (kz, zmin, zmax))
except:
 _st_.goboom(132)
_st_.blockend()
try:
 _st_.current_tex_line = 134
 _st_.plot(1, format='notprovided', _p_=p)
except:
 _st_.goboom(134)
try:
 _st_.current_tex_line = 145
 _st_.inline(5, latex(lambdas[0]))
except:
 _st_.goboom(145)
try:
 _st_.current_tex_line = 145
 _st_.inline(6, latex(lambdas[1]))
except:
 _st_.goboom(145)
try:
 _st_.current_tex_line = 145
 _st_.inline(7, latex(a[2]))
except:
 _st_.goboom(145)
_st_.endofdoc()
