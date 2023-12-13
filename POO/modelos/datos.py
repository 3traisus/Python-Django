

# base de datos de encuestas
datos_encuestas =[
    {"id":100,
     "nombre":"Habilidades de estudio",
     "instrucciones": "La presente encuesta está formada por tres breves cuestionarios, en los cuales puedes indicar los problemas referentes a organización, técnicas y motivación en el estudio, que quizá perjudican tu rendimiento académico. Si contestas todas las preguntas con sinceridad y reflexión podrás identificar mucho de tus actuales defectos al estudiar",
     "descripcion": "Descripcion . . . ",
     "estado": False
     },
    {"id":200,
     "nombre":"Estilos de aprendizaje 'Honey Alonso'",
     "instrucciones": "Este cuestionario ha sido diseñado para identificar su Estilo preferido de Aprendizaje. No es un test de inteligencia, ni de personalidad. No hay límite de tiempo para contestar el Cuestionario. No le ocupará más de 15 minutos. No hay respuestas correctas o errores. Será útil en la medida que sea sincero(a) en sus respuestas. Si está más en desacuerdo que de acuerdo, ponga un signo menos (-).",
     "descripcion": "Descripcion . . . ",
     "estado": False
     },
    {"id":300,
     "nombre":"Test de acertividad",
     "instrucciones": "Por favor marca con una X la opción con la que mejor te identificas.",
     "descripcion": "Descripcion . . . ",
     "estado": False
     },
    {"id":400,
     "nombre":"Test de autoestima",
     "instrucciones": "Realiza el siguiente test para evaluar y comprobar tu nivel de autoestima. Contesta con la mayor sinceridad posible a cada una de las siguientes preguntas eligiendo la respuesta que más se identifique con tu forma de pensar o de actuar.",
     "descripcion": "Descripcion . . . ",
     "estado": True
     }
]

# Preguntas
datos_preguntas =[
    {"id_pregunta":1,
     "id_encuesta":400,
     "numero_pregunta": 1,
     "titulo_pregunta": "A la hora de tomar decisiones en tu vida, como proponer cosas nuevas en el trabajo, iniciar alguna actividad de ocio, o elegir un color nuevo para pintar tu casa, ¿sueles buscar la aprobación o el apoyo de las personas que te rodean?"
     },
    {"id_pregunta":2,
     "id_encuesta":400,
     "numero_pregunta": 2,
     "titulo_pregunta": "Imagina que estás en una reunión social o familiar importante; adviertes que no vas vestido para la ocasión y que desentonas con los demás, ¿cómo te comportas?"
     },
    {"id_pregunta":3,
     "id_encuesta":400,
     "numero_pregunta": 3,
     "titulo_pregunta": "Tienes muchas ganas de irte a comprar ropa y le pides a algún amigo que te acompañe. Esta persona es más alta y más atractiva que tú, y todo lo que se prueba le queda mucho mejor que a ti."
     },
    {"id_pregunta":4,
     "id_encuesta":400,
     "numero_pregunta": 4,
     "titulo_pregunta": "Un día conoces a alguien nuevo y muy interesante, estás charlando animadamente y llega el momento de hablar de ti, ¿cuál de las siguientes opciones se ajusta mejor a lo que cuentas?"
     },
    {"id_pregunta":5,
     "id_encuesta":400,
     "numero_pregunta": 5,
     "titulo_pregunta": "En tu lugar de trabajo o de estudios, se está explicando algo que es completamente nuevo para ti. Llega un momento en que te das cuenta que no has entendido casi nada ¿qué haces?",
     },
    {"id_pregunta":6,
     "id_encuesta":400,
     "numero_pregunta": 6,
     "titulo_pregunta": "Tener un trabajo bien remunerado y que nos guste es algo difícil de conseguir, si tuvieras que valorar tu empleo o tu situación laboral, ¿cómo la definirías?",
     },
    {"id_pregunta":7,
     "id_encuesta":400,
     "numero_pregunta": 7,
     "titulo_pregunta": "Has tenido un día duro, has trabajado con más ahínco para finalizar una tarea en la oficina, has hecho todas las gestiones que tenías pendientes, has resuelto un par de problemas domésticos y encima le has hecho un favor a un amigo. ¿Qué haces al llegar a casa?",
     },
    {"id_pregunta":8,
     "id_encuesta":400,
     "numero_pregunta": 8,
     "titulo_pregunta": "En tu trabajo están buscando a una persona que represente a la empresa en un concurso del ramo. Piden una persona que cumpla unos requisitos, entre ellos, explicar bien nuestro trabajo y que haga una demostración práctica del mismo.",
     },
    {"id_pregunta":9,
     "id_encuesta":400,
     "numero_pregunta": 9,
     "titulo_pregunta": "¿Con cuál de las siguientes frases sobre la buena fortuna estás más de acuerdo?",
     },
    {"id_pregunta":10,
     "id_encuesta":400,
     "numero_pregunta": 10,
     "titulo_pregunta": "En una fiesta en La que no conoces a nadie excepto a Los anfitriones, te presentan a un grupo de personas de aspecto interesante. ¿Cuál es tu actitud?",
     },
]

