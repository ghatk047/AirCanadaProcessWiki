# -*- coding: utf-8 -*-
"""AC-CM-CP — Crew Planning and Pairing (6) and AC-CM-CR — Rostering and Bidding (6)."""
from content_lib import P, S

# ── CP: Crew Planning and Pairing ───────────────────────────────────────────
P("AC-CM-CP-01",
  desc="Crew demand is forecast against the seasonal schedule and translated into an establishment plan by "
       "base, fleet type and rank, feeding recruitment and training capacity planning.",
  trig="A seasonal schedule is committed and requires a corresponding crew establishment plan.",
  out="A crew establishment plan by base and rank matched to the committed schedule's flying requirement.",
  note="Establishment planning has to look further ahead than the season it directly serves, because "
       "recruitment and type-rating training both have lead times measured in months, not weeks.",
  phases=["Demand translation", "Establishment calculation", "Gap identification"],
  steps=[
    S("1.1","Translate committed schedule into crew flying hours","Crew Planning Analyst","Lufthansa Systems NetLine",
      "Committed seasonal schedule","Required flying hours by fleet type and base",
      "Translated within 10 business days of schedule commitment at 100 percent","N","N",
      "Flying hour requirements do not translate linearly into headcount because of duty and rest limits"),
    S("2.1","Calculate required establishment by rank","Crew Planning Analyst","Jeppesen Crew",
      "Required flying hours and duty rules","Calculated establishment by base and rank",
      "Calculated for 100 percent of bases each planning cycle","N","N",
      "Establishment calculation has to reserve capacity for training, leave and sick absence, not just flying"),
    S("2.2","Identify gap against current establishment","Crew Planning Analyst","Jeppesen Crew",
      "Calculated requirement and current headcount","Identified gap by base and rank",
      "Gap identified within 5 business days of calculation at 100 percent","N","N",
      "A gap identified late compresses the lead time available for recruitment or training response"),
    S("3.1","Feed gap into recruitment and training planning","Crew Planning Analyst","Phenom",
      "Identified gap","Recruitment and training demand signal",
      "Signal delivered within 5 business days of gap identification at 100 percent","N","N",
      "Recruitment and type-rating training lead times are measured in months and cannot absorb a late signal"),
  ],
  kpis=["Translated within 10 business days of schedule commitment at 100 percent",
        "Gap identified within 5 business days of calculation at 100 percent",
        "Signal delivered to recruitment within 5 business days of gap identification at 100 percent",
        "Establishment gap closure rate against the planning horizon tracked"],
  risks=["Recruitment and type-rating training lead times being unable to absorb a late-identified gap",
         "Establishment calculation understating the reserve needed for training, leave and sick absence",
         "Flying hour requirements not translating linearly into headcount due to duty and rest limits",
         "A gap identified late compressing the lead time available for any response"])

P("AC-CM-CP-02",
  desc="Crew pairings, the sequences of flights a crew member operates together as a work unit, are built "
       "and optimised in Jeppesen against the committed schedule.",
  trig="The seasonal schedule is committed and crew planning reaches the pairing build stage.",
  out="A set of feasible, cost-optimised pairings covering the full flying requirement, ready for bid "
      "package assembly.",
  note="Pairing optimisation has to satisfy flight and duty time regulation, collective agreement terms "
      "across four bargaining units, and cost efficiency simultaneously, which makes it one of the more "
      "constrained optimisation problems anywhere in the airline.",
  phases=["Pairing generation", "Constraint validation", "Cost optimisation"],
  steps=[
    S("1.1","Generate candidate pairings from the schedule","Crew Planning Analyst","Jeppesen Crew",
      "Committed schedule","Candidate pairing set",
      "Candidates generated covering 100 percent of flying requirement","N","N",
      "Pairing generation for a complex hub schedule produces a very large candidate solution space"),
    S("2.1","Validate flight and duty time compliance","Crew Planning Analyst","Jeppesen Crew",
      "Candidate pairings","Compliance-validated pairings",
      "100 percent of pairings compliant with Canadian Aviation Regulations duty limits","Y","N",
      "Duty time rules interact with time zone crossing in ways that are easy to miscalculate manually"),
    S("2.2","Validate collective agreement compliance","Crew Planning Analyst","Jeppesen Crew",
      "Candidate pairings","Agreement-compliant pairings",
      "100 percent of pairings compliant with the applicable collective agreement","Y","N",
      "Four different collective agreements apply to different crew groups on overlapping pairings"),
    S("3.1","Optimise pairings for cost efficiency","Crew Planning Analyst","Jeppesen Crew",
      "Compliant pairing set","Cost-optimised pairing set",
      "Optimisation completed within the planning cycle at 100 percent","N","N",
      "Cost optimisation can produce pairings that are technically compliant but operationally fragile to disruption"),
  ],
  kpis=["Candidates generated covering 100 percent of flying requirement",
        "100 percent of pairings compliant with Canadian Aviation Regulations duty limits",
        "100 percent of pairings compliant with the applicable collective agreement",
        "Pairing cost efficiency against the planning target tracked each cycle"],
  risks=["Duty time rules interacting with time zone crossing in ways that are easy to miscalculate manually",
         "Four different collective agreements applying to different crew groups on overlapping pairings",
         "Cost-optimised pairings being technically compliant but operationally fragile to routine disruption",
         "Pairing generation producing a solution space too large to fully explore within the planning window"])

