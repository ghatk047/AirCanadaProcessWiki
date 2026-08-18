# -*- coding: utf-8 -*-
"""AC-CG-CS — Customs, PACT and Dangerous Goods (5) and AC-CG-CP (4 remaining, CP-04 already in a_pilot)."""
from content_lib import P, S

# ── CS: Customs, PACT and Dangerous Goods ───────────────────────────────────
P("AC-CG-CS-01",
  desc="Pre-load air cargo targeting data is filed with CBSA before a shipment is loaded, meeting the "
       "mandatory pre-load filing requirement in force since April 2025.",
  trig="A cargo shipment destined for or transiting Canada is accepted for a scheduled flight.",
  out="Complete, accurate pre-load data filed with CBSA before loading, clearing the shipment for loading "
      "or flagging it for hold.",
  note="Canada PACT has no tolerance for interface downtime, since filing has to complete before loading, "
      "which makes this one of the least flexible regulatory gates in the entire cargo operation.",
  phases=["Data compilation", "PACT filing", "Loading clearance"],
  steps=[
    S("1.1","Compile shipment data for PACT filing","Cargo Compliance Agent","Canada PACT",
      "Accepted shipment details","Compiled filing data",
      "Compiled for 100 percent of applicable shipments before filing deadline at 100 percent","N","N",
      "Data completeness depends on accurate information captured at the original acceptance in AC-CG-GH-01"),
    S("2.1","File pre-load data with CBSA","Cargo Compliance Agent","Canada PACT",
      "Compiled data","Filed PACT submission",
      "Filed before the mandatory pre-load deadline at 100 percent","N","N",
      "The filing has to complete before loading with zero tolerance for interface downtime"),
    S("2.2","Respond to a CBSA hold or query","Cargo Compliance Agent","Canada PACT",
      "Filed submission flagged by CBSA","Resolved hold or query",
      "Resolved within the time available before the flight's scheduled departure at 90 percent","N","Y",
      "A hold resolved too late results in the shipment being offloaded from the flight"),
    S("3.1","Confirm loading clearance","Cargo Compliance Agent","Canada PACT",
      "Cleared filing","Confirmed loading clearance",
      "Confirmed before physical loading begins at 100 percent","N","N",
      "Loading without confirmed clearance is a direct violation of the mandatory pre-load requirement"),
  ],
  kpis=["Compiled for 100 percent of applicable shipments before filing deadline at 100 percent",
        "Filed before the mandatory pre-load deadline at 100 percent",
        "Confirmed before physical loading begins at 100 percent",
        "Zero shipments loaded without confirmed PACT clearance"],
  risks=["Loading without confirmed clearance constituting a direct violation of the mandatory pre-load requirement",
         "A hold resolved too late resulting in the shipment being offloaded from the flight",
         "Data completeness depending on accurate information captured at the original acceptance step",
         "Interface downtime having zero tolerance given the hard pre-load filing deadline"])

