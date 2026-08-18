"""
Air Canada system registry.

Single source of truth for every system referenced anywhere in the wiki.
Each entry: (css_class, tooltip, evidence_tier, vendor)

Evidence tiers (from the pre-sales due-diligence evidence base):
  A = confirmed  — AC or vendor press release, AC portal, tribunal/regulator filing
  B = indicated  — job postings, technographic databases, trade press, vendor lists
  C = pattern    — industry-typical inference, NOT evidenced for Air Canada.
                   Never assert a C-tier system as fact in a bid.
  U = unknown    — named gap; a discovery question, deliberately retained so
                   downstream links do not dangle.

Corrections applied vs. common (wrong) assumptions about Air Canada:
  * MRO core is TRAX  -- not AMOS, not Ramco, not IFS/Mxi Maintenix
  * Cargo is CHAMP Cargospot neo (implementation in flight) -- not IBS iCargo
  * Ops planning / scheduling is Lufthansa Systems NetLine -- not FlightKeys
  * Crew and OCC run on Jeppesen
  * Cloud posture is AWS-first -- not GCP-primary
  * Analytics platform is Databricks lakehouse (Cloudera sunsetting) -- not Snowflake
  * Contact centre is Amazon Connect + Salesforce Service Cloud Voice -- not Genesys
  * Customer identity is SAP Customer Data Cloud (Gigya) -- Okta is not evidenced
"""

