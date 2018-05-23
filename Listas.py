#!/usr/bin/env python
#-*- coding: utf-8 -*-
aliprinc = ["Harina", "Arroz", "Cereal", "Frijol", "Lenteja",
             "Garvanzo", "Carne", "Pescado", "Mani", "Huevos",
             "Mariscos", "Langosta"]

alisecun = ["Fideos", "Aceite", "Leche", "Atun", "Sardina",
            "Frutas", "Verduras", "Azucar", "Sal", "Coladas",
            "Cremas", "Tortas", "Manjares"]

aliterc = ["Galletas", "Dulces", "Arequipe", "Mermelada",
           "Gomas", "Mecatos", "Detergentes", "Condimentos",
           "Queso", "Mantequilla", "Refrescos", "Geladas"]

farmacos = ["Rituximab", "Rdalimumab", "Trastuzumab",
            "Etanercept", "Antiinhibidor", "Infliximab",
            "Meropenem", "Bevacizumab", "Insulina"]

text_ropa = ["Telas", "Algodon", "Pantalones", "Camisas",
             "Zapatos", "Gorras","Chaquetas", "Pantalonetas",
             "Shorts", "Jeans", "Sombreros"]

building = ["Hierro", "Cemento", "Acelerantes",
            "Ceramica", "Pintura", "Estuco", "Fibrocemento",
            "Superboard", "Policarbonato", "Aluminio",
            "Acrilico", "Metalflex", "Malla Presoldada"]

combustible = ["Gas Natural", "ACPM", "Gasolina",
               "Aceites Lubricantes", "Parafinas", "Refrigerantes",
               "Betunes", "Energia Electrica"]

automotores = ['Autos Deportivos', "Camiones", "Buses",
               "Busetas", "Vans", "Volquetas", "Motocicletas",
               "Tractocamiones", "Yates", "Lanchas", 'Autos Todoterreno',
               'Camionetas', 'Retroescabadoras', 'Maquinaria pesada']

tecnologia = ["Computadores", "Celulares", "Tablets",
             "Equipos De Sonido", "Televisores", "Lavadoras",
             "Neveras", "Hornos", "Estufas", "Licuadoras",
             "Cafeteras", "Arroceras"]

herramientas = ["Pulidoras", "Taladros", "Lijadoras",
                "Llaves", "Bobinas", "Escobillas", "Brocas",
                "Sisayas", "Saltarines", "Revolvedoras", 
                "Motores", "Llantas" ]

accesorios = ["Colonias", "Lociones", "Jugutes",
              "Vajillas", "Ollas", "Cubiertos",
              "Mesas", "Comedores", "Armarios",
              "Sillas", "Escritorios"]
  
  
#Unidades de medidas/////////////////////////////////////////////////
            
kilogramo = ["Harina", "Arroz", "Cereal", "Frijol", "Lenteja",
             "Garvanzo", "Carne", "Pescado", "Mani",
             "Mariscos", "Langosta",
             "Cangrejo", "Fideos", "Aceite", "Leche", "Atun", "Sardina",
             "Frutas", "Verduras", "Azucar", "Sal", "Coladas",
             "Cremas", "Galletas", "Dulces", "Arequipe", "Mermelada",
             "Gomas", "Mecatos", "Detergentes", "Condimentos",
             "Queso", "Mantequilla", "Geladas"]
           
arroba = ["Harina", "Arroz", "Cereal", "Frijol", "Lenteja",
             "Garvanzo", "Pescado", "Mani",
             "Fideos", "Aceite",
             "Frutas", "Verduras", "Azucar", "Sal", "Coladas",
             "Cremas", "Galletas", "Dulces",
             "Mecatos", "Detergentes", "Condimentos",
             "Queso", "Geladas"]

