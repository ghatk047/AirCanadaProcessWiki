# -*- coding: utf-8 -*-
"""AC-HR-TA — Talent Acquisition (5) and AC-HR-WM — Workforce Management and Payroll (5)."""
from content_lib import P, S

# ── TA: Talent Acquisition ──────────────────────────────────────────────────
P("AC-HR-TA-01",
  desc="Workforce demand is forecast and a requisition raised and approved, translating an operational or "
       "corporate hiring need into an active recruitment process in Phenom.",
  trig="A business function identifies a headcount need, or the crew establishment gap from AC-CM-CP-01 "
       "feeds a recruitment demand signal.",
  out="An approved requisition ready for candidate sourcing, correctly reflecting the role's actual "
      "requirements and approval level.",
  note="A requisition originating from crew establishment planning arrives with an unusually long lead "
      "time requirement, since crew hiring feeds directly into a training pipeline with its own fixed "
      "capacity constraints.",
  phases=["Demand identification", "Requisition creation", "Approval"],
  steps=[
    S("1.1","Identify workforce demand","Talent Acquisition Coordinator","Phenom",
      "Operational need or establishment gap","Identified demand with role requirements",
      "Identified within the standard planning cycle at 100 percent","N","N",
      "A crew-related requisition arrives with a longer lead time requirement given downstream training capacity limits"),
    S("2.1","Create requisition with role specification","Talent Acquisition Coordinator","Phenom",
      "Identified demand","Created requisition",
      "Created within 5 business days of demand identification at 95 percent","N","N",
      "Role specification quality directly determines candidate sourcing effectiveness later in the process"),
    S("3.1","Approve requisition against headcount authority","Hiring Manager","Phenom",
      "Created requisition","Approved requisition",
      "Approved within the standard approval service level at 90 percent","Y","N",
      "Approval delay for a time-sensitive operational role compounds into the same downstream capacity risk identified in AC-CM-CP-01"),
    S("3.2","Release requisition to sourcing","Talent Acquisition Coordinator","Phenom",
      "Approved requisition","Released requisition for sourcing",
      "Released within 1 business day of approval at 100 percent","N","N",
      "A requisition approved but not promptly released loses time from the same long lead window it was raised to protect"),
  ],
  kpis=["Identified within the standard planning cycle at 100 percent",
        "Created within 5 business days of demand identification at 95 percent",
        "Approved within the standard approval service level at 90 percent",
        "Requisition-to-approval cycle time meeting target"],
  risks=["A crew-related requisition arriving with a longer lead time given downstream training capacity limits",
         "Role specification quality directly determining candidate sourcing effectiveness later in the process",
         "Approval delay for a time-sensitive operational role compounding into a downstream capacity risk",
         "A requisition raised without clear headcount authority creating an approval bottleneck"])

P("AC-HR-TA-02",
  desc="Candidates are sourced and screened against an open requisition, from initial application through "
       "a shortlist ready for interview.",
  trig="An approved requisition opens for candidate sourcing.",
  out="A qualified shortlist of candidates ready for interview, sourced and screened against the role "
      "requirement.",
  note="Sourcing effectiveness for a specialised operational role, such as a licensed technician or a "
      "pilot, is materially different from a corporate role, given the much smaller qualified candidate "
      "pool available in the market.",
  phases=["Candidate sourcing", "Application screening", "Shortlist confirmation"],
  steps=[
    S("1.1","Source candidates against the role","Talent Acquisition Coordinator","Phenom",
      "Open requisition","Sourced candidate pool",
      "Sourced within the standard sourcing window at 90 percent","N","N",
      "A specialised operational role draws from a materially smaller qualified candidate pool than a corporate role"),
    S("2.1","Screen applications against role requirements","Talent Acquisition Coordinator","Phenom",
      "Sourced candidates","Screened candidate list",
      "Screened within 10 business days of application at 95 percent","N","N",
      "Screening criteria have to correctly reflect mandatory qualifications, such as a licence, versus preferred experience"),
    S("3.1","Confirm interview shortlist","Talent Acquisition Coordinator","Phenom",
      "Screened candidates","Confirmed shortlist",
      "Confirmed within 5 business days of screening completion at 100 percent","N","N",
      "A shortlist that is too narrow risks an unsuccessful search cycle for a hard-to-fill role"),
    S("3.2","Schedule shortlisted candidates for interview","Talent Acquisition Coordinator","Phenom",
      "Confirmed shortlist","Scheduled interviews",
      "Scheduled within 5 business days of shortlist confirmation at 90 percent","N","N",
      "Scheduling delay for a hard-to-fill role risks losing a candidate to a faster-moving competing process"),
  ],
  kpis=["Sourced within the standard sourcing window at 90 percent",
        "Screened within 10 business days of application at 95 percent",
        "Confirmed within 5 business days of screening completion at 100 percent",
        "Time to fill for specialised operational roles tracked against market benchmark"],
  risks=["A specialised operational role drawing from a materially smaller qualified candidate pool",
         "Screening criteria not correctly distinguishing mandatory qualifications from preferred experience",
         "A shortlist too narrow risking an unsuccessful search cycle for a hard-to-fill role",
         "Sourcing timeline pressure for an urgent role compressing genuine screening quality"])

