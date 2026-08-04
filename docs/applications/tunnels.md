# Tunnel Instrumentation

## Objective

Monitor ground movement around tunnel excavation, convergence of linings, and pore-pressure changes during construction — protecting both the tunnel cross-section and adjacent structures above.

---

## Comprehensive Chapter References from Reference Manuals

### From Dunnicliff — Geotechnical Instrumentation for Monitoring Field Performance
| Chapter | Title | Application to Tunnel Instrumentation |
|---------|-------|----------------------------------------|
| **Ch 1** | Geotechnical Instrumentation: An Overview | Importance of tunnel monitoring, collapse consequences |
| **Ch 2** | Behavior of Soil and Rock | Rock mass behavior, squeezing ground, rockburst |
| **Ch 3** | Benefits of Using Geotechnical Instrumentation | Design verification, construction safety, contractual |
| **Ch 4** | Systematic Approach to Planning Monitoring Programs | 20-step planning for tunnel projects |
| **Ch 8** | Instrumentation Transducers & Data Acquisition | Convergence sensors, automated systems |
| **Ch 9** | Measurement of Groundwater Pressure | Dewatering pressures, piezometers at tunnel face |
| **Ch 12** | **Measurement of Deformation** | **Primary** — Convergence, extensometers, inclinometers |
| **Ch 13** | Measurement of Load and Strain | Rock bolt loads, lining stress, telltales |
| **Ch 17** | Installation of Instruments | Tunnel-specific: drilling from tunnel, limited space |
| **Ch 18** | Collection, Processing, Presentation, Interpretation | Real-time convergence monitoring, alarm systems |
| **Ch 23** | **Underground Excavations** | **Primary chapter for tunnels** — convergence, rock bolts, groundwater, face pressure |

### From Das — Principles of Foundation Engineering (7th Ed)
| Chapter | Application |
|---------|-------------|
| **Ch 13** | Lateral Earth Pressure — tunnel lining design |
| **Ch 15** | Slope Stability — portal slopes, surface settlement |

### From Das — Principles of Geotechnical Engineering (7th Ed)
| Chapter | Application |
|---------|-------------|
| **Ch 12** | Shear Strength — rock mass strength parameters |
| **Ch 15** | Slope Stability — portal stability, surface settlement trough |

### From Murthy — Advanced Foundation Engineering
| Topic | Application |
|-------|-------------|
| Tunnel linings | Segmental lining design, segment joints |
| TBM monitoring | Shield pressure, articulation, articulation |

### From Benerjee & Butterfield — Advanced Geotechnical Analyses
| Topic | Application |
|-------|-------------|
| Numerical modeling | FEM/DEM for tunnel excavation sequence |

### From Field Methods for Geologists and Hydrologists
| Topic | Application |
|-------|-------------|
| Structural geology | Discontinuity mapping, rock mass classification |

### From Encyclopedia of Field and General Geology
| Topic | Application |
|-------|-------------|
| Tunneling methods | Drill & blast, TBM, NATM, sequential excavation |

---

## Typical Instrument Array for Tunnel Instrumentation

| Instrument | Purpose | Dunnicliff Chapter | RST Instruments Product |
|------------|---------|-------------------|------------------------|
| **Convergence arrays / tape extensometers** | Monitor tunnel cross-section closure | Ch 12, 23 | Tape extensometers, convergence arrays |
| **Multi-point borehole extensometers (MPBX)** | Rock mass displacement above crown | Ch 12, 23 | MPBX extensometers, RSTAR wireless |
| **Inclinometers (surface/portal)** | Detect surface settlement trough | Ch 12, 23 | MEMS inclinometers, IPI arrays |
| **Piezometers** | Dewatering pressures near tunnel face | Ch 9, 23 | VW piezometers, RSTAR wireless |
| **Rock bolt load cells** | Anchor/bolt load monitoring | Ch 13, 23 | VW load cells, strain gages |
| **Convergence meters** | Real-time lining convergence | Ch 12, 23 | Convergence meters, RSTAR wireless |
| **Rock bolt strain gages** | Bolt load monitoring | Ch 13 | VW strain gages, RSTAR wireless |
| **Pressure cells (NATM)** | Ground pressure on lining | Ch 10, 23 | VW pressure cells |
| **Crackmeters / jointmeters** | Segment joint opening | Ch 12, 23 | Crackmeters, jointmeters |
| **Inclinometer (TBM shield)** | TBM articulation/alignment | Ch 12 | MEMS tilt sensors |
| **RSTAR mesh radio** | Data from tunnel to surface gateway | Ch 8, 18 | RSTAR mesh + surface gateway |

---

## Installation Guidelines (from Dunnicliff Ch 12, 17, 23)

### Convergence Monitoring
- **Array types**: Tape extensometer, convergence meter, MPBX
- **Locations**: Crown, springlines, invert
- **Frequency**: Daily (excavation), weekly (construction), monthly (operation)

### Extensometer Installation (MPBX)
- **Anchor depths**: Multiple anchors at varying rock cover depths
- **Installation**: From tunnel crown/drilling from surface
- **Reference head**: Stable location outside tunnel influence zone

### Piezometer Installation
- **Locations**: Ahead of face, at face, behind lining
- **Types**: VW piezometers for remote reading
- **Dewatering monitoring**: Upstream/downstream of tunnel

### Rock Bolt Monitoring
- **Load cells**: Installed at bolt head
- **Strain gages**: Bonded to bolt shank
- **Tell-tales**: For long bolt elongation

---

## Data Interpretation Guidelines (from Dunnicliff Ch 18, 23)

| Parameter | Normal Range | Alert Level | Critical Level | Reference |
|-----------|--------------|-------------|----------------|-----------|
| Convergence rate | < 2 mm/day | > 5 mm/day | > 10 mm/day | Ch 23 |
| Crown settlement rate | < 2 mm/day | > 5 mm/day | > 10 mm/day | Ch 23 |
| Rock bolt load loss | < 10% | > 20% | > 30% | Ch 13 |
| Pore pressure change | Baseline | 2× baseline | > design value | Ch 9, 23 |
| Rock bolt load loss rate | < 5%/mo | > 10%/mo | > 20%/mo | Ch 13 |

---

## Automated Monitoring for Tunnels (Dunnicliff Ch 18, Ch 23)

| System | Function | RST Implementation |
|--------|----------|-------------------|
| **Real-time convergence** | Continuous crown/springline monitoring | RSTAR wireless convergence sensors |
| **Face pressure monitoring** | TBM shield pressure, dewatering | RSTAR wireless piezometers |
| **Rock bolt monitoring** | Bolt load + strain | VW load cells + strain gages |
| **Automated alarms** | Threshold exceedance | Terra Insights Cloud |
| **TBM data integration** | Shield pressure, articulation | RSTAR mesh + TBM interface |

---

## Related Pages
- [RST Extensometers](../rst-instruments/extensometers.md)
- [RST Inclinometers](../rst-instruments/inclinometers.md)
- [RST Piezometers](../rst-instruments/piezometers.md)
- [RSTAR Affinity Platform](../rst-instruments/rstar-affinity.md)
- [Dunnicliff Chapter 23](../reference-manuals/dunnicliff.md#chapter-23)
- [GTI Doctor — Ask about tunnel monitoring](../gti-doctor.md)

---

*Source: Compiled from Dunnicliff (616 chunks), Das Foundation (817 pp), Das Geotechnical (683 pp), Murthy (821 pp), Benerjee & Butterfield (394 pp), Field Methods (405 pp), Encyclopedia (952 pp), NCHRP Synthesis 89, and RST Instruments official support articles.*