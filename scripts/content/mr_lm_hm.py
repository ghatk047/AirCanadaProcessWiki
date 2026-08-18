# -*- coding: utf-8 -*-
"""AC-MR-LM (5 remaining, LM-01 already in a_pilot) and AC-MR-HM — Heavy and Base Maintenance (6)."""
from content_lib import P, S

# ── LM: Line Maintenance (remaining 5) ──────────────────────────────────────
P("AC-MR-LM-02",
  desc="A defect reported by the flight crew is entered into the aircraft technical log and coded in TRAX, "
       "the record every subsequent maintenance action against that defect traces back to.",
  trig="A flight crew member identifies and reports a defect during or after a flight.",
  out="A correctly coded technical log entry in TRAX, ready for maintenance control assessment and "
      "rectification planning.",
  note="The technical log entry is the origin record for the entire defect lifecycle; an ambiguous or "
      "poorly coded entry here creates interpretation work at every downstream step that a precise entry "
      "would have avoided.",
  phases=["Defect capture", "Technical log entry", "TRAX coding"],
  steps=[
    S("1.1","Capture crew-reported defect description","Line Maintenance Technician","TRAX",
      "Crew verbal or written defect report","Captured defect description",
      "Captured within 15 minutes of report at 100 percent","N","N",
      "Crew descriptions are operational in nature and need technical interpretation before coding"),
    S("2.1","Enter defect in the aircraft technical log","Line Maintenance Technician","TRAX",
      "Captured description","Technical log entry",
      "Entered before the aircraft's next dispatch at 100 percent","N","N",
      "A defect not entered before dispatch can be missed by the next station's maintenance review"),
    S("3.1","Code defect against the correct ATA chapter","Line Maintenance Technician","TRAX",
      "Log entry","Coded defect in TRAX",
      "Coded correctly for 95 percent of entries at first pass","Y","N",
      "Incorrect ATA chapter coding misdirects the defect into the wrong reliability trend category"),
    S("3.2","Route defect to maintenance control for assessment","Line Maintenance Technician","TRAX",
      "Coded defect","Routed defect for MEL and rectification assessment",
      "Routed within 5 minutes of coding at 100 percent","N","N",
      "A defect not promptly routed delays the MEL applicability check in AC-MR-LM-03"),
  ],
  kpis=["Captured within 15 minutes of report at 100 percent",
        "Entered before the aircraft's next dispatch at 100 percent",
        "Coded correctly for 95 percent of entries at first pass",
        "Defect recoding rate after initial entry below target"],
  risks=["An ambiguous or poorly coded entry creating interpretation work at every downstream step",
         "A defect not entered before dispatch being missed by the next station's maintenance review",
         "Incorrect ATA chapter coding misdirecting the defect into the wrong reliability trend category",
         "Crew operational descriptions needing technical interpretation before they can be correctly coded"])