P("AC-CM-CP-03",
  desc="Reserve crew coverage is sized and distributed across bases to absorb sick calls, delays and "
       "irregular operations without triggering a cascading crew shortage.",
  trig="The seasonal pairing build is complete and reserve sizing is calculated against expected disruption "
       "volume.",
  out="A reserve coverage plan by base sized against historical disruption patterns, balancing crew cost "
      "against recovery resilience.",
  note="Reserve sizing is a direct trade-off between cost, since reserve crew are paid without necessarily "
      "flying, and operational resilience, since insufficient reserve is what turns an isolated disruption "
      "into a cascading crew shortage.",
  phases=["Disruption pattern analysis", "Reserve sizing", "Base distribution"],
  steps=[
    S("1.1","Analyse historical disruption and sick call patterns","Crew Planning Analyst","Jeppesen Crew",
      "Historical crew disruption data by base","Disruption pattern analysis by base",
      "Analysed for 100 percent of bases each planning cycle","N","N",
      "Disruption patterns shift seasonally and a single annual average can misrepresent a specific season's need"),
    S("2.1","Calculate reserve coverage requirement","Crew Planning Analyst","Jeppesen Crew",
      "Disruption pattern and cost target","Calculated reserve level by base",
      "Calculated for 100 percent of bases each planning cycle","N","N",
      "The cost-resilience trade-off has no single objectively correct answer"),
    S("2.2","Validate reserve coverage against fatigue rules","Crew Planning Analyst","Jeppesen Crew",
      "Calculated reserve level","Fatigue-compliant reserve schedule",
      "100 percent compliant with fatigue risk management standards","Y","N",
      "Reserve duty itself carries fatigue implications distinct from active flying duty"),
    S("3.1","Distribute reserve across bases in the schedule","Crew Planning Analyst","Jeppesen Crew",
      "Validated reserve plan","Distributed reserve coverage in the published schedule",
      "Distributed before schedule publication at 100 percent","N","N",
      "Reserve concentrated at the wrong base leaves a different base structurally exposed to a shortage"),
  ],
  kpis=["Analysed for 100 percent of bases each planning cycle",
        "100 percent compliant with fatigue risk management standards",
        "Distributed before schedule publication at 100 percent",
        "Reserve utilisation rate against sizing assumption tracked each season"],
  risks=["Insufficient reserve at a specific base turning an isolated disruption into a cascading crew shortage",
         "Reserve duty itself carrying fatigue implications distinct from active flying duty",
         "A single annual average disruption pattern misrepresenting a specific season's actual need",
         "Reserve concentrated at the wrong base leaving a different base structurally exposed"])