SYSTEMS = {

    # ---- Passenger Service System : Amadeus Altea -------------------------
    "Amadeus Altea Reservations": ("amadeus", "Core PSS reservations. Replaced Air Canada's 22-year in-house PSS at the 2019-20 cutover.", "A", "Amadeus"),
    "Amadeus Altea Inventory": ("amadeus", "Seat inventory and availability control. Consumes RM bid prices from PROS.", "A", "Amadeus"),
    "Amadeus Altea DCS": ("amadeus", "Departure Control. Check-in, bag acceptance, boarding and load control across mainline, Rouge and Express.", "A", "Amadeus"),
    "Amadeus Altea Customer Management": ("amadeus", "Customer profile and PNR servicing layer. Feeds case context to Salesforce.", "A", "Amadeus"),
    "Amadeus Passenger Recovery": ("amadeus", "Automated IRROP re-accommodation. Replaced largely manual disruption handling pre-2020.", "A", "Amadeus"),
    "Amadeus Altea NDC": ("amadeus", "IATA NDC distribution via Amadeus Travel Platform, live 2023. Single-PNR NDC and EDIFACT.", "A", "Amadeus"),
    "Amadeus Anytime Merchandising": ("amadeus", "Ancillary offer construction and dynamic bundling at the shopping touchpoint.", "A", "Amadeus"),

    # ---- Revenue Management & Pricing ------------------------------------
    "PROS Real-Time Dynamic Pricing": ("pros", "Continuous willingness-to-pay pricing. Air Canada is a 30-year-plus PROS reference account.", "A", "PROS"),
    "PROS Revenue Management": ("pros", "O&D revenue management and bid-price optimisation feeding Altea Inventory.", "B", "PROS"),
    "ATPCO": ("iata", "Industry fare filing, rules, footnotes and tax data. The rate-limiting step on pricing agility.", "B", "ATPCO"),
    "Sabre GDS": ("gds", "Legacy GDS distribution channel. Agency bookings settle through IATA BSP.", "C", "Sabre"),
    "Travelport": ("gds", "Secondary GDS distribution channel.", "C", "Travelport"),
    "IATA BSP": ("iata", "Billing and Settlement Plan. Agency sales settlement and revenue accounting reconciliation.", "B", "IATA"),
    "ARC": ("iata", "Airlines Reporting Corporation. US agency sales settlement.", "C", "ARC"),

    # ---- Loyalty : Aeroplan ----------------------------------------------
    "Aeroplan Platform": ("aeroplan", "In-house loyalty engine. Reacquired from Aimia for CA$450M and relaunched 8 Nov 2020.", "A", "Air Canada"),
    "SAP Customer Data Cloud": ("sap", "Customer identity, consent and profile (ex-Gigya). Migration delivered with Trew Knowledge. Carries Law 25 consent.", "A", "SAP"),
    "Aeroplan Partner Interfaces": ("aeroplan", "Co-brand and partner accrual feeds: TD, CIBC, Amex, retail and hotel partners.", "A", "Air Canada"),

    # ---- Customer channels & contact centre ------------------------------
    "aircanada.com": ("channel", "Primary direct digital channel, cloud-native on AWS. Undergoing redevelopment under the CDO.", "A", "Air Canada"),
    "Air Canada Mobile App": ("channel", "iOS and Android. Booking, check-in, boarding pass, in-app bag tracking and mobility-aid tracking.", "A", "Air Canada"),
    "Amazon Connect": ("aws", "Cloud contact centre and IVR. Handles very high monthly IVR volume with secure PCI payment capture.", "A", "AWS"),
    "Salesforce Service Cloud": ("salesforce", "Agent desktop, case management and Service Cloud Voice. System of record for customer cases and APPR claims.", "A", "Salesforce"),
    "Air Canada Virtual Assistant": ("aiml", "Bilingual customer-facing assistant. Predecessor bot was withdrawn c. April 2024 after the Moffatt ruling.", "B", "Air Canada"),
    "Simul8": ("aiml", "Contact-centre digital twin used for capacity and staffing simulation.", "A", "Simul8"),
    "Adobe Experience Manager": ("channel", "Web content management for aircanada.com. Carries the Official Languages Act EN/FR parity burden.", "C", "Adobe"),

    # ---- Network planning, flight ops & crew -----------------------------
    "Lufthansa Systems NetLine": ("netline", "Network planning, scheduling and operations control suite. Schedule build through day-of-operation.", "B", "Lufthansa Systems"),
    "NetLine/Plan": ("netline", "Long-range schedule design, fleet assignment and rotation build.", "B", "Lufthansa Systems"),
    "NetLine/Ops": ("netline", "Operations control: flight watch, delay management and schedule recovery at the OCC.", "B", "Lufthansa Systems"),
    "Jeppesen Crew": ("jeppesen", "Crew pairing, rostering, bidding and day-of-operations tracking under ACPA and CUPE agreements.", "B", "Boeing Jeppesen"),
    "Jeppesen OCC": ("jeppesen", "Operations control and disruption recovery decision support at the YYZ operations centre.", "B", "Boeing Jeppesen"),
    "Jeppesen Charts": ("jeppesen", "Terminal charts and navigation data delivered to the flight deck EFB.", "B", "Boeing Jeppesen"),
    "ACARS Datalink": ("datalink", "Air-ground messaging. OOOI times, load messages, ATC datalink and maintenance downlinks.", "C", "SITA / ARINC"),
    "NAV CANADA": ("regulator", "Canadian ANSP. NOTAM, flight data, oceanic clearance and traffic flow management.", "B", "NAV CANADA"),
    "Electronic Flight Bag": ("datalink", "Flight-deck EFB carrying charts, performance calculations and operational manuals.", "C", "Multiple"),
    "Weight and Balance System": ("datalink", "Load planning, trim sheet and final loadsheet issue to the flight deck.", "C", "Multiple"),
    "Safety Management System": ("regulator", "Occurrence reporting, hazard register and risk assessment under CARs and IOSA.", "C", "Multiple"),

    # ---- Maintenance & Engineering ---------------------------------------
    "TRAX": ("trax", "Air Canada's maintenance and engineering core: work orders, task cards, parts, tech records and airworthiness.", "B", "TRAX"),
    "TRAX eMobility": ("trax", "Mobile maintenance execution at the aircraft. Addresses line-maintenance usability at the gate.", "B", "TRAX"),
    "Aeroxchange": ("trax", "Aviation parts B2B marketplace and ATA Spec 2000 supplier messaging.", "C", "Aeroxchange"),
    "Transport Canada CAWIS": ("regulator", "Airworthiness directive and continuing-airworthiness compliance against CARs.", "C", "Transport Canada"),

    # ---- Cargo ------------------------------------------------------------
    "CHAMP Cargospot neo": ("champ", "Cargo booking, capacity and documentation. Selected 2026 and currently in implementation.", "A", "CHAMP"),
    "Cargospot neo Handling": ("champ", "Cargo warehouse and ground handling execution, ULD build-up and breakdown.", "A", "CHAMP"),
    "Cargospot neo Revenue Accounting": ("champ", "Cargo revenue accounting and IATA CASS settlement.", "A", "CHAMP"),
    "Cargospot Mobile": ("champ", "Mobile cargo warehouse and ramp execution.", "A", "CHAMP"),
    "Canada PACT": ("regulator", "CBSA pre-load air cargo targeting. Mandatory pre-load data filing in force since 1 April 2025.", "B", "CBSA"),
    "OnAsset Vision": ("champ", "IoT sensor tracking for cargo condition, location and cold-chain compliance.", "B", "OnAsset"),

    # ---- Airport & baggage -------------------------------------------------
    "SITA WorldTracer": ("sita", "Global mishandled-baggage tracing and PIR file management.", "B", "SITA"),
    "Baggage Reconciliation System": ("sita", "Bag-to-passenger matching and IATA Resolution 753 tracking at load and transfer.", "C", "SITA"),
    "CUPPS": ("sita", "Common-use passenger processing at shared airport counters and kiosks.", "C", "Multiple"),
    "Airport Resource Management": ("sita", "Gate, stand and check-in resource allocation at YYZ, YUL and YVR.", "C", "Multiple"),

    # ---- ERP, finance & HR -------------------------------------------------
    "SAP S/4HANA": ("sap", "Finance core, delivered under the internal Unifier programme. Recognised in the SAP Innovation Awards.", "A", "SAP"),
    "SAP Ariba": ("sap", "Source-to-pay, supplier management and contract compliance.", "A", "SAP"),
    "SAP Analytics Cloud": ("sap", "Planning, budgeting and management reporting on the S/4HANA finance core.", "B", "SAP"),
    "Revenue Accounting System": ("sap", "Passenger revenue accounting, proration, interline billing and BSP reconciliation.", "C", "Multiple"),
    "Dayforce": ("hcm", "Time, attendance, scheduling and payroll. Complex union rule sets across four bargaining units.", "B", "Dayforce"),
    "Phenom": ("hcm", "Talent acquisition and candidate relationship management.", "B", "Phenom"),

    # ---- Data, cloud, integration & IT -------------------------------------
    "AWS": ("aws", "Primary hyperscaler. Loyalty platform, contact centre and digital channels run cloud-native on AWS.", "A", "AWS"),
    "Databricks Lakehouse": ("databricks", "Enterprise lakehouse. Target grounding surface for analytics and AI; replacing legacy Cloudera.", "B", "Databricks"),
    "Cloudera": ("databricks", "Legacy Hadoop data platform, being retired in favour of the Databricks lakehouse.", "B", "Cloudera"),
    "Unity Catalog": ("databricks", "Lakehouse governance, lineage and access control. Foundation for governed AI grounding.", "C", "Databricks"),
    "Integration Platform": ("unknown", "API gateway, ESB and event streaming. Product UNCONFIRMED - a top-three discovery question.", "U", "UNKNOWN"),
    "ITSM Platform": ("itsm", "Incident, request, change and CMDB. ServiceNow assumed on market pattern - CONFIRM in discovery.", "C", "UNKNOWN"),
    "Observability Platform": ("itsm", "APM, logging and synthetic monitoring. Product UNCONFIRMED.", "C", "UNKNOWN"),
    "SIEM and SOC": ("unknown", "Security monitoring and incident response tooling. Product UNCONFIRMED - a discovery question.", "U", "UNKNOWN"),
    "Workforce Identity": ("unknown", "Employee SSO, MFA and privileged access. Product UNCONFIRMED. Note: SAP CDC covers customer identity only.", "U", "UNKNOWN"),
    "Microsoft 365": ("m365", "Email, collaboration and document management for approximately 35,000 employees.", "C", "Microsoft"),

    # ---- Alliance, regulator & partner interfaces --------------------------
    "Star Alliance Interline": ("iata", "26-member interline, through-check, baggage and status recognition messaging.", "A", "Star Alliance"),
    "A++ Atlantic Joint Venture": ("iata", "Transatlantic JV with United and Lufthansa Group. Coordinated schedules and revenue share.", "A", "A++ JV"),
    "IATA Type-B Messaging": ("iata", "Legacy airline teletype messaging: PNL, ADL, BSM, LDM, MVT. Still load-bearing across the estate.", "C", "IATA"),
    "CBSA API and PNR": ("regulator", "Advance passenger information and PNR transmission to CBSA, CATSA, US CBP Secure Flight.", "A", "CBSA / CBP"),
    "CTA Complaint Interface": ("regulator", "Canadian Transportation Agency complaint and Air Passenger Protection Regulations adjudication channel.", "A", "CTA"),
    "Jazz and PAL Operator Interface": ("express", "Air Canada Express capacity-purchase operators running their own crew, ops and maintenance systems.", "A", "Jazz / PAL"),
}


