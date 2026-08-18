# -*- coding: utf-8 -*-
"""AC-CM-DO — Day-of-Operations Crew Tracking (6) and AC-CM-CC — Compliance, Training and Pay (6)."""
from content_lib import P, S

# ── DO: Day-of-Operations Crew Tracking ─────────────────────────────────────
P("AC-CM-DO-01",
  desc="Crew sign-on is tracked at each duty period, confirming a crew member has actually reported for "
       "duty against the roster and flagging any no-show or late arrival immediately.",
  trig="A crew member's scheduled duty period begins.",
  out="Confirmed sign-on status for every scheduled crew member, with any no-show or delay flagged for "
      "immediate action.",
  note="Sign-on tracking is the bridge between the published roster and operational reality; a delay in "
      "detecting a no-show delays every recovery action that depends on knowing the crew is actually "
      "unavailable.",
  phases=["Duty period monitoring", "Sign-on confirmation", "Exception flagging"],
  steps=[
    S("1.1","Monitor scheduled duty period start","Crew Tracking Coordinator","Jeppesen Crew",
      "Published roster and current time","Monitored duty period status",
      "Monitored continuously for 100 percent of scheduled duty periods","N","N",
      "Sign-on location can vary between crew report points, which complicates uniform monitoring"),
    S("2.1","Confirm crew sign-on","Crew Tracking Coordinator","Jeppesen Crew",
      "Crew member sign-on action","Confirmed sign-on status",
      "Confirmed within 5 minutes of the scheduled report time at 95 percent","N","N",
      "A system sign-on delay does not always mean the crew member is actually absent"),
    S("3.1","Flag no-show or late arrival","Crew Tracking Coordinator","Jeppesen OCC",
      "Unconfirmed sign-on past the threshold","Flagged exception",
      "Flagged within 10 minutes of the missed report time at 100 percent","N","Y",
      "A flag raised too early risks a false alarm; raised too late delays the recovery response"),
    S("3.2","Initiate crew recovery for a confirmed no-show","Crew Tracking Coordinator","Jeppesen OCC",
      "Confirmed no-show","Initiated recovery via reassignment or reserve call-out",
      "Recovery initiated within 5 minutes of confirmation at 100 percent","N","N",
      "Recovery initiation timing directly determines whether the affected flight departs on schedule"),
  ],
  kpis=["Monitored continuously for 100 percent of scheduled duty periods",
        "Confirmed within 5 minutes of the scheduled report time at 95 percent",
        "Flagged within 10 minutes of the missed report time at 100 percent",
        "No-show detection false positive rate below target"],
  risks=["A delay in detecting a genuine no-show delaying every downstream recovery action",
         "A flag raised too early producing a false alarm that consumes recovery attention unnecessarily",
         "Sign-on location variability across report points complicating uniform, reliable monitoring",
         "A system sign-on delay being mistaken for actual crew absence, or the reverse"])

