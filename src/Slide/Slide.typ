#import "lib.typ": *
#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge
#import "@preview/showybox:2.0.4": *



// ----- Lancement du thème diatypst sans la 1re diapo par défaut -----
#show: slides.with(
  title: "Markov Chain",            // requis
  subtitle: "A brief introduction",
  date: none,
  authors: ("Guerand Dewell, Arnaud Ullens, Arnaud Stienon"),
  ratio: 4/3,                   // cohérent avec la page ci-dessus
  layout: "medium",             // "small" | "medium" | "large"
  first-slide: true,           // désactive la diapo titre par défaut
  toc: true,
  count: none,
  footer: true,
  logo : "pictures/image.png",
  title-color: navy
)
= Introduction 
= Context

== Context

  - Guerre civile 
  #columns(2)[
    Pavel Nekrasov 

    Independance $<=>$ Loi des grands nombres
    #image("pictures/téléchargement.jpg", width: 60%)


    #colbreak()
    Andrei Markov



    Independance $=>$ Loi des grands nombres 
    #image("pictures/téléchargement (1).jpg", width: 60%)

  ]
  
== Small exemple $(1)$

Imaginons que nous voulions estimer la probabilitée qu'ils pleuvent ou qu'il y ait grand soleil. 
On peut créer le graphe suivant :

#align(center ,diagram(
	node-stroke: .1em,
	node-fill: blue,
	spacing: 4em,
	node((0,0), `Sunny day`, radius: 3em , ),
	edge($20%$, "<|-" , bend: 20deg),

	node((2,0), `Rainy day`, radius: 3em),
edge((0,0),(2,0),$30%$, "-|>" , bend: -20deg),

	edge((0,0), (0,0), $70%$, "<|-", bend: 130deg),
 edge((2,0), (2,0), $80%$, "-|>", bend: 130deg),
 
))
Ici nous avons deux états : Sunny et Rainy

== Small exemple $(2)$

On peut en fait représenter ce graphe de la manière suivante en terme de probabilitée : 
#figure(
  table(
    columns: 3,
    stroke: none,

    table.header[][S][R],
    [S], [$70%$], [$30%$], 
    
    [R], [$20%$], [$80%$], 
    
  ),
) <probe-a>

#showybox(
  frame: (
    border-color: luma(0).darken(50%),
    title-color: luma(170).lighten(60%),
    body-color: luma(170).lighten(80%)
  ),
  title-style: (
    color: black,
    weight: "regular",
   
  ),
  shadow: (
    offset: 3pt,
  ),
  title: "Definition",
  [ 
    Un état $S_i$ est une situation possible du système à un instant donné, choisie dans un ensemble fini ou dénombrable.

    Ici dans notre exmple nous avons $S = mat(S ,R)$

    Avec $S$ = Sunny et $R$ = Rainy
  ],
)




= Theory 
= Credit risk Measurement
== 
#showybox(
  frame: (
    border-color: luma(0).darken(50%),
    title-color: luma(170).lighten(60%),
    body-color: luma(170).lighten(80%)
  ),
  title-style: (
    color: black,
    weight: "regular",
   
  ),
  shadow: (
    offset: 3pt,
  ),
  title: "Definition : Note de crédit",
  [ 
    Note attribué a une entreprise pour déterminer la fiabilitée de remboursement des dettes de l'entreprise.
  ],

)
But : Déterminer la probabilitée qu'une entreprise change de note d'une année à l'autre.

On veut alors créer la matrice de transition mais comment ? 

Deux possibilitées : 
- Note basée sur l'historique des données
- Note basée sur des experts 

Possibilitées de combiner les deux : 
$ P_("total") = alpha P_("agency") + (1 - alpha) P_("expert") $
== Exemple 


#figure(
  table(
    columns: 9,
    stroke: none,

    table.header[][AAA][AA][A][BBB][BB][B][CCC][D],

    [AAA], [$0.88$], [$0.08$], [$0.02$], [$0.01$], [$0.005$], [$0.003$], [$0.001$], [$0.001$],
[AA],  [$0.04$], [$0.85$], [$0.06$], [$0.03$], [$0.01$],  [$0.005$], [$0.003$], [$0.002$],
[A],   [$0.01$], [$0.06$], [$0.80$], [$0.08$], [$0.03$],  [$0.01$],  [$0.008$], [$0.002$],
[BBB], [$0.005$],[$0.02$], [$0.07$], [$0.75$], [$0.10$],  [$0.03$],  [$0.02$],  [$0.005$],
[BB],  [$0.002$],[$0.01$], [$0.03$], [$0.10$], [$0.70$],  [$0.10$],  [$0.05$],  [$0.008$],
[B],   [$0.001$],[$0.005$],[$0.015$],[$0.04$], [$0.15$],  [$0.60$],  [$0.15$],  [$0.039$],
[CCC], [$0$],   [$0.002$],[$0.008$],[$0.03$], [$0.10$],  [$0.16$],  [$0.50$],  [$0.20$],
[D],   [$0$],   [$0$],    [$0$],    [$0$],    [$0$],     [$0$],     [$0$],     [$1$],

  ),
  caption: [Complete credit rating transition matrix (AAA to D)],
)

Si l'ont veut estimer la probabilitée d'être que l'entreprise ait un autre rating en se basant sur notre état actuel : $S_n = S_0 P_n$. On peut également déterminer la probabilitée à long terme d'être dans chaque état. 

== Exemple

