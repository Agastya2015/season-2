def shutdown(computer,battery):
    computer = 100
    battery = computer-battery
    if battery == 1 or battery == 0:
        print("Battery percentage: ", battery, "%")
        print("Computer shuts down🪫🪫🪫")
    else:
        print("Battery percentage: ", battery, "%")
        print("Computer stay's on for longer🔋🔋🔋")
shutdown(100,100)
