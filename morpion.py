def morpion():
    grid = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
    print(grid[0][0] + "  " + grid[0][1] + "  " + grid[0][2] + "\n" + grid[1][0] + "  " + grid[1][1] + "  " + grid[1][2] + "\n" + grid[2][0] + "  " + grid[2][1] + "  " + grid[2][2] + "\n>" )
    joueurLigne = input("Quelle ligne ?\n>")
    joueurColone = input("Quelle colone ?\n>")
    replace = len(grid)
    for i in range(10):
        grid[i]
print(morpion())        