P("AC-MR-LM-03",
  desc="A defect that cannot be immediately rectified is deferred under the minimum equipment list, with "
      "the rectification interval tracked until the deferral is closed.",
  trig="A defect cannot be rectified before the aircraft's next scheduled departure and MEL relief is "
      "available.",
  out="A correctly deferred defect with a tracked rectification interval, closed within its permitted "
      "window.",
  note="An MEL deferral is a documented, time-bound exception to full serviceability, and the discipline of "
      "closing it within its permitted interval is what keeps deferral a controlled tool rather than a way "
      "of quietly accumulating unaddressed defects.",
  phases=["MEL applicability check", "Deferral entry", "Interval tracking"],
  steps=[
    S("1.1","Assess MEL applicability for the defect","Maintenance Controller","TRAX",
      "Defect and aircraft configuration","MEL applicability determination",
      "Determined before dispatch for 100 percent of deferral candidates","Y","N",
      "MEL applicability depends on precise aircraft configuration that has to be correctly matched"),
    S("2.1","Enter the deferral with rectification interval","Maintenance Controller","TRAX",
      "MEL applicability","Entered deferral with tracked interval",
      "Entered before dispatch for 100 percent of deferred defects","N","N",
      "An interval calculated from the wrong reference date understates the actual time remaining"),
    S("3.1","Track deferral status through the rectification interval","Maintenance Controller","TRAX",
      "Entered deferral","Tracked status against interval",
      "Tracked continuously for 100 percent of open deferrals","N","N",
      "A deferral tracked only at the maintenance system level is not automatically visible to ops control planning around it"),
    S("3.2","Close deferral within the permitted interval","Line Maintenance Technician","TRAX",
      "Tracked deferral approaching interval end","Closed deferral with rectification completed",
      "Zero deferrals closed outside their permitted interval","N","Y",
      "A deferral not closed in time forces an unplanned aircraft removal from service"),
  ],
  kpis=["Determined before dispatch for 100 percent of deferral candidates",
        "Entered before dispatch for 100 percent of deferred defects",
        "Tracked continuously for 100 percent of open deferrals",
        "Zero deferrals closed outside their permitted interval"],
  risks=["A deferral not closed within its permitted interval forcing an unplanned aircraft removal",
         "An interval calculated from the wrong reference date understating the actual time remaining",
         "A deferral not being automatically visible to ops control planning around it",
         "MEL applicability depending on precise aircraft configuration matching that is easy to get wrong"])

P("AC-MR-LM-04",
  desc="An aircraft-on-ground event is responded to at a line station, mobilising parts, technician "
       "resource and technical support to return the aircraft to service as quickly as possible.",
  trig="A defect prevents an aircraft from being dispatchable and the aircraft becomes AOG.",
  out="The aircraft returned to service with the defect rectified, or a recovery plan executed if immediate "
      "rectification is not possible at the station.",
  note="An AOG event has cascading network consequences beyond the single aircraft, since every flight in "
      "that aircraft's onward rotation is affected until it returns to service, which is why AOG response "
      "carries a materially higher urgency than a routine line defect.",
  phases=["AOG declaration and assessment", "Resource mobilisation", "Return to service or recovery"],
  steps=[
    S("1.1","Declare AOG and assess the defect","Maintenance Controller","TRAX",
      "Non-dispatchable defect","Declared AOG with defect assessment",
      "Declared within 15 minutes of the defect being confirmed non-dispatchable at 100 percent","N","N",
      "Assessment under AOG time pressure has to balance speed against getting the diagnosis right the first time"),
    S("2.1","Mobilise required parts","Materials Planner","Aeroxchange",
      "Assessed defect and required parts","Mobilised parts to the AOG station",
      "Mobilised within the target response time at 85 percent","N","N",
      "A part not stocked at the AOG station requires urgent sourcing that can be the critical path"),
    S("2.2","Mobilise qualified technician resource","Line Maintenance Supervisor","TRAX",
      "Assessed defect requiring specific qualification","Mobilised qualified technician",
      "Mobilised within the target response time at 85 percent","N","N",
      "The required qualification may not be available at every station, requiring technician travel"),
    S("3.1","Rectify and return aircraft to service","Certifying Technician","TRAX",
      "Mobilised parts and technician","Rectified and certified aircraft",
      "Returned to service within the target AOG resolution time at 80 percent","N","N",
      "Network impact accumulates for every hour the aircraft remains AOG, adding pressure without compromising the work"),
  ],
  kpis=["Declared within 15 minutes of the defect being confirmed non-dispatchable at 100 percent",
        "Mobilised parts within the target response time at 85 percent",
        "Mobilised technician resource within the target response time at 85 percent",
        "Returned to service within the target AOG resolution time at 80 percent"],
  risks=["A part not stocked at the AOG station requiring urgent sourcing that becomes the critical path",
         "The required technician qualification not being available at every station",
         "Network impact accumulating for every hour AOG, creating pressure that must not compromise the actual work",
         "Assessment under time pressure balancing speed against getting the diagnosis right the first time"])