For instance if we want to predict for different value of $n$ : 
#table(
    columns: 9,

[*n*],  [*AAA*],  [*AA*],  [*A*],   [*BBB*], [*BB*],  [*B*],   [*CCC*], [*D*],

[5],    [$0.552$], [$0.238$], [$0.088$], [$0.054$], [$0.031$], [$0.016$], [$0.009$], [$0.011$],

[10],   [$0.339$], [$0.270$], [$0.136$], [$0.098$], [$0.065$], [$0.033$], [$0.021$], [$0.039$],

[100],  [$0.023$], [$0.042$], [$0.040$], [$0.040$], [$0.035$], [$0.019$], [$0.012$], [$0.790$],

[1000], [$0.000$], [$0.000$], [$0.000$], [$0.000$], [$0.000$], [$0.000$], [$0.000$], [$1.000$],



  )
= Hidden markov model 


= Further reading
= About _diatypst_

== General

_diatypst_ is a simple slide generator for _typst_.

Features:

- easy delimiter for slides and sections (just use headings)
- sensible styling
- dot counter in upper right corner (like LaTeX beamer)
- adjustable color-theme
- default show rules for terms, code, lists, ... that match color-theme

This short presentation is a showcase of the features and options of _diatypst_.

== Usage

To start a presentation, initialize it in your typst document:

```typst
#import "@preview/diatypst:0.8.0": *
#show: slides.with(
  title: "Diatypst", // Required
  subtitle: "easy slides in typst",
  date: "01.07.2024",
  authors: ("John Doe"),
)
...
```

Then, insert your content.

- Level-one headings corresponds to new sections.
- Level-two headings corresponds to new slides.

== Options


To start a presentation, only the title key is needed, all else is optional!

Basic Content Options:
#table(
  columns: 3,
  [*Keyword*], [*Description*], [*Default*],
  [_title_], [Title of your Presentation, visible also in footer], [`none` (required!)],
  [_subtitle_], [Subtitle, also visible in footer], [`none`],
  [_date_], [a normal string presenting your date], [`none`],
  [_authors_], [either string or array of strings], [`none`],
  [_footer-title_], [custom text in the footer title (left)], [same as `title`],
  [_footer-subtitle_], [custom text in the footer subtitle (right)], [same as `subtitle`],
)

#pagebreak()

Advanced Styling Options:
#table(
  columns: 3,
  [*Keyword*], [*Description*], [*Default*],
  [_layout_], [one of _small, medium, large_, adjusts sizing of the elements on the slides], [`"medium"`],
  [_ratio_], [aspect ratio of the slides, e.g., 16/9], [`4/3`],
  [_title-color_], [Color to base the Elements of the Presentation on], [`blue.darken(50%)`],
  [_bg-color_], [Background color of the slides, can be any color], [`white`],
  [_count_], [one of _dot, number, none_, adjusts the style of page counter in the right corner], [`"dot"`],
  [_footer_], [whether to display the footer at the bottom], [`true`],
  [_toc_], [whether to display the table of contents], [`true`],
  [_theme_], [one of _normal, full_, adjusts the theme of the slide], [`"normal"`],
  [_first-slide_], [whether to include the default title slide], [`true`],
)

The full theme adds more styling to the slides, similar to a a full LaTeX beamer theme.

= Default Styling in diatypst

== Terms, Code, Lists

_diatypst_ defines some default styling for elements, e.g Terms created with ```typc / Term: Definition``` will look like this

/ *Term*: Definition

A code block like this

```python
// Example Code
print("Hello World!")
```

Lists have their marker respect the `title-color`

#columns(2)[
  - A
    - AAA
      - B
  #colbreak()
  1. AAA
  2. BBB
  3. CCC
]



== Tables and Quotes



#columns(2)[
  Look at this styled table
  #table(
    columns: 3,
    [*Header*],[*Header*],[*Header*],
    [Cell],[Cell],[Cell],
    [Cell],[Cell],[Cell],
  )
  #colbreak()
  compared to an original one
  #table(
    stroke: 1pt,
    columns: 3,
    [*Header*],[*Header*],[*Header*],
    [Cell],[Cell],[Cell],
    [Cell],[Cell],[Cell],
  )
]

And here comes a quote

#quote(attribution: [Plato])[
  This is a quote
]

And finally, web links are styled like this: #link("https://typst.app")[typst.app]

= Additional

== More Info

For more information, visit the #link("www.github.com/skriptum/diatypst")[diatypst repository]. The package is also available on the #link("https://typst.app/universe/package/diatypst")[typst universe].

For Issues and Feature Requests, please use the GitHub Repo.

To find the source code for this presentation, visit the #link("https://github.com/skriptum/diatypst/tree/main/example")[example folder on GitHub]. An minimal template can also be #link("https://github.com/skriptum/diatypst/blob/main/template/main.typ")[found here]

== Inspiration

this template is inspired by #link("https://github.com/glambrechts/slydst")[slydst], and takes part of the code from it. If you want simpler slides, look here!

The word _diatypst_ is inspired by

#columns(2)[
  // #image("diaprojektor.jpg", height: 3cm)
  // the ease of use of a #link("https://de.wikipedia.org/wiki/Diaprojektor")[Diaprojektor] (German for Slide Projector)

  // #colbreak()

  // #image("diatype.jpg", height: 3cm)
  // and the #link("https://en.wikipedia.org/wiki/Diatype_(machine)")[Diatype] (60s typesetting machine)
]