P("AC-CM-DO-02",
  desc="A crew member's flight and duty time legality is verified continuously through the operating day, "
       "particularly during irregular operations when the original roster assumption no longer holds.",
  trig="An operational change affects a crew member's originally planned duty, requiring legality "
       "re-verification.",
  out="Confirmed crew legality against actual, as-flown duty time, with any legality risk flagged before it "
      "is breached.",
  note="A crew member's legality can erode gradually through a day of cascading delays, so continuous "
      "re-verification during disruption is materially different from the single legality check performed "
      "at original roster award.",
  phases=["Real-time duty tracking", "Legality recalculation", "Risk flagging"],
  steps=[
    S("1.1","Track actual duty time in real time","Crew Tracking Coordinator","Jeppesen Crew",
      "Actual flight and duty progress","Tracked actual duty time",
      "Tracked continuously for 100 percent of active duty periods","N","N",
      "Actual duty time diverges from planned duty time as soon as any delay occurs"),
    S("2.1","Recalculate legality against cumulative duty","Crew Tracking Coordinator","Jeppesen Crew",
      "Tracked actual duty time","Recalculated legality position",
      "Recalculated within 5 minutes of a material duty change at 100 percent","Y","N",
      "Legality recalculation has to account for cumulative duty across the full pairing, not just the current leg"),
    S("3.1","Flag crew approaching a legality limit","Crew Tracking Coordinator","Jeppesen OCC",
      "Recalculated legality position","Flagged approaching-limit crew",
      "Flagged at least 60 minutes before the projected limit at 90 percent","N","Y",
      "A flag that arrives too close to the actual limit leaves no time for a recovery option"),
    S("3.2","Trigger a swap or reassignment before the limit is reached","Crew Tracking Coordinator","Jeppesen Crew",
      "Flagged approaching-limit crew","Initiated reassignment ahead of the limit",
      "Initiated before the projected limit for 100 percent of flagged cases","N","N",
      "Waiting until the limit is reached rather than acting on the flag removes the whole point of early warning"),
  ],
  kpis=["Tracked continuously for 100 percent of active duty periods",
        "Recalculated within 5 minutes of a material duty change at 100 percent",
        "Flagged at least 60 minutes before the projected limit at 90 percent",
        "Zero confirmed legality breaches during irregular operations"],
  risks=["Crew legality eroding gradually through a day of cascading delays without continuous re-verification",
         "A flag arriving too close to the actual limit leaving no time for a genuine recovery option",
         "Legality recalculation failing to account for cumulative duty across the full pairing",
         "Actual duty time diverging from the planned roster assumption as soon as any delay occurs"])

P("AC-CM-DO-03",
  desc="A crew member is reassigned during a disruption when their originally planned duty can no longer be "
       "flown, drawing on reserve or legal open crew to maintain flight coverage.",
  trig="A disruption invalidates a crew member's originally planned assignment, or the crew swap process "
       "in AC-FO-OC-03 requires a corresponding crew reassignment.",
  out="A legally compliant crew reassignment maintaining flight coverage, with the affected crew member's "
      "roster correctly updated.",
  note="Crew reassignment during disruption competes directly with the reserve sizing decisions made months "
      "earlier in AC-CM-CP-03, so a disruption severe enough to exhaust local reserve exposes exactly the "
      "trade-off that reserve sizing was trying to manage.",
  phases=["Reassignment need identification", "Legal candidate identification", "Assignment execution"],
  steps=[
    S("1.1","Identify the reassignment requirement","Crew Tracking Coordinator","Jeppesen OCC",
      "Disrupted crew assignment","Identified reassignment need",
      "Identified within 10 minutes of the disruption at 100 percent","N","N",
      "The reassignment need is often identified simultaneously with several other disrupted assignments"),
    S("2.1","Identify legally available candidate crew","Crew Tracking Coordinator","Jeppesen Crew",
      "Reassignment need and reserve position","Candidate crew list",
      "Candidates identified within 15 minutes of the need at 90 percent","N","N",
      "Legal candidate identification has to check duty time, qualification and base simultaneously"),
    S("2.2","Select and contact the reassigned crew member","Crew Tracking Coordinator","Jeppesen Crew",
      "Candidate list","Contacted and confirmed crew member",
      "Contacted within 20 minutes of candidate identification at 85 percent","N","N",
      "Contact success rate depends on crew reachability, which is not guaranteed for off-duty reserve"),
    S("3.1","Execute reassignment and update roster","Crew Tracking Coordinator","Jeppesen Crew",
      "Confirmed crew member","Updated roster with reassignment",
      "Updated within 10 minutes of confirmation at 100 percent","N","N",
      "A roster not updated promptly can create a duplicate assignment conflict elsewhere in the system"),
  ],
  kpis=["Identified within 10 minutes of the disruption at 100 percent",
        "Candidates identified within 15 minutes of the need at 90 percent",
        "Contacted within 20 minutes of candidate identification at 85 percent",
        "Flight coverage maintained without a crew-caused cancellation at target rate"],
  risks=["A disruption severe enough to exhaust local reserve exposing the exact trade-off reserve sizing manages",
         "Contact success rate for off-duty reserve crew not being guaranteed",
         "A roster not updated promptly creating a duplicate assignment conflict elsewhere in the system",
         "The reassignment need being identified simultaneously with several other disrupted assignments, straining capacity"])

