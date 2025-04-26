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
| ![Grid Example](path/to/grid_screenshot.png) | ![Chart Example](path/to/chart_screenshot.png) |

*(Add your screenshots here!)*

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
