# -*- coding: utf-8 -*-
"""
Air Canada process taxonomy.

12 L1 domains -> 48 L2 groups -> 284 L3 processes.
PID format: AC-{L1}-{L2}-{NN}

L2 groups are research-informed: the taxonomy retains the 12-domain shape but
folds in the safety/compliance and data/integration content that a purely
commercial taxonomy misses, and points every group at evidenced systems.
"""

DOMAINS = [
 {"code":"NP","name":"Network Planning & Scheduling","icon":"\U0001F5FA",
  "blurb":"Schedule design, fleet assignment and slot strategy across mainline, Rouge and the Express operators. Built in Lufthansa Systems NetLine and published to the industry through SSIM.",
  "systems":["Lufthansa Systems NetLine","NetLine/Plan","Star Alliance Interline","A++ Atlantic Joint Venture"],
  "l2":[
   {"code":"SP","name":"Schedule Planning & Design","blurb":"Route case through published schedule.","p":[
     "Long-Range Network Strategy and Route Case Development",
     "Seasonal Schedule Build in NetLine Plan",
     "Sixth Freedom Connecting Bank Design at YYZ",
     "Hub Bank Structure Design for YUL and YVR",
     "Schedule Publication and SSIM Distribution",
     "Codeshare and Interline Schedule Alignment",
     "Rouge Leisure Schedule Integration",
     "Schedule Change Management and Passenger Re-protection"]},
   {"code":"FA","name":"Fleet Assignment & Rotation","blurb":"Matching gauge and tail to demand while protecting maintenance opportunity.","p":[
     "Fleet Assignment Optimisation by Demand",
     "Aircraft Rotation and Tail Assignment Build",
     "Maintenance Opportunity Embedding in Rotations",
     "Narrowbody Widebody Gauge Swap Evaluation",
     "A220 Deployment Planning on Thin Transcontinental Routes",
     "Express Operator Capacity Purchase Allocation",
     "Fleet Renewal Impact Modelling",
     "Charter and Jetz Sub-Fleet Scheduling"]},
   {"code":"SL","name":"Slots, Alliance & Codeshare","blurb":"Level 3 slot holdings, Star Alliance and the A++ transatlantic joint venture.","p":[
     "IATA Slot Conference Coordination",
     "Level 3 Airport Slot Application and Retention",
     "Slot Compliance and Use It Or Lose It Monitoring",
     "Star Alliance Schedule Coordination",
     "A Plus Plus Atlantic Joint Venture Schedule Alignment",
     "Codeshare Agreement Onboarding",
     "Bilateral and Regulatory Route Authority Filing"]},
   {"code":"NM","name":"Network Performance & Monitoring","blurb":"Did the schedule earn what the route case promised.","p":[
     "Route Profitability Review and Network Scorecard",
     "Competitor Capacity and Schedule Benchmarking",
     "Load Factor and RASK Variance Analysis",
     "On Time Performance Root Cause Attribution",
     "Connection Bank Integrity Monitoring",
     "Schedule Reliability and Block Time Tuning",
     "Network Post Implementation Review"]}]},

 {"code":"RM","name":"Revenue Management & Pricing","icon":"\U0001F4C8",
  "blurb":"O&D revenue management and continuous pricing on PROS, feeding inventory controls into Amadeus Altea. Fare filing through ATPCO remains the rate-limiting step on pricing agility.",
  "systems":["PROS Real-Time Dynamic Pricing","PROS Revenue Management","Amadeus Altea Inventory","ATPCO"],
  "l2":[
   {"code":"IY","name":"Inventory & Yield Control","blurb":"Forecast, bid price and seat availability.","p":[
     "O and D Demand Forecast Generation",
     "Bid Price and Inventory Control Optimisation",
     "Overbooking and No Show Forecasting",
     "Group Booking Evaluation and Quote",
     "Inventory Feed Reconciliation to Altea",
     "Class Availability Override and Manual Intervention",
     "Award Seat Inventory Allocation for Aeroplan",
     "Interline and Codeshare Inventory Control"]},
   {"code":"PF","name":"Pricing & Fare Filing","blurb":"Fare construction, ATPCO filing and competitive response.","p":[
     "Fare Construction and Filing to ATPCO",
     "Real Time Dynamic Pricing Model Governance",
     "Competitive Fare Response and Match Decision",
     "Promotional Fare Campaign Launch",
     "Corporate and Negotiated Fare Administration",
     "Tax Fee and Surcharge Maintenance",
     "Fare Rule and Penalty Structure Design",
     "Currency and Point of Sale Pricing Management"]},
   {"code":"AN","name":"Ancillary & Merchandising","blurb":"Seats, bags, bundles and buy-ups through Anytime Merchandising.","p":[
     "Seat Selection Product Pricing",
     "Checked Baggage Fee Management",
     "Branded Fare Family Design and Merchandising",
     "Upgrade and Cabin Buy Up Offer Management",
     "Ancillary Bundle Construction in Anytime Merchandising",
     "Third Party Ancillary Partner Management",
     "Ancillary Revenue Performance Tracking"]},
   {"code":"YM","name":"RM Analytics & Performance","blurb":"Analyst cycle, model drift and revenue integrity.","p":[
     "Revenue Management Analyst Daily Review Cycle",
     "Forecast Accuracy and Model Drift Monitoring",
     "Spill and Spoilage Analysis",
     "Revenue Integrity and Fare Abuse Detection",
     "RM System Exception and Alert Handling",
     "Pricing and RM Data Feed to the Lakehouse",
     "Revenue Uplift Attribution and Benefit Tracking"]}]},

 {"code":"AP","name":"Aeroplan Loyalty","icon":"\U0001F341",
  "blurb":"The in-house loyalty engine reacquired from Aimia and relaunched in November 2020, with customer identity consolidated onto SAP Customer Data Cloud and accrual flowing from TD, CIBC and Amex.",
  "systems":["Aeroplan Platform","SAP Customer Data Cloud","Aeroplan Partner Interfaces"],
  "l2":[
   {"code":"EN","name":"Enrolment & Member Identity","blurb":"Identity, consent and profile integrity on SAP CDC.","p":[
     "Member Enrolment and Identity Creation",
     "Consent Capture and Preference Management",
     "Member Profile Consolidation Across Channels",
     "Duplicate Account Detection and Merge",
     "Member Authentication and Account Recovery",
     "Member Data Privacy Request Handling"]},
   {"code":"RE","name":"Redemption","blurb":"Burning points across Air Canada and Star Alliance.","p":[
     "Flight Award Redemption Booking",
     "Dynamic Award Pricing and Availability",
     "Star Alliance Partner Award Redemption",
     "Points Plus Cash Redemption",
     "eUpgrade Redemption and Clearance",
     "Redemption Reversal and Refund"]},
   {"code":"PA","name":"Partner & Co-Brand Accrual","blurb":"Earning points and settling the liability with issuers.","p":[
     "Co Brand Card Accrual Posting",
     "Flight Accrual and Retro Credit Processing",
     "Retail and Hotel Partner Accrual Integration",
     "Partner Settlement and Points Liability Reconciliation",
     "Partner Onboarding and Interface Certification",
     "Accrual Dispute Investigation"]},
   {"code":"TM","name":"Altitude Tier Management","blurb":"Status qualification, benefits and liability valuation.","p":[
     "Altitude Status Qualification Tracking",
     "Status Tier Award and Downgrade Cycle",
     "Elite Benefit Entitlement Provisioning",
     "Status Match and Challenge Administration",
     "Member Segmentation and Campaign Targeting",
     "Points Liability Actuarial Valuation"]}]},

 {"code":"CX","name":"Customer Experience & Channels","icon":"\U0001F4AC",
  "blurb":"Digital channels on AWS, a contact centre on Amazon Connect with Salesforce Service Cloud Voice, and the APPR complaint machine that the Canadian Transportation Agency backlog runs through.",
  "systems":["aircanada.com","Air Canada Mobile App","Amazon Connect","Salesforce Service Cloud","CTA Complaint Interface"],
  "l2":[
   {"code":"DC","name":"Digital Channels","blurb":"aircanada.com and the mobile app, bilingual by regulation.","p":[
     "Online Booking Flow and Shopping Session",
     "Mobile App Check In and Boarding Pass Issue",
     "In App Baggage Tracking Experience",
     "Digital Content Publication with English and French Parity",
     "Digital Personalisation and Offer Targeting",
     "Digital Channel Incident and Degraded Mode"]},
   {"code":"CC","name":"Contact Centre","blurb":"Voice, IVR and assisted service on Amazon Connect.","p":[
     "Inbound Service Call Handling",
     "IVR Routing and Self Service Containment",
     "Virtual Assistant Conversation Handling",
     "Agent Assist Knowledge Grounding",
     "Contact Centre Capacity and Workforce Planning",
     "Secure Payment Capture in the Contact Centre"]},
   {"code":"SS","name":"Special Services & Accessibility","blurb":"ATPDR obligations and assisted travel.","p":[
     "Mobility Aid Handling and Tracking",
     "Accessible Travel Request under ATPDR",
     "Unaccompanied Minor Handling",
     "Special Meal and Medical Clearance",
     "Service Animal Acceptance",
     "Group and Event Travel Servicing"]},
   {"code":"CR","name":"Complaints, APPR & Claims","blurb":"Entitlement determination against the Air Passenger Protection Regulations.","p":[
     "APPR Complaint Intake and Triage",
     "APPR Entitlement Determination and Compensation",
     "CTA Escalation and Regulatory Response",
     "Third Party Arbitration Case Handling",
     "Baggage Claim and Compensation Settlement",
     "Goodwill Gesture and Customer Recovery"]}]},

 {"code":"FO","name":"Flight Operations & Dispatch","icon":"✈",
  "blurb":"Dispatch and operations control from the YYZ operations centre. NetLine Ops and Jeppesen carry flight watch and recovery; the June 2023 communicator outage is the resilience reference point.",
  "systems":["NetLine/Ops","Jeppesen OCC","NAV CANADA","ACARS Datalink","Amadeus Passenger Recovery"],
  "l2":[
   {"code":"FD","name":"Flight Planning & Dispatch","blurb":"Operational flight plan through dispatch release.","p":[
     "Operational Flight Plan Construction",
     "Fuel Policy Application and Tankering Decision",
     "ETOPS and Oceanic Route Planning",
     "Dispatch Release and Joint Responsibility Sign Off",
     "Payload and Weight Balance Load Planning",
     "Flight Plan Filing to NAV CANADA"]},
   {"code":"WX","name":"Weather, NOTAM & Nav Data","blurb":"Briefing packages, NOTAM screening and winter operations.","p":[
     "Weather Briefing Package Assembly",
     "NOTAM Review and Applicability Screening",
     "Navigation Database Cycle Update",
     "Volcanic Ash and Space Weather Response",
     "Winter Operations De Icing Coordination",
     "Runway Condition and Performance Assessment"]},
   {"code":"OC","name":"Ops Control & IRROP Recovery","blurb":"Flight watch, disruption recovery and the Express operator seam.","p":[
     "Flight Watch and Day of Operation Monitoring",
     "Irregular Operations Declaration and Recovery Plan",
     "Aircraft Swap and Rotation Recovery",
     "Diversion Management and Handling",
     "Express Operator Disruption Reconciliation",
     "Ground Stop and System Outage Fallback Operation"]},
   {"code":"SR","name":"Safety & Occurrence Reporting","blurb":"SMS, mandatory reporting and IOSA evidence.","p":[
     "Safety Occurrence Reporting and Capture",
     "Hazard Identification and Risk Assessment",
     "Mandatory Occurrence Reporting to Transport Canada",
     "Flight Data Monitoring and Analysis",
     "Fatigue Risk Management Review",
     "IOSA Audit Preparation and Evidence"]}]},

 {"code":"CM","name":"Crew Management","icon":"\U0001F468‍✈",
  "blurb":"Pairing, rostering and day-of-operations crew tracking in Jeppesen, against four collective agreements and Canadian Aviation Regulations flight and duty time limits.",
  "systems":["Jeppesen Crew","Dayforce","Lufthansa Systems NetLine"],
  "l2":[
   {"code":"CP","name":"Crew Planning & Pairing","blurb":"Establishment, pairing optimisation and reserve sizing.","p":[
     "Crew Demand Forecasting and Establishment Planning",
     "Pairing Optimisation Build in Jeppesen",
     "Reserve Coverage and Standby Sizing",
     "Crew Base Assignment and Transfer",
     "Collective Agreement Rule Configuration",
     "Training Footprint Integration into the Crew Plan"]},
   {"code":"CR","name":"Rostering & Bidding","blurb":"Monthly bid cycle through published roster.","p":[
     "Monthly Bid Package Publication",
     "Preferential Bidding and Roster Award",
     "Vacation and Leave Bidding",
     "Roster Adjustment and Trip Trade",
     "Open Time and Premium Pickup Assignment",
     "Roster Publication and Crew Notification"]},
   {"code":"DO","name":"Day-of-Operations Crew Tracking","blurb":"Sign-on, legality and disruption reassignment.","p":[
     "Crew Check In and Sign On Tracking",
     "Crew Legality and Flight Duty Time Verification",
     "Crew Reassignment During Disruption",
     "Reserve Call Out and Assignment",
     "Crew Hotel and Transport Coordination",
     "Crew Positioning and Deadhead Booking"]},
   {"code":"CC","name":"Crew Compliance, Training & Pay","blurb":"Currency, recurrent training, pay and grievances.","p":[
     "Licence Medical and Qualification Currency Tracking",
     "Recurrent Training Scheduling and Compliance",
     "Crew Pay Calculation and Credit Reconciliation",
     "Collective Agreement Grievance Handling",
     "Fatigue Report Intake and Disposition",
     "Crew Records and Regulatory Audit Evidence"]}]},

 {"code":"GO","name":"Ground Operations & Airports","icon":"\U0001F6EB",
  "blurb":"Check-in, boarding, baggage and turnaround on Amadeus Altea DCS across the YYZ, YUL, YVR and YYC hubs, with SITA WorldTracer carrying mishandled bag tracing.",
  "systems":["Amadeus Altea DCS","SITA WorldTracer","Baggage Reconciliation System","CUPPS"],
  "l2":[
   {"code":"CI","name":"Check-In, DCS & Boarding","blurb":"Acceptance through boarding, including degraded mode.","p":[
     "Airport Check In and Bag Acceptance",
     "Kiosk and Mobile Self Service Check In",
     "Advance Passenger Information Transmission",
     "Boarding Gate Control and Sequencing",
     "Denied Boarding and Oversale Management",
     "DCS Degraded Mode and Manual Fallback"]},
   {"code":"BA","name":"Baggage","blurb":"Acceptance, reconciliation, tracing and repatriation.","p":[
     "Baggage Acceptance and Tag Issue",
     "Baggage Sortation and Load Reconciliation",
     "Transfer Baggage Handling at YYZ",
     "Mishandled Baggage Tracing and PIR Creation",
     "Baggage Delivery and Repatriation",
     "Baggage Performance and Resolution 753 Reporting"]},
   {"code":"GT","name":"Gate, Turnaround & Resource","blurb":"The turn: stand, fuel, catering and off-block.","p":[
     "Turnaround Plan and Gate Assignment",
     "Aircraft Ground Handling Sequence",
     "Fuelling Coordination and Uplift Confirmation",
     "Cabin Servicing and Catering Uplift",
     "Pushback Clearance and Off Block Reporting",
     "Ground Handler Performance Management"]},
   {"code":"VH","name":"Premium, Lounge & VIP Handling","blurb":"Maple Leaf Lounge, Super Elite and Star Gold recognition.","p":[
     "Maple Leaf Lounge Access Control",
     "Premium Cabin Ground Experience",
     "Super Elite and VIP Handling",
     "Star Alliance Gold Recognition at Airport",
     "Priority Baggage and Fast Track Delivery",
     "Ground Product Service Recovery"]}]},

 {"code":"MR","name":"Maintenance & Engineering","icon":"\U0001F527",
  "blurb":"Air Canada Technical Services running line and base maintenance on TRAX, against Transport Canada continuing-airworthiness obligations under the Canadian Aviation Regulations.",
  "systems":["TRAX","TRAX eMobility","Transport Canada CAWIS","Aeroxchange"],
  "l2":[
   {"code":"LM","name":"Line Maintenance","blurb":"Turnaround defects, MEL deferrals and AOG recovery.","p":[
     "Line Maintenance Work Order Execution",
     "Defect Reporting and Technical Log Entry",
     "Minimum Equipment List Deferral Management",
     "AOG Response and Recovery",
     "Transit and Daily Check Execution",
     "Line Station Support and Contract Maintenance"]},
   {"code":"HM","name":"Heavy & Base Maintenance","blurb":"Check planning, work packages and return to service.","p":[
     "Heavy Check Planning and Slot Booking",
     "Base Maintenance Work Package Build",
     "Third Party MRO Vendor Management",
     "Component Removal and Shop Visit Routing",
     "Cabin Reconfiguration and Modification",
     "Return to Service and Check Closure"]},
   {"code":"EN","name":"Engineering & Reliability","blurb":"Modifications, airworthiness directives and predictive maintenance.","p":[
     "Engineering Order and Modification Design",
     "Airworthiness Directive Assessment and Embodiment",
     "Service Bulletin Evaluation",
     "Reliability Monitoring and Trend Analysis",
     "Predictive Maintenance Model Deployment",
     "Technical Publication and Manual Revision Control"]},
   {"code":"QA","name":"Airworthiness, Records & Quality","blurb":"Technical records, parts provisioning and regulator audit.","p":[
     "Aircraft Technical Records Management",
     "Continuing Airworthiness Compliance Review",
     "Parts Provisioning and Inventory Planning",
     "Supplier Quality and Spec 2000 Ordering",
     "Maintenance Audit and Finding Closure",
     "Certification and Approval Maintenance with Transport Canada"]}]},

 {"code":"CG","name":"Air Canada Cargo","icon":"\U0001F4E6",
  "blurb":"Freighter and belly cargo, mid-implementation on CHAMP Cargospot neo, with mandatory CBSA pre-load air cargo targeting filing in force since April 2025.",
  "systems":["CHAMP Cargospot neo","Cargospot neo Handling","Canada PACT","Cargospot neo Revenue Accounting"],
  "l2":[
   {"code":"BK","name":"Capacity & Booking","blurb":"Selling belly and freighter capacity.","p":[
     "Cargo Capacity Forecast and Allocation",
     "Air Waybill Booking and Rate Quotation",
     "Freighter Network Capacity Management",
     "Special Cargo Acceptance and Booking",
     "Cargo Charter and Block Space Agreement"]},
   {"code":"GH","name":"Ground Handling & ULD","blurb":"Warehouse receipt through proof of delivery.","p":[
     "Cargo Acceptance and Warehouse Receipt",
     "ULD Build Up and Load Planning",
     "Cold Chain and Pharma Handling",
     "Cargo Transfer and Interline Handover",
     "Cargo Delivery and Proof of Delivery"]},
   {"code":"CS","name":"Customs, PACT & Dangerous Goods","blurb":"Pre-load filing, customs and DG compliance.","p":[
     "Canada PACT Pre Load Data Filing",
     "Export and Import Customs Declaration",
     "Dangerous Goods Acceptance and Documentation",
     "Restricted and Embargoed Goods Screening",
     "Cargo Security Screening Compliance"]},
   {"code":"CP","name":"Cargo Revenue & Performance","blurb":"Settlement, yield, claims and the Cargospot cutover.","p":[
     "Cargo Revenue Accounting and CASS Settlement",
     "Cargo Yield and Capacity Utilisation Review",
     "Cargo Claims and Damage Settlement",
     "Cargospot neo Migration Cutover Control",
     "Cargo Partner and GSA Performance Review"]}]},

 {"code":"IT","name":"Information Technology & Security","icon":"\U0001F5A5",
  "blurb":"Service management, cybersecurity, data engineering and AI platform. This is the application management and user support tower, and the domain the Moffatt ruling made a governance question.",
  "systems":["ITSM Platform","Databricks Lakehouse","AWS","Integration Platform","SIEM and SOC"],
  "l2":[
   {"code":"SM","name":"Service Management & User Support","blurb":"Incident, request, change and service level governance.","p":[
     "Incident Management and Major Incident Command",
     "Service Request and End User Support",
     "Change and Release Management",
     "Configuration Management and CMDB Assurance",
     "Service Level Management and Vendor Governance"]},
   {"code":"CS","name":"Cybersecurity & Identity","blurb":"Access lifecycle, detection and response.","p":[
     "Identity and Access Lifecycle Management",
     "Privileged Access and Credential Control",
     "Security Monitoring and Threat Detection",
     "Vulnerability Management and Patch Assurance",
     "Security Incident Response and Forensics"]},
   {"code":"DE","name":"Data Engineering & Integration","blurb":"Lakehouse ingestion, APIs and the Type-B gateway.","p":[
     "Source System Ingestion to the Lakehouse",
     "Interface Design and API Lifecycle Management",
     "Type B and EDIFACT Message Gateway Operations",
     "Data Quality Monitoring and Remediation",
     "Cloudera to Databricks Migration Execution"]},
   {"code":"AI","name":"AI & ML Platform","blurb":"Use case intake through governed production models.","p":[
     "AI Use Case Intake and Value Assessment",
     "Model Development and Feature Engineering",
     "AI Governance and Human In Loop Control Design",
     "Model Deployment and Production Monitoring",
     "Customer Facing Assistant Content Grounding"]}]},

 {"code":"FN","name":"Finance, Procurement & Treasury","icon":"\U0001F4B0",
  "blurb":"SAP S/4HANA finance core delivered under the internal Unifier programme, with SAP Ariba source-to-pay and passenger revenue accounting reconciling to IATA BSP.",
  "systems":["SAP S/4HANA","SAP Ariba","SAP Analytics Cloud","IATA BSP","Revenue Accounting System"],
  "l2":[
   {"code":"RA","name":"Revenue Accounting","blurb":"Recognition, proration, interline billing and audit.","p":[
     "Passenger Revenue Recognition and Proration",
     "Interline Billing and Settlement",
     "BSP and ARC Sales Reconciliation",
     "Unearned Revenue and Air Traffic Liability",
     "Revenue Audit and Leakage Recovery"]},
   {"code":"AP","name":"Procure-to-Pay","blurb":"Requisition through payment on SAP Ariba and S/4HANA.","p":[
     "Purchase Requisition and Approval",
     "Supplier Onboarding and Master Data",
     "Invoice Processing and Three Way Match",
     "Payment Run and Disbursement",
     "Contract Compliance and Spend Analytics"]},
   {"code":"TR","name":"Treasury & Risk","blurb":"Liquidity, FX, fuel hedging and aircraft financing.","p":[
     "Cash Positioning and Liquidity Management",
     "Foreign Exchange Exposure Management",
     "Fuel Hedging Programme Administration",
     "Aircraft Financing and Lease Accounting",
     "Card Acquiring and Payment Settlement"]},
   {"code":"FP","name":"Planning & Analysis","blurb":"Budget, forecast, board reporting and capital appraisal.","p":[
     "Annual Budget and Operating Plan Build",
     "Monthly Forecast and Reforecast Cycle",
     "Management Reporting and Board Pack",
     "Capital Investment Appraisal and Approval",
     "Cost Transformation Benefit Tracking"]}]},

 {"code":"HR","name":"Human Resources & Labour","icon":"\U0001F465",
  "blurb":"Approximately 35,000 employees across four bargaining units, with Dayforce carrying time, attendance and payroll under some of the most complex union rule sets in Canadian aviation.",
  "systems":["Dayforce","Phenom","Microsoft 365","SAP S/4HANA"],
  "l2":[
   {"code":"TA","name":"Talent Acquisition","blurb":"Requisition through first day.","p":[
     "Workforce Demand and Requisition Approval",
     "Candidate Sourcing and Screening",
     "Interview Selection and Offer Management",
     "Pre Employment Clearance and Security Vetting",
     "Onboarding and First Day Enablement"]},
   {"code":"WM","name":"Workforce Management & Payroll","blurb":"Rostering, attendance and union-rule payroll.","p":[
     "Shift Rostering for Airport and Contact Centre Staff",
     "Time and Attendance Capture",
     "Payroll Processing and Union Rule Application",
     "Absence Leave and Return to Work Management",
     "Overtime and Premium Pay Control"]},
   {"code":"LR","name":"Labour Relations","blurb":"Bargaining, grievance and labour cost modelling.","p":[
     "Collective Bargaining Preparation and Mandate",
     "Grievance and Arbitration Case Management",
     "Union Consultation and Change Notification",
     "Discipline and Performance Management",
     "Labour Cost Modelling and Scenario Analysis"]},
   {"code":"DE","name":"Engagement, Learning & Inclusion","blurb":"Engagement, learning, official languages and succession.","p":[
     "Employee Engagement Survey and Action Planning",
     "Diversity Equity and Inclusion Programme Delivery",
     "Learning Curriculum Design and Delivery",
     "Official Languages Compliance in the Workplace",
     "Talent Review and Succession Planning"]}]},
]