P("AC-CM-CP-04",
  desc="A crew member's base assignment or transfer between bases is processed, coordinating the "
       "operational, contractual and personal logistics of relocating a crew member's home base.",
  trig="A crew member requests a base transfer, or an operational requirement necessitates reassigning crew "
       "base allocation.",
  out="A completed base assignment or transfer with all contractual, scheduling and logistical elements "
      "coordinated.",
  note="A base transfer touches several systems and processes that were not designed with each other in "
      "mind, from bidding seniority to relocation logistics, which makes coordination the actual difficulty "
      "rather than any single step.",
  phases=["Transfer request and eligibility", "Contractual and scheduling coordination", "Relocation completion"],
  steps=[
    S("1.1","Receive and validate transfer eligibility","Crew Planning Analyst","Jeppesen Crew",
      "Crew member transfer request","Validated eligibility against collective agreement terms",
      "Validated within the collective agreement's defined response window at 100 percent","Y","N",
      "Transfer eligibility rules differ across the four collective agreements"),
    S("2.1","Coordinate with base seniority and bidding impact","Crew Planning Analyst","Jeppesen Crew",
      "Validated transfer","Assessed seniority and bidding position impact",
      "Assessed before transfer confirmation at 100 percent","N","N",
      "A transfer changes the crew member's seniority position at the new base in ways not always anticipated"),
    S("2.2","Confirm operational capacity for the transfer","Crew Planning Analyst","Jeppesen Crew",
      "Assessed impact","Confirmed base capacity to receive the transfer",
      "Confirmed within the establishment plan's defined capacity at 100 percent","N","N",
      "A transfer into an already-tight base establishment can create a new capacity gap elsewhere"),
    S("3.1","Complete relocation logistics coordination","Crew Planning Analyst","SAP S/4HANA",
      "Confirmed transfer","Completed relocation coordination",
      "Completed within the agreed transfer timeline at 90 percent","N","N",
      "Relocation logistics fall partly outside crew planning's own systems and require cross-team coordination"),
  ],
  kpis=["Validated within the collective agreement's defined response window at 100 percent",
        "Assessed before transfer confirmation at 100 percent",
        "Confirmed within the establishment plan's defined capacity at 100 percent",
        "Completed within the agreed transfer timeline at 90 percent"],
  risks=["A transfer changing seniority position at the new base in ways not anticipated by the crew member",
         "A transfer into an already-tight base establishment creating a new capacity gap elsewhere",
         "Transfer eligibility rules differing across four collective agreements, risking inconsistent application",
         "Relocation logistics falling partly outside crew planning's own systems, requiring cross-team coordination"])

P("AC-CM-CP-05",
  desc="Collective agreement rules from all four bargaining units, ACPA, CUPE, Teamsters and UNIFOR, are "
       "configured into the crew planning system's rule engine, kept current as agreements are renegotiated.",
  trig="A collective agreement is renegotiated or amended, requiring the pairing and rostering rule engine "
       "to be updated.",
  out="A correctly configured rule engine reflecting the current terms of all four collective agreements.",
  note="Getting a collective agreement rule wrong in the system does not just risk an inefficient roster, it "
       "risks a contractual violation that becomes a grievance, which is why this configuration work sits "
       "closer to compliance than to routine system administration.",
  phases=["Agreement change identification", "Rule translation", "Configuration validation"],
  steps=[
    S("1.1","Identify rule changes from a renegotiated agreement","Crew Planning Analyst","Jeppesen Crew",
      "Renegotiated collective agreement text","Identified rule changes",
      "Identified within 10 business days of agreement ratification at 100 percent","N","N",
      "Legal agreement language does not always translate unambiguously into a system rule"),
    S("2.1","Translate agreement terms into system rules","Crew Planning Analyst","Jeppesen Crew",
      "Identified rule changes","Configured system rules",
      "Configured before the agreement's effective date at 100 percent","N","N",
      "A rule translated incorrectly can silently generate non-compliant rosters until caught"),
    S("2.2","Validate configuration against test scenarios","Crew Planning Analyst","Jeppesen Crew",
      "Configured rules","Validated configuration",
      "100 percent of material rule changes tested before go-live","Y","N",
      "Test scenario coverage rarely spans every edge case a real roster will eventually encounter"),
    S("3.1","Deploy and confirm rule engine currency","Crew Planning Analyst","Jeppesen Crew",
      "Validated configuration","Deployed and confirmed current rule engine",
      "Deployed before the agreement's effective date at 100 percent","N","N",
      "A deployment gap between agreement effective date and system update creates a compliance exposure window"),
  ],
  kpis=["Configured before the agreement's effective date at 100 percent",
        "100 percent of material rule changes tested before go-live",
        "Deployed before the agreement's effective date at 100 percent",
        "Grievances attributable to rule engine misconfiguration below target threshold"],
  risks=["A rule translated incorrectly silently generating non-compliant rosters until caught",
         "A deployment gap between agreement effective date and system update creating a compliance exposure",
         "Legal agreement language not translating unambiguously into a discrete system rule",
         "Test scenario coverage missing an edge case a real roster eventually encounters"])

