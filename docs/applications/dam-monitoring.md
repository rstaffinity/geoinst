# Dam Monitoring

## Objective

Detect seepage changes, internal erosion, and deformation in embankment / concrete dams to prevent catastrophic failure.

---

## Comprehensive Chapter References from Reference Manuals

### From Dunnicliff — Geotechnical Instrumentation for Monitoring Field Performance
| Chapter | Title | Application to Dam Monitoring |
|---------|-------|--------------------------------|
| **Ch 1** | Geotechnical Instrumentation: An Overview | Importance of dam monitoring, failure consequences |
| **Ch 2** | Behavior of Soil and Rock | Embankment behavior, seepage, internal erosion |
| **Ch 3** | Benefits of Using Geotechnical Instrumentation | Safety, design verification, operational control |
| **Ch 4** | Systematic Approach to Planning Monitoring Programs | 20-step planning specific to dams |
| **Ch 9** | **Measurement of Groundwater Pressure** | **Primary** — Piezometers in embankment, foundation, abutments |
| **Ch 10** | Measurement of Total Stress in Soil | Earth pressure cells in embankment core |
| **Ch 11** | Measurement of Stress Change in Rock | Foundation rock stress monitoring |
| **Ch 12** | **Measurement of Deformation** | Extensometers, settlement, inclinometers, convergence |
| **Ch 13** | Measurement of Load and Strain | Strut loads, strain gages in concrete structures |
| **Ch 17** | Installation of Instruments | Drilling in embankments, grouting, cable routing |
| **Ch 18** | Collection, Processing, Presentation, Interpretation | Automated data acquisition (Ch 18.1.2), alarm thresholds |
| **Ch 21** | **Embankment Dams** | **Primary chapter for dams** — pore pressure, deformation, seepage, ADAS |

### From Das — Principles of Foundation Engineering (7th Ed)
| Chapter | Application |
|---------|-------------|
| **Ch 15** | Slope Stability — upstream/downstream slope stability |
| **Ch 12** | Shear Strength — effective stress analysis for dam cores |
| **Ch 9** | In Situ Stresses — foundation stress state |

### From Das — Principles of Geotechnical Engineering (7th Ed)
| Chapter | Application |
|---------|-------------|
| **Ch 15** | Slope Stability — upstream/downstream, seismic |
| **Ch 12** | Shear Strength — effective stress parameters for cores |
| **Ch 7** | Permeability — seepage analysis, filter design |
| **Ch 10** | Stresses in Soil Mass — embankment stress distribution |

### From Murthy — Advanced Foundation Engineering
| Topic | Application |
|-------|-------------|
| Seepage analysis | Flow nets, phreatic line, filter design |
| Dam stability | Upstream/downstream stability, seismic |

### From Field Methods for Geologists and Hydrologists
| Topic | Application |
|-------|-------------|
| Hydrogeology | Aquifer testing, dewatering, seepage measurement |

### From Encyclopedia of Field and General Geology
| Topic | Application |
|-------|-------------|
| Dam geology | Foundation geology, abutment stability, reservoir rim stability |

### NCHRP Synthesis 89
| Topic | Application |
|-------|-------------|
| Highway practice | Dam monitoring for highway agency dams |

---

## Typical Instrument Array for Dam Monitoring