P("AC-CG-CS-02",
  desc="Export and import customs declarations are prepared and filed for a cargo shipment, distinct from "
       "the pre-load targeting filing, covering the formal customs clearance process.",
  trig="A shipment requires export or import customs declaration for its origin or destination.",
  out="Complete, accurate customs declarations filed and cleared, allowing the shipment to proceed through "
      "customs without delay.",
  note="Customs declaration accuracy has consequences beyond a single shipment delay, since a pattern of "
      "declaration errors can trigger heightened scrutiny of Air Canada Cargo's future shipments by the "
      "relevant customs authority.",
  phases=["Declaration preparation", "Filing", "Clearance confirmation"],
  steps=[
    S("1.1","Prepare customs declaration","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Shipment commodity and value data","Prepared declaration",
      "Prepared for 100 percent of applicable shipments before filing at 100 percent","N","N",
      "Commodity classification for customs purposes requires specific expertise that varies by product category"),
    S("2.1","File declaration with the relevant customs authority","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Prepared declaration","Filed declaration",
      "Filed within the required timeframe at 100 percent","N","N",
      "Filing requirements and formats differ by origin and destination customs authority"),
    S("2.2","Respond to a customs query or inspection hold","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Flagged declaration","Resolved query or hold",
      "Resolved within the customs authority's response window at 90 percent","N","Y",
      "A pattern of declaration errors can trigger heightened scrutiny of future Air Canada Cargo shipments"),
    S("3.1","Confirm customs clearance","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Resolved declaration","Confirmed clearance",
      "Confirmed before the shipment proceeds at 100 percent","N","N",
      "A shipment proceeding without confirmed clearance risks a customs violation at the destination"),
  ],
  kpis=["Prepared for 100 percent of applicable shipments before filing at 100 percent",
        "Filed within the required timeframe at 100 percent",
        "Resolved within the customs authority's response window at 90 percent",
        "Declaration error rate below target across all customs authorities"],
  risks=["A pattern of declaration errors triggering heightened scrutiny of future Air Canada Cargo shipments",
         "Commodity classification for customs purposes requiring specific expertise that varies by product category",
         "Filing requirements and formats differing meaningfully by origin and destination customs authority",
         "A shipment proceeding without confirmed clearance risking a customs violation at the destination"])

P("AC-CG-CS-03",
  desc="Dangerous goods are accepted and documented in accordance with IATA dangerous goods regulations, "
       "confirming correct classification, packaging and labelling before the shipment is loaded.",
  trig="A shipment containing dangerous goods is presented for acceptance.",
  out="Dangerous goods correctly classified, documented and accepted, or declined where the shipment does "
      "not meet regulatory requirements.",
  note="Dangerous goods acceptance is one of the highest-consequence checks in the entire cargo operation, "
      "since an incorrectly classified or improperly packaged shipment loaded onto an aircraft is a direct "
      "safety hazard rather than a compliance technicality.",
  phases=["Classification verification", "Packaging and labelling inspection", "Acceptance decision"],
  steps=[
    S("1.1","Verify dangerous goods classification","Dangerous Goods Agent","CHAMP Cargospot neo",
      "Shipper's declaration for dangerous goods","Verified classification",
      "Verified for 100 percent of dangerous goods shipments at 100 percent","Y","N",
      "Misclassification by the shipper, whether intentional or accidental, is the primary risk this step guards against"),
    S("2.1","Inspect packaging and labelling","Dangerous Goods Agent","CHAMP Cargospot neo",
      "Verified classification","Inspection findings",
      "Inspected for 100 percent of dangerous goods shipments at 100 percent","N","N",
      "Packaging and labelling standards are extremely specific and easy to fail on a technicality that still matters for safety"),
    S("2.2","Confirm aircraft loading compatibility","Dangerous Goods Agent","Weight and Balance System",
      "Classified and inspected shipment","Confirmed loading compatibility",
      "Confirmed before acceptance for 100 percent of dangerous goods at 100 percent","Y","N",
      "Certain dangerous goods classes are incompatible with each other or with specific aircraft loading positions"),
    S("3.1","Accept or decline the shipment","Dangerous Goods Agent","CHAMP Cargospot neo",
      "Confirmed compatibility","Accepted or declined shipment",
      "Decision documented for 100 percent of dangerous goods shipments at 100 percent","N","N",
      "A shipment accepted despite a marginal compliance gap is a safety exposure, not a commercial trade-off"),
  ],
  kpis=["Verified for 100 percent of dangerous goods shipments at 100 percent",
        "Inspected for 100 percent of dangerous goods shipments at 100 percent",
        "Confirmed before acceptance for 100 percent of dangerous goods at 100 percent",
        "Zero dangerous goods incidents attributable to acceptance process failure"],
  risks=["An incorrectly classified or improperly packaged shipment loaded onto an aircraft being a direct safety hazard",
         "Misclassification by the shipper, whether intentional or accidental, being the primary risk to guard against",
         "Certain dangerous goods classes being incompatible with each other or with specific loading positions",
         "A shipment accepted despite a marginal compliance gap constituting a safety exposure, not a trade-off"])