P("AC-HR-TA-03",
  desc="A candidate is interviewed and selected, with an offer extended and negotiated to close the "
       "requisition.",
  trig="A shortlisted candidate is scheduled for interview.",
  out="A selected candidate with an accepted offer, or a documented reason the search continues.",
  note="Offer negotiation for a specialised or senior role has genuine commercial stakes, since losing a "
      "strong candidate over an avoidable negotiation misstep restarts a search that may already have taken "
      "months.",
  phases=["Interview process", "Selection decision", "Offer and negotiation"],
  steps=[
    S("1.1","Conduct structured interviews","Hiring Manager","Phenom",
      "Shortlisted candidate","Completed interview with assessment",
      "Completed within the interview panel's standard timeline at 90 percent","N","N",
      "Interview panel availability, particularly for an operational role, can be a genuine scheduling constraint"),
    S("2.1","Make selection decision","Hiring Manager","Phenom",
      "Completed interviews across candidates","Selected candidate",
      "Decided within 5 business days of final interview at 90 percent","Y","N",
      "A slow decision on a strong candidate creates a real risk of losing them to a competing offer"),
    S("2.2","Extend and negotiate offer","Talent Acquisition Coordinator","Phenom",
      "Selected candidate","Extended offer",
      "Extended within 3 business days of selection decision at 95 percent","N","N",
      "Losing a strong candidate over an avoidable negotiation misstep restarts a search that may already have taken months"),
    S("3.1","Confirm offer acceptance and close requisition","Talent Acquisition Coordinator","Phenom",
      "Extended offer","Confirmed acceptance with closed requisition",
      "Confirmed within the offer's validity window at 100 percent","N","N",
      "An unaccepted offer past its validity window has to be either extended or the search reopened"),
  ],
  kpis=["Completed within the interview panel's standard timeline at 90 percent",
        "Decided within 5 business days of final interview at 90 percent",
        "Extended within 3 business days of selection decision at 95 percent",
        "Offer acceptance rate meeting target"],
  risks=["A slow selection decision on a strong candidate creating a real risk of losing them to a competing offer",
         "Losing a strong candidate over an avoidable negotiation misstep, restarting a search that already took months",
         "Interview panel availability for an operational role being a genuine scheduling constraint",
         "An unaccepted offer past its validity window requiring either extension or a reopened search"])