# Preguntas
datos_respuestas =[
    {"id_respuesta":1,
     "id_pregunta":1,
     "titulo_respuesta": "No, consideras que tu opinión sea buena y que la de los demás no tenga por qué serlo siempre.",
     },
    {"id_respuesta":2,
     "id_pregunta":1,
     "titulo_respuesta": "Sí, pero sólo ante las decisiones que consideras demasiado importantes como para actuar precipitadamente.",
     },
    {"id_respuesta":3,
     "id_pregunta":1,
     "titulo_respuesta": "Sí, siempre que puedes consultas con los demás. Te equivocas con frecuencia y quieres hacer las cosas bien.",
     },
    {"id_respuesta":4,
     "id_pregunta":1,
     "titulo_respuesta": "Depende de la decisión. Sueles tener claro lo que vas a hacer, pero consideras las posibilidades que te ofrecen los demás."
     },
    {"id_respuesta":5,
     "id_pregunta":2,
     "titulo_respuesta": "No le das importancia, te comportas con naturalidad y si alguien te lo comenta haces alguna broma al respecto."
     },
    {"id_respuesta":6,
     "id_pregunta":2,
     "titulo_respuesta": "Te da mucha vergüenza. Procuras situarte en algún lugar discreto y pasar desapercibido."
     },
    {"id_respuesta":7,
     "id_pregunta":2,
     "titulo_respuesta": "Te sientes incómodo pero tratas de no pensar en ello, te integras en la reunión y das alguna excusa por tu error."
     },
    {"id_respuesta":8,
     "id_pregunta":2,
     "titulo_respuesta": "No te importa nada en absoluto, aunque no lleves la ropa adecuada tienes estilo y sabes llevar bien cualquier cosa."
     },
    {"id_respuesta":9,
     "id_pregunta":3,
     "titulo_respuesta": "Admiras el estilo de tu acompañante, al final compras un par de prendas necesarias pero muy simples en cuanto a forma y color."
     },
    {"id_respuesta":10,
     "id_pregunta":3,
     "titulo_respuesta": "No estás dispuesto a que te gane, decides comprar varias prendas muy modernas y bastante caras."
     },
    {"id_respuesta":11,
     "id_pregunta":3,
     "titulo_respuesta": "Admiras su estilo pero eres muy consciente del tuyo, compras la ropa que mejor te sienta y que necesitas, y pasas un rato ameno probándo cosas diferentes."
     },
    {"id_respuesta":12,
     "id_pregunta":3,
     "titulo_respuesta": "A su lado te sientes bastante poca cosa, te quita las ganas de probarte algo y mucho menos de comprar. Pones una excusa y te marchas."
     },
    {"id_respuesta":13,
     "id_pregunta":4,
     "titulo_respuesta": "No crees que tengas mucho que contar, tu trabajo es muy corriente, tus amigos son normales y tus aficiones también. Prefieres que esta persona te cuente su vida."
     },
    {"id_respuesta": 14,
     "id_pregunta": 4,
     "titulo_respuesta": "Tu trabajo te gusta y aunque sea corriente, siempre lo enfocas desde una perspectiva interesante, tus aficiones son tu pasión y disfrutas hablando de ellas, también hablas de tus proyectos futuros."
     },
    {"id_respuesta": 15,
     "id_pregunta": 4,
     "titulo_respuesta": "Hablas en general de tu trabajo y de tus aficiones, sobre todo hablas de tus amigos y de lo más interesante de sus vidas."
     },
    {"id_respuesta": 16,
     "id_pregunta": 4,
     "titulo_respuesta": "Más que de tu trabajo actual, hablas de tus proyectos y de tus objetivos, y de lo que vas a hacer para lograrlos, de lo buenas que son tus amistades y lo poco usual de tus aficiones. Te gusta hablar de ti."
     },
    {"id_respuesta": 17,
     "id_pregunta": 5,
     "titulo_respuesta": "Paras la explicación y requieres que se empiece de nuevo, si tu no lo entiendes habrá mucha gente que tampoco lo haga."
     },
    {"id_respuesta": 18,
     "id_pregunta": 5,
     "titulo_respuesta": "Si hay más gente que pregunte tu también lo haces, si no, buscas aparte al ponente para que te aclare las dudas."
     },
    {"id_respuesta": 19,
     "id_pregunta": 5,
     "titulo_respuesta": "Te da mucha vergüenza preguntar y demostrar así que no entiendes. Más tarde preguntarás a algún amigo o intentarás informarte por tu cuenta."
     },
    {"id_respuesta": 20,
     "id_pregunta": 5,
     "titulo_respuesta": "Tomas nota de lo que no entiendes para preguntarlo al finalizar la charla, si sigues con dudas pedirás información complementaria para prepararte mejor."
     },
    {"id_respuesta": 21,
     "id_pregunta": 6,
     "titulo_respuesta": "Satisfactoria, tratas de buscar el lado positivo de las cosas y nunca te faltan proyectos y objetivos que perseguir."
     },
    {"id_respuesta": 22,
     "id_pregunta": 6,
     "titulo_respuesta": "Horrible, no obstante, sabes que las cosas están mal y que tienes que aguantar lo que sea. Estás muy agradecido por tener trabajo."
     },
    {"id_respuesta": 23,
     "id_pregunta": 6,
     "titulo_respuesta": "No te preocupa especialmente el tema, tienes un montón de proyectos más importantes y con tu valía los alcanzarás."
     },
    {"id_respuesta": 24,
     "id_pregunta": 6,
     "titulo_respuesta": "Has logrado que no te afecte, consideras más importante tu vida personal y privada y eso es por lo que luchas."
     },
    {"id_respuesta": 25,
     "id_pregunta": 7,
     "titulo_respuesta": "Prefieres no pensarlo, el día ha sido duro pero para ti no es algo nuevo, solo pides poder dormir bien y que mañana sea un día más tranquilo."
     },
   {"id_respuesta": 26,
     "id_pregunta": 7,
     "titulo_respuesta": "Se lo cuentas a todo el mundo, te gusta que se te reconozca cuando haces las cosas bien y exiges en casa que te mimen por haberte esforzado tanto."
     },
   {"id_respuesta": 27,
     "id_pregunta": 7,
     "titulo_respuesta": "Estás muy satisfecho y decides darte un capricho, darte un baño de espuma y ver una buena película, o comprarte un regalito que hace tiempo querías."
     },
   {"id_respuesta": 28,
     "id_pregunta": 7,
     "titulo_respuesta": "Te preocupa que se te haya olvidado algo o haber hecho algo mal por la prisa, repasas mentalmente las actividades y al día siguiente esperas no tener queja de nadie."
     },
   {"id_respuesta": 29,
     "id_pregunta": 8,
     "titulo_respuesta": "No te planteas ser voluntario, hay mil personas más capacitadas que tú para la demostración y no se te da bien hablar en público"
     },
   {"id_respuesta":30,
     "id_pregunta": 8,
     "titulo_respuesta": "Te presentas voluntario, puede ser una experiencia interesante y si sales elegido puedes hacer una presentación innovadora."
     },
   {"id_respuesta":31,
     "id_pregunta": 8,
     "titulo_respuesta": "No te presentas, serías capaz de hacerla bien pero crees que hay gente mejor preparada y más original que tú."
     },
   {"id_respuesta":32,
     "id_pregunta": 8,
     "titulo_respuesta": "Te presentas y estás casi seguro de que te elegirán, haces buenos proyectos y darás una buena imagen de la empresa."
     },
   {"id_respuesta":33,
     "id_pregunta": 9,
     "titulo_respuesta": "La buena suerte puede tocarle a todo el mundo, yo me considero una persona afortunada a la que la vida le sonríe."
     },
   {"id_respuesta":34,
     "id_pregunta": 9,
     "titulo_respuesta": "Para tener buena suerte hay que trabajar duro, sólo los muy afortunados la tienen sin apenas esfuerzo."
     },
   {"id_respuesta": 35,
    "id_pregunta": 9,
    "titulo_respuesta": "Yo no tengo suerte, tanto los premios como las cosas especiales sólo les pasan a los demás."
    },
   {"id_respuesta": 36,
    "id_pregunta": 9,
    "titulo_respuesta": "La suerte respecto a los premios es una cuestión de probabilidad, y respecto a las cosas de la vida, siempre depende de cómo se perciban."
    },
   {"id_respuesta": 37,
    "id_pregunta": 10,
    "titulo_respuesta": "Te interesa conocerlos no sólo para pasar un buen rato en la reunión sino porque puede ser una forma de iniciar una amistad."
    },
   {"id_respuesta": 38,
    "id_pregunta": 10,
    "titulo_respuesta": "Esperas causarles una buena impresión y decir cosas que les puedan interesar."
    },
   {"id_respuesta": 39,
    "id_pregunta": 10,
    "titulo_respuesta": "Te gustaría llevarles a tu terreno en la conversación para así poder hablar de los temas que más te interesan."
    },
   {"id_respuesta": 40,
    "id_pregunta": 10,
    "titulo_respuesta": "Antes de iniciar una conversación escuchas lo que dicen, y es peras para hablar a que lo hagan de temas que tú conozcas."
    }

]