P("AC-CM-DO-04",
  desc="Reserve crew are called out and assigned to cover an operational need, drawing from the reserve "
       "pool established in seasonal planning against the day's actual disruption.",
  trig="An operational need for reserve coverage arises during the operating day.",
  out="A reserve crew member called out and assigned in accordance with the collective agreement's call-out "
      "procedures and notice requirements.",
  note="Call-out order and notice requirements are specific contractual obligations under each collective "
      "agreement, not just an operational convenience, so getting the order wrong is a labour relations "
      "issue as much as an operational one.",
  phases=["Call-out order determination", "Reserve contact", "Assignment confirmation"],
  steps=[
    S("1.1","Determine call-out order","Crew Tracking Coordinator","Jeppesen Crew",
      "Reserve pool and collective agreement call-out rules","Determined call-out order",
      "Determined correctly against the applicable agreement at 100 percent","Y","N",
      "Call-out order rules differ across the four collective agreements and are easy to apply inconsistently"),
    S("2.1","Contact reserve crew in order","Crew Tracking Coordinator","Jeppesen Crew",
      "Determined order","Contacted reserve crew member",
      "First contact attempted within the agreement's required notice period at 100 percent","N","N",
      "A missed contact attempt has to move to the next crew member in the defined order, not an arbitrary one"),
    S("2.2","Confirm reserve crew availability","Crew Tracking Coordinator","Jeppesen Crew",
      "Contacted crew member","Confirmed availability",
      "Confirmed within the agreement's response window at 90 percent","N","N",
      "A reserve crew member declining or not responding requires moving down the call-out order without delay"),
    S("3.1","Assign and update the roster","Crew Tracking Coordinator","Jeppesen Crew",
      "Confirmed reserve crew","Updated roster with assignment",
      "Updated within 10 minutes of confirmation at 100 percent","N","N",
      "A pay and credit calculation dependent on this assignment has to reflect the actual call-out time, not the roster time"),
  ],
  kpis=["Determined correctly against the applicable agreement at 100 percent",
        "First contact attempted within the agreement's required notice period at 100 percent",
        "Confirmed within the agreement's response window at 90 percent",
        "Zero call-outs made out of the contractually defined order"],
  risks=["Call-out order rules differing across four collective agreements, risking inconsistent application",
         "A missed contact attempt moving to an arbitrary next crew member rather than the defined order",
         "A pay and credit calculation not correctly reflecting the actual call-out time versus the roster time",
         "A reserve crew member declining or not responding requiring the process to move down the order without delay"])

