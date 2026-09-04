# GravityX

**Artificial Gravity Space Station Concept**

## Overview

GravityX is a research and systems-design concept for a sustainable rotating space station that explores Earth-like artificial gravity. The repository contains an interactive mission-control dashboard used to communicate and simulate parts of the proposed system.

## Problem

The project explores how a rotating space-station concept can be monitored and controlled through a clear technical interface. The included dashboard focuses on representing rotational behavior, operational telemetry, chamber status, alerts, and energy recovery in one control surface.

## Concept / Solution

GravityX proposes a rotating-station concept supported by a mission-control dashboard. The interface models:

- Rotation values for multiple sections of the system
- Internal chamber RPM
- Operational controls and status indicators
- Alert and emergency-control states
- Piezoelectric energy-recovery readings
- A path for receiving telemetry and alerts through MQTT

The values shown by the current standalone dashboard are simulated in the browser. MQTT topics are present as an integration path for connected telemetry.

## My Role

- Project Lead
- Technical Development
- Research
- Simulation
- Systems Design

## Recognition

- 3rd Place in Saudi Arabia — WRO 2025
- Global Special Award — GRC 2025

## Technical Work

- HTML
- CSS
- JavaScript
- Browser-based telemetry simulation
- Dashboard and control-interface design
- MQTT integration structure
- Audio and visual alert feedback

## Architecture / System

The repository currently represents the interface and simulation layer:

1. A browser-based mission-control dashboard presents station state and controls.
2. JavaScript generates simulated RPM and energy values for demonstration.
3. MQTT topic definitions provide a path for external telemetry and alert messages.
4. Interface controls represent start, tracking, and emergency-stop operations.

## Dashboard Preview

- [Open the primary dashboard source](index.html)
- [Open the alternate dashboard file](gravityx_dashboard.html)

The repository does not currently contain a static screenshot or a hosted live demo.

## Project Status

Research concept and interactive dashboard prototype. Hardware telemetry integration is represented in the interface structure but is not configured as a production connection in this repository.

## About the Builder

**Afnan Al-Duhaim**<br>
Technology Product Builder<br>
Founder of Nawwsaj Innovation Lab<br>
[View Afnan's portfolio](https://afnan-ahmad-portfolio.vercel.app)
