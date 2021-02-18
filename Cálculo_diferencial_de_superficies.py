from manimlib.imports import *

#####################################################################################
###### Composición de una superficie con funciones lineales y traslaciones ##########
#####################################################################################

##########esferas
class superficie_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -2,
        "u_max": 2,
        "v_min": -2,
        "v_max": 2,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, u, v):
        #Se puede modificar para cambiar el radio de la esfera 
        r=0.2
        return np.array([u,v,r*np.sin(7*(v+u))]) 
        
class superficie_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0,
        "u_max": 2*np.pi,
        "v_min": 0,
        "v_max": 2*np.pi,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, u, v):
        #Se puede modificar para cambiar el radio de la esfera 
        r=1
        return np.array([r*np.cos(u)*np.cos(v),r*np.cos(v)*np.sin(u),r*np.sin(v)]) 
class superficie_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0,
        "u_max": 2*np.pi,
        "v_min": 0,
        "v_max": 2*np.pi,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, u, v):
        #Se puede modificar para cambiar el radio de la esfera 
        r=1
        #Se puede modificar para cambiar la transformación
        k=0.1
        return np.array([r*np.cos(u)*np.cos(v),r*np.cos(v)*np.sin(u),k*r*np.sin(v)]) 
class superficie_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0,
        "u_max": 2*np.pi,
        "v_min": 0,
        "v_max": 2*np.pi,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, u, v):
        #Se puede modificar para cambiar el radio de la esfera 
        r=1
        #Se puede modificar para cambiar la transformación
        k=2
        return np.array([r*np.cos(u)*np.cos(v),r*np.cos(v)*np.sin(u),k*r*np.sin(v)]) 
#### segundo ejemplo

class superficie_5(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -2.5,
        "u_max": 2.5,
        "v_min": -2.5,
        "v_max": 2.5,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,(np.sin(3*(x+y))+y)*0.3])
class superficie_5_reflejada(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -2.5,
        "u_max": 2.5,
        "v_min": -2.5,
        "v_max": 2.5,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,(np.sin(3*(x-y))-y)*0.3]) 
class superficie_5_reflejada1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -2.5,
        "u_max": 2.5,
        "v_min": -2.5,
        "v_max": 2.5,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,(np.sin(3*(-x+y))+y)*0.3]) 