quintal = ["Harina", "Arroz", "Cereal", "Frijol", "Lenteja",
             "Garvanzo",  "Mani",
             "Fideos", "Aceite", 
             "Frutas", "Verduras", "Azucar", "Sal",
             "Cremas", "Dulces",
             "Mecatos", "Detergentes",
             "Queso", 'Acelerantes', 'Fibrocemento', 'Superboard'
             'Policarbonato']
             
tonelada = ["Harina", "Arroz", "Cereal", "Frijol", "Lenteja",
            "Garvanzo",  "Mani", "Fideos", "Aceite", 
            "Frutas", "Verduras", "Azucar", "Sal", "Detergentes",
            "Hierro", "Cemento", "Acelerantes",
            "Ceramica", "Pintura", "Estuco", "Fibrocemento",
            "Superboard", "Policarbonato", "Aluminio",
            "Acrilico", "Metalflex", "Malla Presoldada",             
            "Telas", "Algodon", "Pantalones", "Camisas",
            "Zapatos", "Gorras","Chaquetas", "Pantalonetas",
            "Shorts", "Jeans", "Sombreros"
            "Colonias", "Lociones", "Jugutes",
            "Vajillas", "Ollas", "Cubiertos"]
            
litros = ['Leche', 'Refrescos', 'Detergentes', 'Acelerantes',
          'Pintura', 'ACPM', 'Gasolina', 'Aceites Lubricantes',
          'Parafinas', 'Refrigerantes']

barril = ['Acelerantes', 'Pintura', 'ACPM', 'Gasolina',
          'Aceites Lubricantes', 'Parafinas', 'Refrigerantes']

galones = ['Acelerantes', 'Pintura', 'ACPM', 'Gasolina',
          'Aceites Lubricantes', 'Parafinas', 'Refrigerantes', 'Leche'
          'Refrescos', 'Arequipe', 'Manjares', 'Aceite']
          
unidades = ["Pulidoras", "Taladros", "Lijadoras",
            "Llaves", "Bobinas", "Escobillas", "Brocas",
            "Sisayas", "Saltarines", "Revolvedoras", 
            "Motores", "Llantas", "Colonias", "Lociones", "Jugutes",
            "Vajillas", "Ollas", "Cubiertos",
            "Mesas", "Comedores", "Armarios",
            'Autos Deportivos', "Camiones", "Buses",
            "Busetas", "Vans", "Volquetas", "Motocicletas",
            "Tractocamiones", "Yates", "Lanchas", 'Autos Todoterreno',
            'Camionetas', 'Retroescabadoras', 'Maquinaria pesada'
            "Sillas", "Escritorios", "Computadores", "Celulares", "Tablets",
            "Equipos De Sonido", "Televisores", "Lavadoras",
            "Neveras", "Hornos", "Estufas", "Licuadoras",
            "Cafeteras", "Arroceras", "Pantalones", "Camisas",
            "Zapatos", "Gorras","Chaquetas", "Pantalonetas",
            "Shorts", "Jeans", "Sombreros"]
            
cajas = ['Galletas', 'Geladas', 'Atun', 'Sardina',
         'Huevos', 'Dulces', 'Aceite', 'Mecatos'
         'Detergentes', 'Ceramica', 'Betunes', 'Colonias'
         'Vagillas', 'Cubiertos', 'Lociones', 'Juguetes']
                   
ecuador = [aliprinc[1], aliprinc[2], aliprinc[3],
           aliprinc[4], alisecun[0], aliterc[10], building[10],
           alisecun[1], aliterc[0], aliterc[1], text_ropa[10],
           building[0], building[1], building[3], aliterc[11],
           combustible[1], combustible[2], aliprinc[11], alisecun[8]]
           
peru = [aliprinc[0], aliprinc[1], aliprinc[2],
        aliprinc[3], aliprinc[4], aliprinc[5],
        aliprinc[6], aliprinc[7], aliprinc[8],
        aliprinc[9], aliprinc[10], alisecun[0], alisecun[1],
        alisecun[2], alisecun[3], alisecun[4],
        alisecun[5], alisecun[6], alisecun[7],
        alisecun[8], aliterc[0], aliterc[1], alisecun[9],
        aliterc[2], aliterc[3], aliterc[4], aliterc[5],
        aliterc[6], aliterc[7], aliterc[8], alisecun[10],]
        
