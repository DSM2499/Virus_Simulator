from mesa import Agent
from enum import Enum

class HealthStatus(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2
    DEAD = 3

class PersonAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = HealthStatus.SUSCEPTIBLE
        self.infection_timer = 0 # How many steps the agent has been infected
        self.is_symptomatic = None
        self.recovery_timer = None
        self.is_vaccinated = False
    
    def move(self):
        ''' Move to a random neighboring empty cell'''
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore = True,
            include_center = False
        )
        empty_cells = [cell for cell in possible_steps if self.model.grid.is_cell_empty(cell)]
        if empty_cells:
            new_position = self.random.choice(empty_cells)
            self.model.grid.move_agent(self, new_position)
    
    def step(self):
        
        if self.status == HealthStatus.DEAD:
            return
        
        if self.is_vaccinated and self.status == HealthStatus.SUSCEPTIBLE:
        # Vaccinated agents stay immune unless vaccine fails later (advanced)
            return

        if self.model.enable_mobility:
            self.move()

        if self.status == HealthStatus.INFECTED:
            self.infection_timer += 1

            #Try to infect neighbors
            neighbors = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False)
            for neighbor in neighbors:
                if neighbor.status == HealthStatus.SUSCEPTIBLE:
                    transmission_chance = self.model.infection_probability
                    if self.model.enable_asymptomatic and self.is_symptomatic == False:
                        transmission_chance *= self.model.asymptomatic_transmission_factor
                    if self.random.random() < transmission_chance:
                        neighbor.become_infected()
            
            #Check for recovery
            if self.infection_timer >= self.model.recovery_steps:
            # Decide whether agent recovers or dies
                if self.random.random() < self.model.fatality_rate:
                    self.status = HealthStatus.DEAD
                else:
                    self.status = HealthStatus.RECOVERED
        
        elif self.status == HealthStatus.RECOVERED:
            if self.recovery_timer is not None:
                self.recovery_timer += 1
                if self.recover_timer >= self.model.immunity_duration:
                    self.status = HealthStatus.SUSCEPTIBLE
                    self.recovery_timer = None

    def become_infected(self):
        self.status = HealthStatus.INFECTED
        if self.model.enable_asymptomatic:
            if self.random.random() < self.model.asymptomatic_fraction:
                self.is_symptomatic = False
            else:
                self.is_symptomatic = True
        else:
            self.is_symptomatic = True  # Default: all are symptomatic