P("AC-HR-TA-04",
  desc="A new hire's pre-employment clearance and security vetting is completed before their first day, "
       "covering background check and, where applicable, aviation-specific security clearance.",
  trig="An offer is accepted and pre-employment clearance is required before the start date.",
  out="Completed clearance confirming the candidate is cleared to begin employment, or a documented reason "
      "clearance could not be confirmed before the planned start date.",
  note="Aviation-specific security clearance requirements, particularly for a role with airside access, add "
      "a regulatory dimension to pre-employment screening that a purely corporate role does not carry, which "
      "means clearance timing has to be built into the offer's start date planning from the outset.",
  phases=["Background check initiation", "Aviation security clearance", "Clearance confirmation"],
  steps=[
    S("1.1","Initiate background check","Talent Acquisition Coordinator","Phenom",
      "Accepted offer","Initiated background check",
      "Initiated within 2 business days of offer acceptance at 100 percent","N","N",
      "Background check turnaround time varies and is not fully within Air Canada's own control"),
    S("2.1","Process aviation security clearance where required","Talent Acquisition Coordinator","Transport Canada CAWIS",
      "Role requiring airside or restricted access","Processed security clearance",
      "Processed within the regulatory timeframe for 100 percent of applicable roles","Y","N",
      "Aviation security clearance timing can extend beyond the planned start date and requires proactive scheduling"),
    S("2.2","Resolve a clearance finding","Talent Acquisition Coordinator","Phenom",
      "Flagged background or clearance finding","Resolved finding or withdrawn offer",
      "Resolved before the start date at 90 percent","N","Y",
      "A finding that surfaces close to the start date compresses the time available for resolution"),
    S("3.1","Confirm clearance and readiness for start date","Talent Acquisition Coordinator","Phenom",
      "Completed clearance","Confirmed readiness",
      "Confirmed before the planned start date at 95 percent","N","N",
      "Starting an employee in an airside role without confirmed clearance is a direct regulatory compliance failure"),
  ],
  kpis=["Initiated within 2 business days of offer acceptance at 100 percent",
        "Processed within the regulatory timeframe for 100 percent of applicable roles",
        "Resolved before the start date at 90 percent",
        "Confirmed before the planned start date at 95 percent"],
  risks=["Starting an employee in an airside role without confirmed clearance being a direct regulatory compliance failure",
         "Aviation security clearance timing extending beyond the planned start date without proactive scheduling",
         "Background check turnaround time not being fully within Air Canada's own control",
         "A finding surfacing close to the start date compressing the time available for resolution"])

P("AC-HR-TA-05",
  desc="A new employee is onboarded from confirmed start date through first-day and first-week enablement, "
       "provisioning system access, equipment and role-specific orientation.",
  trig="A new employee's confirmed start date arrives.",
  out="A fully enabled new employee, with system access, equipment and orientation completed by the end "
      "of the first week.",
  note="Onboarding coordinates several independent provisioning processes, including the workforce identity "
      "access lifecycle in AC-IT-CS-01, into a single first-day experience, which makes onboarding "
      "coordination quality, not any single step, the actual determinant of a smooth start.",
  phases=["Pre-arrival preparation", "First-day enablement", "First-week orientation"],
  steps=[
    S("1.1","Prepare access and equipment ahead of start date","Talent Acquisition Coordinator","Workforce Identity",
      "Confirmed start date","Prepared access and equipment request",
      "Prepared before the start date at 95 percent","N","N",
      "Access provisioning depends on the identity lifecycle process in AC-IT-CS-01 completing in time"),
    S("2.1","Complete first-day system access provisioning","IT Access Coordinator","Workforce Identity",
      "Prepared request","Provisioned first-day access",
      "Provisioned by the start of the first day at 90 percent","N","N",
      "A provisioning delay for a new employee's first day generates avoidable friction on their earliest impression"),
    S("2.2","Deliver role-specific orientation","Talent Acquisition Coordinator","Phenom",
      "New employee on first day","Delivered orientation",
      "Delivered within the first week for 100 percent of new hires at 100 percent","N","N",
      "Orientation content that is not tailored to the specific role provides limited practical value"),
    S("3.1","Confirm first-week enablement complete","Talent Acquisition Coordinator","Phenom",
      "Delivered orientation and provisioned access","Confirmed enablement",
      "Confirmed within 5 business days of start date at 90 percent","N","N",
      "Confirmation without genuine verification can mark an incomplete onboarding as complete"),
  ],
  kpis=["Prepared before the start date at 95 percent",
        "Provisioned by the start of the first day at 90 percent",
        "Delivered within the first week for 100 percent of new hires at 100 percent",
        "Confirmed within 5 business days of start date at 90 percent"],
  risks=["Access provisioning depending on the identity lifecycle process completing in time for the start date",
         "A provisioning delay on the first day generating avoidable friction on the new employee's earliest impression",
         "Orientation content not tailored to the specific role providing limited practical value",
         "Confirmation without genuine verification marking an incomplete onboarding as complete"])

