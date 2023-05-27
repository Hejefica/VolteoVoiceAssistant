#Programa para obtener arreglos entre dos colores
#se utiliza la funcion "fade" con los argumentos color 1, color 2 y el numero de colores que se quieren
#para obtener un color fade entre ambos colores



def dec(rgb):
    color = [0,0,0]
    for i in range(3):
        #print(rgb[(i*2):((i+1)*2)])
        color[i] = int((rgb[((i*2)+1):(((i+1)*2)+1)]), 16)
    return color

def rgb(dec):
    color_matrix = ['x' for i in range(len(dec))]
    
    for i in range(len(dec)):
        string = '#'
        for j in range(3):
            hexa = hex(dec[i][j])
            if(len(hexa)<4):
                string=string+'0'+hexa[2:]
            else:
                string=string+hexa[2:]
        color_matrix[i]=string

    print(color_matrix)

    return color_matrix

def fade(color1, color2, frames):
    iterations = frames - 1
    color1_d = dec(color1)
    color2_d = dec(color2)
    color_matrix = [[0]* 3 for i in range(frames)]
    color_matrix[0]= color1_d

    for i in range(3):
        difference = color2_d[i] - color1_d[i]
        adding = float(difference/iterations)
        summary = color1_d[i]

        for j in range(iterations):
            summary = summary + adding
            color_matrix[j+1][i] = int(round(summary))        
    #print(color_matrix)

    return color_matrix

r = fade('#67D69E','#68E9F2',20)
s = rgb(r)
r = fade('#68E9F2','#50A848',20)
s = rgb(r)
r = fade('#50A848','#67D69E',20)
s = rgb(r)

print('pruebas:')
r = fade('#CC3733','#2C39AD',60)
s = rgb(r)
  
