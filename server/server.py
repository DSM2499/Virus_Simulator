# server/server.py

from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.ModularVisualization import ModularServer



from src.model import VirusModel
from src.agent import HealthStatus

class StatusText(TextElement):
    """Display current counts of each health status."""

    def render(self, model):
        susceptible = model.count_health_status(model, HealthStatus.SUSCEPTIBLE)
        infected = model.count_health_status(model, HealthStatus.INFECTED)
        recovered = model.count_health_status(model, HealthStatus.RECOVERED)
        dead = model.count_health_status(model, HealthStatus.DEAD)
        vaccinated = sum(1 for agent in model.schedule.agents if agent.is_vaccinated)

        return f"Susceptible: {susceptible} | Infected: {infected} | Recovered: {recovered} | Dead: {dead} | Vaccinated: {vaccinated}"

def agent_portrayal(agent):
    if agent.is_vaccinated:
        color = "blue"  # Vaccinated agents
    elif agent.status == HealthStatus.SUSCEPTIBLE:
        color = "white"
    elif agent.status == HealthStatus.INFECTED:
        if agent.is_symptomatic is False:
            color = "yellow"
        else:
            color = "red"
    elif agent.status == HealthStatus.RECOVERED:
        color = "green"
    elif agent.status == HealthStatus.DEAD:
        color = "black"
    else:
        color = "gray"

    portrayal = {
        "Shape": "circle",
        "Filled": True,
        "r": 0.3,
        "Color": color,
        "Layer": 0,
    }
    return portrayal

grid = CanvasGrid(agent_portrayal, 100, 100, 1000, 1000)

chart = ChartModule([
    {"Label": "Susceptible", "Color": "grey"},
    {"Label": "Infected", "Color": "red"},
    {"Label": "Recovered", "Color": "green"},
    {"Label": "Vaccinated", "Color": "blue"},
    {"Label": "Dead", "Color": "black"},
])

status_text = StatusText()

server = ModularServer(
    VirusModel,
    [status_text, grid, chart],
    "Virus Spread Model",
    {
        "width": 100,
        "height": 100,
        "initial_agents": 1000,
        "infection_probability": 0.6,
        "recovery_steps": 80,
        "initial_infected_pct": 0.02,
        "enable_mobility": True,
        "enable_asymptomatic": True,
        "asymptomatic_fraction": 0.3,
        "asymptomatic_transmission_factor": 0.9,
        "fatality_rate": 0.7,
        "immunity_duration": 20,
        "vaccination_start_step": 100,
        "vaccination_rate": 0.05,
        "vaccination_efficacy": 0.6,
    }
)


server.port = 8521

if __name__ == "__main__":
    server.launch()