chile = [aliprinc[0], aliprinc[1], aliprinc[2], building[12],
         aliprinc[3], aliprinc[4], aliprinc[5],
         aliprinc[6], aliprinc[7], aliprinc[8], building[11],
         building[0], building[1], building[2],
         building[3], building[4], building[5], alisecun[10],
         building[6], building[7], building[8], building[9],
         alisecun[0], alisecun[1], alisecun[2],
         alisecun[3], alisecun[4], alisecun[5],aliterc[0],
         aliterc[1], aliterc[2], aliterc[3], building[10],
         aliterc[4], aliterc[5],accesorios[0],
         accesorios[1], accesorios[2], accesorios[3],
         accesorios[4], accesorios[5], accesorios[6],aliprinc[11]]
        
brazil = [aliterc[0], aliterc[1], aliterc[2], aliterc[3],
          aliterc[4], aliterc[5], aliterc[6], text_ropa[7],
          aliterc[7], aliterc[8], accesorios[0], building[11],
          accesorios[1], accesorios[2], accesorios[3],
          accesorios[4], accesorios[5], accesorios[6],
          combustible[1], combustible[3], combustible[4],
          combustible[5], combustible[6], combustible[7],
          aliprinc[0], aliprinc[1], aliprinc[2],
          aliprinc[3], aliprinc[4], aliprinc[5],
          alisecun[0], alisecun[1], alisecun[2], 
          alisecun[3], alisecun[4], alisecun[5], aliterc[10]]
            
argentina = [aliprinc[0], aliprinc[1], aliprinc[2], aliterc[10],
             aliprinc[3], aliprinc[4], aliprinc[5],
             aliprinc[6], aliprinc[7], aliprinc[8],
             aliprinc[9], aliprinc[10], alisecun[2],
             alisecun[3], alisecun[4], alisecun[5],
             alisecun[6], alisecun[7],  aliterc[0], aliterc[1],
             aliterc[2], aliterc[3], aliterc[4],
             aliterc[5], aliterc[6], aliterc[7], aliterc[8]]

mexico = [combustible[0], combustible[1], herramientas[0],
          herramientas[1], herramientas[2], text_ropa[7],
          herramientas[3], accesorios[0], accesorios[1],
          accesorios[2], accesorios[3], accesorios[4],
          accesorios[5], accesorios[6], aliterc[11],
          farmacos[0], farmacos[1], farmacos[2],
          farmacos[3], farmacos[4], alisecun[11], text_ropa[6]]
         
venezuela = [aliprinc[0], aliprinc[1], aliprinc[2],
             aliprinc[3], aliprinc[4], aliprinc[5],
             aliprinc[6], aliprinc[7], aliprinc[8],
             aliprinc[9], aliprinc[10], combustible[0],
             combustible[1], combustible[2], combustible[3],
             combustible[4], combustible[5], text_ropa[9],
             alisecun[2], alisecun[3], alisecun[4],
             alisecun[5], alisecun[6], alisecun[7], aliterc[0],
             aliterc[1], aliterc[2], aliterc[3],
             aliterc[4], aliterc[5], aliterc[6],
             aliterc[7], aliterc[8], alisecun[12],]

EEUU = [farmacos[1], farmacos[2], farmacos[3], aliterc[10], text_ropa[7],
        farmacos[4], farmacos[5], farmacos[6], text_ropa[6], automotores[12],
        alisecun[1], alisecun[3], alisecun[4], aliterc[11], text_ropa[9], tecnologia[11],
        herramientas[0],  herramientas[1],  herramientas[2], automotores[10],
        herramientas[3],  herramientas[4], tecnologia[0], tecnologia[1], tecnologia[10],
        tecnologia[2], tecnologia[3], tecnologia[4], tecnologia[5], tecnologia[9],
        tecnologia[5], tecnologia[6], tecnologia[7], tecnologia[8], alisecun[10],]
        