P("AC-CM-CP-06",
  desc="Recurrent and initial training requirements are embedded into the crew planning and pairing cycle, "
       "protecting training slots against operational schedule pressure.",
  trig="The seasonal pairing build reaches training integration, or an individual crew member's training "
       "currency approaches its renewal deadline.",
  out="Training slots protected within the pairing build, with every crew member's currency maintained "
      "ahead of its renewal deadline.",
  note="Training slots are one of the first things schedule pressure tends to squeeze, since deferring a "
      "training slot has no immediate visible operational cost the way cancelling a flight does, until the "
      "currency deadline actually arrives.",
  phases=["Training requirement identification", "Slot embedding", "Currency protection"],
  steps=[
    S("1.1","Identify individual training requirements","Crew Planning Analyst","Jeppesen Crew",
      "Crew member currency and training record","Identified training requirement by crew member",
      "Identified for 100 percent of crew members each planning cycle","N","N",
      "Currency deadlines are individually staggered across the crew base rather than aligned to a single date"),
    S("2.1","Embed training slots into the pairing build","Crew Planning Analyst","Jeppesen Crew",
      "Identified requirements and pairing build","Embedded training slots",
      "Embedded for 100 percent of due training requirements at each cycle","Y","N",
      "Embedding a training slot can force rebuilding an otherwise efficient pairing"),
    S("2.2","Protect embedded slots against schedule pressure","Crew Planning Analyst","Jeppesen Crew",
      "Embedded training slots","Protected slots resistant to displacement",
      "Zero training slots displaced by operational pressure without a compliant rescheduling","N","N",
      "Training slots are one of the first things displaced under schedule pressure since the cost is not immediately visible"),
    S("3.1","Monitor currency deadline compliance","Crew Planning Analyst","Jeppesen Crew",
      "Protected training schedule","Currency compliance status",
      "Zero crew members operating beyond their currency deadline","N","Y",
      "A crew member whose training is displaced too many times risks reaching their deadline without renewal"),
  ],
  kpis=["Identified for 100 percent of crew members each planning cycle",
        "Embedded for 100 percent of due training requirements at each cycle",
        "Zero training slots displaced without a compliant rescheduling",
        "Zero crew members operating beyond their currency deadline"],
  risks=["A training slot's deferral cost being invisible until the currency deadline actually arrives",
         "Embedding a training slot forcing rebuild of an otherwise efficient pairing",
         "A crew member whose training is displaced too many times reaching their deadline without renewal",
         "Currency deadlines being individually staggered rather than aligned to a single manageable date"])

# ── CR: Rostering and Bidding ───────────────────────────────────────────────
P("AC-CM-CR-01",
  desc="The monthly bid package, containing available pairings, reserve blocks and other assignable "
       "activities, is published to crew members ahead of the preferential bidding window.",
  trig="The monthly bid cycle opens following completion of the pairing build.",
  out="A complete, accurate bid package published to all eligible crew members within the required lead "
      "time.",
  note="Bid package accuracy matters because crew members make binding preference decisions against it; a "
      "package error discovered after bidding closes forces a difficult choice between re-running the whole "
      "bid or living with a known inaccuracy.",
  phases=["Package assembly", "Accuracy validation", "Publication"],
  steps=[
    S("1.1","Assemble the bid package from the pairing build","Crew Rostering Analyst","Jeppesen Crew",
      "Completed pairing build","Assembled bid package",
      "Assembled within 5 business days of pairing build completion at 100 percent","N","N",
      "The package has to correctly reflect every base and fleet-specific pairing set simultaneously"),
    S("2.1","Validate package accuracy against the pairing build","Crew Rostering Analyst","Jeppesen Crew",
      "Assembled package","Validated package",
      "Validated before publication at 100 percent","Y","N",
      "An error discovered after bidding closes forces a choice between re-running the bid or living with the inaccuracy"),
    S("3.1","Publish the bid package to crew members","Crew Rostering Analyst","Jeppesen Crew",
      "Validated package","Published bid package",
      "Published within the required lead time before the bidding window opens at 100 percent","N","N",
      "A late publication compresses the time crew members have to make an informed bidding decision"),
    S("3.2","Open the bidding window for submissions","Crew Rostering Analyst","Jeppesen Crew",
      "Published package","Open bidding window",
      "Window opened on the published schedule at 100 percent","N","N",
      "A window that opens late compounds any delay from the publication step before it"),
  ],
  kpis=["Assembled within 5 business days of pairing build completion at 100 percent",
        "Validated before publication at 100 percent",
        "Published within the required lead time before the bidding window opens at 100 percent",
        "Bid package accuracy errors requiring correction after publication below target"],
  risks=["A package error discovered after bidding closes forcing a choice between re-running the bid or living with it",
         "A late publication compressing the time available for an informed crew bidding decision",
         "The package failing to correctly reflect every base and fleet-specific pairing set simultaneously",
         "Crew members bidding against an inaccuracy that is only caught after their preferences are locked in"])

