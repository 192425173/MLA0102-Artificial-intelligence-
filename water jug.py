def water_jug():
    jug4, jug3 = 0, 0
    while True:
        print(f"(4-gal: {jug4}, 3-gal: {jug3})")
        if jug4 == 2:
            print("Goal Reached!")
            break
        elif jug3 == 0:
            jug3 = 3
            print("Fill 3-gallon jug")
        elif jug4 < 4:
            transfer = min(4 - jug4, jug3)
            jug4 += transfer
            jug3 -= transfer
            print("Pour 3-gallon → 4-gallon")
        elif jug4 == 4:
            jug4 = 0
            print("Empty 4-gallon jug")

water_jug()