P("AC-CM-DO-05",
  desc="Crew hotel and ground transport are coordinated for a layover or an irregular operations "
       "reassignment, ensuring adequate rest facilities are arranged before the crew's next duty period.",
  trig="A crew pairing includes a scheduled layover, or a disruption creates an unplanned overnight "
       "requirement.",
  out="Crew hotel and transport arranged, giving adequate rest opportunity before the next duty period "
      "begins.",
  note="Rest facility adequacy is not a hospitality consideration, it is a direct input to the fatigue risk "
      "management standard the crew's next duty period has to comply with.",
  phases=["Layover requirement identification", "Accommodation and transport arrangement", "Rest confirmation"],
  steps=[
    S("1.1","Identify layover or unplanned overnight requirement","Crew Tracking Coordinator","Jeppesen Crew",
      "Pairing schedule or disruption event","Identified requirement with location and duration",
      "Identified within 15 minutes of a disruption-driven requirement at 100 percent","N","N",
      "An unplanned overnight from a disruption has none of the lead time a scheduled layover has"),
    S("2.1","Arrange hotel accommodation","Crew Tracking Coordinator","Jeppesen Crew",
      "Identified requirement","Confirmed hotel booking",
      "Confirmed before crew arrival at the layover station at 95 percent","N","N",
      "Hotel availability at short notice during a widespread disruption can be genuinely constrained"),
    S("2.2","Arrange ground transport to and from the hotel","Crew Tracking Coordinator","Jeppesen Crew",
      "Confirmed hotel","Confirmed ground transport",
      "Confirmed before crew arrival at 90 percent","N","N",
      "Transport coordination at an unfamiliar station during a disruption is harder than at a regular layover point"),
    S("3.1","Confirm rest opportunity meets fatigue standards","Crew Tracking Coordinator","Jeppesen Crew",
      "Confirmed arrangements and next duty period","Confirmed compliant rest opportunity",
      "100 percent of layovers confirmed compliant before the next duty period","Y","N",
      "A rest opportunity that is technically sufficient in hours can still be inadequate given travel time to and from the hotel"),
  ],
  kpis=["Confirmed before crew arrival at the layover station at 95 percent",
        "Confirmed before crew arrival for ground transport at 90 percent",
        "100 percent of layovers confirmed compliant before the next duty period",
        "Hotel and transport arrangement time for unplanned overnights tracked against target"],
  risks=["Hotel availability at short notice during a widespread disruption being genuinely constrained",
         "A rest opportunity technically sufficient in hours being inadequate given travel time to and from the hotel",
         "Transport coordination at an unfamiliar station during a disruption being harder than at a regular layover point",
         "An unplanned overnight from a disruption having none of the lead time a scheduled layover has"])

P("AC-CM-DO-06",
  desc="Crew are positioned as passengers, deadheading, on a revenue or ferry flight to reach their next "
       "assignment or return to base, coordinated within the constraints of the operating flight's capacity.",
  trig="A pairing or reassignment requires a crew member to be positioned to a different location without "
       "operating the flight.",
  out="Crew correctly positioned to their required location, booked within the operating flight's capacity "
      "and reflected accurately in the pairing record.",
  note="Deadhead positioning competes directly with revenue passenger capacity on the same flight, which "
      "means a crew positioning need discovered late can be blocked by a flight that has already sold out.",
  phases=["Positioning requirement identification", "Capacity booking", "Confirmation"],
  steps=[
    S("1.1","Identify crew positioning requirement","Crew Tracking Coordinator","Jeppesen Crew",
      "Pairing or reassignment plan","Identified positioning need",
      "Identified within the pairing planning cycle or immediately for a disruption need","N","N",
      "A positioning need identified late competes with revenue inventory that is already largely sold"),
    S("2.1","Book crew position within flight capacity","Crew Tracking Coordinator","Amadeus Altea Inventory",
      "Positioning need and flight availability","Booked crew position",
      "Booked within capacity for 95 percent of positioning needs","N","N",
      "A flight with no available capacity requires an alternative positioning option to be found"),
    S("2.2","Coordinate with revenue management on capacity impact","Crew Tracking Coordinator","PROS Revenue Management",
      "Booked crew position","Confirmed capacity impact acknowledged",
      "Acknowledged within the standard coordination process at 100 percent","N","N",
      "Crew positioning displaces a seat that revenue management would otherwise sell"),
    S("3.1","Confirm positioning in the pairing record","Crew Tracking Coordinator","Jeppesen Crew",
      "Confirmed booking","Updated pairing record",
      "Updated within 24 hours of booking confirmation at 100 percent","N","N",
      "A pairing record that does not reflect actual deadhead positioning misstates the crew member's duty time"),
  ],
  kpis=["Booked within capacity for 95 percent of positioning needs",
        "Identified within the pairing planning cycle or immediately for a disruption need",
        "Acknowledged within the standard coordination process at 100 percent",
        "Updated within 24 hours of booking confirmation at 100 percent"],
  risks=["A late-identified positioning need competing with revenue inventory that is already largely sold",
         "A flight with no available capacity requiring an alternative positioning option under time pressure",
         "A pairing record that does not reflect actual deadhead positioning, misstating duty time",
         "Crew positioning displacing revenue seat inventory without visibility to revenue management"])