P("AC-CG-CS-04",
  desc="Cargo is screened against restricted party and embargo lists before acceptance, confirming the "
       "shipment does not involve a sanctioned entity or a prohibited destination.",
  trig="A cargo booking or acceptance requires restricted party and embargo screening.",
  out="A screened shipment confirmed clear of restricted party and embargo concerns, or held pending "
      "compliance review.",
  note="Sanctions and embargo compliance carries severe regulatory and reputational consequences if missed, "
      "which makes this screening step a hard gate rather than a routine check that can be waived under "
      "commercial pressure.",
  phases=["Party and destination screening", "Compliance review", "Acceptance or hold decision"],
  steps=[
    S("1.1","Screen shipper and consignee against restricted party lists","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Shipper and consignee identity","Screening result",
      "Screened for 100 percent of bookings before acceptance at 100 percent","N","N",
      "Restricted party lists are updated by regulators on their own schedule and have to be kept current"),
    S("1.2","Screen destination against embargo restrictions","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Destination country and commodity","Embargo screening result",
      "Screened for 100 percent of international bookings at 100 percent","N","N",
      "Embargo restrictions can be commodity-specific within an otherwise permitted destination"),
    S("2.1","Review flagged screening results","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Flagged screening result","Compliance review outcome",
      "Reviewed within the required timeframe before acceptance at 100 percent","Y","N",
      "A false positive match against a common name has to be resolved without excessive delay to a legitimate shipment"),
    S("3.1","Confirm acceptance or hold the shipment","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Reviewed result","Confirmed acceptance or documented hold",
      "Decision documented for 100 percent of screened shipments at 100 percent","N","N",
      "A shipment accepted without full screening resolution is a severe regulatory and reputational exposure"),
  ],
  kpis=["Screened for 100 percent of bookings before acceptance at 100 percent",
        "Screened for 100 percent of international bookings at 100 percent",
        "Reviewed within the required timeframe before acceptance at 100 percent",
        "Zero shipments accepted without full screening resolution"],
  risks=["Sanctions and embargo compliance carrying severe regulatory and reputational consequences if missed",
         "A false positive against a common name causing excessive delay to a legitimate shipment",
         "Restricted party lists being updated by regulators on their own schedule and needing to stay current",
         "Embargo restrictions being commodity-specific within an otherwise permitted destination"])

P("AC-CG-CS-05",
  desc="Cargo security screening is applied in compliance with regulatory requirements, confirming a "
       "shipment has undergone required screening before it can be loaded onto a passenger or all-cargo "
       "aircraft.",
  trig="A cargo shipment requires security screening ahead of loading.",
  out="A shipment confirmed to have passed required security screening, cleared for loading, or held "
      "pending resolution.",
  note="Cargo security screening on a passenger aircraft carries a materially higher regulatory bar than "
      "screening for an all-cargo freighter, given the number of passengers whose safety depends on the "
      "same hold.",
  phases=["Screening requirement determination", "Screening execution", "Clearance confirmation"],
  steps=[
    S("1.1","Determine screening requirement","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Shipment and aircraft type","Determined screening requirement",
      "Determined for 100 percent of shipments before screening at 100 percent","N","N",
      "Passenger aircraft carry a materially higher screening bar than an all-cargo freighter"),
    S("2.1","Execute required security screening","Cargo Warehouse Agent","Cargospot neo Handling",
      "Determined requirement","Screening result",
      "Executed for 100 percent of shipments meeting the determined requirement at 100 percent","N","N",
      "Screening method and equipment availability can vary by station, especially at smaller outstations"),
    S("2.2","Resolve a screening alert","Cargo Warehouse Agent","Cargospot neo Handling",
      "Flagged screening alert","Resolved alert",
      "Resolved before the shipment can proceed at 100 percent","Y","Y",
      "An unresolved screening alert has to hold the shipment regardless of flight timing pressure"),
    S("3.1","Confirm screening clearance for loading","Cargo Compliance Agent","CHAMP Cargospot neo",
      "Resolved screening","Confirmed clearance",
      "Confirmed before physical loading begins at 100 percent","N","N",
      "Loading without confirmed screening clearance is a direct security compliance violation"),
  ],
  kpis=["Determined for 100 percent of shipments before screening at 100 percent",
        "Executed for 100 percent of shipments meeting the determined requirement at 100 percent",
        "Resolved before the shipment can proceed at 100 percent",
        "Zero shipments loaded without confirmed screening clearance"],
  risks=["Passenger aircraft carrying a materially higher regulatory screening bar than an all-cargo freighter",
         "An unresolved screening alert having to hold the shipment regardless of flight timing pressure",
         "Screening method and equipment availability varying by station, especially at smaller outstations",
         "Loading without confirmed screening clearance constituting a direct security compliance violation"])