P("AC-MR-LM-05",
  desc="Transit and daily checks are performed within the turnaround or overnight ground time, confirming "
       "the aircraft's continued airworthiness for the next flight or flying day.",
  trig="An aircraft's scheduled transit or daily check interval comes due.",
  out="A completed check confirming continued airworthiness, with the aircraft cleared for its next flight "
      "or flying day.",
  note="Transit and daily checks are the routine backbone of line maintenance, and their reliability depends "
      "on being consistently performed within a ground time that also has to accommodate every other "
      "turnaround service, as covered in AC-GO-GT-01.",
  phases=["Check scheduling", "Check execution", "Clearance"],
  steps=[
    S("1.1","Schedule the check within available ground time","Line Maintenance Supervisor","TRAX",
      "Check due date and turnaround plan","Scheduled check within ground time",
      "Scheduled within available ground time at 90 percent","N","N",
      "A check competing for the same ground time as every other turnaround service can be squeezed"),
    S("2.1","Perform the check per the task card","Line Maintenance Technician","TRAX eMobility",
      "Task card and aircraft","Completed check with findings",
      "Completed within the scheduled window at 90 percent","N","N",
      "A finding during the check can extend the check beyond its scheduled time, competing with departure pressure"),
    S("3.1","Certify and clear the aircraft","Certifying Technician","TRAX",
      "Completed check","Certified aircraft cleared for flight",
      "Certified before the required departure time at 95 percent","N","N",
      "Certification depends on an authorised technician being physically available at the check completion time"),
    S("3.2","Close the check record in TRAX","Line Maintenance Supervisor","TRAX",
      "Certified clearance","Closed check record",
      "Closed within 1 hour of certification at 100 percent","N","N",
      "An unclosed check record leaves the next station's maintenance review without a clean starting point"),
  ],
  kpis=["Scheduled within available ground time at 90 percent",
        "Completed within the scheduled window at 90 percent",
        "Certified before the required departure time at 95 percent",
        "Check-related departure delay rate below target"],
  risks=["A check competing for the same ground time as every other turnaround service, risking being squeezed",
         "A finding during the check extending it beyond its scheduled time under departure pressure",
         "Certification depending on an authorised technician being physically available at completion time",
         "Routine check reliability depending on consistency across a very high volume of daily occurrences"])

P("AC-MR-LM-06",
  desc="A third-party contract maintenance provider performs line maintenance on Air Canada's behalf at a "
       "station without in-house technician coverage, governed by a service agreement.",
  trig="An aircraft requires line maintenance at a station where Air Canada relies on contract maintenance "
       "coverage.",
  out="Contract maintenance performed to Air Canada's standard and certified, with the work correctly "
      "recorded in TRAX despite being performed by a third party.",
  note="Contract line maintenance stations are a genuine oversight gap risk, since the work itself happens "
      "outside Air Canada's direct supervision, which makes correct recording and periodic audit the actual "
      "controls rather than direct oversight.",
  phases=["Contract station engagement", "Contract maintenance execution", "Record integration and audit"],
  steps=[
    S("1.1","Engage the contract maintenance provider","Maintenance Controller","Aeroxchange",
      "Aircraft requiring service at the contract station","Engaged contract provider",
      "Engaged within the required lead time at 95 percent","N","N",
      "Contract station engagement is coordinated remotely without direct Air Canada supervision at the point of work"),
    S("2.1","Contract technician performs and certifies work","Contract Technician","TRAX",
      "Task requirement per Air Canada standard","Completed and certified work",
      "Completed to Air Canada's specified standard at 100 percent","N","N",
      "Verifying work quality against Air Canada's standard is harder without direct on-site supervision"),
    S("2.2","Transmit work record for TRAX entry","Maintenance Controller","TRAX",
      "Completed contract work","Work record transmitted for entry",
      "Transmitted within 24 hours of completion at 95 percent","N","N",
      "A work record not promptly transmitted delays the aircraft's technical record currency"),
    S("3.1","Audit contract station performance periodically","Maintenance Controller","TRAX",
      "Cumulative contract work history","Audit findings",
      "Audited on a recurring cycle for 100 percent of contract stations","N","N",
      "Periodic audit is the actual oversight mechanism given the absence of direct supervision at the point of work"),
  ],
  kpis=["Engaged within the required lead time at 95 percent",
        "Completed to Air Canada's specified standard at 100 percent",
        "Transmitted within 24 hours of completion at 95 percent",
        "Audited on a recurring cycle for 100 percent of contract stations"],
  risks=["Contract work happening outside Air Canada's direct supervision at the actual point of work",
         "Verifying work quality against Air Canada's standard being harder without on-site supervision",
         "A work record not promptly transmitted delaying the aircraft's technical record currency",
         "Periodic audit being the actual oversight control given the absence of direct supervision"])

