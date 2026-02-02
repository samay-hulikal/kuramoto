import numpy as np

class Oscillator:
    """
    Creates an oscillator with a certain natural frequency and initial phase.

    Attributes:
        omega: natural frequency
        theta: time-dependent phase
    """
    def __init__(self, omega, theta = None):
        """
        Creates an oscillator with input parameters omega and theta.
        """
        self.omega = omega
        if theta == None:
            self.theta = np.random.uniform(0, 2 * np.pi)
        else:
            self.theta = theta

    def dtpropagate(self, dt, coupling):
        """
        Propagate phase of oscillator in time by an amount dt. 

        d theta/dt = omega + K/N (coupling(t))
        theta(t + dt) = theta(t) + dt(omega + K/N (coupling(t)))
        """
        self.theta += dt * (self.omega + coupling)

    def position(self):
        """
        Get (x, y) position on a circle.
        """
        return np.array([np.cos(self.theta), np.sin(self.theta)])

    def __repr__(self):
        """
        Represents the object as a string for printing. 
        """
        return f"Oscillator(omega = {self.omega:.2f}, theta = {self.theta:.2f})"



