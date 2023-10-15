from manim import *
from manim_slides import Slide


class TitleSlide(Slide):
    def construct(self):
        self.wait_time_between_slides = 0.1

        background = ImageMobject("cabodehornos", scale_to_resolution=1080, z_index=0)
        udec_logo = ImageMobject("udec", z_index=10).scale(0.5).to_edge(UL, buff=0.5)

        title = VGroup(
                Text("Estabilización dinámica de una mesa", t2w={"Estabilización dinámica": BOLD}, t2c={"Estabilización dinámica": RED, "mesa": BLUE}),
                Text("abordo de una embarcación marina", t2w={"embarcación marina": BOLD}, t2c={"embarcación marina": YELLOW})
        ).arrange(DOWN).shift(2*DOWN).set_z_index(10)

        title_box = Rectangle(
                width=title.width + 1, height=title.height + 1,
                fill_color=DARK_GRAY, stroke_width=0, fill_opacity=0.7, z_index=9
        ).move_to(title.get_center())

        self.add(background)
        self.play(FadeIn(title_box, title, udec_logo))

        ode_title = Text("Determinemos nuestra EDO").to_edge(UP)

        self.next_slide()
        self.play(self.wipe([title, title_box, udec_logo, background], ode_title))

        ode = MathTex(
                r"M", r"({{q}})", r"\ddot q", r"+ ", r"C", r"({{q, \dot q}})", r"\dot q", "+", "G", r"=", r"\tau", r"+", r"\tau_w",
                font_size=72,
        ).to_edge(DOWN).set_color_by_tex('q', YELLOW).set_color_by_tex('M', BLUE).set_color_by_tex('C', GREEN).set_color_by_tex('G', RED).set_color_by_tex('tau', PURPLE)
        ode.set_opacity_by_tex('q', 0).set_opacity_by_tex('M', 0).set_opacity_by_tex('C', 0).set_opacity_by_tex('G', 0).set_opacity_by_tex('tau', 0)
        self.play(FadeIn(ode))

        ### Variable q

        q_var = MathTex(
                r"q", r"= \begin{bmatrix} z \\ \phi \\ \theta \end{bmatrix}",
                font_size=72
        )

        self.play(Write(q_var))
        self.next_slide()

        self.play(ode.animate.set_opacity_by_tex("q", opacity=1), Transform(q_var, ode.get_parts_by_tex("q")))
        self.wait(0.5)

        ### Variable M

        m_var = MathTex(
                r"M(q)", r"= \begin{bmatrix} m_p & 0 & 0 \\ 0 & I_y c^2\phi + I_z s^2\phi & (I_y - I_z) c\phi c\theta s\phi \\ 0 & (I_y - I_z) c\phi c\theta c\phi & I_z c^2\phi c^2\theta + I_y c^2\theta s^2\phi + I_x s^2\theta \end{bmatrix}",
                font_size=48
        )
        self.play(Write(m_var))
        self.next_slide()

        self.play(ode.animate.set_opacity_by_tex("M", opacity=1), Transform(m_var, ode.get_parts_by_tex("M")))
        self.wait(0.5)

        ### Variable C

        c_var = MathTex(
                r"C(q, \dot q)", r"= \begin{bmatrix} 0 & 0 & 0 \\ 0 & (I_z - I_y) \dot\phi s 2\phi & (I_z - I_y)(\dot\phi c\theta - 4 \dot\phi c\phi c\theta + \dot\theta c\phi s\phi s\theta) \\ 0 & (I_z - I_y) (\dot\phi c\theta - 4 \dot\phi c\phi c\theta + \dot\theta c\phi s\phi s\theta) & \begin{smallmatrix} 2(I_x - I_y s^2\phi - I_z c^2\phi) \dot\theta s\theta c\theta \\ {}+ 2(I_y - I_z) \dot\phi c\phi c\theta s\phi c\theta \end{smallmatrix} \end{bmatrix}",
                font_size=32
        )
        self.play(Write(c_var))
        self.next_slide()

        self.play(ode.animate.set_opacity_by_tex("C", opacity=1), Transform(c_var, ode.get_parts_by_tex("C")))
        self.wait(0.5)

        ### Variable G

        g_var = MathTex(
                r"G", r"= \begin{bmatrix} m_p g \\ 0 \\ 0 \end{bmatrix}",
                font_size=72
        )

        self.play(Write(g_var))
        self.next_slide()

        self.play(ode.animate.set_opacity_by_tex("G", opacity=1), Transform(g_var, ode.get_parts_by_tex("G")))
        self.wait(0.5)

        ### Variable tau

        t_var = MathTex(
                r"\tau", r"&= \begin{bmatrix} \tau_1 \\ \tau_2 \\ \tau_3 \end{bmatrix} &",
                r"\tau_w", r"&= \begin{bmatrix} \tau_{w,1} \\ \tau_{w,2} \\ \tau_{w,3} \end{bmatrix}",
                font_size=72
        )

        self.play(Write(t_var))
        self.next_slide()

        self.play(ode.animate.set_opacity_by_tex("tau", opacity=1), Transform(t_var, ode.get_parts_by_tex("tau")))
        self.wait(0.25)

        self.play(ode.animate.move_to(0*UP))
        self.play(Circumscribe(ode))

        author = VGroup(
                Text("Creado por"),
                Text("Bruno Pacheco Champin"),
                Text("Grupo 23")
                ).arrange(DOWN).scale(0.3).to_edge(DL)


        course = VGroup(
                Text("Departamento de Ingeniería Eléctrica"),
                Text("Modelación de Procesos"),
                Text("Profesor Juan Pablo Segovia")
                ).arrange(DOWN).scale(0.3).to_edge(DR)

        self.play(Write(author), Write(course))


class Introduction(Slide):
    def construct(self):
        welcome = Text("This is the Manim Slides starter")
        square = Square(color=BLUE)
        dot = Dot(color=RED).shift(RIGHT + UP)

        self.play(FadeIn(welcome))
        self.next_slide()

        self.play(self.wipe(welcome, square))
        self.play(FadeIn(dot))
        self.next_slide()

        self.start_loop()
        self.play(
            MoveAlongPath(dot, square, rate_func=linear), run_time=2
        )
        self.end_loop()


class WithTeX(Slide):
    def construct(self):
        tex, text = VGroup(
            Tex(r"You can also use \TeX, e.g., $\cos\theta=1$"),
            Text("which does not render like plain text"),
        ).arrange(DOWN)

        self.play(FadeIn(tex))
        self.next_slide()

        self.play(FadeIn(text, shift=DOWN))


class Outro(Slide):
    def construct(self):
        learn_more = VGroup(
            Text("Learn more about Manim Slides:"),
            Text("https://manim-slides.eertmans.be"),
        ).arrange(DOWN)

        self.play(FadeIn(learn_more))
