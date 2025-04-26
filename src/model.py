from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.batchrunner import batch_run

from src.agent import PersonAgent, HealthStatus

class VirusModel(Model):
    def __init__(self, width = 50, height = 50, initial_agents = 750, 
                 infection_probability = 0.05, recovery_steps = 14, initial_infected_pct = 0.02,
                 enable_mobility = True, enable_asymptomatic = True, asymptomatic_fraction = 0.4,
                 asymptomatic_transmission_factor = 0.8, fatality_rate = 0.09, immunity_duration = 30,
                 vaccination_start_step = 100, vaccination_rate = 0.01, vaccination_efficacy = 0.8):
        
        super().__init__()
        self.width = width
        self.height = height
        self.initial_agents = initial_agents
        self.infection_probability = infection_probability
        self.recovery_steps = recovery_steps
        self.initial_infected_pct = initial_infected_pct
        self.enable_mobility = enable_mobility
        self.fatality_rate = fatality_rate
        self.immunity_duration = immunity_duration
        self.vaccination_start_step = vaccination_start_step
        self.vaccination_rate = vaccination_rate
        self.vaccination_efficacy = vaccination_efficacy

        self.current_step = 0

        self.enable_asymptomatic = enable_asymptomatic
        self.asymptomatic_fraction = asymptomatic_fraction
        self.asymptomatic_transmission_factor = asymptomatic_transmission_factor

        self.grid = MultiGrid(width, height, torus = False)
        self.schedule = RandomActivation(self)

        self.datacollector = DataCollector(
            model_reporters = {
                "Susceptible": lambda m: self.count_health_status(m, HealthStatus.SUSCEPTIBLE),
                "Infected": lambda m: self.count_health_status(m, HealthStatus.INFECTED),
                "Recovered": lambda m: self.count_health_status(m, HealthStatus.RECOVERED),
                "Dead": lambda m: self.count_health_status(m, HealthStatus.DEAD),
                "Vaccinated": lambda m: sum(1 for agent in m.schedule.agents if agent.is_vaccinated),
            }
        )

        self.running = True
        self.create_agents()

    def create_agents(self):
        for i in range(self.initial_agents):
            agent = PersonAgent(i, self)
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            while not self.grid.is_cell_empty((x, y)):
                x = self.random.randrange(self.width)
                y = self.random.randrange(self.height)
            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)

            #Randomly infect some agents
            if self.random.random() < self.initial_infected_pct:
                agent.status = HealthStatus.INFECTED
    
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
        self.current_step += 1

        if self.current_step >= self.vaccination_start_step:
            self.vaccinate_agents()
                
    @staticmethod
    def count_health_status(model, status):
        return sum(1 for agent in model.schedule.agents if agent.status == status)
    
    def vaccinate_agents(self):
        num_to_vaccinate = int(self.initial_agents * self.vaccination_rate)
        candidates = [agent for agent in self.schedule.agents if agent.status == HealthStatus.SUSCEPTIBLE and not agent.is_vaccinated]
        if candidates:
            selected = self.random.sample(candidates, min(num_to_vaccinate, len(candidates)))
            for agent in selected:
                if self.random.random() < self.vaccination_efficacy:
                    agent.is_vaccinated = True

        
