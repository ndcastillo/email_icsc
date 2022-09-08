import pandas as pd
# emails = '''
# <alejandro.garces@utp.edu.co>,
#  <araoki@gmail.com>, 
#  <alexeis.fernandez@intec.edu.do>, 
#  <andres.alvarado@ucuenca.edu.ec>, 
#  <anibal.zanini@gmail.com>, 
#  <antoni.sudria@gmail.com>, 
#  <avitali@campus.ungs.edu.ar>, 
# <lmbate49@nauta.cu>, 
#  <bernardo.silva@inesctec.pt>, 
#  <bwfranca@id.uff.br>, 
#  <camila@cear.ufpb.br>, 
#  <glopez@edeste.com.ar>, 
#  <carlos.moreira@inesctec.pt>, 
#  <cicelimar@gmail.com>, 
#  <coordenacao.ppgies@unila.edu.br>, 
#  <cristiandeangelo@gmail.com>, 
#  <danny.lopez@correounivalle.edu.co>, 
#  <denizar.martins@gmail.com>, 
#  <deyslen.mariano@intec.edu.do>, 
#  <diegosanchez@ipse.gov.co>, 
#  <delisei@crexel.com.ar>, 
#  <feroldi@cifasis-conicet.gov.ar>, 
#  <dgiacosa@ute.com.uy>, 
#  <espinoza_trejo_dr@uaslp.mx>, 
#  <watanabe@coe.ufrj.br>, 
#  <eduardo.caicedo@correounivalle.edu.co>, 
#  <eduardo.gomez@correounivalle.edu.co>, 
#  <eduardo.prieto-araujo@citcea.upc.edu>, 
#  <emsangoi@gmail.com>, 
#  <ecquispe@uao.edu.co>, 
#  <esteban@500rpm.org>, 
#  <eg.mendoza.guerra@gmail.com>, 
#  <fabiana.colombelli@unila.edu.br>, 
#  <aguilerafacundo@gmail.com>, 
#  <serrafederico@gmail.com>, 
#  <fguglialmell@edetsa.com>, 
#  <botteron@gmail.com>, 
#  <santos@uclv.edu.cu>, 
#  <oggier.german@gmail.com>, 
#  <gonzalogomez.utn@outlook.com>, 
#  <GDLopez@ute.com.uy>, 
#  <gonzalo.martin@ciemat.es>, 
#  <gonzalo@syrenergia.com.ar>, 
#  <rolim@ufrj.br>, 
#  <grcatu@gmail.com>, 
#  <guillermo.guevara.80@gmail.com>, 
#  <ga.jimeneze@uniandes.edu.co>, 
#  <glpleitavino@gmail.com>, 
#  <gustavo.rivas@unila.edu.br>, 
#  <gplacer@campus.ungs.edu.ar>, 
#  <gustavoairasca@gmail.com>, 
#  <gusmart2004@gmail.com>, 
#  <gramos@uniandes.edu.co>, 
#  <helisei@crexel.com.ar>, 
#  <ivan.andrade@umag.cl>, 
#  <jiam.frigo@unila.edu.br>, 
#  <jbenavides@uao.edu.co>, 
#  <jcabello@fceia.unr.edu.ar>, 
#  <javier.perezr@itson.du.mx>, John Davies <john3jjj@gmail.com>, 
#  <jposada@uao.edu.co>, 
#  <jnino@inti.gob.ar>, 
#  <jrgcaicedo@gmail.com>, 
#  <jorge.ledesma@unila.edu.br>, 
#  <jorgemirez2002@gmail.com>, 
#  <jrvega@frsf.utn.edu.ar>, 
#  <restrepo@usb.ve>, 
#  <angel.pecina@uaslp.mx>, 
#  <japomilio@gmail.com>, 
#  <jose.salgado@unila.edu.br>, 
#  <jose.silva@lactec.org.br>, 
#  <jaberistain@itson.edu.mx>, 
#  <fjimenez@uniandes.edu.co>, 
#  <dematosjosegomes@gmail.com>, 
#  <jaller@usb.ve>, 
#  <jose.manueldape@gmail.com>, 
#  <jose.ramirez@correounivalle.edu.co>, 
#  <jjvilela@gmail.com>, 
#  <joao.inacio.ota@gmail.com>, 
#  <juandavid.molina@colombiainteligente.org>, 
#  <juan.espinoza@ucuenca.edu.ec>, 
#  <juan.antonio.tapia@gmail.com>, 
#  <juliana@ghmsolutions.com.br>, 
#  <jviola@ups.edu.ec>, 
#  <kati@rtds.com>, 
#  <katya.freitas@unila.edu.br>, 
#  <lesyani@uclv.edu.cu>, 
#  <lucio.medeiros@lactec.org.br>, 
#  <LCataldo@ute.com.uy>, 
#  <luis.gonzalez@ucuenca.edu.ec>, 
#  <luis.hernandez.callejo@uva.es>, 
#  <luissilva@unraf.edu.ar>, 
#  <l.a.desouzaribeiro@ieee.org>, 
#  <lui@unicamp.br>, 
#  <manuel@500rpm.org>, 
#  <marcelatrindade@gmail.com>, 
#  <Marcela.Trindade@opal-rt.com>, 
#  <mar.heldwein@gmail.com>, 
#  <marcia.becker@unila.edu.br>, 
#  <marcio.goes@unila.edu.br>, 
#  <mpoliti@inti.gob.ar>, 
#  <pnelliar@yahoo.com>, 
#  <marketing@ghmsolutions.com.br>, 
#  <carvajal.maria@correounivalle.edu.co>, 
#  <Matias.DiazD@usach.cl>, 
#  <mauricio.aredes@gmail.com>, 
#  <mauricio@syrenergia.com.ar>, 
#  <maguir@itba.edu.ar>, 
#  <Miguel.Aybar@intec.edu.do>, 
#  <miguelfuertes@pti-sa.com.co>, 
#  <labordemiguel67@gmail.com>, 
#  <nnemirov@itba.edu.ar>, 
#  <nbarbieri@frsn.utn.edu.ar>, 
#  <gomis@citcea.upc.edu>, 
#  <oscar.izquierdo@ciemat.es>, 
#  <o.saavedra@ieee.org>, 
#  <oswaldo.junior@unila.edu.br>, 
#  <otto.sollberger@estudios-electricos.com>, 
#  <pablobertinat@gmail.com>, 
#  <PMaggi@ute.com.uy>, 
#  <rullo@cifasis-conicet.gov.ar>, 
#  <paula.pena@ciemat.es>, 
#  <renzo.espinoza@pti.org.br>, 
#  <rmoreno@uao.edu.co>, 
#  <carballore@gmail.com>, 
#  <roberto.moncadag@gmail.com>, 
#  <roberto.villafafila@citcea.upc.edu>, 
#  <dias@dee.ufrj.br>, 
#  <diretoria@microrredes.org.br>, 
#  <rodrigobueno@pti.org.br>, 
#  <rodrigo.sempertegui@ucuenca.edu.ec>, 
#  <nunez.ruben.o@gmail.com>, 
#  <santiago.torres@ucuenca.edu.ec>, 
#  <sdevalis@ciecs-conicet.gob.ar>, 
#  <srgjunco@gmail.com>, 
#  <thami@ghmsolutions.com.br>, 
#  <DiLavello@ute.com.uy>, 
#  <tomasquintilla@gmail.com>
# '''

