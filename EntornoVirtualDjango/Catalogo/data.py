categorias = [
    (100, 'Brandy', 'brandy', 'Es un licor hecho originalmente de hollejos de uvas. Hay variedades que incluyen la uva entera u otras frutas, y estas adquieren su nombre a partir de su origen o procesamiento, es considerado un licor fino para ser bebido como bajativo.',  0.0, True, 'Categoria-1.jpg'),
    (200, 'Ginebra', 'ginebra', 'La ginebra también conocido como gin en inglés es un aguardiente que se obtiene mediante la destilación de la cebada sin maltear una vez fermentada, sus niveles de alcohol se encuentran entre 37° y 47°.', 0.0, True, 'Categoria-2.jpg'),
    (300, 'Ron', 'ron', 'El ron es un licor que se obtiene mediante la fermentación, destilación y el añejamiento de la caña de azúcar (o melazas derivadas de esta) en barricas de madera durante periodos de tiempos que varían según el fabricante, generalmente de roble. Este aguardiente llega a tener 80° de alcohol', 0.0, True, 'Categoria-3.jpg'),
    (400, 'Tequila', 'tequila', 'Es un aguardiente elaborado en México, mediante la destilación del mosto fermentado que se obtiene del corazón del mezcal. De todos los mezcales que se producen en en el país, sin duda es el mas famoso es el de la región de Tequila, localizada a unas 15 leguas al noroeste de Guadalajara, Jalisco.', 0.0, True, 'Categoria-4.jpg'),
    (500, 'Vodka', 'vodka', 'Es la bebida espirituosa más consumida en el mundo, su sabor suave y delicado permite tomarla sola, o combinarla con otros ingredientes para elaborar tragos. La vodka se compone principalmente de agua y alcohol (etanol), y puede contener agregados aromatizantes. ', 0.0, True, 'Categoria-5.jpg'),
    (600, 'Whiskey', 'whiskey', 'El whisky es una bebida que dispone de una elevada graduación alcohólica y puede producirse con la utilización de diferentes granos. A partir de la fermentación de cereales como el centeno, la cebada, el maíz o el trigo.', 0.0, True, 'Categoria-6.jpg'),
]


