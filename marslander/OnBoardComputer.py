class OnBoardComputer:
    
    def get_next_burn(self, status):
        burn = (status.get_velocity() * status.get_velocity())/ (2 * status.get_altitude()) + 98
        if burn > 200:
            burn = 200
        if burn < 0:
            burn = 0
        print(f"auto burn: {burn:.0f}")  # hack!
        return burn