# emails = emails.replace('<','')
# emails = emails.replace('>','')
# emails = emails.replace('\n','')
# emails = emails.replace('  ','')

# arrayEmails = emails.split(',')

# dicEmails = {'correos':arrayEmails}
# df = pd.DataFrame(data=dicEmails)
# df.to_csv(path_or_buf='./correos.csv',index=False,header=False)

nombre = """
Alejandro Garcés (UTP-Colombia)  

Alexandre Aoki (UFPR, Brasil)

Alexeis Fernández Bonilla (INTEC, Rep.Dominicana)

Andres Omar Alvarado Martinez (U.Cuenca, Ecuador)

Anibal Zanini (UBA-Argentina)

Antoni Sudrià (Toni, Barcelona, España)

Armando Vitali (UNGS-Argentina)

Batista 

Bernardo Silva (INESCTEC-Portugal)

Bruno Wanderley França (UFF, Brasil)

Camila Gehrke (UFPB, Brasil)

Carlos Gabriel Lopez (EDESTE-Argentina)

Carlos Moreira (INESCTEC-Portugal) Portugal)

Ciceli Martins (CEMIG-Brasil)

Coordenação Pós-Graduação (UNILA, Brasil)

Cristian de Angelo (GEA_CONICET-Argentina)

Danny Mauricio López (UniValle-Colombia)

Denizar Cruz Martins (UFSC-BR)

Desylen Mariano Hernández (INTEC, Rep.Dominicana)

Diego Edison Sánchez Ochoa (IPSE, Colombia)

Diego Elisei (CREXEL, Argentina)

Diego Feroldi (CIFASIS-Argentina)

Diego Giacosa (UTE, Uruguay)

Diego Rivelino Espinoza Trejo (UASLP-México)

Edson H. Watanabe (UFRJ-Brasil)

Eduardo Francisco Caicedo Bravo (UniValle-Colombia)

Eduardo Gomez (UniValle, Colombia)

Eduardo Prieto Araujo (UPC-ES)

Emmanuel Sangoi (UTN-FRSF)

Enrique Ciro Quispe Oqueña (UAO-Colombia)

Esteban Van Dam -(500rpm, Argentina)

Estefani Mendoza Guerra (UNI-Peru)

Fabiana Colombelli (UNILA, Brasil)

Facundo Aguilera (UNRC CONICET-Argentina)

Federico Serra (UNSL-Argentina)

Fernanda Guglialmelli (EDET, Tucuman, Secretaria Horacio Nadra, ADEERA)

Fernando Botterón (UNaM-Argentina)

Félix Santos García (UCLV, Cuba)

Germán Oggier (GEA_CONICET-Argentina)

Gonzalo Gaston Gomez (UTN-FRRo, Argentina)

Gonzalo Lopez (UTE-Uruguay)

Gonzalo Martín Jiménez (CEDER-CIEMAT, España)

Gonzalo Rodriguez (SyR Energia-Argentina)

Guilherme Rolim (UFRJ-Brasil)

Guillermo Catuogno (UNSL-Argentina)

Guillermo Guevara (BISENERGIA, AR)

Guillermo Jimenez Estevez (UniAndes-Colombia)

Guillermo Pleitavino (500RPM)

Gustavo Adolfo Ronceros Rivas (UNILA, Brasil)

Gustavo Gimenez Placer (UNGS-Argentina)

Gustavo Luis Airasca (UNR, Argentina)

Gustavo Martinez (BisEnergia, AR)

Gustavo Ramos Lopez (UniAndes-Colombia)

Hugo Elisei (CREXEL, Argentina)

Ivan Andrade (UMag, Chile)

J. Iam (UNILA, Brasil)

Jairo Benavides Martínez (UAO, Colombia)

Javier Martín Cabello (UNR-Argentina)

Javier Perez Ramirez (ITde Sonora, Mexico)

Johnny Posada Contreras (UAO-Colombia)

Jorge Andrés Niño (INTI, Argentina)

Jorge Caicedo (UFRJ-Brasil)

Jorge Javier Gimenez Ledesma (UNILA, Brasil)

Jorge Luis Mírez Tarrillo (UNI-Perú)

Jorge Vega (UTN-FRSF-Argentina)

Jose Alex Restrepo (USB-Venezuela)

Jose Angel Pecina Sanchez (UASLP, México)

Jose Antenor Pomilio (UNICAMP, Brasil)

Jose Salgado (UNILA, Brasil)

Jose Silva (LACTEC-Brasil)

José Antonio Beristáin Jiménez (ITde Sonora, Mexico)

José Fernando Jimenez Vargas (UniAndes, Colombia)

José Gomes de Matos (UFMA-Brasil)

José Manuel Aller Castro (USB-Venezuela)

José Manuel Da Peña (EDESTE-Argentina)

José Miguel Ramírez Scarpeta (UniValle-Colombia)

João Américo Vilela (UFPR-Brasil)

João Inácio Ota (UNICAMP, Brasil)

Juan David Molina Castro (CI-Colombia)

Juan Leonardo Eespinoza Abad (U.Cuenca, Ecuador)

Juan Tapia (USM, Chile)

Juliana Ulian (GHMS, Brasil)

Julio Cesar Viola (UPS, Ecuador)

Kati Sidwall (RTDS, Canada)

Katya Regina de Freitas (UNILA, Brasil)

León Lesyani (UCLV, Cuba)

Lucio Medeiros (LACTEC-Brasil)

Luis Cataldo (UTE, Uruguay)

Luis Gerardo Gonzalez Morales (U.Cuenca, Ecuador)

Luis Hernandez Callejo (UValladolid-España)

Luis Silva (UNRaf-Argentina)

Luiz Antonio DeSouza Ribeiro (UFMA-Brasil)

Luiz Carlos (UNICAMP-Brasil)

Manuel Perez Larraburu (500rpm, Argentina)

Marcela da Trindade (OPAL-RT, Brasil)

Marcela Ribeiro Gonçalves da Trindade (OPAL-RT, Brasil)

Marcelo Lobo Heldwein (UFSC-Brasil)

Marcia Regina Becker -(UNILA, Brasil)

Marcio Goes (UNILA, Brasil)

Marcos Politi (INTI, Argentina)

Mario Pierantonelli (UNVM, Argentina)

Marketing (GHMS, Brasil)

María Isabel Carvajal (UniValle-Colombia)

Matias Diaz (USACH, Chile)

Mauricio Aredes (UFRJ-Brasil)

Mauricio Schneebeli (SyR Energia-Argentina)

Miguel Aguirre (ITBA-Argentina)

Miguel Aybar (INTEC, Rep.Dominicana)

Miguel Fuertes (PTI, Colombia)

Miguel Laborde (UBA, AR)

Nicolas Matias Nemirovsky (ITBA-Argentina)

Norberto Barbieri (UTN-FRSN-Argentina) MEIHAPER)

Oriol Gomis (UPC-España)

Oscar Izquierdo Monge (CEDER-CIEMAT, España)

Osvaldo Ronald Saavedra (UFMA-Brasil)

Oswaldo Junior (UNILA, Brasil)

Otto Sollberger (Est.Electricos, Argentina)

Pablo Bertinat (PERMER-Argentina)

Pablo Maggi (UTE-Uruguay)

Pablo Rullo (UTN-FRSN-Argentina)

Paula Peña Carro (CEDER-CIEMAT, España)

Renzo Grover Fabián Espinoza (PTI-Brasil)

Ricardo Moreno (UAO-Colombia)

Roberto Carballo (UNaM-Argentina)

Roberto Moncada (UFrontera, Chile)

Roberto Villafafila (UPC-España)

Robson Dias (UFRJ-Brasil)

Rodrigo Bueno Otto (ABMR-Brasil)

Rodrigo Bueno Otto (PTI, Brasil)

Rodrigo Efrain Sempertegui Alvarez (U.Cuenca, Ecuador)

Rubén Núñez (Beatriz, UNaM, Oberá, Argentina)

Santiago Patricio Torres Contreras (U.Cuenca, Ecuador)

Sergio Devalis (CEC-CECS, Argentina)

Sergio Junco (UNR-Argentina)

Thami Lutzenberger (GHMS, Brasil)

Tomas Di Lavello (UTE-Uruguay)

Tomás Quintilla (UNVM-Argentina)

"""

nombre = nombre.replace('\n\n',';')
arrayNombres = nombre.split(';')

dicNombres = {'correos':arrayNombres}
df = pd.DataFrame(data=dicNombres)
df.to_csv(path_or_buf='./nombres.csv',index=False,header=False)
print(nombre)