P("AC-CM-CR-02",
  desc="Crew bids are processed through the preferential bidding system, awarding rosters by seniority "
       "against each crew member's stated preferences within the constraints of the published bid package.",
  trig="The bidding window closes and preferential bidding award processing begins.",
  out="Awarded monthly rosters for every crew member, correctly reflecting seniority-based preference "
      "satisfaction within system constraints.",
  note="Seniority-based award is a foundational principle across all four collective agreements, so the "
      "integrity of the award algorithm and its correct, auditable application matters as much to labour "
      "relations as it does to operational feasibility.",
  phases=["Bid collection and validation", "Seniority-based award processing", "Roster distribution"],
  steps=[
    S("1.1","Collect and validate submitted bids","Crew Rostering Analyst","Jeppesen Crew",
      "Crew member bid submissions","Validated bid set",
      "Validated within 24 hours of the bidding window closing at 100 percent","N","N",
      "An invalid bid submission has to be resolved with the crew member before award processing can run"),
    S("2.1","Run seniority-based award processing","Crew Rostering Analyst","Jeppesen Crew",
      "Validated bids and seniority list","Awarded roster by crew member",
      "Award run completed within the standard processing window at 100 percent","N","N",
      "The award algorithm has to correctly apply seniority order across a large simultaneous bid pool"),
    S("2.2","Validate awarded rosters for compliance","Crew Rostering Analyst","Jeppesen Crew",
      "Awarded rosters","Compliance-validated rosters",
      "100 percent of awarded rosters compliant with duty and agreement rules","Y","N",
      "An award that satisfies preference and seniority still has to independently pass compliance validation"),
    S("3.1","Distribute awarded rosters to crew members","Crew Rostering Analyst","Jeppesen Crew",
      "Validated rosters","Distributed rosters",
      "Distributed within the required lead time before the roster month at 100 percent","N","N",
      "A late roster distribution reduces crew members' ability to plan personal commitments around it"),
  ],
  kpis=["Validated within 24 hours of the bidding window closing at 100 percent",
        "Award run completed within the standard processing window at 100 percent",
        "100 percent of awarded rosters compliant with duty and agreement rules",
        "Distributed within the required lead time before the roster month at 100 percent"],
  risks=["The award algorithm incorrectly applying seniority order across a large simultaneous bid pool",
         "An award satisfying preference and seniority while still failing independent compliance validation",
         "A late roster distribution reducing crew members' ability to plan personal commitments",
         "An invalid bid submission delaying award processing for the entire affected bid pool"])