# ── WM: Workforce Management and Payroll ────────────────────────────────────
P("AC-HR-WM-01",
  desc="Shift rosters are built for airport and contact centre staff, distinct from the crew rostering "
       "process in AC-CM-CR-01, covering ground-based workforce scheduling against forecast operational "
       "demand.",
  trig="The recurring shift scheduling cycle runs ahead of an operating period.",
  out="A published shift roster meeting forecast demand within labour cost and employee preference "
      "constraints.",
  note="Ground and contact centre shift scheduling shares the same fundamental demand-forecasting "
      "discipline as the contact centre workforce planning covered in AC-CX-CC-05, applied to a wider "
      "ground operations workforce with its own peak patterns.",
  phases=["Demand forecasting", "Shift build", "Roster publication"],
  steps=[
    S("1.1","Forecast demand by shift interval","Workforce Planning Analyst","Dayforce",
      "Historical demand and known operational drivers","Forecast demand by interval",
      "Forecast for 100 percent of scheduling intervals each cycle at 100 percent","N","N",
      "Airport demand forecasting has to account for the flight schedule's own peaks and troughs, distinct from contact centre call volume"),
    S("2.1","Build shift roster against forecast","Workforce Planning Analyst","Dayforce",
      "Forecast demand and available staff","Built shift roster",
      "Built to meet forecast demand within labour budget at 90 percent","N","N",
      "Balancing labour cost against service coverage has no single objectively correct answer"),
    S("2.2","Apply employee preference and fairness rules","Workforce Planning Analyst","Dayforce",
      "Built roster and preference data","Preference-adjusted roster",
      "Preferences accommodated where operationally feasible for 80 percent of requests","N","N",
      "Preference accommodation competes directly with meeting minimum coverage at every shift interval"),
    S("3.1","Publish shift roster","Workforce Planning Analyst","Dayforce",
      "Finalised roster","Published roster",
      "Published within the required lead time before the operating period at 100 percent","N","N",
      "A late-published roster reduces staff ability to plan personal commitments around their shifts"),
  ],
  kpis=["Forecast for 100 percent of scheduling intervals each cycle at 100 percent",
        "Built to meet forecast demand within labour budget at 90 percent",
        "Preferences accommodated where operationally feasible for 80 percent of requests",
        "Published within the required lead time before the operating period at 100 percent"],
  risks=["Balancing labour cost against service coverage having no single objectively correct answer",
         "Preference accommodation competing directly with meeting minimum coverage at every shift interval",
         "Airport demand forecasting needing to account for flight schedule peaks distinct from contact centre patterns",
         "A late-published roster reducing staff ability to plan personal commitments around their shifts"])

P("AC-HR-WM-02",
  desc="Employee time and attendance is captured and validated against the published roster, forming the "
       "record payroll calculation in AC-HR-WM-03 depends on.",
  trig="An employee's scheduled shift occurs.",
  out="Accurate time and attendance captured for every scheduled employee, ready for payroll calculation.",
  note="Time and attendance capture accuracy directly determines payroll accuracy downstream, which makes "
      "this the same kind of foundational record for the ground workforce that crew day-of-operations "
      "tracking in AC-CM-DO-01 is for flight crew.",
  phases=["Time capture", "Attendance validation", "Exception handling"],
  steps=[
    S("1.1","Capture time worked against the shift","Workforce Planning Analyst","Dayforce",
      "Employee clock-in and clock-out data","Captured time record",
      "Captured for 100 percent of scheduled shifts at 100 percent","N","N",
      "Time capture method varies by role and station, from a physical time clock to a system login event"),
    S("2.1","Validate attendance against the published roster","Workforce Planning Analyst","Dayforce",
      "Captured time and published roster","Validated attendance record",
      "Validated within 24 hours of the shift at 95 percent","N","N",
      "A discrepancy between actual and scheduled time requires resolution before it can feed payroll"),
    S("3.1","Resolve time and attendance exceptions","Workforce Planning Analyst","Dayforce",
      "Flagged discrepancy","Resolved exception",
      "Resolved within 3 business days of the shift at 90 percent","N","Y",
      "An unresolved exception delays payroll accuracy for the affected employee's next pay cycle"),
    S("3.2","Release validated record to payroll processing","Workforce Planning Analyst","Dayforce",
      "Resolved attendance record","Released record for payroll",
      "Released before the payroll processing cutoff at 100 percent","N","N",
      "A record not released before cutoff pushes the employee's pay to the following cycle"),
  ],
  kpis=["Captured for 100 percent of scheduled shifts at 100 percent",
        "Validated within 24 hours of the shift at 95 percent",
        "Resolved within 3 business days of the shift at 90 percent",
        "Time and attendance exception rate below target"],
  risks=["An unresolved exception delaying payroll accuracy for the affected employee's next pay cycle",
         "Time capture method varying by role and station, complicating consistent validation",
         "A discrepancy between actual and scheduled time requiring resolution before it can feed payroll",
         "Time and attendance capture accuracy directly determining downstream payroll accuracy"])

