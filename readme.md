# 🧬 Virus Spread Simulator

A flexible, agent-based modeling (ABM) simulation of virus spread dynamics — built in Python using Mesa.

This project simulates how viruses multiply and spread in a realistic environment, with parameters that control:
- Infection probability
- Symptom visibility (Asymptomatic carriers)
- Agent mobility
- Recovery, fatality
- Immunity duration and reinfection
- Vaccination rollout and efficacy

> 🎯 Designed for **visual storytelling** and **epidemiological realism**.  
> 🚀 Built to **showcase deep simulation, modeling, and coding skills**.

---

## 🌎 Features

- **Grid-based Petri dish environment** (customizable size, e.g., 100x100)
- **Mobility toggle** (moving vs stationary agents)
- **Asymptomatic transmission modeling**
- **Fatality modeling** with configurable fatality rates
- **Immunity loss and reinfection**
- **Vaccination rollout** starting at a configurable step
- **Live dashboard** of:
  - Susceptible
  - Infected
  - Recovered
  - Dead
  - Vaccinated agents
- **Dynamic color-coded visualization**:
  - 🟢 Green = Recovered
  - 🔴 Red = Infected (Symptomatic)
  - 🟡 Yellow = Infected (Asymptomatic)
  - ⚪ White = Susceptible
  - ⚫ Black = Dead
  - 🔵 Blue = Vaccinated
- **Live Chart** showing population health trends over time

---

## 📸 Screenshots

| Grid Simulation | Population Chart |
|:---------------:|:----------------:|
| ![Grid Example](https://github.com/DSM2499/Virus_Simulator/blob/main/Graph.png) | ![Chart Example](https://github.com/DSM2499/Virus_Simulator/blob/main/Grid.png) |



---

## 🏗️ Project Structure

```bash
Virus Simulator/
├── src/
│   ├── agent.py        # Defines agent behavior (infection, movement, recovery, death)
│   ├── model.py        # Defines environment, rules, and parameters
│
├── server/
│   ├── server.py       # Visualization server (Grid, Chart, Live Status Dashboard)
│
├── venv/               # Virtual environment (not included in GitHub repo)
├── requirements.txt    # Project dependencies
├── README.md           # This file
```
<heading>⚙️ Configurable Parameters</heading>
  <p>All parameters can be tuned inside <code>server/server.py</code> before starting the simulation.</p>
  <table>
    <tr><th>Parameter</th><th>Description</th></tr>
    <tr><td><code>width</code>, <code>height</code></td><td>Grid size</td></tr>
    <tr><td><code>initial_agents</code></td><td>Number of agents</td></tr>
    <tr><td><code>infection_probability</code></td><td>Chance of infection per contact</td></tr>
    <tr><td><code>recovery_steps</code></td><td>How long infection lasts before recovery or death</td></tr>
    <tr><td><code>fatality_rate</code></td><td>Chance of death after infection</td></tr>
    <tr><td><code>immunity_duration</code></td><td>How long immunity lasts after recovery</td></tr>
    <tr><td><code>enable_mobility</code></td><td>Toggle agent movement</td></tr>
    <tr><td><code>enable_asymptomatic</code></td><td>Toggle asymptomatic carriers</td></tr>
    <tr><td><code>vaccination_start_step</code></td><td>When vaccination campaign starts</td></tr>
    <tr><td><code>vaccination_rate</code></td><td>Portion vaccinated each step</td></tr>
    <tr><td><code>vaccine_efficacy</code></td><td>Effectiveness of the vaccine</td></tr>
  </table>
  <p>✅ Easily simulate different disease types (COVID-19, Influenza, etc.) by adjusting these values.</p>
</section>

<hr/>

<section>
  <heading>🙌 Acknowledgements</heading>
  <ul>
    <li><a href="https://github.com/projectmesa/mesa">Mesa</a> – Agent-based modeling in Python</li>
    <li><a href="https://www.tornadoweb.org/">Tornado</a> – WebSocket handling</li>
  </ul>
</section>

<hr/>

<section>
  <heading>📢 Author</heading>
  <p><strong>Dinakar Murthy</strong></p>
  <ul>
    <li>Data Scientist | Simulation Engineer | Python Enthusiast</li>
    <li>📫 <a href="https://www.linkedin.com/in/dinakar-murthy/">LinkedIn Profile</a></li>
    <li>🌟 Always excited about AI, Data, and building the future!</li>
  </ul>
</section>