P("AC-CM-CR-03",
  desc="Crew vacation and other planned leave is bid and awarded separately from the monthly operational "
       "roster, coordinated against establishment capacity to avoid a leave-driven crew shortfall.",
  trig="The annual or seasonal vacation bidding cycle opens.",
  out="Awarded vacation and leave periods by crew member, coordinated against establishment capacity to "
      "avoid a shortfall at any base.",
  note="Vacation bidding awards leave months ahead of when it is taken, which means the establishment "
      "capacity assumption behind the award has to hold up over a much longer horizon than a monthly roster "
      "award does.",
  phases=["Vacation bid collection", "Capacity-constrained award", "Confirmation"],
  steps=[
    S("1.1","Collect vacation bid submissions","Crew Rostering Analyst","Jeppesen Crew",
      "Crew member vacation preferences","Collected bid submissions",
      "Collected within the defined bidding window at 100 percent","N","N",
      "Vacation preferences cluster heavily around peak leisure periods, concentrating demand on the same weeks"),
    S("2.1","Assess capacity constraint by base and period","Crew Rostering Analyst","Jeppesen Crew",
      "Bid submissions and establishment plan","Capacity assessment by period",
      "Assessed for 100 percent of bases before award processing at 100 percent","N","N",
      "A capacity assessment made months ahead can be invalidated by a later establishment change"),
    S("2.2","Award vacation by seniority within capacity limits","Crew Rostering Analyst","Jeppesen Crew",
      "Capacity assessment and seniority order","Awarded vacation periods",
      "Awarded within the capacity constraint at 100 percent","Y","N",
      "Peak-period demand clustering means many bids compete for the same limited capacity window"),
    S("3.1","Confirm awarded vacation to crew members","Crew Rostering Analyst","Jeppesen Crew",
      "Awarded periods","Confirmed vacation award",
      "Confirmed within the required lead time before the vacation year at 100 percent","N","N",
      "A confirmed award that is later revised due to a capacity change is highly disruptive to personal planning"),
  ],
  kpis=["Collected within the defined bidding window at 100 percent",
        "Assessed for 100 percent of bases before award processing at 100 percent",
        "Awarded within the capacity constraint at 100 percent",
        "Confirmed within the required lead time before the vacation year at 100 percent"],
  risks=["A capacity assessment made months ahead being invalidated by a later establishment change",
         "Peak-period demand clustering meaning many bids compete for the same limited capacity window",
         "A confirmed vacation award later being revised due to a capacity change, disrupting personal planning",
         "Vacation award commitments made far ahead of the leave being taken, extending the risk horizon"])

P("AC-CM-CR-04",
  desc="A crew member's roster is adjusted after award, through a trip trade with another crew member or a "
       "direct schedule change request, subject to seniority, legality and agreement constraints.",
  trig="A crew member requests a roster adjustment or initiates a trip trade with another crew member.",
  out="A completed, compliant roster adjustment reflecting the trade or change, with both affected crew "
      "members' rosters correctly updated.",
  note="A trip trade between two crew members has to be validated as a pair, not independently, since a "
      "trade that is individually legal for each crew member can still create a combined outcome that "
      "violates a duty or rest requirement.",
  phases=["Adjustment request", "Legality and agreement validation", "Roster update"],
  steps=[
    S("1.1","Receive adjustment or trade request","Crew Rostering Analyst","Jeppesen Crew",
      "Crew member request","Registered adjustment request",
      "Registered within 1 business day of submission at 100 percent","N","N",
      "A trip trade request involves two crew members whose availability has to align before it can even be assessed"),
    S("2.1","Validate combined legality of the trade","Crew Rostering Analyst","Jeppesen Crew",
      "Trade request and both crew members' current rosters","Combined legality validation",
      "Validated as a combined pair, not independently, at 100 percent","Y","N",
      "A trade individually legal for each crew member can still violate a duty or rest requirement in combination"),
    S("2.2","Validate against collective agreement trade rules","Crew Rostering Analyst","Jeppesen Crew",
      "Validated trade","Agreement-compliant trade",
      "100 percent compliant with the applicable collective agreement trade provisions","N","N",
      "Trade eligibility rules differ across the four collective agreements"),
    S("3.1","Update both crew members' rosters","Crew Rostering Analyst","Jeppesen Crew",
      "Approved trade","Updated rosters for both crew members",
      "Updated within 24 hours of approval at 100 percent","N","N",
      "An update applied to only one side of the trade leaves both rosters inconsistent with reality"),
  ],
  kpis=["Registered within 1 business day of submission at 100 percent",
        "Validated as a combined pair at 100 percent",
        "100 percent compliant with the applicable collective agreement trade provisions",
        "Updated within 24 hours of approval at 100 percent"],
  risks=["A trade individually legal for each crew member violating a duty or rest requirement in combination",
         "An update applied to only one side of a trade leaving both rosters inconsistent with reality",
         "Trade eligibility rules differing across four collective agreements, risking inconsistent application",
         "A trip trade request depending on two crew members' availability aligning before it can even be assessed"])