P("AC-HR-WM-03",
  desc="Payroll is processed for the ground and corporate workforce, applying the correct union rule set "
       "where applicable, distinct from the crew-specific pay calculation covered in AC-CM-CC-03.",
  trig="The recurring payroll processing cycle runs following validated time and attendance data.",
  out="Accurate payroll calculated and posted, correctly applying the applicable union rule set for each "
      "employee group.",
  note="Payroll for the ground workforce spans multiple bargaining units, CUPE, Teamsters and UNIFOR "
      "depending on role and station, each with distinct rule sets that have to be correctly applied "
      "alongside non-union corporate pay rules in the same processing cycle.",
  phases=["Time and attendance compilation", "Union rule application", "Payroll posting"],
  steps=[
    S("1.1","Compile validated time and attendance","Payroll Analyst","Dayforce",
      "Validated attendance records","Compiled payroll input",
      "Compiled for 100 percent of employees at period close at 100 percent","N","N",
      "Compilation has to correctly aggregate across employees who may work across multiple stations in one pay period"),
    S("2.1","Apply applicable union or corporate pay rules","Payroll Analyst","Dayforce",
      "Compiled input and employee bargaining unit","Calculated pay by employee",
      "Calculated correctly against the applicable rule set at 100 percent","Y","N",
      "Multiple bargaining units with distinct rule sets have to be correctly applied alongside non-union corporate rules"),
    S("2.2","Reconcile payroll calculation exceptions","Payroll Analyst","Dayforce",
      "Calculated pay with flagged anomalies","Resolved exceptions",
      "Resolved before the pay run deadline for 95 percent of exceptions at 100 percent","N","Y",
      "An exception unresolved before the pay run deadline delays that employee's payment"),
    S("3.1","Post payroll and disburse payment","Payroll Analyst","SAP S/4HANA",
      "Reconciled calculation","Posted and disbursed payroll",
      "Disbursed on the scheduled pay date at 100 percent","N","N",
      "A posting error discovered after disbursement requires a correction cycle that delays resolution for the employee"),
  ],
  kpis=["Compiled for 100 percent of employees at period close at 100 percent",
        "Calculated correctly against the applicable rule set at 100 percent",
        "Resolved before the pay run deadline for 95 percent of exceptions at 100 percent",
        "Disbursed on the scheduled pay date at 100 percent"],
  risks=["Multiple bargaining units with distinct rule sets needing correct application alongside non-union rules",
         "An exception unresolved before the pay run deadline delaying that employee's payment",
         "A posting error discovered after disbursement requiring a correction cycle that delays employee resolution",
         "Compilation needing to correctly aggregate across employees working multiple stations in one pay period"])