#### tercer ejemplo
class superficie_6(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -1.5,
        "u_max": 1.5,
        "v_min": -1.5,
        "v_max": 1.5,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        #Se puede cambiar a y b para modificar la translación
        a=0
        b=0
        return np.array([x+a,y+b,x**2+(y**2*(np.sin(y)**2))]) 
class superficie_6_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -1.5,
        "u_max": 1.5,
        "v_min": -1.5,
        "v_max": 1.5,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        #Se puede cambiar a y b para modificar la translación
        a=2
        b=0
        return np.array([x+a,y+b,x**2+(y**2*(np.sin(y)**2))])

class superficie_6_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -1.5,
        "u_max": 1.5,
        "v_min": -1.5,
        "v_max": 1.5,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
         #Se puede cambiar a y b para modificar la translación
        a=0
        b=2
        return np.array([x+a,y+b,x**2+(y**2*(np.sin(y)**2))])


class Composicion_de_Superficie_Con_Funciones(ThreeDScene):
    def construct (self):
        titulo=TextMobject('''Traslaciones y homotecias \n
                                en superficies''')
        #Cambiar función de superficie
        text1=TextMobject('''Tomemos $f(x,y)=(0.2\sin(7*(x+y)))$''')
        text2=TextMobject('''Una translación vertical de la superficie es de \n
                            la forma: $f(x,y)+k$''').move_to(3*UP)
        text3=TextMobject('''Por ejemplo: $f(x,y)-2$ ''').move_to(3*UP)
        text4=TexMobject(r"f(x,y)+3").move_to(3*UP)
        text5=TextMobject('''También podemos multiplicar superficies por un escalar, \n
                                    es decir: $kf(x,y)$.''').move_to(3*UP)
        text6=TextMobject('''Si $k=0.1$, la gráfica se encoje verticalmente hacia el plano \n
                                del dominio $xy$''').move_to(3*UP)
        text7=TextMobject('''Si $k=2$, la gráfica se estira verticalmente \n
                                alejando los puntos del plano $xy$ ''').move_to(3*UP)
        text8=TextMobject('''También podemos reflejar superficies.''').move_to(3*UP)
        text8_1=TextMobject('''Si $k=-1$, la gráfica de $kf(x,y)$ es la reflexión de la gráfica \n
                                de $f$ respecto al plano $xy$. ''').move_to(3*UP)
        text9=TextMobject('''Para reflejar respecto al plano $yz$, ''').move_to(3*UP)
        text9_1=TextMobject('''tomamos la función $f(x,-y)$.''').move_to(text9.get_center()+0.5*DOWN)
        text10=TextMobject('''Mientras que la gráfica de $f(-x,-y)$ es una \n
                                    reflexión respecto al eje vertical. ''').move_to(3*UP)
        text11=TextMobject('''¿Qué pasa con $f(k(x,y))$, con $k\\in\\mathbb{R}$? ''')
        text12=TextMobject('''También podemos hacer traslaciones horizontales. Por ejemplo:''').move_to(3*UP)
        text13=TextMobject('''$g(x,y)=x^{2}+y^{2}\\sin^{2}(y)$''').move_to(3*DOWN)
        text14=TextMobject('''La gráfica de $g((x,y)+(2,0))$ se ve: ''').move_to(3*DOWN)
        text15=TextMobject('''Pero la de $g((x,y)+(0,2))$: ''').move_to(3*DOWN)
        text16=TextMobject('''Modifica el código para crear más ejemplos''')

        axes=ThreeDAxes()
        #Superficies
        superficie1=superficie_1()
        fondo=Rectangle(height=1, width=10,fill_opacity=1,fill_color=BLACK).move_to(text11)

        #Parámetros que se pueden cambiar
        k1=-2
        superficie2=superficie_1().move_to([0,0,k1])
        k2=3
        superficie3=superficie_1().move_to([0,0,k2])
        superficie4=superficie_2()
        superficie5=superficie_3()
        superficie6=superficie_4()

        superficie7=superficie_5()
        superficie7_reflejadayz=superficie_5_reflejada()
        superficie8=superficie_5_reflejada1()

        superficie9=superficie_6()
        superficie10=superficie_6_1()
        superficie11=superficie_6_2()


    
        self.play(Write(titulo))
        self.wait(6)
        self.play(FadeOut(titulo))
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi,distance=12)
        self.add_fixed_in_frame_mobjects(text1)
        self.play(Write(text1))
        self.wait(4)
        self.play(text1.shift,3*UP,runtime=3)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie1)) 
        self.wait(3)       
        self.play(FadeOut(text1))
        self.add_fixed_in_frame_mobjects(text2)
        self.play(Write(text2))
        self.wait(8)
        self.play(FadeOut(text2))
        self.add_fixed_in_frame_mobjects(text3)        
        self.play(Write(text3))
        self.wait(5)
        self.play(ReplacementTransform(superficie1,superficie2))
        self.wait(5)
        self.play(FadeOut(text3))
        self.add_fixed_in_frame_mobjects(text4)        
        self.play(Write(text4))
        #Movimiento de superficie
        self.wait(5)
        self.play(ReplacementTransform(superficie2,superficie3))
        self.wait(6)
        self.play(FadeOut(text4))
        self.play(FadeOut(superficie3))
        self.add_fixed_in_frame_mobjects(text5)        
        self.play(Write(text5))
        self.wait(7)
        self.play(ShowCreation(superficie4))
        self.wait(4)
        self.play(FadeOut(text5))
        self.add_fixed_in_frame_mobjects(text6)        
        self.play(Write(text6))
        self.wait(6)
        self.play(ReplacementTransform(superficie4,superficie5))
        self.wait(6)
        self.play(FadeOut(text6))
        self.add_fixed_in_frame_mobjects(text7)        
        self.play(Write(text7))
        self.wait(9)
        self.play(ReplacementTransform(superficie5,superficie6))
        self.wait(5)
        self.play(FadeOut(text7))
        self.play(FadeOut(superficie6))
        self.add_fixed_in_frame_mobjects(text8)        
        self.play(Write(text8))
        self.wait(4)
        ##Superficie reflejada
        self.play(ShowCreation(superficie7))
        self.wait()
        self.play(FadeOut(text8))
        self.add_fixed_in_frame_mobjects(text9)        
        self.play(Write(text9))
        self.wait(5)
        #Superficie reflejada 2
        self.add_fixed_in_frame_mobjects(text9_1)        
        self.play(Write(text9_1))
        self.wait(3)
        self.play(ReplacementTransform(superficie7,superficie7_reflejadayz))
        self.wait(4)
        self.play(FadeOut(text9),FadeOut(text9_1))
        self.add_fixed_in_frame_mobjects(text10)        
        self.play(Write(text10))
        self.wait(11)
        self.play(ReplacementTransform(superficie7_reflejadayz,superficie8))
        self.wait(5)
        self.play(FadeOut(text10))
        self.play(FadeOut(superficie8))
        self.add_fixed_in_frame_mobjects(fondo)
        self.add_fixed_in_frame_mobjects(text11)        
        self.play(Write(text11),ShowCreation(fondo))
        self.wait(8)
        self.play(FadeOut(text11),FadeOut(fondo))
        self.add_fixed_in_frame_mobjects(text12)        
        self.play(Write(text12))
        self.wait(7)
        self.play(FadeOut(text12))
        self.add_fixed_in_frame_mobjects(text13)        
        self.play(Write(text13))
        self.wait(6)
        self.play(ShowCreation(superficie9))
        self.wait(5)
        self.play(FadeOut(text13))
        self.add_fixed_in_frame_mobjects(text14)        
        self.play(Write(text14))
        self.wait(7)
        self.play(ReplacementTransform(superficie9,superficie10))
        self.wait(5)
        self.play(FadeOut(text14))
        self.add_fixed_in_frame_mobjects(text15)        
        self.play(Write(text15))
        self.wait(6)
        self.play(ReplacementTransform(superficie10,superficie11))
        self.wait(5)
        self.play(FadeOut(text15),FadeOut(axes),FadeOut(superficie11))
        self.add_fixed_in_frame_mobjects(text16)        
        self.play(Write(text16))
        self.wait(8)
        self.play(FadeOut(text16))


