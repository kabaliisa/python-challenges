#square = [value**2 for value in range(1,21)]
#def square_number():
#    print(square[0:5])  

#square_number()    
squares = []
def square_number():

    for value in range(1,21):
        square = value**2
        squares.append(square)
    print(squares[0:5])

square_number()        