P("AC-HR-WM-04",
  desc="An employee's absence and leave, including illness, is managed through the process, coordinating "
       "coverage, entitlement tracking and return to work.",
  trig="An employee reports an absence or requests a planned leave.",
  out="Correctly managed absence with appropriate entitlement applied, coverage arranged where needed, and "
      "a coordinated return to work.",
  note="Unplanned absence at short notice creates an immediate coverage gap that the workforce management "
      "function has to fill from the same limited pool the shift roster in AC-HR-WM-01 already scheduled "
      "against forecast demand.",
  phases=["Absence reporting and entitlement determination", "Coverage arrangement", "Return to work"],
  steps=[
    S("1.1","Report and register absence","Workforce Planning Analyst","Dayforce",
      "Employee-reported absence","Registered absence with type",
      "Registered within the required notification window at 95 percent","N","N",
      "Short-notice absence for an operational shift creates an immediate coverage gap"),
    S("2.1","Determine leave entitlement","Workforce Planning Analyst","Dayforce",
      "Registered absence and employee record","Determined entitlement",
      "Determined correctly against policy for 100 percent of registered absences at 100 percent","Y","N",
      "Entitlement rules differ by absence type and employee tenure, and misapplication creates a pay accuracy issue downstream"),
    S("2.2","Arrange coverage for the absence","Workforce Planning Analyst","Dayforce",
      "Determined absence","Arranged coverage or accepted gap",
      "Coverage arranged for 90 percent of operationally critical absences","N","N",
      "Coverage has to be filled from the same limited staff pool the roster already scheduled against forecast demand"),
    S("3.1","Coordinate return to work","Workforce Planning Analyst","Dayforce",
      "Employee returning from leave","Coordinated return with updated roster",
      "Coordinated within 2 business days of the confirmed return date at 95 percent","N","N",
      "A return not coordinated with the roster leaves the employee's schedule inconsistent with actual availability"),
  ],
  kpis=["Registered within the required notification window at 95 percent",
        "Determined correctly against policy for 100 percent of registered absences at 100 percent",
        "Coverage arranged for 90 percent of operationally critical absences",
        "Coordinated within 2 business days of the confirmed return date at 95 percent"],
  risks=["Coverage having to be filled from the same limited staff pool already scheduled against forecast demand",
         "Entitlement rules differing by absence type and tenure, with misapplication creating a pay accuracy issue",
         "A return not coordinated with the roster leaving the schedule inconsistent with actual availability",
         "Short-notice absence for an operational shift creating an immediate coverage gap"])

P("AC-HR-WM-05",
  desc="Overtime and premium pay are controlled against budget and policy, balancing operational coverage "
       "needs against labour cost discipline.",
  trig="An operational need requires overtime or premium-rate coverage beyond the standard roster.",
  out="Overtime or premium pay authorised within budget and policy limits, with usage tracked against "
      "target.",
  note="Overtime is often the fastest way to fill an urgent coverage gap, which creates a structural "
      "tension between the operational manager wanting the gap filled now and the cost discipline this "
      "process exists to enforce.",
  phases=["Overtime need identification", "Authorisation", "Usage tracking"],
  steps=[
    S("1.1","Identify overtime or premium coverage need","Workforce Planning Analyst","Dayforce",
      "Coverage gap beyond standard roster","Identified need with justification",
      "Identified before the shift requiring coverage at 90 percent","N","N",
      "Overtime is often the fastest way to fill an urgent gap, creating pressure to bypass careful authorisation"),
    S("2.1","Authorise against budget and policy","Workforce Planning Analyst","Dayforce",
      "Identified need","Authorised or declined overtime",
      "Authorised within delegated budget authority at 95 percent","Y","N",
      "Authorisation under time pressure to fill an urgent gap can favour approval over cost discipline"),
    S("2.2","Assign overtime to eligible staff","Workforce Planning Analyst","Dayforce",
      "Authorised overtime","Assigned staff",
      "Assigned per the defined fairness and eligibility rules at 100 percent","N","N",
      "Overtime distribution has to be fair across eligible staff or it becomes a source of workplace grievance"),
    S("3.1","Track overtime usage against budget","Workforce Planning Analyst","SAP Analytics Cloud",
      "Assigned and worked overtime","Usage tracking report",
      "Tracked each period against budget at 100 percent","N","N",
      "Persistent overtime usage above budget can indicate an underlying structural roster gap, not just isolated incidents"),
  ],
  kpis=["Identified before the shift requiring coverage at 90 percent",
        "Authorised within delegated budget authority at 95 percent",
        "Assigned per the defined fairness and eligibility rules at 100 percent",
        "Overtime usage against budget tracked and trending within target"],
  risks=["Overtime being often the fastest way to fill an urgent gap, creating pressure to bypass careful authorisation",
         "Unfair overtime distribution across eligible staff becoming a source of workplace grievance",
         "Persistent overtime usage above budget indicating an underlying structural roster gap",
         "Authorisation under time pressure favouring approval over genuine cost discipline"])