P("AC-CM-CR-05",
  desc="Open flying assignments, arising from a roster gap or a premium pay incentive, are offered and "
       "assigned to crew members through a defined open time process.",
  trig="A roster gap or premium assignment opportunity is identified after monthly award processing.",
  out="Open flying assignments filled through the defined open time process, with premium incentives "
      "correctly applied where offered.",
  note="Open time exists precisely because the monthly award process cannot anticipate every gap, so its "
      "own fairness and transparency in how it allocates opportunity matters as much to crew relations as "
      "the primary bid award does.",
  phases=["Gap identification", "Open time offer", "Assignment confirmation"],
  steps=[
    S("1.1","Identify open flying assignments","Crew Rostering Analyst","Jeppesen Crew",
      "Post-award roster gaps","Identified open assignments",
      "Identified within 24 hours of the gap arising at 100 percent","N","N",
      "Gaps can arise continuously as the roster month progresses, not only at initial award"),
    S("2.1","Determine premium eligibility for the assignment","Crew Rostering Analyst","Jeppesen Crew",
      "Identified assignment and current fill difficulty","Determined premium terms",
      "Determined before the assignment is offered at 100 percent","N","N",
      "Premium terms have to be applied consistently or they become a source of perceived unfairness"),
    S("2.2","Offer open time assignment to eligible crew","Crew Rostering Analyst","Jeppesen Crew",
      "Determined assignment and terms","Offered assignment to eligible crew members",
      "Offered within the defined open time process rules at 100 percent","Y","N",
      "The order and method of offering has to follow the agreement's defined process, not ad hoc discretion"),
    S("3.1","Confirm assignment and update roster","Crew Rostering Analyst","Jeppesen Crew",
      "Accepted offer","Confirmed and updated roster",
      "Confirmed within 24 hours of acceptance at 100 percent","N","N",
      "An unfilled open assignment close to the operating date has to escalate to a different fill mechanism"),
  ],
  kpis=["Identified within 24 hours of the gap arising at 100 percent",
        "Offered within the defined open time process rules at 100 percent",
        "Confirmed within 24 hours of acceptance at 100 percent",
        "Open time fill rate before the operating date meeting target"],
  risks=["Premium terms applied inconsistently becoming a source of perceived unfairness among crew",
         "The order and method of offering not following the agreement's defined process",
         "An unfilled open assignment close to the operating date requiring escalation to a different fill mechanism",
         "Gaps arising continuously through the roster month straining the process's ability to keep pace"])

P("AC-CM-CR-06",
  desc="A finalised roster, incorporating all trades, open time assignments and other post-award changes, "
       "is published and delivered to crew members ahead of the operating month.",
  trig="Post-award roster changes for the upcoming operating month are finalised.",
  out="A final, accurate published roster available to every crew member, correctly reflecting all "
      "post-award changes.",
  note="This is the version of the roster a crew member actually relies on to show up for duty, so any "
      "residual inconsistency between this publication and the operational system used to track sign-on "
      "becomes an operational problem, not just a communication one.",
  phases=["Change consolidation", "Final validation", "Publication and delivery"],
  steps=[
    S("1.1","Consolidate all post-award roster changes","Crew Rostering Analyst","Jeppesen Crew",
      "Trades, open time and other approved changes","Consolidated final roster",
      "Consolidated within the defined publication cycle at 100 percent","N","N",
      "Changes approved right up to the publication deadline have to be captured in the same cycle"),
    S("2.1","Validate final roster consistency","Crew Rostering Analyst","Jeppesen Crew",
      "Consolidated roster","Validated final roster",
      "Validated before publication at 100 percent","Y","N",
      "A validation gap between the published roster and the operational tracking system creates a sign-on discrepancy"),
    S("3.1","Publish and notify crew members","Crew Rostering Analyst","Jeppesen Crew",
      "Validated roster","Published roster with crew notification",
      "Published within the required lead time before the operating month at 100 percent","N","N",
      "A late publication does not give crew adequate notice to plan personal logistics around the final roster"),
    S("3.2","Sync roster to day-of-operations tracking","Crew Rostering Analyst","Jeppesen Crew",
      "Published roster","Synced day-of-operations system",
      "Synced before the operating month begins at 100 percent","N","N",
      "A sync gap between the published roster and the day-of-operations system is what actually causes a sign-on discrepancy"),
  ],
  kpis=["Consolidated within the defined publication cycle at 100 percent",
        "Validated before publication at 100 percent",
        "Published within the required lead time before the operating month at 100 percent",
        "Sign-on discrepancy rate against the published roster below target"],
  risks=["A residual inconsistency between the published roster and the operational sign-on tracking system",
         "Changes approved right up to the publication deadline not being captured in the same cycle",
         "A late publication not giving crew adequate notice to plan personal logistics",
         "The published roster being the version crew actually rely on, making any error operationally consequential"])
