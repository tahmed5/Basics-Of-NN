def get_coordinates():
    x_coord = []
    y_coord = []
    entering_coordinates = True
    print('Enter Your x and y Coordinates in the format x,y')
    print("Type 'done' when you are finished")
    while entering_coordinates == True:
        data = input()
        if data == 'done':
            entering_coordinates = False
            break          
        data = data.split(',')
        if len(data) != 2:
            print("Invalid Format: E.G x,y --> 5,3")
            continue
        if data[0] == '' or data[1] == '':
            print('Incomplete coorindates')
            continue
        try:
            data[0] = int(data[0])
            data[1] = int(data[1])
        except:
            print('Strings Detected')
            continue 
        x_coord.append(data[0])
        y_coord.append(data[1])
        print(x_coord)
        print(y_coord)
        
      
    

def main():
    get_coordinates()
    


main()