# ── HM: Heavy and Base Maintenance ──────────────────────────────────────────
P("AC-MR-HM-01",
  desc="A heavy check is planned and its slot booked at a maintenance base months ahead, coordinating the "
       "aircraft's availability, check scope and base capacity into a committed check window.",
  trig="An aircraft's heavy check interval approaches based on flight hours, cycles or calendar time.",
  out="A booked heavy check slot with the aircraft's fleet rotation adjusted to make it available for the "
      "committed window.",
  note="Heavy check planning has to work backward from the base's slot availability, which is booked months "
      "ahead, into the network schedule established in AC-NP-FA-03, making it one of the longest-lead-time "
      "coordination points between maintenance and network planning.",
  phases=["Check interval forecasting", "Slot booking", "Rotation coordination"],
  steps=[
    S("1.1","Forecast heavy check due date","Heavy Maintenance Planner","TRAX",
      "Utilisation history and check interval","Forecast check due date",
      "Forecast for 100 percent of the fleet at the required planning horizon","N","N",
      "Utilisation running ahead of or behind plan shifts the forecast due date"),
    S("2.1","Book maintenance base slot","Heavy Maintenance Planner","TRAX",
      "Forecast due date and base availability","Booked slot",
      "Booked within the required lead time before the check is due at 100 percent","N","N",
      "Base slot availability is finite and shared across the whole fleet, so booking timing is competitive"),
    S("2.2","Coordinate with network fleet assignment","Heavy Maintenance Planner","Lufthansa Systems NetLine",
      "Booked slot","Fleet rotation adjusted for check availability",
      "Coordinated before the affected season's schedule freeze at 100 percent","Y","N",
      "A slot booked without coordinating fleet availability can conflict with the committed flying schedule"),
    S("3.1","Confirm aircraft availability for the check window","Heavy Maintenance Planner","TRAX",
      "Coordinated rotation","Confirmed aircraft availability",
      "Confirmed before the check window opens at 100 percent","N","N",
      "A confirmed availability that later changes forces a slot rebooking, competing with other aircraft for base capacity"),
  ],
  kpis=["Forecast for 100 percent of the fleet at the required planning horizon",
        "Booked within the required lead time before the check is due at 100 percent",
        "Coordinated before the affected season's schedule freeze at 100 percent",
        "Confirmed before the check window opens at 100 percent"],
  risks=["A slot booked without coordinating fleet availability conflicting with the committed flying schedule",
         "Base slot availability being finite and shared across the whole fleet, making booking timing competitive",
         "A confirmed availability later changing and forcing a slot rebooking against other aircraft",
         "Utilisation running ahead of or behind plan shifting the forecast check due date"])

