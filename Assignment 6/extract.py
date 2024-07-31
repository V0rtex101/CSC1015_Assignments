#Program to output useful data from raw data
#Fulufhelo Mulaudzi
#02 April 2024

def location(block):
    # This function returns the location component in title case.
    comma_index = block.find(",")
    beg_index = block.find(" ", comma_index) + 1
    end_index = block.find("END") - 1
    reverse_place = block[beg_index:end_index]
    place = reverse_place[::-1]
    return place.title()


def temperature(block):
    # This function returns the temperature as a floating point number
    beg_index = block.find(" ") + 1
    end_index = block.find("_")
    output = block[beg_index:end_index]
    return float(output)


def x_coordinate(block):
    # This function returns the x-coordinate as a string
    beg_index = block.find(":") + 1
    end_index = block.find(",")
    output = block[beg_index:end_index]
    return output


def y_coordinate(block):
    # This function returns the y-coordinate as a string
    beg_index = block.find(",") + 1
    end_index = block.find(" ", beg_index)
    output = block[beg_index:end_index]
    return output


def pressure(block):
    # This function returns the pressure as a floating point number
    beg_index = block.find("_") + 1
    end_index = block.find(":")
    output = block[beg_index:end_index]
    return float(output)


def get_block(data):
    # Takes raw data and extracts the sub string starting with 'BEGIN' and ending with 'END'
    beginning = data.find("BEGIN")
    end = data.find("END") + 3
    raw_data = data[beginning:end]
    return raw_data


def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