#####################################################################################
#######################  Límite de cocientes de dos variables #######################
#####################################################################################


#Definición de las superficies
class superficie2_1_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": -0.3,
        "v_min": -3,
        "v_max": -0.3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,1/(x*y)])

class superficie2_1_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 3,
        "u_max": 0.3,
        "v_min": 3,
        "v_max": 0.3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,1/(x*y)])
class superficie2_1_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": -0.3,
        "v_min": 3,
        "v_max": 0.3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,1/(x*y)])
class superficie2_1_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 3,
        "u_max": 0.3,
        "v_min": -3,
        "v_max": -0.3,
        "checkerboard_colors": [ORANGE]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,1/(x*y)])
#Segunda superficie del video       
##############
class superficie2_2_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3.5,
        "u_max": -0.0001,
        "v_min": -3.5,
        "v_max": -0.0001,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,2*(x*y)/(x**2+y**2) ])
class superficie2_2_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 3.5,
        "u_max": 0.0001,
        "v_min": 3.5,
        "v_max": 0.0001,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,2*(x*y)/(x**2+y**2) ])

class superficie2_2_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3.5,
        "u_max": -0.0001,
        "v_min": 3.5,
        "v_max": 0.0001,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,2*(x*y)/(x**2+y**2) ])

class superficie2_2_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 3.5,
        "u_max": 0.0001,
        "v_min": -3.5,
        "v_max": -0.0001,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
        return np.array([x,y,2*(x*y)/(x**2+y**2) ])

class superficie2_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -3,
        "u_max": 3,
        "v_min": -3,
        "v_max": 3,
        "fill_color": BLUE_C,
        "pre_function_handle_to_anchor_scale_factor": 0.0000001,
        "fill_opacity": 1.0,
        "checkerboard_colors": [BLUE_C, BLUE_D],
        "stroke_color": LIGHT_GREY,
        "pre_function_handle_to_anchor_scale_factor": 0.00001
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
      
        return np.array([x,y,0])
def curva(t):
    return np.array([t**3,t,1])
def curva1(t):
    return np.array([t**3,t,0])
