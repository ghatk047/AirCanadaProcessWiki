# -*- coding: utf-8 -*-
"""
Enterprise architecture diagrams -> data/ea.json

Two kinds:
  * 12 domain landscapes  -- layered system views, one per L1 domain
  * 16 cross-domain flows -- how systems actually connect end to end

Both use `flowchart LR` with subgraphs as columns. Cross-subgraph edges are the
whole point of an EA view, and those edges make mermaid discard any `direction`
set inside a subgraph -- so layers are columns and nodes stack within them.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from sanitise_mmd import sanitise_mermaid, validate
import ac_systems

INIT = "%%{init: {'theme':'base','themeVariables':{'fontSize':'14px'}}}%%"


def nid(name):
    s = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")
    return "X" + s[:38]


def lbl(text, limit=40):
    t = re.sub(r"[()&<>\[\]{}|\"']", "", str(text))
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= limit else t[:limit].rsplit(" ", 1)[0] + "..."


def diagram(columns, edges, gaps=()):
    """
    columns: [(column title, [node labels])]
    edges:   [(from label, to label, edge label or "")]
    gaps:    node labels to style as unknown/discovery items
    """
    lines = [INIT, "flowchart LR"]
    for i, (title, nodes) in enumerate(columns, 1):
        lines.append(f"subgraph C{i} [{lbl(title, 44)}]")
        for n in nodes:
            lines.append(f"{nid(n)}[{lbl(n)}]")
        lines.append("end")
    for a, b, l in edges:
        if l:
            lines.append(f"{nid(a)} -->|{lbl(l, 30)}| {nid(b)}")
        else:
            lines.append(f"{nid(a)} --> {nid(b)}")
    for i in range(1, len(columns) + 1):
        lines.append(f"style C{i} fill:#FFF0F2,stroke:#D2001F,stroke-width:2px")
    lines.append("classDef sys fill:#FFFFFF,stroke:#1A1A1A,stroke-width:1px,color:#1A1A1A")
    lines.append("classDef gap fill:#1A1A1A,stroke:#D2001F,stroke-width:2px,color:#FFFFFF")
    allnodes = [n for _, ns in columns for n in ns]
    normal = [n for n in allnodes if n not in gaps]
    if normal:
        lines.append("class " + ",".join(nid(n) for n in normal) + " sys")
    if gaps:
        lines.append("class " + ",".join(nid(n) for n in gaps) + " gap")
    mmd = sanitise_mermaid("\n".join(lines), font_size="14px")
    problems = validate(mmd)
    assert not problems, problems
    return mmd


DIAGRAMS = []


def add(did, slug, title, kind, blurb, columns, edges, systems, notes, gaps=()):
    DIAGRAMS.append({
        "id": did, "slug": slug, "title": title, "kind": kind, "blurb": blurb,
        "systems": systems, "notes": notes,
        "mermaid": diagram(columns, edges, gaps),
    })


# ══════════════════════════════════════════════ 12 DOMAIN LANDSCAPES
add("AC-EA-NP", "ac-np-landscape", "Network Planning and Scheduling Landscape",
    "Domain landscape",
    "How a route case becomes a published schedule, and where slot and alliance obligations constrain it.",
    [("Demand and market inputs", ["Market demand data", "OAG competitor schedules", "Databricks Lakehouse"]),
     ("Planning core", ["NetLine/Plan", "Lufthansa Systems NetLine"]),
     ("Commercial coupling", ["Amadeus Altea Inventory", "PROS Revenue Management"]),
     ("Publication and coordination", ["IATA Type-B Messaging", "Star Alliance Interline",
                                       "A++ Atlantic Joint Venture", "Sabre GDS"])],
    [("Market demand data", "NetLine/Plan", "forecast"),
     ("OAG competitor schedules", "NetLine/Plan", "benchmark"),
     ("Databricks Lakehouse", "NetLine/Plan", "route performance"),
     ("NetLine/Plan", "Lufthansa Systems NetLine", "schedule build"),
     ("Lufthansa Systems NetLine", "Amadeus Altea Inventory", "SSIM schedule"),
     ("Amadeus Altea Inventory", "PROS Revenue Management", "inventory position"),
     ("Lufthansa Systems NetLine", "IATA Type-B Messaging", "schedule change"),
     ("Lufthansa Systems NetLine", "Star Alliance Interline", "codeshare"),
     ("Lufthansa Systems NetLine", "A++ Atlantic Joint Venture", "JV coordination"),
     ("IATA Type-B Messaging", "Sabre GDS", "distribution")],
    ["Lufthansa Systems NetLine", "NetLine/Plan", "Amadeus Altea Inventory",
     "PROS Revenue Management", "Star Alliance Interline", "A++ Atlantic Joint Venture"],
    ["Schedule is the master input to almost every downstream domain: inventory, crew, maintenance "
     "opportunity and airport resource all derive from it.",
     "The A++ transatlantic joint venture and Star Alliance codeshares constrain schedule freedom before "
     "commercial optimisation begins.",
     "Slot holdings at Level 3 airports are a use-it-or-lose-it asset and are governed outside the "
     "planning system itself."])

add("AC-EA-RM", "ac-rm-landscape", "Revenue Management and Pricing Landscape",
    "Domain landscape",
    "PROS drives price and inventory controls into Amadeus Altea, while ATPCO filing remains the "
    "rate-limiting step on pricing agility.",
    [("Demand signal", ["Databricks Lakehouse", "Amadeus Altea Reservations"]),
     ("Optimisation", ["PROS Real-Time Dynamic Pricing", "PROS Revenue Management"]),
     ("Inventory and fare control", ["Amadeus Altea Inventory", "ATPCO"]),
     ("Distribution", ["Amadeus Altea NDC", "Amadeus Anytime Merchandising", "Sabre GDS", "aircanada.com"])],
    [("Amadeus Altea Reservations", "PROS Real-Time Dynamic Pricing", "booking signal"),
     ("Databricks Lakehouse", "PROS Revenue Management", "demand history"),
     ("PROS Revenue Management", "Amadeus Altea Inventory", "bid price"),
     ("PROS Real-Time Dynamic Pricing", "Amadeus Altea Inventory", "dynamic offer"),
     ("ATPCO", "Amadeus Altea Inventory", "filed fares"),
     ("Amadeus Altea Inventory", "Amadeus Altea NDC", "availability"),
     ("Amadeus Altea Inventory", "Sabre GDS", "availability"),
     ("Amadeus Altea NDC", "aircanada.com", "offer"),
     ("Amadeus Anytime Merchandising", "aircanada.com", "ancillary offer")],
    ["PROS Real-Time Dynamic Pricing", "PROS Revenue Management", "Amadeus Altea Inventory",
     "ATPCO", "Amadeus Altea NDC", "Amadeus Anytime Merchandising"],
    ["Air Canada is a long-tenured PROS account; dynamic pricing is strategic rather than experimental.",
     "ATPCO filing latency is the practical ceiling on how fast a price change can reach every channel.",
     "NDC gives an offer-and-order path that the legacy GDS route does not, which is where merchandising "
     "differentiation now lives."])

add("AC-EA-AP", "ac-ap-landscape", "Aeroplan Loyalty Landscape",
    "Domain landscape",
    "The in-house loyalty engine relaunched in 2020, with identity on SAP Customer Data Cloud and accrual "
    "flowing from the co-brand card issuers.",
    [("Member channels", ["Air Canada Mobile App", "aircanada.com"]),
     ("Identity and consent", ["SAP Customer Data Cloud"]),
     ("Loyalty core", ["Aeroplan Platform"]),
     ("Partners and finance", ["Aeroplan Partner Interfaces", "Amadeus Altea Reservations", "SAP S/4HANA"])],
    [("Air Canada Mobile App", "SAP Customer Data Cloud", "authenticate"),
     ("aircanada.com", "SAP Customer Data Cloud", "authenticate"),
     ("SAP Customer Data Cloud", "Aeroplan Platform", "member identity"),
     ("Aeroplan Partner Interfaces", "Aeroplan Platform", "accrual file"),
     ("Aeroplan Platform", "Amadeus Altea Reservations", "award booking"),
     ("Amadeus Altea Reservations", "Aeroplan Platform", "flight accrual"),
     ("Aeroplan Platform", "SAP S/4HANA", "points liability")],
    ["Aeroplan Platform", "SAP Customer Data Cloud", "Aeroplan Partner Interfaces",
     "Amadeus Altea Reservations", "SAP S/4HANA"],
    ["Identity quality on SAP Customer Data Cloud is the upstream determinant of accrual exception volume.",
     "The points liability is a material balance-sheet item, so the loyalty ledger and the finance ledger "
     "must reconcile rather than merely agree in aggregate.",
     "Co-brand issuers TD, CIBC and Amex each send a different file on a different schedule."])

add("AC-EA-CX", "ac-cx-landscape", "Customer Experience and Channels Landscape",
    "Domain landscape",
    "Digital channels and the contact centre on AWS, feeding the case machine that carries APPR exposure.",
    [("Customer touchpoints", ["aircanada.com", "Air Canada Mobile App", "Air Canada Virtual Assistant"]),
     ("Contact centre", ["Amazon Connect", "Salesforce Service Cloud"]),
     ("Servicing core", ["Amadeus Altea Customer Management", "Amadeus Passenger Recovery"]),
     ("Regulatory", ["CTA Complaint Interface", "SAP S/4HANA"])],
    [("aircanada.com", "Amadeus Altea Customer Management", "booking servicing"),
     ("Air Canada Mobile App", "Amadeus Altea Customer Management", "self service"),
     ("Air Canada Virtual Assistant", "Salesforce Service Cloud", "escalation"),
     ("Amazon Connect", "Salesforce Service Cloud", "voice to case"),
     ("Amadeus Altea Customer Management", "Salesforce Service Cloud", "case context"),
     ("Amadeus Passenger Recovery", "Salesforce Service Cloud", "disruption record"),
     ("Salesforce Service Cloud", "CTA Complaint Interface", "regulatory response"),
     ("Salesforce Service Cloud", "SAP S/4HANA", "compensation payment")],
    ["Amazon Connect", "Salesforce Service Cloud", "Amadeus Altea Customer Management",
     "CTA Complaint Interface", "Air Canada Virtual Assistant", "aircanada.com"],
    ["Salesforce Service Cloud is the system of record for customer cases and therefore for APPR "
     "entitlement determinations.",
     "The virtual assistant sits inside the liability perimeter established by Moffatt v. Air Canada: "
     "whatever it states, the airline owns.",
     "Every channel in this landscape carries an Official Languages obligation for English and French parity."])

add("AC-EA-FO", "ac-fo-landscape", "Flight Operations and Dispatch Landscape",
    "Domain landscape",
    "Dispatch and operations control from the Toronto operations centre, including the Express operator seam.",
    [("Planning inputs", ["Lufthansa Systems NetLine", "NAV CANADA"]),
     ("Dispatch", ["Jeppesen Charts", "Weight and Balance System", "Electronic Flight Bag"]),
     ("Operations control", ["NetLine/Ops", "Jeppesen OCC"]),
     ("Execution and recovery", ["ACARS Datalink", "Amadeus Altea DCS",
                                 "Amadeus Passenger Recovery", "Jazz and PAL Operator Interface"])],
    [("Lufthansa Systems NetLine", "NetLine/Ops", "planned schedule"),
     ("NAV CANADA", "NetLine/Ops", "NOTAM and flight data"),
     ("Jeppesen Charts", "Electronic Flight Bag", "charts"),
     ("Weight and Balance System", "Electronic Flight Bag", "loadsheet"),
     ("NetLine/Ops", "Jeppesen OCC", "recovery decision"),
     ("Jeppesen OCC", "ACARS Datalink", "crew and ops message"),
     ("NetLine/Ops", "Amadeus Altea DCS", "flight status"),
     ("NetLine/Ops", "Amadeus Passenger Recovery", "disruption trigger"),
     ("Jazz and PAL Operator Interface", "NetLine/Ops", "manual reconciliation")],
    ["NetLine/Ops", "Jeppesen OCC", "NAV CANADA", "ACARS Datalink",
     "Amadeus Passenger Recovery", "Jazz and PAL Operator Interface"],
    ["The Express operator link into ops control is reconciled manually today. It is the highest-value "
     "integration seam in the estate.",
     "The June 2023 communicator outage delayed or cancelled the large majority of a day's flights and is "
     "the reference point for degraded-mode design.",
     "Delay reason codes originate here and become regulatory evidence downstream in APPR adjudication."])

add("AC-EA-CM", "ac-cm-landscape", "Crew Management Landscape",
    "Domain landscape",
    "Pairing through pay on Jeppesen, against four collective agreements and Canadian flight and duty limits.",
    [("Demand", ["Lufthansa Systems NetLine"]),
     ("Crew planning", ["Jeppesen Crew"]),
     ("Day of operations", ["Jeppesen OCC", "ACARS Datalink"]),
     ("Compliance and pay", ["Dayforce", "SAP S/4HANA"])],
    [("Lufthansa Systems NetLine", "Jeppesen Crew", "published schedule"),
     ("Jeppesen Crew", "Jeppesen OCC", "published roster"),
     ("Jeppesen OCC", "ACARS Datalink", "crew notification"),
     ("Jeppesen OCC", "Jeppesen Crew", "day of ops changes"),
     ("Jeppesen Crew", "Dayforce", "credit and duty record"),
     ("Dayforce", "SAP S/4HANA", "payroll posting")],
    ["Jeppesen Crew", "Jeppesen OCC", "Dayforce", "Lufthansa Systems NetLine", "SAP S/4HANA"],
    ["Four bargaining units mean four distinct rule sets encoded in pairing, rostering and pay.",
     "Flight and duty time limits under the Canadian Aviation Regulations are a hard operational "
     "constraint on recovery options, not a preference.",
     "Crew legality is the binding constraint in most irregular operations recovery decisions."])

add("AC-EA-GO", "ac-go-landscape", "Ground Operations and Airports Landscape",
    "Domain landscape",
    "Check-in through off-block on Amadeus Altea DCS across the hubs, with baggage tracing on SITA WorldTracer.",
    [("Passenger channels", ["Air Canada Mobile App", "CUPPS"]),
     ("Departure control", ["Amadeus Altea DCS"]),
     ("Baggage", ["Baggage Reconciliation System", "SITA WorldTracer"]),
     ("Turnaround and reporting", ["Airport Resource Management", "Weight and Balance System",
                                   "CBSA API and PNR", "IATA Type-B Messaging"])],
    [("Air Canada Mobile App", "Amadeus Altea DCS", "mobile check in"),
     ("CUPPS", "Amadeus Altea DCS", "common use check in"),
     ("Amadeus Altea DCS", "Baggage Reconciliation System", "bag message"),
     ("Baggage Reconciliation System", "SITA WorldTracer", "mishandled bag"),
     ("Amadeus Altea DCS", "CBSA API and PNR", "advance passenger info"),
     ("Amadeus Altea DCS", "Weight and Balance System", "passenger load"),
     ("Amadeus Altea DCS", "IATA Type-B Messaging", "PNL and ADL"),
     ("Airport Resource Management", "Amadeus Altea DCS", "gate and stand")],
    ["Amadeus Altea DCS", "SITA WorldTracer", "Baggage Reconciliation System",
     "CBSA API and PNR", "IATA Type-B Messaging"],
    ["A February 2023 outage took out departure control at Toronto, so manual fallback is a real "
     "operating mode rather than a theoretical one.",
     "Bag-to-passenger matching under IATA Resolution 753 depends on Type-B messaging that predates "
     "every other integration pattern in the estate.",
     "Mishandled-bag claim details are re-entered between WorldTracer and the compensation process."])

add("AC-EA-MR", "ac-mr-landscape", "Maintenance and Engineering Landscape",
    "Domain landscape",
    "Air Canada Technical Services on TRAX, against Transport Canada continuing-airworthiness obligations.",
    [("Maintenance demand", ["Lufthansa Systems NetLine", "ACARS Datalink"]),
     ("M and E core", ["TRAX"]),
     ("Execution", ["TRAX eMobility"]),
     ("Supply and regulator", ["Aeroxchange", "Transport Canada CAWIS", "SAP S/4HANA"])],
    [("Lufthansa Systems NetLine", "TRAX", "maintenance opportunity"),
     ("ACARS Datalink", "TRAX", "fault downlink"),
     ("TRAX", "TRAX eMobility", "task card"),
     ("TRAX eMobility", "TRAX", "findings and parts"),
     ("TRAX", "Aeroxchange", "parts order"),
     ("TRAX", "Transport Canada CAWIS", "airworthiness compliance"),
     ("TRAX", "SAP S/4HANA", "cost and inventory")],
    ["TRAX", "TRAX eMobility", "Aeroxchange", "Transport Canada CAWIS", "SAP S/4HANA"],
    ["TRAX is the maintenance and engineering core. It is not AMOS, Ramco or Maintenix, and naming one of "
     "those is a credibility failure in front of Technical Services.",
     "Maintenance opportunity is set upstream in the rotation build, so a late work order consumes buffer "
     "the network plan already spent.",
     "Usability of the maintenance record at the aircraft is the practical constraint on turnaround time."])

add("AC-EA-CG", "ac-cg-landscape", "Air Canada Cargo Landscape",
    "Domain landscape",
    "Cargo mid-migration onto CHAMP Cargospot neo, with mandatory CBSA pre-load filing since April 2025.",
    [("Booking channels", ["CHAMP Cargospot neo"]),
     ("Handling", ["Cargospot neo Handling", "Cargospot Mobile", "OnAsset Vision"]),
     ("Capacity", ["Lufthansa Systems NetLine", "Amadeus Altea DCS"]),
     ("Compliance and settlement", ["Canada PACT", "Cargospot neo Revenue Accounting", "SAP S/4HANA"])],
    [("CHAMP Cargospot neo", "Cargospot neo Handling", "booking to warehouse"),
     ("Cargospot neo Handling", "Cargospot Mobile", "warehouse execution"),
     ("OnAsset Vision", "Cargospot neo Handling", "condition telemetry"),
     ("Lufthansa Systems NetLine", "CHAMP Cargospot neo", "belly capacity"),
     ("CHAMP Cargospot neo", "Canada PACT", "pre-load filing"),
     ("CHAMP Cargospot neo", "Cargospot neo Revenue Accounting", "air waybill"),
     ("Cargospot neo Revenue Accounting", "SAP S/4HANA", "CASS settlement"),
     ("Cargospot neo Handling", "Amadeus Altea DCS", "load to aircraft")],
    ["CHAMP Cargospot neo", "Cargospot neo Handling", "Cargospot neo Revenue Accounting",
     "Canada PACT", "Cargospot Mobile", "OnAsset Vision"],
    ["The migration is in flight, which means a live interim period of double entry between the legacy "
     "platform and Cargospot. That is a time-bounded re-key risk worth solving now.",
     "Pre-load air cargo targeting has no tolerance for interface downtime during a cutover window.",
     "Air Canada Cargo selected CHAMP Cargospot neo. Claiming IBS iCargo is a known-wrong assertion."])

add("AC-EA-IT", "ac-it-landscape", "Information Technology and Security Landscape",
    "Domain landscape",
    "The application management and user support tower, with the four genuine discovery gaps shown in black.",
    [("Service management", ["ITSM Platform", "Observability Platform"]),
     ("Integration", ["Integration Platform", "IATA Type-B Messaging"]),
     ("Data and AI", ["Databricks Lakehouse", "Unity Catalog", "Cloudera", "AWS"]),
     ("Security and identity", ["SIEM and SOC", "Workforce Identity", "SAP Customer Data Cloud"])],
    [("Observability Platform", "ITSM Platform", "event to incident"),
     ("Integration Platform", "ITSM Platform", "interface incident"),
     ("IATA Type-B Messaging", "Integration Platform", "airline messaging"),
     ("Integration Platform", "Databricks Lakehouse", "event stream"),
     ("Cloudera", "Databricks Lakehouse", "migration"),
     ("Databricks Lakehouse", "Unity Catalog", "governance"),
     ("AWS", "Databricks Lakehouse", "platform"),
     ("Workforce Identity", "ITSM Platform", "access request"),
     ("SIEM and SOC", "ITSM Platform", "security incident")],
    ["ITSM Platform", "Integration Platform", "Databricks Lakehouse", "AWS",
     "SIEM and SOC", "Workforce Identity", "Unity Catalog"],
    ["The four black nodes are genuinely unknown from public sources: integration middleware, SIEM and SOC, "
     "workforce identity, and the ITSM product. They are the top clarification asks for any data room.",
     "Every agentic or automation use case depends on read and write access through the integration layer, "
     "which makes it the single most consequential unknown.",
     "The lakehouse migration means the grounding surface for AI is being rebuilt right now."],
    gaps=("Integration Platform", "SIEM and SOC", "Workforce Identity", "ITSM Platform",
          "Observability Platform"))

add("AC-EA-FN", "ac-fn-landscape", "Finance, Procurement and Treasury Landscape",
    "Domain landscape",
    "SAP S/4HANA finance core delivered under the internal Unifier programme, with revenue accounting "
    "reconciling to IATA settlement.",
    [("Revenue sources", ["Amadeus Altea Reservations", "Cargospot neo Revenue Accounting", "Aeroplan Platform"]),
     ("Revenue accounting", ["Revenue Accounting System", "IATA BSP", "ARC"]),
     ("Finance core", ["SAP S/4HANA", "SAP Ariba"]),
     ("Planning", ["SAP Analytics Cloud", "Databricks Lakehouse"])],
    [("Amadeus Altea Reservations", "Revenue Accounting System", "coupon and sales"),
     ("IATA BSP", "Revenue Accounting System", "agency settlement"),
     ("ARC", "Revenue Accounting System", "US agency sales"),
     ("Revenue Accounting System", "SAP S/4HANA", "recognised revenue"),
     ("Cargospot neo Revenue Accounting", "SAP S/4HANA", "cargo revenue"),
     ("Aeroplan Platform", "SAP S/4HANA", "points liability"),
     ("SAP Ariba", "SAP S/4HANA", "source to pay"),
     ("SAP S/4HANA", "SAP Analytics Cloud", "actuals"),
     ("Databricks Lakehouse", "SAP Analytics Cloud", "operational drivers")],
    ["SAP S/4HANA", "SAP Ariba", "SAP Analytics Cloud", "IATA BSP", "Revenue Accounting System"],
    ["Air traffic liability, the value of tickets sold but not yet flown, is the largest single judgement "
     "in the revenue accounting close.",
     "Interline billing crosses the Star Alliance and A++ joint venture boundary and settles on industry "
     "clearing timetables rather than Air Canada's own.",
     "The points liability arriving from Aeroplan depends on breakage assumptions set outside finance."])

add("AC-EA-HR", "ac-hr-landscape", "Human Resources and Labour Landscape",
    "Domain landscape",
    "Roughly 35,000 employees across four bargaining units, with Dayforce carrying union-rule payroll.",
    [("Attraction", ["Phenom"]),
     ("Workforce management", ["Dayforce"]),
     ("Operational demand", ["Jeppesen Crew", "Lufthansa Systems NetLine"]),
     ("Corporate", ["SAP S/4HANA", "Microsoft 365"])],
    [("Phenom", "Dayforce", "new hire"),
     ("Jeppesen Crew", "Dayforce", "crew credit"),
     ("Lufthansa Systems NetLine", "Dayforce", "operational demand"),
     ("Dayforce", "SAP S/4HANA", "payroll posting"),
     ("Dayforce", "Microsoft 365", "provisioning")],
    ["Dayforce", "Phenom", "SAP S/4HANA", "Jeppesen Crew", "Microsoft 365"],
    ["Four bargaining units with materially different rule sets make payroll one of the most complex "
     "configurations in the estate.",
     "Crew pay derives from Jeppesen credit rather than from clock time, so the interface between crew "
     "systems and payroll is a reconciliation, not a feed.",
     "Official Languages obligations apply to the employee experience, not only to the customer channels."])


# ══════════════════════════════════════════════ 16 CROSS-DOMAIN FLOWS
add("AC-X1", "ac-x1-aeroplan-earn-to-burn", "Aeroplan Earn to Burn: Accrual through Redemption",
    "Cross-domain flow",
    "A member earns points on a co-brand card and burns them on an award seat, crossing identity, loyalty, "
    "inventory and finance.",
    [("Earn", ["Aeroplan Partner Interfaces", "Amadeus Altea Reservations"]),
     ("Identity", ["SAP Customer Data Cloud"]),
     ("Ledger", ["Aeroplan Platform"]),
     ("Burn", ["Amadeus Altea Inventory", "Star Alliance Interline"]),
     ("Settle", ["SAP S/4HANA"])],
    [("Aeroplan Partner Interfaces", "SAP Customer Data Cloud", "match member"),
     ("Amadeus Altea Reservations", "Aeroplan Platform", "flight accrual"),
     ("SAP Customer Data Cloud", "Aeroplan Platform", "verified identity"),
     ("Aeroplan Platform", "Amadeus Altea Inventory", "award seat request"),
     ("Amadeus Altea Inventory", "Aeroplan Platform", "award availability"),
     ("Aeroplan Platform", "Star Alliance Interline", "partner award"),
     ("Aeroplan Platform", "SAP S/4HANA", "liability movement"),
     ("Aeroplan Partner Interfaces", "SAP S/4HANA", "issuer settlement")],
    ["Aeroplan Platform", "SAP Customer Data Cloud", "Aeroplan Partner Interfaces",
     "Amadeus Altea Inventory", "SAP S/4HANA", "Star Alliance Interline"],
    ["Identity match quality at the first hop determines exception volume for the whole flow.",
     "Award seat availability is an inventory decision, so loyalty value is ultimately set by revenue "
     "management rather than by the loyalty platform."])

add("AC-X2", "ac-x2-revenue-management", "Revenue Management: PROS, Altea Inventory and ATPCO",
    "Cross-domain flow",
    "How a demand signal becomes a filed fare and an inventory control, and where the latency sits.",
    [("Signal", ["Amadeus Altea Reservations", "Databricks Lakehouse"]),
     ("Optimise", ["PROS Revenue Management", "PROS Real-Time Dynamic Pricing"]),
     ("File and control", ["ATPCO", "Amadeus Altea Inventory"]),
     ("Sell", ["Amadeus Altea NDC", "Sabre GDS", "aircanada.com"])],
    [("Amadeus Altea Reservations", "PROS Revenue Management", "bookings"),
     ("Databricks Lakehouse", "PROS Revenue Management", "history"),
     ("PROS Revenue Management", "PROS Real-Time Dynamic Pricing", "willingness to pay"),
     ("PROS Revenue Management", "Amadeus Altea Inventory", "bid price"),
     ("PROS Real-Time Dynamic Pricing", "ATPCO", "fare change"),
     ("ATPCO", "Amadeus Altea Inventory", "filed fare"),
     ("Amadeus Altea Inventory", "Amadeus Altea NDC", "offer"),
     ("Amadeus Altea Inventory", "Sabre GDS", "availability"),
     ("Amadeus Altea NDC", "aircanada.com", "dynamic offer")],
    ["PROS Real-Time Dynamic Pricing", "PROS Revenue Management", "Amadeus Altea Inventory",
     "ATPCO", "Amadeus Altea NDC"],
    ["The ATPCO filing hop is the slowest link in an otherwise near-real-time chain.",
     "NDC allows a dynamic offer that never has to become a filed fare, which is why the NDC path and the "
     "GDS path increasingly diverge in price."])

add("AC-X3", "ac-x3-passenger-journey", "Passenger Journey: Shop to Boarding Gate",
    "Cross-domain flow",
    "One passenger, end to end, and the eight systems that touch them between shopping and boarding.",
    [("Shop and book", ["aircanada.com", "Amadeus Altea NDC", "Amadeus Altea Reservations"]),
     ("Identify", ["SAP Customer Data Cloud", "Aeroplan Platform"]),
     ("Check in", ["Air Canada Mobile App", "Amadeus Altea DCS"]),
     ("Board", ["Baggage Reconciliation System", "CBSA API and PNR"])],
    [("aircanada.com", "Amadeus Altea NDC", "shopping request"),
     ("Amadeus Altea NDC", "Amadeus Altea Reservations", "create PNR"),
     ("SAP Customer Data Cloud", "aircanada.com", "authenticated member"),
     ("Aeroplan Platform", "Amadeus Altea Reservations", "member benefits"),
     ("Amadeus Altea Reservations", "Amadeus Altea DCS", "passenger list"),
     ("Air Canada Mobile App", "Amadeus Altea DCS", "check in"),
     ("Amadeus Altea DCS", "CBSA API and PNR", "advance passenger info"),
     ("Amadeus Altea DCS", "Baggage Reconciliation System", "bag match")],
    ["aircanada.com", "Amadeus Altea NDC", "Amadeus Altea Reservations", "Amadeus Altea DCS",
     "SAP Customer Data Cloud", "CBSA API and PNR"],
    ["Identity is established once and then relied on by every subsequent stage.",
     "The advance passenger information hop is a regulatory hard gate; failure there stops the flight, "
     "not just the passenger."])

add("AC-X4", "ac-x4-flight-ops", "Flight Operations: Dispatch, Datalink and the Operations Centre",
    "Cross-domain flow",
    "From planned schedule to airborne aircraft, and back through datalink into the operational record.",
    [("Plan", ["Lufthansa Systems NetLine", "NAV CANADA"]),
     ("Dispatch", ["NetLine/Ops", "Weight and Balance System"]),
     ("Flight deck", ["Electronic Flight Bag", "Jeppesen Charts"]),
     ("Monitor", ["ACARS Datalink", "Jeppesen OCC"])],
    [("Lufthansa Systems NetLine", "NetLine/Ops", "flight schedule"),
     ("NAV CANADA", "NetLine/Ops", "NOTAM and weather"),
     ("NetLine/Ops", "Weight and Balance System", "planned payload"),
     ("Weight and Balance System", "Electronic Flight Bag", "loadsheet"),
     ("Jeppesen Charts", "Electronic Flight Bag", "terminal charts"),
     ("Electronic Flight Bag", "ACARS Datalink", "crew acknowledgement"),
     ("ACARS Datalink", "Jeppesen OCC", "OOOI times"),
     ("Jeppesen OCC", "NetLine/Ops", "operational status")],
    ["NetLine/Ops", "Jeppesen OCC", "NAV CANADA", "ACARS Datalink", "Weight and Balance System"],
    ["OOOI times returning through datalink are the timestamps that later determine APPR delay duration.",
     "The dispatch release is a joint responsibility between dispatcher and captain, which makes the "
     "sign-off a control point rather than a formality."])

add("AC-X5", "ac-x5-crew-recovery", "Crew Management: Pairing through Irregular Operations Recovery",
    "Cross-domain flow",
    "How a published roster survives contact with a disrupted day, and where legality binds.",
    [("Plan", ["Lufthansa Systems NetLine", "Jeppesen Crew"]),
     ("Publish", ["Dayforce"]),
     ("Disrupt", ["NetLine/Ops", "Jeppesen OCC"]),
     ("Recover and pay", ["ACARS Datalink", "SAP S/4HANA"])],
    [("Lufthansa Systems NetLine", "Jeppesen Crew", "schedule demand"),
     ("Jeppesen Crew", "Dayforce", "published roster"),
     ("NetLine/Ops", "Jeppesen OCC", "irregularity"),
     ("Jeppesen OCC", "Jeppesen Crew", "legality check"),
     ("Jeppesen Crew", "Jeppesen OCC", "legal crew options"),
     ("Jeppesen OCC", "ACARS Datalink", "crew reassignment"),
     ("Jeppesen Crew", "Dayforce", "actual credit"),
     ("Dayforce", "SAP S/4HANA", "pay posting")],
    ["Jeppesen Crew", "Jeppesen OCC", "NetLine/Ops", "Dayforce", "SAP S/4HANA"],
    ["The legality check is the binding constraint on recovery. An aircraft without a legal crew is not a "
     "recovery option regardless of what the network plan says.",
     "Collective agreement rules under four bargaining units are encoded in the pairing engine, so a "
     "recovery that breaks them creates a grievance rather than a delay."])

add("AC-X6", "ac-x6-mro-airworthiness", "Maintenance and Airworthiness: TRAX, Regulator and Finance",
    "Cross-domain flow",
    "A defect from the technical log through rectification, certification and cost posting.",
    [("Detect", ["ACARS Datalink", "TRAX"]),
     ("Plan", ["Aeroxchange", "Lufthansa Systems NetLine"]),
     ("Execute", ["TRAX eMobility"]),
     ("Certify and post", ["Transport Canada CAWIS", "SAP S/4HANA"])],
    [("ACARS Datalink", "TRAX", "fault downlink"),
     ("TRAX", "Aeroxchange", "parts requirement"),
     ("Lufthansa Systems NetLine", "TRAX", "ground time available"),
     ("TRAX", "TRAX eMobility", "task card"),
     ("TRAX eMobility", "TRAX", "certification and findings"),
     ("TRAX", "Transport Canada CAWIS", "airworthiness record"),
     ("TRAX", "SAP S/4HANA", "labour and parts cost")],
    ["TRAX", "TRAX eMobility", "Transport Canada CAWIS", "Aeroxchange", "SAP S/4HANA"],
    ["Certification is the gate that releases the aircraft; everything downstream of it is accounting.",
     "Ground time available comes from the rotation build, which is why a maintenance overrun is a "
     "network problem before it is an engineering one."])

add("AC-X7", "ac-x7-cargo", "Cargo: Cargospot neo, Pre-Load Customs and Settlement",
    "Cross-domain flow",
    "An air waybill from booking to settlement, across the live Cargospot migration boundary.",
    [("Book", ["CHAMP Cargospot neo"]),
     ("Comply", ["Canada PACT"]),
     ("Handle and fly", ["Cargospot neo Handling", "Cargospot Mobile", "Amadeus Altea DCS"]),
     ("Settle", ["Cargospot neo Revenue Accounting", "SAP S/4HANA"])],
    [("CHAMP Cargospot neo", "Canada PACT", "pre-load data"),
     ("CHAMP Cargospot neo", "Cargospot neo Handling", "booking"),
     ("Cargospot neo Handling", "Cargospot Mobile", "warehouse task"),
     ("Cargospot neo Handling", "Amadeus Altea DCS", "uplift to aircraft"),
     ("Cargospot neo Handling", "Cargospot neo Revenue Accounting", "proof of carriage"),
     ("Cargospot neo Revenue Accounting", "SAP S/4HANA", "CASS settlement")],
    ["CHAMP Cargospot neo", "Cargospot neo Handling", "Canada PACT",
     "Cargospot neo Revenue Accounting", "SAP S/4HANA"],
    ["Pre-load filing must complete before loading. It is a gate, not a report.",
     "During the migration this whole flow runs twice, once in legacy and once in Cargospot, which is "
     "where revenue-accounting variance originates."])

add("AC-X8", "ac-x8-network-publication", "Network Planning: Schedule Build to Market Publication",
    "Cross-domain flow",
    "How a schedule decision reaches every selling channel and every alliance partner.",
    [("Build", ["NetLine/Plan"]),
     ("Coordinate", ["Star Alliance Interline", "A++ Atlantic Joint Venture"]),
     ("Load", ["Amadeus Altea Inventory", "Lufthansa Systems NetLine"]),
     ("Publish", ["IATA Type-B Messaging", "Sabre GDS", "aircanada.com"])],
    [("NetLine/Plan", "Star Alliance Interline", "codeshare intent"),
     ("NetLine/Plan", "A++ Atlantic Joint Venture", "JV schedule"),
     ("NetLine/Plan", "Lufthansa Systems NetLine", "committed schedule"),
     ("Lufthansa Systems NetLine", "Amadeus Altea Inventory", "SSIM load"),
     ("Lufthansa Systems NetLine", "IATA Type-B Messaging", "schedule change"),
     ("IATA Type-B Messaging", "Sabre GDS", "distribution"),
     ("Amadeus Altea Inventory", "aircanada.com", "sellable schedule")],
    ["NetLine/Plan", "Lufthansa Systems NetLine", "Amadeus Altea Inventory",
     "Star Alliance Interline", "IATA Type-B Messaging"],
    ["A schedule change after load triggers passenger re-protection, so late changes are expensive in a "
     "way the planning system does not price.",
     "Joint venture coordination happens before the schedule is committed, not after."])

add("AC-X9", "ac-x9-finance-settlement", "Finance: Revenue Accounting, Interline Settlement and Treasury",
    "Cross-domain flow",
    "From a flown coupon to recognised revenue, settled interline balances and a cash position.",
    [("Sell", ["Amadeus Altea Reservations", "IATA BSP"]),
     ("Account", ["Revenue Accounting System"]),
     ("Settle", ["Star Alliance Interline", "SAP S/4HANA"]),
     ("Report", ["SAP Analytics Cloud"])],
    [("Amadeus Altea Reservations", "Revenue Accounting System", "coupon lifted"),
     ("IATA BSP", "Revenue Accounting System", "agency sales"),
     ("Revenue Accounting System", "Star Alliance Interline", "interline billing"),
     ("Revenue Accounting System", "SAP S/4HANA", "recognised revenue"),
     ("Star Alliance Interline", "SAP S/4HANA", "settled balances"),
     ("SAP S/4HANA", "SAP Analytics Cloud", "management reporting")],
    ["Revenue Accounting System", "IATA BSP", "SAP S/4HANA", "SAP Analytics Cloud",
     "Star Alliance Interline"],
    ["Revenue is recognised on lift, not on sale, which is what creates the air traffic liability.",
     "Interline settlement runs on industry clearing timetables outside Air Canada's control."])

add("AC-X10", "ac-x10-data-platform", "Data Platform: AWS, Databricks and the Cloudera Sunset",
    "Cross-domain flow",
    "The grounding surface for analytics and AI, currently being rebuilt.",
    [("Sources", ["Amadeus Altea Reservations", "NetLine/Ops", "TRAX", "Salesforce Service Cloud"]),
     ("Ingest", ["Integration Platform"]),
     ("Lakehouse", ["Cloudera", "Databricks Lakehouse", "Unity Catalog"]),
     ("Consume", ["PROS Revenue Management", "SAP Analytics Cloud"])],
    [("Amadeus Altea Reservations", "Integration Platform", "booking events"),
     ("NetLine/Ops", "Integration Platform", "operational events"),
     ("TRAX", "Integration Platform", "maintenance events"),
     ("Salesforce Service Cloud", "Integration Platform", "case events"),
     ("Integration Platform", "Databricks Lakehouse", "ingest"),
     ("Cloudera", "Databricks Lakehouse", "migrate and retire"),
     ("Databricks Lakehouse", "Unity Catalog", "govern"),
     ("Databricks Lakehouse", "PROS Revenue Management", "demand history"),
     ("Databricks Lakehouse", "SAP Analytics Cloud", "operational drivers")],
    ["Databricks Lakehouse", "Cloudera", "Unity Catalog", "Integration Platform", "AWS"],
    ["The ingest layer is an unconfirmed product and every AI use case depends on it.",
     "Because the lakehouse is being rebuilt now, governance and lineage can be designed in rather than "
     "retrofitted."],
    gaps=("Integration Platform",))

add("AC-X11", "ac-x11-irrop-end-to-end", "Irregular Operations End to End: Detection to Compensation",
    "Cross-domain flow",
    "The single most consequential chain in the estate: a disruption becomes a crew problem, a passenger "
    "problem and finally a regulatory liability.",
    [("Detect", ["NetLine/Ops", "Jazz and PAL Operator Interface"]),
     ("Recover", ["Jeppesen OCC", "Jeppesen Crew", "Amadeus Passenger Recovery"]),
     ("Notify", ["Air Canada Mobile App", "Amazon Connect"]),
     ("Adjudicate", ["Salesforce Service Cloud", "CTA Complaint Interface", "SAP S/4HANA"])],
    [("Jazz and PAL Operator Interface", "NetLine/Ops", "manual reconciliation"),
     ("NetLine/Ops", "Jeppesen OCC", "recovery decision"),
     ("Jeppesen OCC", "Jeppesen Crew", "crew legality"),
     ("Jeppesen OCC", "Amadeus Passenger Recovery", "reaccommodate"),
     ("Amadeus Passenger Recovery", "Air Canada Mobile App", "new itinerary"),
     ("Amadeus Passenger Recovery", "Amazon Connect", "assisted rebooking"),
     ("NetLine/Ops", "Salesforce Service Cloud", "delay reason code"),
     ("Salesforce Service Cloud", "CTA Complaint Interface", "regulatory response"),
     ("Salesforce Service Cloud", "SAP S/4HANA", "compensation")],
    ["NetLine/Ops", "Jeppesen OCC", "Amadeus Passenger Recovery", "Salesforce Service Cloud",
     "Jazz and PAL Operator Interface", "CTA Complaint Interface"],
    ["The delay reason code set at the first hop determines the compensation outcome at the last. An "
     "inconsistent code at the Express operator seam becomes a regulatory exposure four systems later.",
     "This chain crosses six domains and no single system holds the whole picture.",
     "Improving reason-code fidelity at source is worth more than improving adjudication downstream."])

add("AC-X12", "ac-x12-service-management", "IT Service Management: Event to Resolution",
    "Cross-domain flow",
    "How an operational event becomes an incident, a change and a service level position.",
    [("Detect", ["Observability Platform", "Amadeus Altea DCS", "NetLine/Ops"]),
     ("Triage", ["ITSM Platform"]),
     ("Resolve", ["Integration Platform", "AWS"]),
     ("Govern", ["SAP Ariba"])],
    [("Observability Platform", "ITSM Platform", "alert to incident"),
     ("Amadeus Altea DCS", "ITSM Platform", "user-reported fault"),
     ("NetLine/Ops", "ITSM Platform", "operational impact"),
     ("ITSM Platform", "Integration Platform", "interface fix"),
     ("ITSM Platform", "AWS", "platform change"),
     ("ITSM Platform", "SAP Ariba", "vendor service credit")],
    ["ITSM Platform", "Observability Platform", "Integration Platform", "AWS"],
    ["The ITSM product and the observability product are both unconfirmed and are direct scope questions "
     "for an application management engagement.",
     "The 2023 outages show the gap is not detection alone but the absence of a rehearsed degraded-mode "
     "operating procedure for the airport and ops-control estate."],
    gaps=("ITSM Platform", "Observability Platform", "Integration Platform"))

add("AC-X13", "ac-x13-cybersecurity", "Cybersecurity and Identity: Customer and Workforce Perimeters",
    "Cross-domain flow",
    "Two distinct identity perimeters, one evidenced and one not.",
    [("Customer perimeter", ["SAP Customer Data Cloud", "aircanada.com", "Air Canada Mobile App"]),
     ("Workforce perimeter", ["Workforce Identity", "Microsoft 365"]),
     ("Detect", ["SIEM and SOC"]),
     ("Respond", ["ITSM Platform"])],
    [("aircanada.com", "SAP Customer Data Cloud", "customer authentication"),
     ("Air Canada Mobile App", "SAP Customer Data Cloud", "customer authentication"),
     ("Workforce Identity", "Microsoft 365", "employee SSO"),
     ("SAP Customer Data Cloud", "SIEM and SOC", "auth telemetry"),
     ("Microsoft 365", "SIEM and SOC", "auth telemetry"),
     ("SIEM and SOC", "ITSM Platform", "security incident")],
    ["SAP Customer Data Cloud", "Workforce Identity", "SIEM and SOC", "Microsoft 365", "ITSM Platform"],
    ["Customer identity on SAP Customer Data Cloud is confirmed. Workforce identity is not evidenced in "
     "public sources and should not be named in a bid.",
     "SAP Customer Data Cloud also carries consent, which makes it a privacy control point under PIPEDA "
     "and Quebec Law 25, not only an authentication service."],
    gaps=("Workforce Identity", "SIEM and SOC", "ITSM Platform"))

add("AC-X14", "ac-x14-contact-centre", "Contact Centre: Voice, Assistant and Case",
    "Cross-domain flow",
    "How a customer contact becomes a case, and where the AI governance boundary sits.",
    [("Contact", ["Air Canada Virtual Assistant", "Amazon Connect"]),
     ("Context", ["Amadeus Altea Customer Management", "Aeroplan Platform"]),
     ("Case", ["Salesforce Service Cloud"]),
     ("Plan capacity", ["Simul8"])],
    [("Air Canada Virtual Assistant", "Salesforce Service Cloud", "escalated conversation"),
     ("Amazon Connect", "Salesforce Service Cloud", "voice to case"),
     ("Amadeus Altea Customer Management", "Salesforce Service Cloud", "booking context"),
     ("Aeroplan Platform", "Salesforce Service Cloud", "member context"),
     ("Amazon Connect", "Simul8", "volume telemetry"),
     ("Simul8", "Amazon Connect", "staffing model")],
    ["Amazon Connect", "Salesforce Service Cloud", "Air Canada Virtual Assistant",
     "Amadeus Altea Customer Management", "Simul8"],
    ["The virtual assistant is inside the liability perimeter set by Moffatt v. Air Canada. Any automated "
     "response that states policy must have a human decision point and restricted grounding.",
     "Every interaction in this flow carries a bilingual obligation in English and French."])

add("AC-X15", "ac-x15-turnaround", "Ground Turnaround: Arrival to Off-Block at the Hub",
    "Cross-domain flow",
    "The turn itself, where schedule, baggage, load and maintenance all have to agree inside the ground time.",
    [("Arrive", ["ACARS Datalink", "Airport Resource Management"]),
     ("Service", ["Amadeus Altea DCS", "Baggage Reconciliation System", "TRAX eMobility"]),
     ("Load", ["Weight and Balance System"]),
     ("Depart", ["NetLine/Ops", "IATA Type-B Messaging"])],
    [("ACARS Datalink", "Airport Resource Management", "on-block"),
     ("Airport Resource Management", "Amadeus Altea DCS", "gate assignment"),
     ("Amadeus Altea DCS", "Baggage Reconciliation System", "bag reconciliation"),
     ("TRAX eMobility", "NetLine/Ops", "maintenance release"),
     ("Amadeus Altea DCS", "Weight and Balance System", "final passenger load"),
     ("Baggage Reconciliation System", "Weight and Balance System", "bag load"),
     ("Weight and Balance System", "NetLine/Ops", "loadsheet issued"),
     ("NetLine/Ops", "IATA Type-B Messaging", "movement message")],
    ["Amadeus Altea DCS", "Weight and Balance System", "Baggage Reconciliation System",
     "TRAX eMobility", "NetLine/Ops"],
    ["The loadsheet is the last gate before off-block, so every upstream delay compresses into it.",
     "A maintenance release arriving late converts an engineering task into a departure delay and, if it "
     "runs long enough, into an APPR liability."])

add("AC-X16", "ac-x16-manual-rekey", "Manual Re-Key Hotspots and Automation Targets",
    "Cross-domain flow",
    "The seams where a human retypes data that a system already holds. These are the highest-value "
    "automation targets in the estate, and each one is a defect surface as well as a cost.",
    [("Re-key hotspot", ["Express operator disruption reconciliation",
                         "APPR entitlement from PNR and reason code",
                         "Mishandled bag claim to compensation",
                         "Cargo interim double entry",
                         "Bilingual content parity"]),
     ("Systems either side", ["Jazz and PAL Operator Interface", "Salesforce Service Cloud",
                              "SITA WorldTracer", "CHAMP Cargospot neo"]),
     ("Consequence", ["Regulatory exposure", "Revenue variance", "Cycle time and cost"])],
    [("Express operator disruption reconciliation", "Jazz and PAL Operator Interface", ""),
     ("APPR entitlement from PNR and reason code", "Salesforce Service Cloud", ""),
     ("Mishandled bag claim to compensation", "SITA WorldTracer", ""),
     ("Cargo interim double entry", "CHAMP Cargospot neo", ""),
     ("Jazz and PAL Operator Interface", "Regulatory exposure", "wrong reason code"),
     ("Salesforce Service Cloud", "Regulatory exposure", "wrong entitlement"),
     ("SITA WorldTracer", "Cycle time and cost", "claim delay"),
     ("CHAMP Cargospot neo", "Revenue variance", "divergent records"),
     ("Bilingual content parity", "Cycle time and cost", "duplicated QA")],
    ["Jazz and PAL Operator Interface", "Salesforce Service Cloud", "SITA WorldTracer",
     "CHAMP Cargospot neo"],
    ["Each hotspot is a place where a system already holds the data and a person retypes it into another "
     "system. That is both a cost and a defect surface.",
     "The APPR and Express-operator hotspots compound: a wrong reason code entered at the operational "
     "seam produces a wrong entitlement determination three systems downstream.",
     "The cargo hotspot is time-bounded by the Cargospot migration, which makes it the cheapest one to "
     "justify solving now.",
     "Any automation proposed against these seams must carry a human decision point, given the Moffatt "
     "precedent on automated statements."],
    gaps=("Regulatory exposure", "Revenue variance", "Cycle time and cost"))


if __name__ == "__main__":
    out = os.path.join(ROOT, "data", "ea.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"diagrams": DIAGRAMS}, f, ensure_ascii=False, indent=1)
    land = sum(1 for d in DIAGRAMS if d["kind"] == "Domain landscape")
    flow = len(DIAGRAMS) - land
    print(f"{len(DIAGRAMS)} EA diagrams: {land} domain landscapes, {flow} cross-domain flows")
    print(f"  -> data/ea.json ({os.path.getsize(out)/1024:.0f} KB)")