# ── CC: Crew Compliance, Training and Pay ───────────────────────────────────
P("AC-CM-CC-01",
  desc="A crew member's licence, medical certificate and type qualification currency are tracked "
       "continuously, ensuring no crew member is rostered for duty beyond their valid currency.",
  trig="The recurring currency tracking cycle runs, or an individual crew member's currency approaches "
       "expiry.",
  out="Accurate, current tracking of every crew member's licence, medical and qualification status, "
      "preventing any rostering beyond valid currency.",
  note="This tracking is the last line of defence against a crew member operating without valid "
      "certification, which makes its accuracy a direct flight safety and regulatory compliance control, "
      "not an administrative record.",
  phases=["Currency data compilation", "Expiry monitoring", "Rostering restriction"],
  steps=[
    S("1.1","Compile current licence and medical status","Crew Compliance Coordinator","Jeppesen Crew",
      "Individual crew member certification records","Compiled current status by crew member",
      "Compiled and current for 100 percent of active crew at all times","N","N",
      "Medical certificate renewal happens outside the airline's own systems and depends on timely crew reporting"),
    S("2.1","Monitor for approaching expiry","Crew Compliance Coordinator","Jeppesen Crew",
      "Compiled currency status","Flagged approaching expiry list",
      "Flagged at least 30 days before expiry at 100 percent","Y","N",
      "A crew member who does not proactively report a renewal in progress can appear to be lapsing when they are not"),
    S("3.1","Restrict rostering beyond expiry","Crew Compliance Coordinator","Jeppesen Crew",
      "Expired or expiring currency","System-enforced rostering restriction",
      "Zero crew members rostered beyond a valid currency date","N","Y",
      "A restriction that is not enforced at the system level depends entirely on manual vigilance"),
    S("3.2","Confirm restoration of eligibility upon renewal","Crew Compliance Coordinator","Jeppesen Crew",
      "Renewed licence or medical certificate","Restored rostering eligibility",
      "Restored within 24 hours of confirmed renewal at 100 percent","N","N",
      "A delay in restoring eligibility after a genuine renewal unnecessarily removes a crew member from availability"),
  ],
  kpis=["Compiled and current for 100 percent of active crew at all times",
        "Flagged at least 30 days before expiry at 100 percent",
        "Zero crew members rostered beyond a valid currency date",
        "Currency lapses caught before rostering versus after tracked as a leading indicator"],
  risks=["A crew member operating without valid certification if this tracking control fails",
         "Medical certificate renewal happening outside the airline's own systems, depending on timely crew reporting",
         "A restriction not enforced at the system level depending entirely on manual vigilance",
         "A crew member appearing to lapse when a renewal is actually already in progress but not yet reported"])

