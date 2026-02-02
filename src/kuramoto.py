"""
Rudimentary Kuramoto model synchronization to (re)learn python.
"""

import numpy as np

class Kuramoto:
    """
    Kuramoto model of N coupled oscillators with environmental forcing.

    Equation:
        d theta_i/dt = omega_i + K/N sum_{j = 1}^N sin(theta_i - theta_j) + Kenv/N sin(omega_text{env} t - theta_i)

    Attributes:
        N: Number of oscillators
        K: Coupling constant
        Kenv: Environmental coupling
        theta: Array of phases at given step
        omega: Array of oscillator frequencies
        stdomega: Standard deviation for the oscillator frequency
        envomega: Forcing from the environment
        time: Simultaion time

    The mean frequency of the oscillators is set to 1. 
    """

    def __init__(self, N, K, stdomega, envomega = 0):
        """
        Initialize Kuramoto model.

        Args:
            N: Number of oscillators
            K: Coupling constant
            stdomega: Standard deviation for the oscillator ensemble
            envomega: Frequency of the environmental forcing
        """
        self.N = N
        self.K = K
        self.stdomega = stdomega
        self.envomega = envomega
        self.time = 0

        self.theta = np.random.uniform(0, 2 * np.pi, N)
        self.omega = np.random.normal(1, stdomega, N) # Negative frequencies are okay; moving frames

    # def coupling(self, oscillatori):
    #     """
    #     Calculating the coupling for the i^text{th} oscillator as K/N sum_{j = 0}^N sin(theta_i - theta_j)
    #
    #     Args:
    #         oscillatori: Oscillator index
    #
    #     Returns:
    #         K/N sum_{j = 0}^N sin(theta_i - theta_j)
    #     """
    #     coupling_sum = 0
    #     for j in range(self.N):
    #         coupling_sum += np.sin(- self.theta[j] + self.theta[oscillatori])
    #
    #     return (self.K/self.N) * coupling_sum
    
    def step(self, dt):
        """
        Taking a step in the integration- theta_i(t + dt) = theta_i(t) + dt * (omega_i + coupling_i(t)).

        Args:
            dt: Step size
        """
        theta_diff = self.theta[:, np.newaxis] - self.theta[np.newaxis, :]
        coupling_array = (self.K/self.N) * np.sum(np.sin(theta_diff), axis = 1)
        self.theta += dt * (self.omega + coupling_array)
        self.time += dt
        # for i in range(self.N):
        #     self.theta[i] += dt * (self.omega[i] + self.coupling(i))
        #
        # self.time += dt
        
    def orderparameter(self):
        """
        Calculates the order parameter r = |<exp^{i theta_j}>_j|.

        Returns:
            r: Center of mass of the phases
        """
        return np.abs(np.mean(np.exp(1j * self.theta)))

    def __repr__(self):
        """
        Representing the class as a string.
        """
        r = self.orderparameter()
        return f"Kuramoto model: N = {self.N:d}, K = {self.K:.3f}, r = {r:.3f}, time = {self.time:.3f}"

