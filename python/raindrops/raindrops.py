raindrops = {3:"Pling", 5:"Plang", 7:"Plong"}

def convert(number):
    converted= ""
    for key, value in raindrops.items():
        if number%key == 0:
            converted += value
    if not converted:
        converted = str(number)
    return converted