# ── CP: Cargo Revenue and Performance (remaining 4) ─────────────────────────
P("AC-CG-CP-01",
  desc="Cargo revenue is recognised and settled against IATA CASS, reconciling flown air waybills to "
       "recognised revenue and industry settlement.",
  trig="A cargo shipment is flown and requires revenue recognition and CASS settlement.",
  out="Recognised cargo revenue correctly settled through IATA CASS, reconciled against flown air waybills.",
  note="Cargo revenue accounting mirrors passenger revenue accounting's core discipline in AC-FN-RA-01, "
       "recognition on actual carriage rather than on booking, but runs through CASS rather than BSP as its "
       "industry settlement mechanism.",
  phases=["Flown shipment compilation", "Revenue recognition", "CASS settlement"],
  steps=[
    S("1.1","Compile flown air waybills","Cargo Revenue Analyst","Cargospot neo Revenue Accounting",
      "Completed flight and loaded shipments","Compiled flown air waybill list",
      "Compiled within 2 business days of flight completion at 100 percent","N","N",
      "A shipment loaded but not correctly matched to its air waybill record creates a revenue recognition gap"),
    S("2.1","Recognise revenue on flown carriage","Cargo Revenue Analyst","Cargospot neo Revenue Accounting",
      "Compiled air waybills","Recognised revenue",
      "Recognised within the standard accounting period close timetable at 100 percent","N","N",
      "Revenue recognition timing has to correctly reflect actual carriage, not the original booking date"),
    S("2.2","Reconcile against IATA CASS settlement","Cargo Revenue Analyst","IATA BSP",
      "Recognised revenue and CASS statement","Reconciled settlement position",
      "Reconciled within the CASS settlement cycle at 100 percent","Y","N",
      "A reconciliation variance between recognised revenue and the CASS statement needs prompt investigation"),
    S("3.1","Settle and post to the general ledger","Cargo Revenue Analyst","SAP S/4HANA",
      "Reconciled position","Posted settlement",
      "Posted within the financial close timetable at 100 percent","N","N",
      "A settlement not posted within the close timetable delays the broader finance close it feeds into"),
  ],
  kpis=["Compiled within 2 business days of flight completion at 100 percent",
        "Recognised within the standard accounting period close timetable at 100 percent",
        "Reconciled within the CASS settlement cycle at 100 percent",
        "Posted within the financial close timetable at 100 percent"],
  risks=["A shipment loaded but not correctly matched to its air waybill record creating a revenue recognition gap",
         "A reconciliation variance between recognised revenue and the CASS statement needing prompt investigation",
         "Revenue recognition timing needing to correctly reflect actual carriage rather than the original booking date",
         "A settlement not posted within the close timetable delaying the broader finance close"])