def slugify(text):
    import re
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def all_processes():
    """Yield a flat, ordered list of process dicts with fully-formed PIDs."""
    out = []
    for d in DOMAINS:
        for g in d["l2"]:
            for i, name in enumerate(g["p"], 1):
                out.append({
                    "pid": f"AC-{d['code']}-{g['code']}-{i:02d}",
                    "l1_code": d["code"], "l1_name": d["name"], "l1_slug": slugify(d["name"]),
                    "l2_code": g["code"], "l2_name": g["name"], "l2_slug": slugify(g["name"]),
                    "l3_name": name, "l3_slug": slugify(name),
                    "domain_systems": d["systems"],
                })
    return out


if __name__ == "__main__":
    procs = all_processes()
    print(f"{len(DOMAINS)} L1 domains")
    print(f"{sum(len(d['l2']) for d in DOMAINS)} L2 groups")
    print(f"{len(procs)} L3 processes\n")
    for d in DOMAINS:
        n = sum(len(g["p"]) for g in d["l2"])
        print(f"  {d['code']}  {d['name']:<38} {len(d['l2'])} groups  {n:>3} processes")
    pids = [p["pid"] for p in procs]
    assert len(pids) == len(set(pids)), "DUPLICATE PIDs"
    print("\nPID uniqueness: OK")
    print("Sample:", ", ".join(pids[:3]), "...", pids[-1])