P("AC-MR-HM-02",
  desc="A base maintenance work package is built for a committed heavy check, defining the full scope of "
       "scheduled tasks, expected findings work and modification embodiments for the check.",
  trig="A heavy check slot is booked and work package build begins ahead of aircraft induction.",
  out="A complete work package defining scheduled tasks, anticipated findings allowance and modification "
      "scope for the check.",
  note="A well-scoped work package is what keeps a heavy check within its planned duration, since the gap "
      "between anticipated and actual findings work is the single largest source of check duration overrun.",
  phases=["Scope definition", "Modification embodiment planning", "Package finalisation"],
  steps=[
    S("1.1","Define scheduled task scope","Heavy Maintenance Planner","TRAX",
      "Check type and maintenance programme","Defined scheduled task scope",
      "Defined for 100 percent of committed checks before induction","N","N",
      "Task scope has to correctly reference the current maintenance programme revision"),
    S("2.1","Plan modification and service bulletin embodiment","Engineering Planner","TRAX",
      "Open modification and service bulletin backlog","Planned embodiment scope for the check",
      "Planned before package finalisation for 100 percent of eligible modifications","N","N",
      "Embodying every eligible modification in one check can extend duration beyond what the base slot allows"),
    S("2.2","Estimate anticipated findings allowance","Heavy Maintenance Planner","TRAX",
      "Aircraft age, history and check type","Estimated findings allowance",
      "Estimated using documented historical basis for 100 percent of checks","N","N",
      "The gap between anticipated and actual findings work is the largest source of check duration overrun"),
    S("3.1","Finalise and issue the work package","Heavy Maintenance Planner","TRAX",
      "Defined scope and estimated allowance","Finalised work package",
      "Finalised before aircraft induction at 100 percent","N","N",
      "A package finalised without adequate findings allowance sets an unrealistic duration expectation from the start"),
  ],
  kpis=["Defined for 100 percent of committed checks before induction",
        "Planned before package finalisation for 100 percent of eligible modifications",
        "Estimated using documented historical basis for 100 percent of checks",
        "Actual check duration within the planned window at target rate"],
  risks=["The gap between anticipated and actual findings work being the largest source of check duration overrun",
         "Embodying every eligible modification in one check extending duration beyond what the base slot allows",
         "Task scope not correctly referencing the current maintenance programme revision",
         "A package finalised without adequate findings allowance setting an unrealistic duration expectation"])

P("AC-MR-HM-03",
  desc="Third-party MRO vendors performing heavy maintenance work on Air Canada's behalf are managed and "
       "governed against contracted service levels and quality standards.",
  trig="A heavy check or specific maintenance scope is contracted to a third-party MRO vendor.",
  out="Vendor-performed work meeting Air Canada's quality and airworthiness standards, delivered within "
      "contracted timelines.",
  note="Air Canada remains ultimately accountable to Transport Canada for airworthiness regardless of who "
      "physically performs the work, which means vendor governance is a compliance control, not just a "
      "commercial contract management exercise.",
  phases=["Vendor scope agreement", "Work oversight", "Delivery and quality confirmation"],
  steps=[
    S("1.1","Agree work scope and standard with the vendor","MRO Vendor Manager","SAP Ariba",
      "Committed check and vendor contract","Agreed scope and standard",
      "Agreed before work begins for 100 percent of contracted checks","N","N",
      "Scope ambiguity between Air Canada's expectation and the vendor's contract terms surfaces mid-check"),
    S("2.1","Provide oversight during vendor execution","MRO Vendor Manager","TRAX",
      "Agreed scope and in-progress work","Oversight findings",
      "On-site or remote oversight maintained for 100 percent of the check duration","N","N",
      "The depth of practical oversight Air Canada can maintain at a vendor's own facility is inherently limited"),
    S("2.2","Review and approve findings work","MRO Vendor Manager","TRAX",
      "Vendor-identified findings","Approved or queried findings disposition",
      "Reviewed within the vendor's required response window at 95 percent","Y","N",
      "A findings disposition approved too quickly under schedule pressure risks an inadequate technical review"),
    S("3.1","Confirm delivery meets quality standard","MRO Vendor Manager","TRAX",
      "Completed vendor work","Confirmed quality acceptance",
      "Confirmed before aircraft release for 100 percent of vendor checks","N","N",
      "Air Canada remains accountable to Transport Canada regardless of which organisation physically performed the work"),
  ],
  kpis=["Agreed before work begins for 100 percent of contracted checks",
        "On-site or remote oversight maintained for 100 percent of the check duration",
        "Reviewed within the vendor's required response window at 95 percent",
        "Confirmed before aircraft release for 100 percent of vendor checks"],
  risks=["Air Canada remaining accountable to Transport Canada regardless of which organisation performed the work",
         "The depth of practical oversight at a vendor's own facility being inherently limited",
         "A findings disposition approved too quickly under schedule pressure risking inadequate technical review",
         "Scope ambiguity between Air Canada's expectation and the vendor's contract terms surfacing mid-check"])