#cuarta superficie
class superficie2_4_1(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -2.7,
        "u_max": -0.3,
        "v_min": -2.7,
        "v_max": 2.7,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
       return np.array([x,y,1/(2*x)**2]) 
class superficie2_4_2(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0.3,
        "u_max": 2.7,
        "v_min": -2.7,
        "v_max": 2.7,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
       return np.array([x,y,1/(2*x)**2])    
class superficie2_4_3(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": 0.2,
        "u_max": 4,
        "v_min": 0.2,
        "v_max": 4,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
       return np.array([x,y,((x-y)**2)**(1/2)/(x+y)**2])    

class superficie2_4_4(ParametricSurface):
    def __init__(self, **kwargs):
        kwargs = {
        "u_min": -0.2,
        "u_max": -3,
        "v_min": -0.2,
        "v_max": -3,
        "checkerboard_colors": [BLUE_E]
        }
        ParametricSurface.__init__(self, self.func, **kwargs)
    def func(self, x, y):
       return np.array([x,y,((x-y)**2)**(1/2)/(x+y)**2])    

class super3 (ThreeDScene):
    ### Parte 1 de la animación
    def parte0 (self):
        titulo=TextMobject('''Límite de cocientes \n
                                de dos variables''').scale(2.5)
        text1=TextMobject(''' Cuando trabajamos con límites en funciones de $\\mathbb{R}^{2}\\rightarrow\\mathbb{R}$ ''','''\n
                                la cosa se pone interesante debido a que en este''','''\n
                                  caso tenemos diversas maneras de analizar  \n
                                 el límite: métrica, direcciones, curvas, sucesiones.''')
        text2=TextMobject('''Así, para argumentar que existe o no el límite,''','''\n
                                 esto se complica, en comparación con el caso''','''\n
                                    en que la variable es real.''')
        text3=TextMobject('''Pero no todo está perdido, hay diversos detalles \n 
                                con los que podemos argumentar si el \n
                                 límite existe o no.''')
        text4=TextMobject('''Ilustremos esto con algunos ejemplos.''')

        self.play(Write(titulo))
        self.wait(5)
        self.play(FadeOut(titulo))
        self.play(Write(text1[0]))
        self.wait(3.5)
        self.play(Write(text1[1]))
        self.wait(4)
        self.play(Write(text1[2]))
        self.wait(4)
        self.wait(3)
        self.play(FadeOut(text1))
        self.play(Write(text2[0]))
        self.wait(5)
        self.play(Write(text2[1]))
        self.wait(4)
        self.play(Write(text2[2]))
        self.wait(3.5)
        self.wait(3)
        self.play(FadeOut(text2))
        self.play(Write(text3))
        self.wait(10)
        self.play(FadeOut(text3))
        self.play(Write(text4))
        self.wait(7)
        self.play(FadeOut(text4))
        self.wait()
    def parte1 (self):
        text5=TextMobject('''Sea $f:\\mathbb{R}^{2}-{\\vec{0}}\\rightarrow\\mathbb{R}$''',''' $$f(x,y)=\\frac{1}{xy}$$ ''')
        text5_1=TextMobject('''$$f(x,y)=\\frac{1}{xy}$$''').move_to(3*UP)
        text6=TextMobject('''Si nos acercamos a la función por la dirección \n
                                dada por la recta identidad, la función \n
                                diverge a $\\infty$.''' ).move_to(3*DOWN)
        text6_1=TextMobject('''El límite con una sucesión. ''').move_to(3*UP)
        text6_2=TextMobject('''Con límite direccional. ''').move_to(3*UP)

        #objetos
        axes=ThreeDAxes()
        #Definimos la superficies por partes por la discontinuidad
        superficie1_1=superficie2_1_1()
        superficie1_2=superficie2_1_2()
        superficie1_3=superficie2_1_3()
        superficie1_4=superficie2_1_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)
        ## Movimiento para la primer convergencia en función +1/xy
        #para z>0
        #Pueden cambiarse los valores n1_1,n1_2, t1_1,t1_1f,t1_2,t1_2f
        #Para cambiar los limites en los cuales se muestran los límites con sucesiones y direccionales
        n1_1= 17 +17
        cjto1_1 = []
        for i in range(2,n1_1):
            if i<= 17:
                x = -3+(0.1*i)
            if i > 17:
                x= -3+(0.1*17)+((i-17)*0.06)
            cjto1_1.append((x,x,1/(x*x)))##Puede cambiarse el conjunto de puntos a una forma general (x,y,1/(x*y))
            #siempre y cuando sólo implemente la variable x para modificar el movimiento de la sucesión
        n1_2= 17+17
        cjto1_2 = []
        for i in range(2,n1_2):
            if i<=17:
                x = 3-(0.1*i)
            if i>17:
                x = 3-(0.1*17)-((i-17)*0.06)
            cjto1_2.append((x,x,1/(x*x)))##Puede cambiarse el conjunto de puntos a una forma general (x,y,1/(x*y))
            #siempre y cuando sólo implemente la variable x para modificar el movimiento de la sucesión
        #Con sucesiones
        Elementos1_1 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_1]
        Elementos11 = VGroup(*Elementos1_1)
        Elementos1_2 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_2]
        Elementos12 = VGroup(*Elementos1_2)

        
        
        ## 
        #Con limite direccional
        t1_1=ValueTracker(-3)
        punto_convergencia1=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([-3,-3,1/(9)])
        t1_1f=-0.45  
        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto_convergencia1.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,t,t**(-2)]))##Puede cambiarse el conjunto de puntos a una forma general (x,y,1/(x*y))
            #siempre y cuando sólo implemente la variable x para modificar el movimiento del límite direccional

        punto_convergencia1.add_updater(mov_sup1)

        #Movimiento del punto en la recta identidad parte positiva
        t1_2=ValueTracker(3)
        punto_convergencia2=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([3,3,1/(9)])
        t1_2f=0.3  
        def mov_sup2 (obj):
            t = t1_2.get_value()
            punto_convergencia2.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,t,t**(-2)]))##Puede cambiarse el conjunto de puntos a una forma general (x,y,1/(x*y))
            #siempre y cuando sólo implemente la variable x para modificar el movimiento del límite direccional

        punto_convergencia2.add_updater(mov_sup2)


        #Pueden modificarles los runtime que aparece para mostrar más rápido o lento el movimiento del límite de la sucesión
        self.play(Write(text5))
        self.wait(7)
        self.play(FadeOut(text5))
        self.set_camera_orientation(0.7*np.pi/2, 1*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text5_1)        
        self.play(Write(text5_1))
        self.wait(4)
        self.play(FadeOut(text5_1))
        self.add_fixed_in_frame_mobjects(text6)        
        self.play(Write(text6))
        self.wait(11)
        self.play(FadeOut(text6))
        self.add_fixed_in_frame_mobjects(text6_1)        
        self.play(Write(text6_1))
        self.play(ShowCreation(Elementos11), run_time=10)
        self.wait()
        self.play(FadeOut(Elementos11),FadeOut(text6_1))
        #Con limite direccional
        self.add_fixed_in_frame_mobjects(text6_2)        
        self.play(Write(text6_2))
        self.add(punto_convergencia1)
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.wait()     
        self.play(FadeOut(text6_2),FadeOut(punto_convergencia1))
        self.move_camera(0.7*np.pi/2, 0*np.pi,distance=12)
        self.add_fixed_in_frame_mobjects(text6_1)        
        self.play(Write(text6_1))
        self.play(ShowCreation(Elementos12), run_time=10)
        self.wait()
        self.play(FadeOut(Elementos12),FadeOut(text6_1))
        self.add_fixed_in_frame_mobjects(text6_2)        
        self.play(Write(text6_2))
        self.add(punto_convergencia2)
        self.play(t1_2.set_value, t1_2f,run_time=10)
        self.wait()     
        self.play(FadeOut(superficie),FadeOut(axes),
                    FadeOut(text6_2),FadeOut(punto_convergencia2))
        self.wait()
    def parte2 (self):
        text7=TextMobject('''Sin embargo, si nos acercamos por la recta menos \n
                                identidad, la función diverge a $-\\infty$.''')
        text7_1=TextMobject('''El límite con una sucesión. ''').move_to(3*UP)
        text7_2=TextMobject('''Con límite direccional. ''').move_to(3*UP)
 
        
        #objetos
        axes=ThreeDAxes()
        #Definimos la superficies por partes por la discontinuidad
        superficie1_1=superficie2_1_1()
        superficie1_2=superficie2_1_2()
        superficie1_3=superficie2_1_3()
        superficie1_4=superficie2_1_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)

        #Analogo a la parte anterior pueden moficiarse los valores n's y t's así como los conjuntos de posiciones para modificar el movimiento de las sucesiones y límites direccionales
        #z<0
        #Con sucesiones
        n1_3= 17 +17
        cjto1_3 = []
        for i in range(2,n1_3):
            if i<= 17:
                x = -3+(0.1*i)
            if i > 17:
                x= -3+(0.1*17)+((i-17)*0.06)
            cjto1_3.append((x,-x,-1/(x**2)))
        n1_4= 17+17
        cjto1_4 = []
        for i in range(2,n1_4):
            if i<=17:
                x = 3-(0.1*i)
            if i>17:
                x = 3-(0.1*17)-((i-17)*0.06)
            cjto1_4.append((x,-x,-1/(x**2)))
        
        Elementos1_3 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_3]
        Elementos13 = VGroup(*Elementos1_3)
        Elementos1_4 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_4]
        Elementos14 = VGroup(*Elementos1_4)
        #Con limite direccional
        #Con limite direccional
        t1_1=ValueTracker(-3)
        punto_convergencia1=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([-3,-3,1/(9)])
        t1_1f=-0.45  
        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto_convergencia1.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,-t,-t**(-2)]))

        punto_convergencia1.add_updater(mov_sup1)

        #Movimiento del punto en la recta identidad parte positiva
        t1_2=ValueTracker(3)
        punto_convergencia2=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([3,3,1/(9)])
        t1_2f=0.3  
        def mov_sup2 (obj):
            t = t1_2.get_value()
            punto_convergencia2.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,-t,-t**(-2)]))
        punto_convergencia2.add_updater(mov_sup2)

        #Animación
        self.add_fixed_in_frame_mobjects(text7)        
        self.play(Write(text7))
        self.wait(10)
        self.play(FadeOut(text7))
        self.set_camera_orientation(0.7*np.pi/2, 0.50*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text7_1)
        self.play(Write(text7_1))
        self.play(ShowCreation(Elementos13), run_time=10)
        self.wait()
        self.play(FadeOut(Elementos13),FadeOut(text7_1))
        self.add_fixed_in_frame_mobjects(text7_2)
        self.play(Write(text7_2))
        self.add(punto_convergencia1)
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.play(FadeOut(punto_convergencia1),FadeOut(text7_2))
        self.move_camera(0.7*np.pi/2, 1.35*np.pi,distance=12)
        self.add_fixed_in_frame_mobjects(text7_1)
        self.play(Write(text7_1))
        self.play(ShowCreation(Elementos14), run_time=10)
        self.wait()
        self.play(FadeOut(Elementos14),FadeOut(text7_1))
        self.add_fixed_in_frame_mobjects(text7_2)
        self.play(Write(text7_2))
        self.add(punto_convergencia2)
        self.play(t1_2.set_value, t1_2f,run_time=10)
        self.play(FadeOut(punto_convergencia2),FadeOut(text7_2),
                FadeOut(axes),FadeOut(superficie))
        self.wait()

    def parte3 (self):
        text8=TextMobject('''Veamos otro ejemplo.''')
        text9=TextMobject('''Sea $f:\\mathbb{R}^{2}-{\\vec{0}}\\rightarrow\\mathbb{R}$\\
                                $f(x,y)=\\frac{2xy}{x^2+y^2}$''').move_to(3*UP)
        text10=TextMobject('''Notemos que si nos aproximamos al origen en el \n
                                dominio en las direcciones canónicas entonces \n
                                el límite es 0.''').move_to(3*DOWN)      
        text11=TextMobject('''Ahora tomemos la dirección dada por la recta \n
                                identidad y veamos qué ocurre.''').move_to(3*UP)
        text12=TextMobject('''Notamos que en este caso el límite es diferente \n
                                    de 0.''').move_to(3*UP)

        #Puede cambiarse t1_t y t1_1f para cambiar el intervalo donde se obtendrá la derivada direccional
        t1_1=ValueTracker(-3)
        punto_convergencia1=Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([-3,-3,1/(9)])
        t1_1f=-0.45  
        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto_convergencia1.become(Sphere(radius=0.05, fill_opacity=1, fill_color = RED).move_to([t,t,t**(-2)]))

        punto_convergencia1.add_updater(mov_sup1)

        #Objetos
        axes=ThreeDAxes()
        superficie1_1=superficie2_2_1()
        superficie1_2=superficie2_2_2()
        superficie1_3=superficie2_2_3()
        superficie1_4=superficie2_2_4()
        superficie=VGroup(superficie1_1,superficie1_2,superficie1_3,superficie1_4)

        #Limite en direcciónes canónicas
        #Puede cambiarse las n's para cambiar el intervalo donde se obtendrá la derivada direccional
        n1_1= 15
        cjto1_1 = []
        cjto1_2 = []
        for i in range(1,n1_1):
            y1=3-i*(0.2)
            x1=0
            x=-3+i*(0.2)
            y=0
            cjto1_2.append((x1,y1,2*x1*y1/(x1**2+y1**2)))
            cjto1_1.append((x,y,2*x*y/(x**2+y**2)))
        
        #Con sucesiones
        Elementos1_1 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_1]
        Elementos1_2 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_2]
        Elementos1 = VGroup(*Elementos1_1,*Elementos1_2)

        
        #Con sucesiones
        Elementos1_1 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_1]
        Elementos1_2 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_2]
        Elementos1 = VGroup(*Elementos1_1,*Elementos1_2)

        #Limite en dirección de la identidad
        n1_2=15
        cjto1_3 = []
        cjto1_4 = []
        for i in range(1,n1_2):
            x2=3-i*(0.2)
            x3=-3+i*(0.2)
            cjto1_3.append((x2,x2,2*x2*x2/(x2**2+x2**2)))
            cjto1_4.append((x3,x3,2*x3*x3/(x3**2+x3**2)))
        Elementos1_3 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_3]
        Elementos1_4 = [Dot(color=RED).set_color(RED_E).move_to(i) for i in cjto1_4]
        Elementos2 = VGroup(*Elementos1_3,*Elementos1_4)

        
        #Animación
        self.add_fixed_in_frame_mobjects(text8)
        self.play(Write(text8))
        self.wait(4.5)
        self.play(FadeOut(text8))
        self.set_camera_orientation(0.7*np.pi/2, (-1.4)*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.play(ShowCreation(superficie))
        self.add_fixed_in_frame_mobjects(text9)
        self.play(Write(text9))
        self.wait(5)
        self.play(FadeOut(text9))
        self.add_fixed_in_frame_mobjects(text10)
        self.play(Write(text10))
        self.wait(4)
        self.play(ShowCreation(Elementos1),runtime=15)
        self.wait(1.5)
        self.play(FadeOut(text10),FadeOut(Elementos1))
        self.add_fixed_in_frame_mobjects(text11)
        self.play(Write(text11))
        self.wait(4)
        self.play(ShowCreation(Elementos2),runtime=15)
        self.wait()
        self.play(FadeOut(text11),FadeOut(Elementos2))
        self.add_fixed_in_frame_mobjects(text12)
        self.play(Write(text12))
        self.wait(7.5)
        self.play(FadeOut(text12),FadeOut(axes),FadeOut(superficie))

    def parte4 (self):
        text13=TextMobject('''Entonces con esto comprobamos que a veces no \n
                                 es suficiente analizar la función en \n
                                      las direcciones canónicas.''')
        text14=TextMobject('''Sin embargo, como es de esperar, \n
                                si encontramos dos direcciones donde el \n
                                límite difiere, entonces podemos concluir \n
                                    que el límite no existe.''')
        text15=TextMobject('''Puede ocurrir que si nos acercamos al punto del\n
                                 dominio en cualquier dirección, el límite sea\n
                                 el mismo, pero la función no tener límite. ''')
        text15_1=TextMobject('''Por ejemplo, $f(x,y)=1$ si $y=x^3$ y $f(x,y)=0$ en otro caso''').move_to(3*UP)
        text15_2=TextMobject(''' $f$ no tiene límite en $\\vec{0}$, aunque sí existen \n
                                todos los límites direccionales en el punto.''').move_to(3*UP)

        text16=TextMobject("¿Cómo argumentamos entonces cuando el límite sí existe?").move_to(2*UP)
        text16_1=TextMobject("Una manera es usando la definición, o sea, la métrica.").move_to(1*UP)
        text17=TextMobject("Pero también podemos usar criterios de comparación.").move_to(0*DOWN)
        text18=TextMobject('''Podemos analizar los órdenes de magnitud de los''').move_to(1*DOWN)
        text18_1=TextMobject('''términos de la función''').move_to(2*DOWN)

        
        axes=ThreeDAxes()
        superficie=superficie2_3()
        f = ParametricFunction(curva,t_min=-(3**(1/3)),t_max=3**(1/3),color=BLUE_D)
        f1 = ParametricFunction(curva1,t_min=-(3**(1/3)),t_max=3**(1/3),color=BLACK)

        t1_1=ValueTracker(-3)
        t1_1f=-0.2
        punto1=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([0,-3,0])
        punto2=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([-3,0,0])
        punto3=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([0,3,0])
        punto4=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([3,0,0])
        punto5=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([3,-3,0])
        punto6=Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([-3,3,0])

       
        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto1.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([0,t,0]))
            punto2.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([t,0,0]))
            punto3.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([0,-t,0]))
            punto4.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED).move_to([-t,0,0]))
            punto5.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED)).move_to([-t,t,0])
            punto6.become(Dot(radius=0.1, fill_opacity=1, fill_color = RED)).move_to([t,-t,0])


        punto1.add_updater(mov_sup1)
        punto2.add_updater(mov_sup1)
        punto3.add_updater(mov_sup1)
        punto4.add_updater(mov_sup1)
        punto5.add_updater(mov_sup1)
        punto6.add_updater(mov_sup1)
        puntos=VGroup(punto1,punto2,punto3,punto4,punto5,punto6)


        #Animación
        self.add_fixed_in_frame_mobjects(text13)
        self.play(Write(text13))
        self.wait(9)
        self.play(FadeOut(text13))
        self.add_fixed_in_frame_mobjects(text14)
        self.play(Write(text14))
        self.wait(10)
        self.play(FadeOut(text14))
        self.add_fixed_in_frame_mobjects(text15)
        self.play(Write(text15))
        self.wait(12)
        self.play(FadeOut(text15))
        self.set_camera_orientation(0.7*np.pi/2, 0.25*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text15_1)
        self.play(Write(text15_1))
        self.wait(6)
        self.play(ShowCreation(superficie))
        self.play(ShowCreation(f),ShowCreation(f1))
        self.wait(2)
        self.play(FadeOut(text15_1))
        self.add_fixed_in_frame_mobjects(text15_2)
        self.play(Write(text15_2))
        self.wait(5)
        self.play(ShowCreation(puntos))
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.play(FadeOut(text15_2),FadeOut(axes),FadeOut(superficie),FadeOut(f),
                    FadeOut(f1),FadeOut(puntos))
        self.add_fixed_in_frame_mobjects(text16)
        self.play(Write(text16))
        self.wait(7)
        self.add_fixed_in_frame_mobjects(text16_1)
        self.play(Write(text16_1))
        self.wait(8)
        self.add_fixed_in_frame_mobjects(text17)
        self.play(Write(text17))
        self.wait(7)
        self.add_fixed_in_frame_mobjects(text18)
        self.play(Write(text18))
        self.add_fixed_in_frame_mobjects(text18_1)
        self.play(Write(text18_1))
        self.wait(9)
        self.play(FadeOut(text17),FadeOut(text16),FadeOut(text16_1),FadeOut(text18),FadeOut(text18_1))

    def parte5 (self):
        text19=TextMobject('''Por ejemplo $f:\\mathbb{R}^{2}-{\\vec{0}}\\rightarrow\\mathbb{R}$\n
                                 $f(x,y)=\\frac{1}{(x+y)^{2}}$''').move_to(3*DOWN)
        text20=TextMobject('''Cuando nos vamos acercando a $\\vec{0}$, \n
                                esta función diverge.''').move_to(3.5*DOWN)
        text21=TextMobject('''Sin embargo no nos pasa \n
                                como en el primer ejemplo, ''','''\n
                                que la función diverge\n
                                 hacia $\\infty$ o $-\\infty$ dependiendo \n
                                 de la dirección\n
                                  que escogemos;''','''\n
                                 en este caso sólo diverge a $\\infty$, \n
                                lo cual se puede demostrar sin mucha \n
                                dificultad porque el numerador es una \n
                                constante y el denominador tiende a \n
                                cero con valores positivos.''')
        text22=TextMobject('''Ahora piensa en la función $f(x,y)=\\frac{|x-y|}{(x+y)^2}$''')
        text23=TextMobject('''Tiende a infinito en el origen,''',''' porque el cuadrado en el \n
                                 denominador afecta a las dos variables,''',''' lo que nos da \n
                                 una valor mucho más pequeño que $|x-y|$ conforme ambas \n
                                  variables tienden a cero.''')#.move_to(2*DOWN)

        axes=ThreeDAxes()
        superficie21=superficie2_4_1()#superficie2_4_1()
        superficie22=superficie2_4_2()
        
        superficie=VGroup(superficie21,superficie22).rotate(-1.25*np.pi,axis=IN)

        t1_1=ValueTracker(-2)
        t1_1f=-0.3
        punto2=Sphere(radius=0.05, fill_opacity=1, checkerboard_colors=[RED_D, RED_C],fill_color = BLUE_E).move_to([-2,-2,1/(6)**2])

        def mov_sup1 (obj):
            t = t1_1.get_value()
            punto2.become(Sphere(radius=0.05, fill_opacity=1, checkerboard_colors=[RED_D, RED_C],fill_color = BLUE_E).move_to([-t,-t,1/(t+t)**2]).rotate(-1.25*np.pi,axis=IN))

        punto2.add_updater(mov_sup1)

        ##animación
        self.set_camera_orientation(0.7*np.pi/2, 0.65*np.pi,distance=12)
        self.play(ShowCreation(axes))
        self.add_fixed_in_frame_mobjects(text19)
        self.play(Write(text19))
        self.wait(5)
        self.play(ShowCreation(superficie))
        self.wait()
        self.play(FadeOut(text19))
        self.add_fixed_in_frame_mobjects(text20)
        self.play(Write(text20))
        self.wait(7)
        self.play(ShowCreation(punto2))
        self.play(t1_1.set_value, t1_1f,run_time=10)
        self.play(FadeOut(punto2),FadeOut(text20),FadeOut(axes),FadeOut(superficie))
        self.add_fixed_in_frame_mobjects(text21[0])
        self.play(Write(text21[0]))
        self.wait(7)
        self.add_fixed_in_frame_mobjects(text21[1])
        self.play(Write(text21[1]))
        self.wait(8)
        self.add_fixed_in_frame_mobjects(text21[2])
        self.play(Write(text21[2]))
        self.wait(17)
        self.play(FadeOut(text21))
        self.add_fixed_in_frame_mobjects(text22)
        self.play(Write(text22))
        self.wait(10)
        self.play(FadeOut(text22))
        self.add_fixed_in_frame_mobjects(text23[0])
        self.play(Write(text23[0]))
        self.wait(5.5)
        self.add_fixed_in_frame_mobjects(text23[1])
        self.play(Write(text23[1]))
        self.wait(7)
        self.add_fixed_in_frame_mobjects(text23[2])
        self.play(Write(text23[2]))
        self.wait(12)
        self.play(FadeOut(text23))
        
    def construct (self):    
        ### ANIMACIÓN PARA LAS DIFERENTES PARTES ###
        self.parte0()
        self.parte1()
        self.parte2()
        self.parte3()
        self.parte4()
        self.parte5()