productos = [
    #(50, 100, 'Bacardi 151', 'bacardi-151', 'Bacardi 151 con nombre largo', 'Descripción del Bacardi 151 con tanto grados de alcohol', 1, 'Botella', '120.50', 20, 0, 1000 , 'brandy-50.webp'),
    #(100, 100, 'Brandi Torres 20', 'brandi-torres-20', 'Brandy Torres 20 150 Aniversario 700 ml', 'Edición especial creada para conmemorar el 150 aniversario del nacimiento de Joan Torres Casals, tiene notas de frutas maduras como ciruelas y pasas.', 1, 'Botella', '940.50', 20, 0, 1000, 'brandy-100.webp'),
    (150, 100, 'Brandi Torres 10 DB', 'brandi-torres-10-db', 'Brandy Torres 10 Double Barrel 700 ml', 'Es un brandy doblemente añejado en barricas de roble americano, tiene un aroma amplio a notas de vainilla y tabaco. En boca es rico y equilibrado con un tostado redondo.', 1, 'Botella', '440.50', 20, 0, 1000, 'brandy-150.webp'),
    (200, 100, 'Brandy Alma De Magno', 'brandy-alma-de-magno', 'Brandy Alma De Magno C/Vaso 700 ml', 'Edición especial con un vaso de regalo. Es un brandy obtenido a partir de holandas y aguardiente de vino de baja graduación, tiene aromas a finas notas de frutos secos con toques de roble.', 1, 'Botella', '500.50', 15, 0, 1000, 'brandy-200.webp'),
    (250, 100, 'Brandy Presidente', 'brandy-presidente', 'Brandy Presidente Edicion 50A 1.75L', 'Envejecido en barricas de roble blanco, tiene un sabor a frutos secos y vainilla.', 1, 'Botella', '220.50', 15, 0, 1000, 'brandy-250.webp'),
    (300, 100, 'Brandy Gran Duque', 'brandy-gran-duque','Brandy Gran Duque D Alba 700ml', 'Envejecido en botas de roble americano envinadas con oloroso, tiene un aroma complejo con notas balsámicas derivadas de la larga crianza en madera.', 1, 'Botella', '1000.00', 10, 0, 1000, 'brandy-300.webp'),

    (350, 200, 'Ginebra Tanqueray Ten', 'ginebra-tanqueray-ten', 'Ginebra Tanqueray Ten Estuche Con Llave 700ml', 'Edición especial en estuche con llave. Es una ginebra con aroma a flores de manzanilla, frutos secos y limón verde, en boca se perciben notas toronja y miel.', 1, 'Botella', '800.90', 10, 0, 1000, 'Ginebra-350.webp'),
    (400, 200, 'Ginebra Beefeater', 'ginebra-beefeater', 'Ginebra Beefeater 24 C/Copa 750ml', 'Edición especial con una copa de regalo. Es un ginebra con distintos tipos de botánicos como té sencha japonés y el té verde chino, posee aromas a notas cítricas y un sabor herbal y cremoso.', 1, 'Botella', '700.90', 10, 0, 1000, 'Ginebra-400.webp'),
    (450, 200, 'Ginebra Greenalls', 'ginebra-greenalls', 'Ginebra Greenalls The Original+Wild Berry C/4 Vasos 750ml', '', 1, 'Paquete', '750.90', 10, 0, 1000, 'Ginebra-450.webp'),
    (500, 200, 'Ginebra Boodles', 'ginebra-boodles', 'Ginebra Boodles Mulberry 750 ml', 'Es la primera ginebra con sabor a moras que combina delicadas moras con notas de frambuesa y grosella para crear un dulce y sutil sabor.', 1, 'Paquete', '509.90', 10, 0, 1000, 'Ginebra-500.webp'),
    (550, 200, 'Ginebra Mom', 'ginebra-mom', 'Ginebra Mom 700 ml', 'Considerada la Reyna de las Ginebras, tiene un intenso aroma a frutos rojos, en boca se percibe un carácter aterciopelado y agradable a frutos rojos.', 1, 'Paquete', '509.90', 10, 0, 1000, 'Ginebra-550.webp'),
    (600, 200, 'Ginebra Tanqueray', 'ginebra-tanqueray', 'Ginebra Tanqueray 750 ML ', 'Destilado en 4 ocasiones de manera artesanal, posee un sabor botánico seco a manzanilla, limón verde y toronja, así como aromas florales.', 1, 'Botella', '400.90', 30, 0, 1000, 'Ginebra-600.webp'),

    (650,300,'Ron Bacardi Blanco Halloween', 'ron-bacardi-blanco-halloween', 'Ron Bacardi Blanco Edic Halloween 750ml','Perfecto para las celebraciones de Hallowen, es un ron en la botella clásica de la marca con una etiqueta disfrazada de Jack-o-lantern que brilla en la oscuridad.',1,'Botella','200.5',15,5,1000, 'Ron-650.webp'),
    (700,300,'Ron Havana', 'ron-havana', 'RON HAVANA SELECCION 700 ML','Elaborado por los mejores maestros roneros de Cuba, posee un aroma a nuez pascana tostada y aroma de especias y tabaco. Tiene una entrada redonda.',1,'Botella','900.5',15,10,1000, 'Ron-700.webp'),
    (750,300,'Ron Bacardi Blanco', 'ron-bacardi-blanco', 'Ron Bacardi Blanco 980ml Raspberry Limon C Hielera y Vasos','Ron Bacardi Blanco 980ml Raspberry Limon C Hielera y Vasos',1,'Botella','600.5',15,10,1000, 'Ron-750.webp'),
    (800,300,'Ron Bacardi Gran Reserva', 'ron-bacardi-gran-reserva', 'Ron Bacardi Gran Reserva Limitada 750ml','Es una mezcla de rones maduros añejados en barriles bajo el sol del Caribe durante 12 años. Es un ron generoso y complejo que muestra suaves notas de caramelo y frutas secas.',1,'Botella','2500.5',15,10,1000, 'Ron-800.webp'),
    (850,300,'Ron Antillano Blanco', 'ron-antillano-blanco', 'Ron Antillano Blanco C/Vaso/Macerador 1L','',1,'Botella','150.5',15,10,1000, 'Ron-850.webp'),
    (900,300,'Ron Flor De Caña', 'ron-flor-de-cana', 'Ron Flor De Caña Gran Rva 7A Party Kit 750ml','',1,'Botella','400.5',15,10,1000, 'Ron-900.webp'),
    (950,300,'Ron Flor De Caña Centenario', 'ron-flor-de-cana-centenario', 'Ron Flor De Caña Centenario 12A 750 ml C/4 Vasos','País de Origen: Nicaragua',1,'Botella','700.5',15,10,1000, 'Ron-950.webp'),

    (1000,400,'Don Julio 70 Añejo 700ml', 'don-julio-70-anejo-700ml', 'Tequila Don Julio 70 Añejo 700ml','Caracterizado por poseer un color cristalino, tiene aromas a notas iniciales de cítricos y frutas como la guayaba y la tradicional esencia del agave.',1,'Botella','800.5',15,10,1000, 'Tequila-1000.webp'),
    (1050,400,'Herradura Rep 950ml', 'herradura-rep-950ml', 'Tequila Herradura Rep 950ml','Considerado el primer tequila reposado en el mundo, tiene un sabor a madera, vainilla, caramelo, ligero agave cocido, frutas, nuez y especias.',1,'Botella','500.5',15,10,1000, 'Tequila-1050.webp'),
    (1100,400,'Cazadores Añejo Cristalino', 'cazadores-anejo-cristalino','Tequila Cazadores Añejo Cristalino 750 ml','Es un tequila sumamente transparente, tiene notas a madera tostada, nuez, almendra y manzana.',1,'Botella','400.5',15,10,1000, 'Tequila-1100.webp'),
    (1150,400,'Herradura Ultra Añejo', 'herradura-ultra-anejo', 'Tequila Herradura Ultra Añejo 750 ml','Ideal para degustarse solo, posee un sabor suave y un aroma a madera, vainilla, caramelo y cítricos, que se entrelazan el ahumado del agave cocido.',1,'Botella','600.5',15,10,1000, 'Tequila-1150.webp'),
    (1200,400,'Gran Centenario', 'gran-centenario', 'Tequila Gran Centenario Añejo 695ml','Considerado el mejor tequila añejo, es elaborado 100% de agave, se madura en barricas de roble blanco y se caracteriza por ser muy suave al paladar y en aromas.',1,'Botella','500.5',15,0,1000, 'Tequila-1200.webp'),
    (1250,400,'Jimador Reposado', 'jimador-reposado', 'Tequila El Jimador Reposado Cristalino 700 ml','Considerado el tequila más suave de la familia, tiene un color limpio y brillante, con notas a cítricos, frutas, flores, hierbas, vainilla y caramelo.',1,'Botella','300.5',15,0,1000, 'Tequila-1250.webp'),

    (1300,500,'Absolut Extrakt', 'absolut-extrakt', 'Vodka Absolut Extrakt C/2 Vasos Shot 700ml','',1,'Botella','300.5',15,0,1000,'Vodka-1300.webp' ),
    (1350,500,'Absolut Azul', 'absolut-azul', 'Vodka Absolut Azul 750 ml con Absolut Lime de 50 ml y copa','Elaborado con elementos naturales, tiene un aroma a notas de cereal puro y fresco. Esta presentación incluye un Absolut Lime de 50 ml y una copa de regalo.',1,'Botella','280.5',15,0,1000,'Vodka-1350.webp'),
    (1400,500,'Zaverich Vanilla', 'zaverich-vanilla', 'Vodka Zaverich Vanilla 1L+Zaverich Premium 1L','Es un vodka ruso destilado a través de la fermentación de granos y otras plantas ricas en almidón, tiene aromas y sabores intensos a vainilla. Incluye una botella de Zaverich Premium de 1 L.',1,'Botella','200.5',15,0,1000,'Vodka-1400.webp'),
    (1450,500,'Outer Space', 'outer-space', 'Vodka Outer Space 750 ml','Es un vodka hecho con maíz 100% americano, sin gluten, el diseño de su botella es único y llamativo. Tiene aromas y sabores a frutos secos.',1,'Botella','700.5',15,0,1000,'Vodka-1450.webp'),
    (1500,500,'Grey Goose', 'grey-goose', 'Vodka Grey Goose Est Alpine 750ml','Edición especial. Es un vodka elaborado con agua pura de manantial y exclusivos ingredientes franceses, es considerado el mejor vodka del mundo.',1,'Botella','700.5',15,0,1000,'Vodka-1500.webp'),
    (1550,500,'Karat', 'karat','Vodka Karat 1 L','Elaborado con grano importado de Estados Unidos, es un vodka de cuerpo ligero y un sabor ideal para preparar todo tipo de cocteles.',1,'Botella','150.5',15,0,1000,'Vodka-1550.webp'),

    (1600,600,'Johnnie Walker Song Of Fire', 'johnnie-walker-song-of-fire', 'Whisky Johnnie Walker Game Thrones A Song Of Fire 700ml','Elaborado con grano importado de Estados Unidos, es un vodka de cuerpo ligero y un sabor ideal para preparar todo tipo de cocteles.',1,'Botella','500.5',15,0,1000, 'Whisky-1600.webp'),
    (1650,600,'Johnnie Walker Red Label', 'johnnie-walker-red-label', 'Whisky Johnnie Walker Red Label 700 ml','Es un whisky ligero con sabor a especias aromáticas con ligeras notas a frutas dulces, y un aroma ahumado.',1,'Botella','300.5',15,0,1000, 'Whisky-1650.webp'),
    (1700,600,'Buchanans Select 15 Años', 'buchanans-select-15-anos','Whisky Buchanans Select 15 Años 750 ml','Es una mezcla de los más finos single malts. Ha sido madurado durante 15 años, ofreciendo un perfil de sabor más audaz y complejo con notas de roble tostado.',1,'Botella','1500.5',15,0,1000, 'Whisky-1700.webp'),
    (1750,600,'Johnnie Walker 18 Años', 'johnnie-walker-18-anos', 'Whisky Johnnie Walker 18 Años 750 ml','Es una mezcla de los mejores whiskies de Escocia de 18 años, tiene un carácter dulce, rico, afrutado y equilibrado con sutil ahumado.',1,'Botella','2000.5',15,0,1000, 'Whisky-1750.webp'),
    (1800,600,'Buchanans 12 Años', 'buchanans-12-anos', 'Whisky Buchanans 12 Años 1L','Ideal para maridar con platillos frescos, tiene aromas a notas de naranja y chocolate; así como un sabor suave a cítricos, chocolate y miel.',1,'Botella','1020.5',15,0,1000, 'Whisky-1800.webp'),
    (1850,600,'William Lawsons Std', 'william-lawsons-std', 'Whisky William Lawsons Std 750 ml','Es un whisky afrutado de cuerpo ligero, se caracteriza por su aroma a pastel de manzana y su sabor a cereal tostado y al tofee, con un final suave.',1,'Botella','170.5',15,0,1000, 'Whisky-1850.webp'),
]



    # for producto in productos:
    #    print("Grabando")
    #    Producto.objects.create(
    #        id_prod = producto[0],
    #        id_cat = get_object_or_404(Categoria,clave=1),
    #        nombre =  producto[2],
    #        slug = producto[3],
    #        descrip =producto[5],
    #        tipo = producto[6],
    #        presentacion = producto[7],
    #        costo = producto[8],
    #        ganancia = producto[9],
    #        descuento = producto[10],
    #        existencia = producto[11],
    #        imagen =  producto[12],
    #    )
    # print("Carga ha terminado")