P("AC-MR-HM-04",
  desc="A component is removed for shop visit, routed to the appropriate repair facility, and tracked "
       "through repair or overhaul back to a serviceable condition.",
  trig="A component reaches its removal interval, or a defect requires its removal for shop repair.",
  out="A component repaired or overhauled and returned to serviceable stock, correctly tracked through the "
      "full shop visit cycle.",
  note="Component routing decisions balance repair cost, turnaround time and shop capability, and a "
      "component sent to the wrong facility or without correct documentation can lose weeks in transit and "
      "administrative correction rather than repair time itself.",
  phases=["Removal and routing decision", "Repair tracking", "Return to serviceable stock"],
  steps=[
    S("1.1","Remove component and confirm routing destination","Materials Planner","TRAX",
      "Removed component and repair capability data","Confirmed routing destination",
      "Routing confirmed before shipment for 100 percent of removed components","N","N",
      "Routing to the wrong facility, one lacking the specific capability, loses time in redirection"),
    S("2.1","Ship component with correct documentation","Materials Planner","Aeroxchange",
      "Confirmed routing","Shipped component with documentation",
      "Documentation complete for 100 percent of shipments at 100 percent","N","N",
      "Incomplete documentation can delay a shop's ability to even begin work on receipt"),
    S("2.2","Track repair progress against expected turnaround","Materials Planner","TRAX",
      "Shipped component","Tracked repair status",
      "Tracked continuously against expected turnaround for 100 percent of open shop visits","N","N",
      "Turnaround time overruns are not always proactively flagged by the repair facility itself"),
    S("3.1","Receive and return component to serviceable stock","Materials Planner","TRAX",
      "Returned component with certification","Confirmed serviceable stock entry",
      "Confirmed serviceable within 48 hours of receipt at 100 percent","N","N",
      "A component received without complete certification documentation cannot legally be returned to serviceable stock"),
  ],
  kpis=["Routing confirmed before shipment for 100 percent of removed components",
        "Documentation complete for 100 percent of shipments at 100 percent",
        "Tracked continuously against expected turnaround for 100 percent of open shop visits",
        "Confirmed serviceable within 48 hours of receipt at 100 percent"],
  risks=["Routing to a facility lacking the specific capability required, losing time in redirection",
         "Incomplete documentation delaying a shop's ability to even begin work on receipt",
         "A component received without complete certification documentation being unable to legally return to stock",
         "Turnaround time overruns not being proactively flagged by the repair facility itself"])