| Instrument | Purpose | Dunnicliff Chapter | RST Instruments Product |
|------------|---------|-------------------|------------------------|
| **Multi-level piezometers** | Profile pore pressure through embankment | Ch 9, 21 | VW piezometer strings, RSTAR wireless |
| **Standpipe / open-well piezometers** | Redundant pore pressure measurement | Ch 9, 21 | Standpipe piezometers |
| **V-notch weirs / seepage meters** | Quantify downstream seepage flow | Ch 21 | Flow measurement |
| **Extensometers (rod/magnetic)** | Internal deformation of embankment | Ch 12, 21 | Rod extensometers, magnetic extensometers |
| **Inclinometers** | Lateral deformation of abutments/foundation | Ch 12, 21 | MEMS inclinometers, IPI arrays |
| **Surface settlement monuments** | Crest settlement, horizontal alignment | Ch 12, 21 | Settlement plates, GNSS |
| **Earth pressure cells** | Stress in embankment core | Ch 10, 21 | VW earth pressure cells |
| **Crackmeters / jointmeters** | Crack/joint monitoring in concrete | Ch 12 | Crackmeters, jointmeters |
| **Pendulums (concrete dams)** | Crest displacement relative to foundation | Ch 21 | Inverted/reverse pendulums |
| **Seepage weirs / flumes** | Quantify seepage discharge | Ch 21 | V-notch weirs |
| **Temperature sensors** | Concrete hydration, freeze-thaw | Ch 14 | Thermistors, RTDs |
| **RSTAR Affinity mesh** | Wireless data from all sensors | Ch 8, 18, 21 | RSTAR Affinity mesh + cellular/satellite backhaul |
| **ADAS (Automated Data Acquisition)** | Real-time alarms, automated reporting | Ch 18.1.2, 21 | RSTAR Affinity + Terra Insights |

---

## Installation Guidelines (from Dunnicliff Ch 9, 10, 12, 17, 21)

### Piezometer Installation in Embankments
- **Multi-level strings**: Install during construction at each lift
- **Filter tip**: Saturated, compatible with core material
- **Seals**: Bentonite above/below each filter zone
- **Cable routing**: Protected in conduit, strain-relieved at each lift
- **Terminal enclosure**: Ch 21.4.3 (above max water level)

### Extensometer Installation
- **Anchor depths**: Multiple anchors at key elevations (foundation, mid-height, near crest)
- **Reference head**: Stable benchmark outside dam influence
- **Readout**: VW or electrical, accessible at crest

### Seepage Measurement
- **V-notch weirs**: Downstream toe, calibrated
- **Seepage collectors**: French drains with flow measurement
- **Tracers**: Dye testing for seepage paths

---

## Data Interpretation Guidelines (from Dunnicliff Ch 18, 21)

| Parameter | Normal Range | Alert Level | Critical Level | Reference |
|-----------|--------------|-------------|----------------|-----------|
| Pore pressure ratio (u/σ') | < 0.5 | > 0.6 | > 0.8 | Ch 21 |
| Seepage flow increase | Baseline | 2× baseline | 5× baseline | Ch 21 |
| Crest settlement rate | < 5 mm/yr | > 20 mm/yr | > 50 mm/yr | Ch 21 |
| Horizontal displacement | < 10 mm/yr | > 25 mm/yr | > 50 mm/yr | Ch 21 |
| Crackmeter opening | < 0.5 mm | > 2 mm | > 5 mm | Ch 13, 21 |

---

## Automated Monitoring (Dunnicliff Ch 18.1.2, Ch 21)

| System | Function | RST Implementation |
|--------|----------|-------------------|
| **ADAS** | Automated data acquisition | RSTAR Affinity + DT Link |
| **Alarm thresholds** | Configurable per parameter | Terra Insights dashboard |
| **Data validation** | Automated QA/QC | Built-in QA/QC |
| **Reporting** | Scheduled reports | Terra Insights scheduled reports |
| **Remote access** | Web-based dashboard | Terra Insights Cloud |

---

## Related Pages
- [RST Piezometers](../rst-instruments/piezometers.md)
- [RST Extensometers](../rst-instruments/extensometers.md)
- [RST Inclinometers](../rst-instruments/inclinometers.md)
- [RSTAR Affinity Platform](../rst-instruments/rstar-affinity.md)
- [Dunnicliff Chapter 21](../reference-manuals/dunnicliff.md#chapter-21)
- [GTI Doctor — Ask about dam monitoring](../gti-doctor.md)

---

*Source: Compiled from Dunnicliff (616 chunks), Das Foundation (817 pp), Das Geotechnical (683 pp), Murthy (821 pp), Benerjee & Butterfield (394 pp), Field Methods (405 pp), Encyclopedia (952 pp), NCHRP Synthesis 89, and RST Instruments official support articles.*