P("AC-CM-CC-02",
  desc="Recurrent training is scheduled for every crew member ahead of their currency deadline, tracked "
       "through completion and confirmed against the compliance record.",
  trig="A crew member's recurrent training cycle comes due.",
  out="Recurrent training scheduled, completed and confirmed for every crew member before their currency "
      "deadline.",
  note="Recurrent training scheduling and the currency protection process in AC-CM-CP-06 are two sides of "
      "the same requirement, one embedding the slot into the pairing build and the other tracking the "
      "individual crew member through to actual completion.",
  phases=["Training due date identification", "Scheduling and completion tracking", "Compliance confirmation"],
  steps=[
    S("1.1","Identify crew members due for recurrent training","Crew Compliance Coordinator","Jeppesen Crew",
      "Training currency records","Identified due list",
      "Identified for 100 percent of crew each cycle at the correct lead time","N","N",
      "Due dates are individually staggered and require continuous monitoring rather than a single annual sweep"),
    S("2.1","Schedule training against available slots","Crew Compliance Coordinator","Jeppesen Crew",
      "Due list and embedded training slots","Scheduled training for each crew member",
      "Scheduled before the currency deadline for 100 percent of due crew","N","N",
      "Available slot capacity has to be coordinated with the embedding done in AC-CM-CP-06"),
    S("2.2","Track training completion","Crew Compliance Coordinator","Jeppesen Crew",
      "Scheduled training","Confirmed completion or non-completion",
      "Tracked within 24 hours of the scheduled training date at 100 percent","N","N",
      "A crew member who misses a scheduled training slot needs immediate rescheduling before their deadline"),
    S("3.1","Confirm compliance record update","Crew Compliance Coordinator","Jeppesen Crew",
      "Confirmed completion","Updated compliance record",
      "Updated within 24 hours of completion confirmation at 100 percent","N","N",
      "A completion not promptly reflected in the compliance record risks an incorrect rostering restriction"),
  ],
  kpis=["Identified for 100 percent of crew each cycle at the correct lead time",
        "Scheduled before the currency deadline for 100 percent of due crew",
        "Tracked within 24 hours of the scheduled training date at 100 percent",
        "Zero crew members lapsing recurrent training currency"],
  risks=["Due dates being individually staggered, requiring continuous monitoring rather than a single sweep",
         "A missed scheduled training slot needing immediate rescheduling before the currency deadline",
         "A completion not promptly reflected in the compliance record risking an incorrect rostering restriction",
         "Available slot capacity not being properly coordinated with the pairing-build embedding process"])

P("AC-CM-CC-03",
  desc="Crew pay is calculated from actual flown and credited duty, reconciling the complex credit rules of "
       "each collective agreement against the day-of-operations record.",
  trig="The recurring pay period close cycle runs, compiling actual duty against roster and credit rules.",
  out="Accurate crew pay calculated and posted, correctly reflecting each collective agreement's credit "
      "rules against actual duty performed.",
  note="Crew pay calculation is one of the most complex payroll problems in the company, since credit is "
      "not simply time worked but a rules-based calculation that differs by agreement, by pairing type and "
      "by whether disruption altered the original plan.",
  phases=["Actual duty compilation", "Credit calculation", "Pay posting"],
  steps=[
    S("1.1","Compile actual duty against the roster","Crew Pay Analyst","Jeppesen Crew",
      "Day-of-operations tracking data","Compiled actual duty record",
      "Compiled for 100 percent of crew at pay period close at 100 percent","N","N",
      "Actual duty during a disrupted period can differ materially from the original roster in ways that need careful capture"),
    S("2.1","Apply collective agreement credit rules","Crew Pay Analyst","Jeppesen Crew",
      "Compiled duty and applicable agreement","Calculated credit by crew member",
      "Calculated correctly against the applicable agreement at 100 percent","Y","N",
      "Credit rules vary meaningfully across four collective agreements and by pairing type within each"),
    S("2.2","Reconcile disruption-affected pay adjustments","Crew Pay Analyst","Jeppesen Crew",
      "Calculated credit and disruption record","Reconciled adjustments",
      "Reconciled for 100 percent of disruption-affected pairings at 100 percent","N","N",
      "Disruption pay adjustments, such as irregular operations premiums, require correctly linking back to the specific event"),
    S("3.1","Post pay to the payroll system","Crew Pay Analyst","Dayforce",
      "Reconciled pay calculation","Posted pay",
      "Posted within the pay period close timetable at 100 percent","N","N",
      "A posting error discovered after payroll runs requires a correction cycle that delays resolution for the crew member"),
  ],
  kpis=["Calculated correctly against the applicable agreement at 100 percent",
        "Reconciled for 100 percent of disruption-affected pairings at 100 percent",
        "Posted within the pay period close timetable at 100 percent",
        "Pay dispute volume as a share of crew members below target threshold"],
  risks=["Credit rules varying meaningfully across four collective agreements and by pairing type within each",
         "Disruption pay adjustments requiring correct linkage back to the specific event that caused them",
         "A posting error discovered after payroll runs requiring a correction cycle that delays crew resolution",
         "Actual duty during a disrupted period differing materially from the original roster in ways easy to miscapture"])