P("AC-MR-HM-05",
  desc="A cabin reconfiguration or modification is executed during heavy maintenance, changing seat "
       "configuration or installing new equipment within the check's scheduled ground time.",
  trig="A committed cabin reconfiguration or modification programme reaches a specific aircraft's check "
       "window.",
  out="A completed cabin reconfiguration or modification, certified and correctly reflected in the "
      "aircraft's configuration record.",
  note="A cabin reconfiguration has commercial as well as technical stakes, since a delayed reconfiguration "
      "means the aircraft returns to revenue service with the wrong product for however long the schedule "
      "has already assumed the new configuration.",
  phases=["Modification scope confirmation", "Execution within the check window", "Configuration record update"],
  steps=[
    S("1.1","Confirm modification scope and materials availability","Engineering Planner","TRAX",
      "Committed reconfiguration programme","Confirmed scope and materials",
      "Confirmed before aircraft induction at 100 percent","N","N",
      "Materials for a large reconfiguration have a long lead time and have to be pre-positioned before induction"),
    S("2.1","Execute reconfiguration within the check window","Base Maintenance Technician","TRAX",
      "Confirmed scope and induced aircraft","Executed reconfiguration",
      "Completed within the check's scheduled duration at 85 percent","N","N",
      "A reconfiguration competing for the same check window as scheduled and findings work can be squeezed"),
    S("2.2","Certify the modification","Certifying Technician","TRAX",
      "Completed reconfiguration","Certified modification",
      "Certified before the aircraft's return to service at 100 percent","Y","N",
      "Certification for a major cabin change requires specific engineering sign-off beyond standard task certification"),
    S("3.1","Update configuration record for commercial systems","Engineering Planner","Amadeus Altea Inventory",
      "Certified modification","Updated configuration record",
      "Updated before the aircraft returns to revenue service at 100 percent","N","N",
      "A configuration record not updated in inventory means the aircraft sells against its old seat map"),
  ],
  kpis=["Confirmed before aircraft induction at 100 percent",
        "Completed within the check's scheduled duration at 85 percent",
        "Certified before the aircraft's return to service at 100 percent",
        "Updated before the aircraft returns to revenue service at 100 percent"],
  risks=["A configuration record not updated in inventory meaning the aircraft sells against its old seat map",
         "A reconfiguration competing for the same check window as scheduled and findings work",
         "Materials for a large reconfiguration having a long lead time requiring pre-positioning before induction",
         "A delayed reconfiguration returning the aircraft to service with the wrong product for the schedule already assumed"])

P("AC-MR-HM-06",
  desc="Return to service documentation is completed and the heavy check is formally closed, certifying "
       "the aircraft airworthy and releasing it back into the operational fleet.",
  trig="All work in a heavy check work package is completed and the aircraft is ready for return to "
      "service.",
  out="A certified airworthy aircraft released back into the operational fleet, with the check formally "
      "closed and documented.",
  note="Return to service closure is the point where every finding, modification and scheduled task "
      "performed during the check converges into a single certification statement that the aircraft is "
      "airworthy.",
  phases=["Work completion verification", "Certification", "Fleet release"],
  steps=[
    S("1.1","Verify all work package items are complete","Heavy Maintenance Planner","TRAX",
      "Work package and completed task records","Verified completion status",
      "Verified for 100 percent of work package items before certification at 100 percent","N","N",
      "An item marked complete without proper closure documentation is not actually verifiable as complete"),
    S("2.1","Compile airworthiness certification documentation","Certifying Technician","TRAX",
      "Verified completion","Compiled certification documentation",
      "Compiled for 100 percent of required documentation before sign-off at 100 percent","N","N",
      "Documentation compiled across a large check spans many individual task cards that all need to be present"),
    S("2.2","Issue the certificate of airworthiness release","Certifying Technician","TRAX",
      "Compiled documentation","Issued certification",
      "Issued before the aircraft leaves the maintenance base at 100 percent","Y","N",
      "The certifying technician's authorisation has to correctly cover the full scope of work performed"),
    S("3.1","Release aircraft to the operational fleet","Heavy Maintenance Planner","Lufthansa Systems NetLine",
      "Issued certification","Released aircraft with updated status",
      "Released within 24 hours of certification at 100 percent","N","N",
      "A release delayed after certification without cause consumes schedule buffer the network plan is counting on"),
  ],
  kpis=["Verified for 100 percent of work package items before certification at 100 percent",
        "Compiled for 100 percent of required documentation before sign-off at 100 percent",
        "Issued before the aircraft leaves the maintenance base at 100 percent",
        "Released within 24 hours of certification at 100 percent"],
  risks=["An item marked complete without proper closure documentation not actually being verifiable as complete",
         "The certifying technician's authorisation not correctly covering the full scope of work performed",
         "Documentation across a large check spanning many task cards that all need to be present and correct",
         "A release delayed after certification without cause consuming schedule buffer the network plan counts on"])
