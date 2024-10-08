


def juntar(lista, inicial, final, meio):
    left_side = lista[inicial:meio]
    right_side = lista[meio:final]
    top_left,top_right =0,0

    for k in range(inicial, final):
        if top_left >= len(left_side):
            lista[k] = right_side[top_right]
            top_right+=1

        elif (top_right >= len(right_side)):
            lista[k] = left_side[top_left]
            top_left+=1

        elif(left_side[top_left] < right_side[top_right]):
            lista[k] = left_side[top_left]
            top_left+=1

        else:
            lista[k] = right_side[top_right]
            top_right+=1

def mergesort(lista, inicial=0, final=None):
    if final is None:
        final = len(lista)

    if((final - inicial) > 1):
        middle = (inicial+final)//2
        mergesort(lista, inicial=inicial , final= middle)
        mergesort(lista, inicial=middle, final=final)
        juntar(lista, inicial, final, middle)


    
    
    

    


    