P("AC-CM-CC-04",
  desc="A collective agreement grievance related to crew scheduling, pay or working conditions is received, "
       "investigated and progressed through the defined grievance process with the relevant union.",
  trig="A crew member or union representative files a grievance under a collective agreement.",
  out="A grievance investigated and progressed through the defined process to resolution or the next "
      "escalation stage, within the agreement's procedural timelines.",
  note="Grievance handling has hard procedural deadlines written into the collective agreement itself, so "
      "missing a response deadline can constitute a procedural failure independent of the grievance's actual "
      "merits.",
  phases=["Grievance intake", "Investigation", "Response and escalation"],
  steps=[
    S("1.1","Receive and log the grievance","Labour Relations Coordinator","Jeppesen Crew",
      "Filed grievance","Logged grievance with procedural deadline",
      "Logged within the agreement's required timeframe at 100 percent","N","N",
      "Grievance filing requirements and formats differ across the four collective agreements"),
    S("2.1","Investigate the underlying facts","Labour Relations Coordinator","Jeppesen Crew",
      "Logged grievance","Investigated facts and applicable agreement provisions",
      "Investigated within the procedural deadline at 100 percent","N","N",
      "Investigation depends on records, such as roster and pay history, that span several systems"),
    S("2.2","Prepare Air Canada's position","Labour Relations Coordinator","Jeppesen Crew",
      "Investigated facts","Prepared response position",
      "Prepared before the procedural response deadline at 100 percent","Y","N",
      "A position that does not correctly apply the agreement provision weakens Air Canada's standing at the next stage"),
    S("3.1","Respond within the procedural timeline","Labour Relations Coordinator","Jeppesen Crew",
      "Prepared position","Filed response or resolution",
      "Filed within the agreement's procedural deadline at 100 percent","N","N",
      "A missed deadline constitutes a procedural failure independent of the grievance's actual merits"),
  ],
  kpis=["Logged within the agreement's required timeframe at 100 percent",
        "Investigated within the procedural deadline at 100 percent",
        "Filed within the agreement's procedural deadline at 100 percent",
        "Grievance resolution rate at first stage tracked against escalation rate"],
  risks=["A missed procedural deadline constituting a compliance failure independent of the grievance's actual merits",
         "Grievance filing requirements and formats differing across four collective agreements",
         "Investigation depending on records spanning several systems not originally designed to be pulled together",
         "A prepared position that does not correctly apply the agreement provision weakening Air Canada's standing"])