china = [text_ropa[0], text_ropa[1], text_ropa[2], tecnologia[10],
         text_ropa[3], text_ropa[4], text_ropa[5], text_ropa[6], accesorios[2],
         automotores[0], automotores[1], automotores[2], building[10],
         automotores[3], automotores[4], automotores[5],
         automotores[6], automotores[7], automotores[8], text_ropa[10],
         automotores[9], herramientas[0],herramientas[1], automotores[10],
         herramientas[2], herramientas[3], herramientas[4], automotores[11],
         herramientas[5], herramientas[6], herramientas[7], tecnologia[9],
         herramientas[8], herramientas[9], herramientas[10],
         herramientas[11], text_ropa[8], text_ropa[9]]
        
canada = [automotores[0], automotores[1], automotores[2],
          automotores[3], automotores[4], automotores[5],
          tecnologia[3],tecnologia[4], text_ropa[9], tecnologia[9],
          tecnologia[8], herramientas[0], herramientas[1],
          herramientas[2], herramientas[3], automotores[10],
          herramientas[4], herramientas[5], herramientas[6],
          herramientas[7], herramientas[8]]
        
panama = [aliprinc[0], aliprinc[1], aliprinc[2],
          aliprinc[3], aliprinc[4], aliprinc[5],
          alisecun[0],  alisecun[1],  alisecun[2],  alisecun[3],
          alisecun[4], text_ropa[0], text_ropa[1],
          text_ropa[2], text_ropa[3], text_ropa[4],
          accesorios[0], accesorios[1]] 
                
holanda = [herramientas[6], herramientas[7],
           herramientas[8], herramientas[9], herramientas[10],
           herramientas[11], text_ropa[10],
           herramientas[5], accesorios[4],
           accesorios[5], accesorios[6], accesorios[7],
           accesorios[8], accesorios[9], accesorios[10],
           farmacos[0], farmacos[1], farmacos[2], farmacos[3],
           farmacos[4], farmacos[5], farmacos[6], alisecun[11]]
        
suiza = [herramientas[0], herramientas[1], herramientas[2], automotores[13],
         herramientas[3], herramientas[4], herramientas[5],
         herramientas[6], herramientas[7], herramientas[8], automotores[11],
         herramientas[9], herramientas[10], herramientas[11]]
        
espana = [aliterc[0], aliterc[1], aliterc[2],
          aliterc[3], aliterc[4], aliterc[5],
          aliterc[6], aliterc[7], aliterc[8], aliterc[9],
          herramientas[0], herramientas[1], herramientas[2],
          herramientas[3], herramientas[4], farmacos[0],
          farmacos[1], farmacos[2], farmacos[3],
          farmacos[4], farmacos[5], farmacos[6], building[10],
          farmacos[7], tecnologia[0], tecnologia[1],
          tecnologia[2], tecnologia[3], tecnologia[4]]
        
japon = [tecnologia[0], tecnologia[1], tecnologia[2],
         tecnologia[3], tecnologia[4], tecnologia[5], tecnologia[9],
         tecnologia[6], tecnologia[7], text_ropa[6], tecnologia[10],
         herramientas[0], herramientas[1], text_ropa[7],
         herramientas[2], herramientas[3], automotores[11],
         herramientas[4], herramientas[5], herramientas[6],
         farmacos[5], farmacos[6], farmacos[7], farmacos[8],
         automotores[0], automotores[1], automotores[2],
         automotores[3], automotores[4], automotores[5],
         automotores[6], automotores[7], automotores[8], automotores[9]]

