
from DescentEvent import DescentEvent


class Vehicle:

    # Various end-of-game messages and status result codes.
    dead = "\nCRASH!!\n\tThere were no survivors.\n\n";
    DEAD = -3;
    crashed = "\nThe Starship crashed. Good luck getting back home. Elon is pissed.\n\n";
    CRASHED = -2;
    emptyfuel = "\nThere is no fuel left. You're floating around like Major Tom.\n\n";
    EMPTYFUEL = -1;
    success = "\nYou made it! Good job!\n\n";
    SUCCESS = 0;
    FLYING = 1;

    def __init__(self, initial_altitude):
        # initialize the altitude AND previous altitude to initialAltitude

        self.altitude= initial_altitude
        self.prev_altitude= initial_altitude

        self.velocity= 1000
        self.fuel = 12000
        self.burn = 0
        self.flying = Vehicle.FLYING
        self.gravity = 100
        pass

    def check_final_status(self):
        s = ""
        if self.altitude <= 0:
            if self.velocity > 10:
                s = self.dead
                self.flying = self.DEAD
            elif 3 < self.velocity <= 10:
                s = self.crashed
                self.flying = self.CRASHED
            elif self.velocity <= 3:
                s = self.success
                self.flying = self.SUCCESS
        else:
            if self.altitude > 0:
                s = self.emptyfuel
                self.flying = self.EMPTYFUEL
        return s


    def compute_deltaV(self):
        # return velocity + gravity - burn amount
        return int(self.velocity + self.gravity - self.burn)

    def adjust_for_burn(self, burnAmount):
        # set burn to burnamount requested
        # save previousAltitude with current Altitude
        # set new velocity to result of computeDeltaV function.
        # subtract speed from Altitude
        # subtract burn amount fuel used from tank
        self.burn = burnAmount
        self.prev_altitude = self.altitude
        self.velocity = self.compute_deltaV()
        self.altitude -= self.velocity
        self.fuel -= burnAmount
        # check if fuel is less than zero

    def still_flying(self):
        # return true if altitude is positive
        if self.altitude > 0:
            return True

    def out_of_fuel(self):
        # return true if fuel is less than or equal to zero
        if self.fuel <= 0:
            return True

    def get_status(self, tick):
        # return a new DescentEvent object
        # with the following parameters
        return DescentEvent(tick, self.velocity, self.fuel, self.altitude, self.flying)

    def get_altitude(self):
        # return the altitude
        return self.altitude
    def get_velocity(self):
        # return the velocity
        return self.velocity