P("AC-CM-CC-05",
  desc="A crew member's discipline or performance issue is addressed through the defined performance "
       "management process, applied consistently and within the bounds of the applicable collective "
       "agreement.",
  trig="A performance or conduct issue involving a crew member is identified.",
  out="A performance issue addressed through the defined process, with consistent application and full "
      "compliance with collective agreement due process requirements.",
  note="Discipline handling has to hold two things in tension: correcting a genuine performance issue "
      "promptly, while ensuring the process itself would withstand scrutiny under the collective agreement's "
      "due process protections.",
  phases=["Issue identification and documentation", "Process application", "Resolution"],
  steps=[
    S("1.1","Identify and document the performance issue","Labour Relations Coordinator","Jeppesen Crew",
      "Observed or reported issue","Documented issue with factual basis",
      "Documented within the required timeframe at 100 percent","N","N",
      "Documentation quality at this stage determines whether the process can withstand later scrutiny"),
    S("2.1","Apply progressive discipline framework","Labour Relations Coordinator","Jeppesen Crew",
      "Documented issue and prior record","Determined discipline level",
      "Applied consistently against the framework at 100 percent","Y","N",
      "Discipline consistency across similar cases and different crew members is essential to withstand a grievance challenge"),
    S("2.2","Ensure collective agreement due process","Labour Relations Coordinator","Jeppesen Crew",
      "Determined discipline","Confirmed due process compliance",
      "100 percent compliant with the applicable agreement's due process requirements","Y","N",
      "Due process requirements, such as union representation rights, differ across the four agreements"),
    S("3.1","Communicate and implement the outcome","Labour Relations Coordinator","Jeppesen Crew",
      "Confirmed process","Implemented discipline outcome",
      "Implemented within the required timeframe at 100 percent","N","N",
      "An outcome implemented outside due process requirements is vulnerable to grievance and reversal"),
  ],
  kpis=["Documented within the required timeframe at 100 percent",
        "Applied consistently against the framework at 100 percent",
        "100 percent compliant with the applicable agreement's due process requirements",
        "Discipline decisions upheld on grievance challenge above target"],
  risks=["Discipline consistency across similar cases and different crew members being essential to withstand challenge",
         "Due process requirements, such as union representation rights, differing across four agreements",
         "An outcome implemented outside due process requirements being vulnerable to grievance and reversal",
         "Documentation quality at the identification stage determining whether the process can withstand scrutiny"])

P("AC-CM-CC-06",
  desc="Crew records, including qualification, training, pay and discipline history, are maintained and "
       "made available for a Transport Canada or internal regulatory audit.",
  trig="The recurring records audit cycle runs, or a Transport Canada audit request is received.",
  out="Complete, accurate crew records available for regulatory audit, demonstrating sustained compliance "
      "rather than a point-in-time assembly exercise.",
  note="This process is the crew management equivalent of the safety management system's audit evidence "
      "discipline in AC-FO-SR-06: continuous record maintenance, not last-minute assembly, is what actually "
      "demonstrates compliance to a regulator.",
  phases=["Record consolidation", "Continuous maintenance", "Audit presentation"],
  steps=[
    S("1.1","Consolidate crew records across systems","Crew Compliance Coordinator","Jeppesen Crew",
      "Qualification, training, pay and discipline records","Consolidated crew record",
      "Consolidated for 100 percent of active crew on a rolling basis","N","N",
      "Records are held across several systems not originally designed to be presented as a single view"),
    S("2.1","Maintain records continuously between audits","Crew Compliance Coordinator","Jeppesen Crew",
      "Ongoing crew management activity","Continuously updated records",
      "Updated on a rolling basis rather than only before an audit at 100 percent","N","N",
      "Records assembled only before an audit are a weaker demonstration of sustained compliance"),
    S("2.2","Conduct internal record completeness review","Crew Compliance Coordinator","Jeppesen Crew",
      "Maintained records","Completeness review findings",
      "Conducted at least 60 days before a scheduled audit at 100 percent","Y","N",
      "A completeness gap found close to an audit date leaves little time for genuine remediation"),
    S("3.1","Present records for regulatory audit","Crew Compliance Coordinator","Jeppesen Crew",
      "Reviewed records","Presented audit-ready records",
      "Presented complete and organised for 100 percent of requested crew members","N","N",
      "Record organisation quality directly affects how efficiently a regulator can complete their review"),
  ],
  kpis=["Consolidated for 100 percent of active crew on a rolling basis",
        "Updated on a rolling basis rather than only before an audit at 100 percent",
        "Conducted at least 60 days before a scheduled audit at 100 percent",
        "Zero audit findings attributable to incomplete or unavailable crew records"],
  risks=["Records assembled only before an audit being a weaker demonstration of sustained compliance",
         "A completeness gap found close to an audit date leaving little time for genuine remediation",
         "Records held across several systems not originally designed to be presented as a single coherent view",
         "Record organisation quality directly affecting how efficiently a regulator can complete their review"])