uruguay = [aliprinc[0], aliprinc[1], aliprinc[2],
           aliprinc[3], aliprinc[4], aliprinc[5],
           aliprinc[6], aliprinc[7], alisecun[0], alisecun[1],
           alisecun[2], alisecun[3], alisecun[4],
           alisecun[5], alisecun[6], alisecun[7],
           alisecun[8], aliterc[0], aliterc[1], aliterc[2],
           aliterc[3], aliterc[4], aliterc[5], aliterc[6],
           accesorios[0], accesorios[1], accesorios[2],
           accesorios[3], accesorios[4],
           accesorios[5], accesorios[6]]

italia = [herramientas[6], herramientas[7], herramientas[8],
          herramientas[9], herramientas[10], herramientas[11],
          automotores[1], aliterc[11],
          automotores[2], automotores[3],  automotores[4],
          automotores[5],  automotores[6], farmacos[0],
          farmacos[1], farmacos[2], tecnologia[9],
          farmacos[3], farmacos[4], farmacos[5], farmacos[6],
          farmacos[7], farmacos[8], accesorios[0], accesorios[1],
          accesorios[2], accesorios[3], accesorios[4],
          accesorios[5], accesorios[6], alisecun[11]]
          
paraguay = [aliprinc[0], aliprinc[1], aliprinc[2],
            aliprinc[3], aliprinc[4], aliprinc[5],
            aliprinc[6], aliprinc[7], aliprinc[8], aliprinc[9], 
            aliprinc[10], aliprinc[11], alisecun[0],
            alisecun[1], alisecun[2], alisecun[3],
            alisecun[4], alisecun[5], alisecun[6],
            alisecun[7], alisecun[8], aliterc[0],
            aliterc[1], aliterc[2], aliterc[3],
            aliterc[4], aliterc[5], aliterc[6], aliterc[7],
            aliterc[8], aliterc[9]]
              
honduras = [aliterc[0], aliterc[1], aliterc[2], aliterc[3],
           aliterc[4], aliterc[5], aliterc[6], aliterc[7],
           aliterc[8], aliterc[9], alisecun[12],
           alisecun[0], alisecun[1], alisecun[2], alisecun[3],
           alisecun[4], alisecun[5], accesorios[6],
           accesorios[7], accesorios[8], accesorios[9], accesorios[10]]



listaImportaciones = [aliprinc, alisecun, aliterc, farmacos,
                      text_ropa, building, combustible, automotores, tecnologia,
                      herramientas, accesorios]
                      
for n in listaImportaciones:
	n.insert(0, '-Select-')

paisesExportadores = ['Ecuador', 'Peru', 'Chile',
                      'Brazil', 'Argentina', 'Mexico',
                      'Venezuela', 'EEUU',
                      'Panama', 'Holanda', 'Suiza', 'Espania',
                      'Japon', 'Uruguay', 'Italia',
                      'Paraguay', 'Honduras', 'China', 'Canada']

productsCountry = [ecuador, peru, chile,
                   brazil, argentina, mexico,
                   venezuela, EEUU, panama, holanda, suiza, espana,
                   japon, uruguay, italia,
                   paraguay, honduras, china, canada,]
                   
arancelCountries = [12, 8, 15, 10, 11, 25, 5, 4, 8, 10, 7,
                    18, 14, 16, 19, 9, 12, 20, 21]
                    
unidades = ['Kilogramo', 'Litros', 'Galon', 'Arroba', 'Quintal',
            'Caja', 'Barril','Tonelada']
       
listUnidades = [kilogramo, litros, galones, arroba, quintal,
                cajas, barril, tonelada]
                   
def listcountryProduct(x, lista):
	i = 0
	lista.append('-Select-')
	for n in productsCountry:
		if x in productsCountry[i]:
			lista.append(paisesExportadores[i])
		i = i + 1
	return lista

def listunitProduct(x, lista):
	i = 0
	lista.append('-Select-')
	for n in listUnidades:
		if x in listUnidades[i]:
			lista.append(unidades[i])
		i = i + 1
	return lista
