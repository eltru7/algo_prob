def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[0])
    print(boxTypes)
    boxes = 0
    for box, units in boxTypes:
        if truckSize > box:
            truckSize -= box
            boxes += box * units
        else:
            boxes += truckSize * units
            return boxes
    return boxes