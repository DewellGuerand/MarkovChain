from manim import *
from manim_slides import Slide

class MarkovChainPresentation(Slide):
    def construct(self):
        # Configuration du logo
        # logo = ImageMobject("image.png").scale(0.15).to_corner(UR)
        # self.add(logo)
        
        # === SLIDE 1 ===
        title1 = Text("Markov Chains", font_size=48, color=WHITE)
        subtitle1 = Text("A brief introduction", font_size=32, color=BLUE)
        subtitle1.next_to(title1, DOWN, buff=0.5)
        subtitle2 = Text("by Guerand Dewell, Arnaud Ullens, Arnaud Stienon", font_size=24, color=WHITE)
        subtitle2.next_to(subtitle1, DOWN, buff=1.5)
        
        # Animation du titre
        self.play(Write(title1))
        self.play(Write(subtitle1))
        self.play(Write(subtitle2))
        self.next_slide()
        
        # === SLIDE 2 - Table des matières ===
        self.play(FadeOut(title1), FadeOut(subtitle1), FadeOut(subtitle2))
        
        title2 = Text("Content", font_size=48, color=WHITE)
        title2.to_edge(UP)
        
        bullet_points = BulletedList(
            "Introduction to Markov Chains",
            "Mathematical Definition",
            "Transition Diagrams",
            "Weather Example",
            "Applications",
            font_size=28,
            dot_scale_factor=1.5,
            color=WHITE
        )
        bullet_points.next_to(title2, DOWN, buff=0.8)
        
        self.play(Write(title2))
        self.play(Write(bullet_points))
        self.next_slide()
        
        # === SLIDE 3 - Introduction ===
        self.play(FadeOut(title2), FadeOut(bullet_points))
        
        title3 = Text("Introduction to Markov Chains", font_size=42, color=WHITE)
        title3.to_edge(UP)

        intro_text = Text(
            "Markov chains are a fundamental part of stochastic processes.\n"
            "They are used widely in many different disciplines.",
            font_size=24,
            color=WHITE,
            line_spacing=1.2
        )
        intro_text.next_to(title3, DOWN, buff=0.8)
        
        markov_property = Text(
            "Markov Property: The past and future are independent\nwhen the present is known.",
            font_size=20,
            color=YELLOW,
            line_spacing=1.2
        )
        markov_property.next_to(intro_text, DOWN, buff=0.8)
        
        advantage_text = Text(
            "This simplicity allows for great reduction of parameters\nwhen studying such processes.",
            font_size=20,
            color=GREEN,
            line_spacing=1.2
        )
        advantage_text.next_to(markov_property, DOWN, buff=0.8)
        
        self.play(Write(title3))
        self.play(Write(intro_text))
        self.next_slide()
        self.play(Write(markov_property))
        self.next_slide()
        self.play(Write(advantage_text))
        self.next_slide()
        
        # === SLIDE 4 - Définition Mathématique ===
        self.play(FadeOut(title3), FadeOut(intro_text), FadeOut(markov_property), FadeOut(advantage_text))
        
        title4 = Text("Mathematical Definition", font_size=42, color=WHITE)
        title4.to_edge(UP)
        
        # Définition du processus
        process_def = MathTex(
            r"X = \{X_n, n \in \mathbb{N}\} \text{ in countable space } S",
            font_size=28
        )
        process_def.next_to(title4, DOWN, buff=0.8)
        
        # Condition 1
        condition1 = MathTex(
            r"\text{For all } n \geq 0, X_n \in S",
            font_size=24
        )
        condition1.next_to(process_def, DOWN, buff=0.6)
        
        # Condition 2 (équation principale)
        condition2 = MathTex(
            r"P(X_n = i_n \mid X_{n-1} = i_{n-1}, \ldots, X_0 = i_0) = P(X_n = i_n \mid X_{n-1} = i_{n-1})",
            font_size=20
        )
        condition2.next_to(condition1, DOWN, buff=0.6)
        
        self.play(Write(title4))
        self.play(Write(process_def))
        self.next_slide()
        self.play(Write(condition1))
        self.next_slide()
        self.play(Write(condition2))
        self.next_slide()
        
        # === SLIDE 5 - Exemple Météo ===
        self.play(FadeOut(title4), FadeOut(process_def), FadeOut(condition1), FadeOut(condition2))
        
        title5 = Text("Weather Example", font_size=42, color=WHITE)
        title5.to_edge(UP)
        
        # Description de l'exemple
        example_text = Text(
            "Weather prediction using Markov chains:",
            font_size=24,
            color=WHITE
        )
        example_text.next_to(title5, DOWN, buff=0.8)
        
        # Probabilities
        prob_text1 = Text(
            "If sunny today: 70% sunny tomorrow, 30% rainy tomorrow",
            font_size=20,
            color=GREEN
        )
        prob_text1.next_to(example_text, DOWN, buff=0.6)
        
        prob_text2 = Text(
            "If rainy today: 20% sunny tomorrow, 80% rainy tomorrow",
            font_size=20,
            color=BLUE
        )
        prob_text2.next_to(prob_text1, DOWN, buff=0.4)
        
        self.play(Write(title5))
        self.play(Write(example_text))
        self.next_slide()
        self.play(Write(prob_text1))
        self.next_slide()
        self.play(Write(prob_text2))
        self.next_slide()
        
        self.play(FadeOut(title5), FadeOut(example_text), FadeOut(prob_text1), FadeOut(prob_text2))

        title6 = Text("Transition Diagram", font_size=42, color=WHITE)
        title6.to_edge(UP)

        # --- États ---
        sunny_state = Circle(radius=1.2, color=YELLOW, fill_color=YELLOW, fill_opacity=0.9, stroke_width=3)
        sunny_state.shift(LEFT * 3)
        sunny_label = Text("Sunny\nDay", font_size=28, color=WHITE).move_to(sunny_state.get_center())

        rainy_state = Circle(radius=1.2, color=BLUE, fill_color=BLUE, fill_opacity=0.9, stroke_width=3)
        rainy_state.shift(RIGHT * 3)
        rainy_label = Text("Rainy\nDay", font_size=28, color=WHITE).move_to(rainy_state.get_center())


        # --- Labels style "boîte blanche" ---
        def boxed_label(text):
            box = Rectangle(color=WHITE, fill_opacity=1, fill_color=WHITE, height=0.5, width=1)
            t = Text(text, font_size=22, color=BLACK)
            group = VGroup(box, t)
            return group


        # --- Boucles ---
        sunny_loop = Arc(
            radius=1.1, 
            angle=TAU * 0.7, 
            start_angle=PI / 2,
            color=BLUE,
            stroke_width=8
        ).move_arc_center_to(sunny_state.get_center())

        sunny_loop_label = boxed_label("70%").next_to(sunny_loop, LEFT, buff=0.2)

        rainy_loop = Arc(
            radius=1.1,
            angle=TAU * 0.7,
            start_angle=-PI / 2,
            color=BLUE,
            stroke_width=8
        ).move_arc_center_to(rainy_state.get_center())

        rainy_loop_label = boxed_label("80%").next_to(rainy_loop, RIGHT, buff=0.2)


        # --- Transitions Sunny → Rainy ---
        sunny_to_rainy = CurvedArrow(
            sunny_state.get_right() + UP * 0.2,
            rainy_state.get_left() + UP * 0.2,
            color=BLUE,
            stroke_width=10,
            tip_length=0.25,
            radius=3.5
        )

        sunny_to_rainy_label = boxed_label("20%").next_to(sunny_to_rainy, UP, buff=0.15)


        # --- Transitions Rainy → Sunny ---
        rainy_to_sunny = CurvedArrow(
            rainy_state.get_left() + DOWN * 0.2,
            sunny_state.get_right() + DOWN * 0.2,
            color=BLUE,
            stroke_width=10,
            tip_length=0.25,
            radius=3.5
        )

        rainy_to_sunny_label = boxed_label("30%").next_to(rainy_to_sunny, DOWN, buff=0.15)


        # --- Animation ---
        self.play(Write(title6))
        self.next_slide()

        # États
        self.play(Create(sunny_state), Write(sunny_label))
        self.play(Create(rainy_state), Write(rainy_label))
        self.next_slide()

        # Boucles
        self.play(Create(sunny_loop), FadeIn(sunny_loop_label))
        self.play(Create(rainy_loop), FadeIn(rainy_loop_label))
        self.next_slide()

        # Transitions
        self.play(Create(sunny_to_rainy), FadeIn(sunny_to_rainy_label))
        self.play(Create(rainy_to_sunny), FadeIn(rainy_to_sunny_label))
        self.next_slide()
        # === SLIDE 7 - Matrice de Transition ===
        self.play(FadeOut(title6), FadeOut(sunny_state), FadeOut(rainy_state), 
                  FadeOut(sunny_label), FadeOut(rainy_label),
                  FadeOut(sunny_loop), FadeOut(rainy_loop),
                  FadeOut(sunny_loop_label), FadeOut(rainy_loop_label),
                  FadeOut(sunny_to_rainy), FadeOut(rainy_to_sunny),
                  FadeOut(sunny_to_rainy_label), FadeOut(rainy_to_sunny_label))
        
        title7 = Text("Transition Matrix", font_size=42, color=WHITE)
        title7.to_edge(UP)
        
        # Matrice de transition
        matrix_title = Text("Transition Matrix P:", font_size=24, color=YELLOW)
        matrix_title.next_to(title7, DOWN, buff=0.8)
        
        transition_matrix = MathTex(
            r"P = \begin{bmatrix} 0.7 & 0.3 \\ 0.2 & 0.8 \end{bmatrix}",
            font_size=36
        )
        transition_matrix.next_to(matrix_title, DOWN, buff=0.8)
        
        # Explication de la matrice
        explanation = Text(
            "Rows: current state\nColumns: next state",
            font_size=20,
            color=GREEN,
            line_spacing=1.2
        )
        explanation.next_to(transition_matrix, DOWN, buff=0.8)
        
        self.play(Write(title7))
        self.play(Write(matrix_title))
        self.next_slide()
        self.play(Write(transition_matrix))
        self.next_slide()
        self.play(Write(explanation))
        self.next_slide()
        
        # === SLIDE 8 - Applications ===
        self.play(FadeOut(title7), FadeOut(matrix_title), FadeOut(transition_matrix), FadeOut(explanation))
        
        title8 = Text("Applications", font_size=42, color=WHITE)
        title8.to_edge(UP)
        
        applications = BulletedList(
            "Natural language processing",
            "Speech recognition",
            "Bioinformatics",
            "Finance and economics",
            "Queueing theory",
            "Game theory",
            font_size=24,
            dot_scale_factor=1.5,
            color=WHITE
        )
        applications.next_to(title8, DOWN, buff=0.8)
        
        self.play(Write(title8))
        self.play(Write(applications))
        self.next_slide()
        
        # === SLIDE FINALE ===
        self.play(FadeOut(title8), FadeOut(applications))
        
        final_title = Text("Thank you for your attention!", font_size=42, color=WHITE)
        questions = Text("Questions?", font_size=36, color=YELLOW)
        questions.next_to(final_title, DOWN, buff=0.8)
        
        self.play(Write(final_title))
        self.play(Write(questions))
        self.next_slide()