P("AC-CG-CP-02",
  desc="Cargo yield and capacity utilisation are analysed by route and period, identifying underperforming "
       "capacity and feeding both pricing and network capacity allocation decisions.",
  trig="The recurring cargo performance reporting cycle runs.",
  out="A cargo yield and utilisation report by route, with underperformance identified and routed to "
      "pricing or capacity planning for action.",
  note="Cargo yield analysis serves the same function for cargo that revenue management analytics serve for "
      "passenger, as covered in AC-RM-YM-01 through 07, but for a commercial product with materially "
      "different demand dynamics and a shorter selling cycle.",
  phases=["Performance compilation", "Yield analysis", "Action routing"],
  steps=[
    S("1.1","Compile cargo revenue and volume by route","Cargo Revenue Analyst","CHAMP Cargospot neo",
      "Flown shipment and revenue data","Compiled performance by route",
      "Compiled within 5 business days of period close at 100 percent","N","N",
      "Freighter and belly cargo performance needs to be compiled and analysed separately given their different economics"),
    S("2.1","Calculate yield and utilisation by route","Cargo Revenue Analyst","SAP Analytics Cloud",
      "Compiled performance","Calculated yield and utilisation",
      "Calculated for 100 percent of routes each period at 100 percent","N","N",
      "Utilisation calculated against allocated capacity can mask an allocation that was itself too conservative"),
    S("2.2","Identify underperforming routes","Cargo Revenue Analyst","SAP Analytics Cloud",
      "Calculated performance","Identified underperformance",
      "Identified for 100 percent of material routes each period at 100 percent","N","N",
      "Underperformance attribution has to distinguish a pricing problem from a genuine demand problem"),
    S("3.1","Route findings to pricing or capacity planning","Cargo Revenue Analyst","CHAMP Cargospot neo",
      "Identified underperformance","Routed findings with recommendation",
      "Routed within 10 business days of period close at 100 percent","N","N",
      "Findings routed without a clear recommendation risk sitting unactioned in the next planning cycle"),
  ],
  kpis=["Compiled within 5 business days of period close at 100 percent",
        "Calculated for 100 percent of routes each period at 100 percent",
        "Identified for 100 percent of material routes each period at 100 percent",
        "Routed within 10 business days of period close at 100 percent"],
  risks=["Utilisation calculated against allocated capacity masking an allocation that was itself too conservative",
         "Underperformance attribution failing to distinguish a pricing problem from a genuine demand problem",
         "Freighter and belly cargo economics needing separate compilation given how differently they behave",
         "Findings routed without a clear recommendation sitting unactioned in the next planning cycle"])