# Aliases: shorthand used while authoring maps to the canonical registry key.
ALIASES = {
    "Altea PSS": "Amadeus Altea Reservations",
    "Altea DCS": "Amadeus Altea DCS",
    "Altea Inventory": "Amadeus Altea Inventory",
    "Altea CM": "Amadeus Altea Customer Management",
    "NetLine": "Lufthansa Systems NetLine",
    "Jeppesen": "Jeppesen Crew",
    "Cargospot": "CHAMP Cargospot neo",
    "S/4HANA": "SAP S/4HANA",
    "SAP CDC": "SAP Customer Data Cloud",
    "Salesforce": "Salesforce Service Cloud",
    "Connect": "Amazon Connect",
    "Databricks": "Databricks Lakehouse",
    "WorldTracer": "SITA WorldTracer",
    "PROS RTDP": "PROS Real-Time Dynamic Pricing",
    "PROS RM": "PROS Revenue Management",
}

TIER_LABEL = {
    "A": "Confirmed - vendor or Air Canada public source",
    "B": "Indicated - job postings, technographics or trade press",
    "C": "Industry pattern - NOT evidenced for Air Canada",
    "U": "Unknown - open discovery question",
}


def resolve(name):
    """Return (canonical_name, css_class, tooltip, tier, vendor) for a system name."""
    key = ALIASES.get(name, name)
    if key in SYSTEMS:
        cls, tip, tier, vendor = SYSTEMS[key]
        return key, cls, tip, tier, vendor
    # Unregistered system: render neutrally rather than silently dropping it.
    return name, "generic", "System not in the Air Canada registry - verify before use in a bid.", "U", "UNKNOWN"


def all_systems():
    return sorted(SYSTEMS.keys())


if __name__ == "__main__":
    from collections import Counter
    tiers = Counter(v[2] for v in SYSTEMS.values())
    print(f"{len(SYSTEMS)} systems registered")
    for t in "ABCU":
        print(f"  Tier {t}: {tiers[t]:>3}  {TIER_LABEL[t]}")