P("AC-CG-CP-03",
  desc="A cargo damage or loss claim is investigated and settled within applicable liability limits, "
       "distinct from a passenger baggage claim but governed by comparable international liability "
       "conventions.",
  trig="A consignee or shipper submits a claim for cargo damage or loss.",
  out="A settled claim within applicable liability limits, or a documented reason for a reduced or denied "
      "settlement.",
  note="Cargo liability limits and documentation standards under international convention are distinct from "
      "the passenger baggage framework in AC-CX-CR-05, and cargo claims often involve materially higher "
      "declared values that warrant a correspondingly more rigorous documentation standard.",
  phases=["Claim intake", "Liability assessment", "Settlement"],
  steps=[
    S("1.1","Receive and register the cargo claim","Cargo Claims Agent","CHAMP Cargospot neo",
      "Shipper or consignee claim submission","Registered claim",
      "Registered within 1 business day of submission at 100 percent","N","N",
      "A claim not correctly linked to its original air waybill and handling record loses supporting context"),
    S("2.1","Assess claim against liability convention limits","Cargo Claims Agent","CHAMP Cargospot neo",
      "Registered claim and declared value","Assessed liability position",
      "Assessed within 15 business days of registration at 90 percent","Y","N",
      "Cargo claims often involve higher declared values than baggage claims, warranting more rigorous documentation review"),
    S("2.2","Investigate cause of damage or loss","Cargo Claims Agent","Cargospot neo Handling",
      "Assessed claim","Investigated cause",
      "Investigated within the assessment window for 100 percent of material claims at 100 percent","N","N",
      "Investigation depends on handling records across every station the shipment passed through"),
    S("3.1","Settle the claim","Cargo Claims Agent","SAP S/4HANA",
      "Investigated and documented claim","Settlement payment or documented denial",
      "Settled within 30 days of complete documentation at 90 percent","N","N",
      "A settlement delay compounds commercial relationship damage with the shipper or forwarder"),
  ],
  kpis=["Registered within 1 business day of submission at 100 percent",
        "Assessed within 15 business days of registration at 90 percent",
        "Settled within 30 days of complete documentation at 90 percent",
        "Settlement consistency across similar claims tracked for fairness"],
  risks=["Cargo claims often involving higher declared values than baggage claims, warranting more rigorous documentation review",
         "Investigation depending on handling records across every station the shipment passed through",
         "A claim not correctly linked to its original air waybill and handling record losing supporting context",
         "A settlement delay compounding commercial relationship damage with the shipper or forwarder"])

P("AC-CG-CP-05",
  desc="Cargo partner and general sales agent performance is reviewed against commercial targets, covering "
       "the network of agents selling Air Canada Cargo capacity on commission.",
  trig="The recurring cargo partner performance review cycle runs, or a partner underperformance pattern is "
       "identified.",
  out="Partner and GSA performance assessed against commercial targets, with underperformance addressed "
      "and strong performers recognised for continued or expanded relationship.",
  note="General sales agents extend Air Canada Cargo's commercial reach into markets a direct sales team "
      "cannot economically cover, which makes partner performance management a genuine extension of the "
      "cargo sales function rather than a separate contract administration exercise.",
  phases=["Performance data compilation", "Target assessment", "Relationship action"],
  steps=[
    S("1.1","Compile partner and GSA sales performance","Cargo Sales Manager","CHAMP Cargospot neo",
      "Booking and revenue data by partner","Compiled performance by partner",
      "Compiled within 5 business days of period close at 100 percent","N","N",
      "Attribution of a booking to a specific partner or GSA depends on correct channel tagging at booking"),
    S("2.1","Assess performance against commercial targets","Cargo Sales Manager","SAP Analytics Cloud",
      "Compiled performance and agreed targets","Assessed performance",
      "Assessed for 100 percent of active partners each cycle at 100 percent","N","N",
      "Targets set without accounting for a partner's specific market conditions can be systematically unfair"),
    S("2.2","Identify underperformance requiring action","Cargo Sales Manager","CHAMP Cargospot neo",
      "Assessed performance","Identified underperforming partners",
      "Identified for 100 percent of material underperformance each cycle at 100 percent","N","N",
      "A single weak period is different from a persistent pattern, and the two need different responses"),
    S("3.1","Take relationship action per the agreement terms","Cargo Sales Manager","SAP Ariba",
      "Identified pattern","Relationship action, from support to termination",
      "Action taken within the agreement's defined timeframe at 100 percent","N","N",
      "Terminating a partner relationship in an underserved market can leave that market without effective coverage"),
  ],
  kpis=["Compiled within 5 business days of period close at 100 percent",
        "Assessed for 100 percent of active partners each cycle at 100 percent",
        "Identified for 100 percent of material underperformance each cycle at 100 percent",
        "Partner network revenue contribution tracked against target"],
  risks=["Attribution of a booking to a specific partner depending on correct channel tagging at booking",
         "Targets set without accounting for a partner's specific market conditions being systematically unfair",
         "Terminating a partner relationship in an underserved market leaving it without effective coverage",
         "A single weak period being treated the same as a persistent underperformance pattern"])
