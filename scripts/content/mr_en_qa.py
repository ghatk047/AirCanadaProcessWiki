# -*- coding: utf-8 -*-
"""AC-MR-EN — Engineering and Reliability (6) and AC-MR-QA — Airworthiness, Records and Quality (6)."""
from content_lib import P, S

# ── EN: Engineering and Reliability ─────────────────────────────────────────
P("AC-MR-EN-01",
  desc="An engineering order or aircraft modification is designed and approved, defining the technical "
       "solution and documentation before it can be embodied on the fleet.",
  trig="A modification requirement is identified, from reliability data, a service bulletin or an "
      "operational need.",
  out="An approved engineering order with complete embodiment documentation, ready for planning into "
      "aircraft maintenance visits.",
  note="An engineering order is a genuinely technical design activity, not a paperwork exercise, and its "
      "quality directly determines how smoothly the embodiment work goes when it eventually reaches a "
      "hangar floor.",
  phases=["Requirement definition", "Design and approval", "Documentation finalisation"],
  steps=[
    S("1.1","Define the modification requirement","Engineering Planner","TRAX",
      "Source requirement, reliability finding or service bulletin","Defined requirement",
      "Defined with a clear technical basis for 100 percent of engineering orders","N","N",
      "A requirement defined without a clear technical basis produces an order that is hard to design against"),
    S("2.1","Design the technical solution","Engineering Planner","TRAX",
      "Defined requirement","Designed technical solution",
      "Designed within the project's planning timeline at 90 percent","N","N",
      "Design has to account for the specific aircraft configuration across the fleet, which is not always uniform"),
    S("2.2","Obtain regulatory design approval where required","Engineering Planner","Transport Canada CAWIS",
      "Designed solution","Approved design",
      "Approved before embodiment planning begins for 100 percent of major modifications","Y","N",
      "Regulatory approval timelines are outside Air Canada's own control and can extend the project"),
    S("3.1","Finalise embodiment documentation","Engineering Planner","TRAX",
      "Approved design","Finalised embodiment instructions",
      "Finalised before handoff to maintenance planning at 100 percent","N","N",
      "Documentation quality here directly determines how smoothly embodiment goes on the hangar floor"),
  ],
  kpis=["Defined with a clear technical basis for 100 percent of engineering orders",
        "Approved before embodiment planning begins for 100 percent of major modifications",
        "Finalised before handoff to maintenance planning at 100 percent",
        "Embodiment issues attributable to documentation quality below target"],
  risks=["A requirement defined without a clear technical basis producing a hard-to-design order",
         "Regulatory approval timelines outside Air Canada's control extending the project",
         "Design not accounting for fleet configuration variation that is not always uniform",
         "Documentation quality at finalisation directly determining embodiment difficulty on the hangar floor"])

P("AC-MR-EN-02",
  desc="An airworthiness directive from Transport Canada or the design authority is assessed for "
       "applicability and embodied within its mandated compliance timeframe across the affected fleet.",
  trig="Transport Canada or the type design authority issues an airworthiness directive.",
  out="The directive assessed, embodied across the affected fleet and closed within its mandated compliance "
      "timeframe.",
  note="An airworthiness directive is a mandatory regulatory instruction, not a recommendation, and the "
      "compliance timeframe is set by the regulator based on the safety risk the directive addresses, which "
      "makes this one of the least flexible deadlines anywhere in maintenance planning.",
  phases=["Applicability assessment", "Fleet-wide embodiment planning", "Compliance closure"],
  steps=[
    S("1.1","Assess directive applicability to the fleet","Engineering Planner","Transport Canada CAWIS",
      "Issued directive and fleet configuration","Applicability assessment by tail",
      "Assessed within the directive's initial review period at 100 percent","Y","N",
      "Applicability depends on precise configuration matching that can be ambiguous for a modified fleet"),
    S("2.1","Plan fleet-wide embodiment against compliance deadline","Engineering Planner","TRAX",
      "Applicability assessment and compliance deadline","Embodiment plan by tail",
      "Planned to meet the mandated deadline for 100 percent of applicable tails","N","N",
      "Embodiment planning has to compete for the same maintenance slots as every other scheduled work"),
    S("2.2","Embody the directive at scheduled maintenance opportunity","Base Maintenance Technician","TRAX",
      "Embodiment plan and induced aircraft","Embodied directive",
      "Embodied within the planned window for 95 percent of applicable tails","N","N",
      "A directive with a very short compliance window can require an unscheduled maintenance visit"),
    S("3.1","Close compliance and report to the regulator where required","Engineering Planner","Transport Canada CAWIS",
      "Embodied directive across the fleet","Closed compliance with regulatory reporting",
      "Compliance closed within the mandated deadline at 100 percent","N","N",
      "A directive not closed within its deadline is a direct regulatory compliance failure"),
  ],
  kpis=["Assessed within the directive's initial review period at 100 percent",
        "Planned to meet the mandated deadline for 100 percent of applicable tails",
        "Embodied within the planned window for 95 percent of applicable tails",
        "Compliance closed within the mandated deadline at 100 percent"],
  risks=["A directive not closed within its mandated deadline constituting a direct regulatory compliance failure",
         "A very short compliance window requiring an unscheduled maintenance visit outside the normal cycle",
         "Applicability assessment being ambiguous for a fleet with varying modification configurations",
         "Embodiment planning competing for the same maintenance slots as every other scheduled work"])

P("AC-MR-EN-03",
  desc="A manufacturer service bulletin is evaluated for adoption, distinct from a mandatory airworthiness "
       "directive, weighing technical merit and cost against Air Canada's own fleet experience.",
  trig="A manufacturer issues a service bulletin applicable to Air Canada's fleet.",
  out="A documented adoption decision, embodying the bulletin where justified or declining with a "
      "documented rationale.",
  note="Unlike a mandatory directive, service bulletin adoption is a genuine engineering judgement call, "
      "which means the evaluation has to weigh technical merit against cost and operational disruption "
      "rather than simply complying.",
  phases=["Bulletin evaluation", "Adoption decision", "Embodiment or documented decline"],
  steps=[
    S("1.1","Evaluate technical merit against fleet experience","Engineering Planner","TRAX",
      "Issued service bulletin and fleet reliability history","Technical evaluation",
      "Evaluated within the manufacturer's recommended review period at 90 percent","N","N",
      "Air Canada's own fleet experience can differ materially from the manufacturer's basis for issuing the bulletin"),
    S("2.1","Assess cost against expected benefit","Engineering Planner","TRAX",
      "Technical evaluation","Cost-benefit assessment",
      "Assessed for 100 percent of material bulletins before decision at 100 percent","N","N",
      "Benefit quantification for a reliability improvement is inherently an estimate, not a certainty"),
    S("2.2","Decide adoption, decline or defer","Engineering Planner","TRAX",
      "Cost-benefit assessment","Documented adoption decision",
      "Decision documented with rationale for 100 percent of evaluated bulletins","Y","N",
      "A decline decision has to be documented well enough to defend the reasoning if later questioned"),
    S("3.1","Embody adopted bulletin or close the evaluation","Engineering Planner","TRAX",
      "Adoption decision","Embodied bulletin or closed evaluation record",
      "Closed within the planning cycle at 100 percent","N","N",
      "An open evaluation left unresolved indefinitely represents an unmanaged engineering decision"),
  ],
  kpis=["Evaluated within the manufacturer's recommended review period at 90 percent",
        "Assessed for 100 percent of material bulletins before decision at 100 percent",
        "Decision documented with rationale for 100 percent of evaluated bulletins",
        "Closed within the planning cycle at 100 percent"],
  risks=["Air Canada's own fleet experience differing materially from the manufacturer's basis for the bulletin",
         "Benefit quantification for a reliability improvement being inherently an estimate rather than a certainty",
         "A decline decision not being documented well enough to defend the reasoning if later questioned",
         "An open evaluation left unresolved indefinitely representing an unmanaged engineering decision"])

P("AC-MR-EN-04",
  desc="Fleet reliability is monitored and trended by ATA chapter, identifying components or systems with "
       "degrading reliability before they drive a material increase in defects or AOG events.",
  trig="The recurring reliability monitoring cycle runs, or a specific trend crosses a defined alert "
       "threshold.",
  out="Identified reliability trends by ATA chapter and fleet type, feeding engineering investigation and "
      "corrective action before the trend materially affects operations.",
  note="Reliability trending is meant to catch a degrading system before it becomes a defect pattern, which "
      "means its value is entirely in acting early, on a trend that is not yet an obvious operational "
      "problem.",
  phases=["Data compilation", "Trend analysis", "Investigation triggering"],
  steps=[
    S("1.1","Compile defect and removal data by ATA chapter","Reliability Engineer","TRAX",
      "Technical log and component removal history","Compiled data by ATA chapter",
      "Compiled for 100 percent of ATA chapters each reporting cycle","N","N",
      "Data completeness depends on consistent ATA chapter coding at the original technical log entry"),
    S("2.1","Analyse trend against alert thresholds","Reliability Engineer","Databricks Lakehouse",
      "Compiled data","Trend analysis with threshold comparison",
      "Analysed for 100 percent of ATA chapters each cycle","N","N",
      "Alert thresholds require periodic recalibration as the fleet ages and utilisation patterns change"),
    S("2.2","Screen for early degradation signal","Reliability Engineer","Databricks Lakehouse",
      "Trend analysis","Identified early-stage degradation candidates",
      "Screened before a trend crosses the alert threshold for 70 percent of eventual material issues","Y","N",
      "The entire value of this step is in catching a signal before it becomes an obvious problem"),
    S("3.1","Trigger engineering investigation on confirmed trend","Reliability Engineer","TRAX",
      "Confirmed trend","Triggered investigation with an assigned engineer",
      "Triggered within 5 business days of confirmation at 100 percent","N","N",
      "A trend confirmed but not promptly triggered into investigation loses the early-warning value of catching it"),
  ],
  kpis=["Compiled for 100 percent of ATA chapters each reporting cycle",
        "Analysed for 100 percent of ATA chapters each cycle",
        "Screened before a trend crosses the alert threshold for 70 percent of eventual material issues",
        "Triggered within 5 business days of confirmation at 100 percent"],
  risks=["Alert thresholds going stale as the fleet ages and utilisation patterns change without recalibration",
         "A trend confirmed but not promptly triggered into investigation losing its early-warning value",
         "Data completeness depending on consistent ATA chapter coding at the original technical log entry",
         "The entire value of trending being lost if a signal is only caught after it becomes an obvious problem"])

P("AC-MR-EN-05",
  desc="A predictive maintenance model is developed and deployed, using aircraft sensor and reliability "
       "data to forecast a component failure before it manifests as an in-service defect.",
  trig="A predictive maintenance opportunity is identified for a component with a material failure "
       "consequence, or an existing model requires retraining.",
  out="A deployed predictive model correctly forecasting failure risk, feeding proactive component "
      "replacement scheduling ahead of an in-service failure.",
  note="A false negative and a false positive have very different costs in this application: missing a "
      "genuine failure risk is a safety exposure, while a false alarm wastes a serviceable component's "
      "remaining life, which shapes how the model's threshold has to be set.",
  phases=["Model development", "Validation", "Deployment and monitoring"],
  steps=[
    S("1.1","Develop the predictive model","Reliability Engineer","Databricks Lakehouse",
      "Historical sensor and failure data","Developed model",
      "Developed within the project timeline at 90 percent","N","N",
      "Model training data quality depends on historical sensor data completeness that is not always consistent"),
    S("2.1","Validate model performance against held-out data","Reliability Engineer","Databricks Lakehouse",
      "Developed model and validation data","Validated model performance",
      "Validated against a defined accuracy standard before deployment at 100 percent","Y","N",
      "A false negative and a false positive carry very different costs, and the threshold has to reflect that asymmetry"),
    S("2.2","Deploy model into predictive maintenance workflow","Reliability Engineer","TRAX",
      "Validated model","Deployed model generating predictions",
      "Deployed within the project timeline at 90 percent","N","N",
      "Predictions have to reach materials planning in time to actually act on them before failure"),
    S("3.1","Monitor model performance in production","Reliability Engineer","Databricks Lakehouse",
      "Production predictions and actual outcomes","Production performance monitoring",
      "Monitored on a recurring cycle for 100 percent of deployed models","N","N",
      "A model that drifts in production without monitoring can silently degrade to below its validated accuracy"),
  ],
  kpis=["Validated against a defined accuracy standard before deployment at 100 percent",
        "Deployed within the project timeline at 90 percent",
        "Monitored on a recurring cycle for 100 percent of deployed models",
        "In-service failures avoided through predictive replacement tracked against target"],
  risks=["A false negative representing a genuine safety exposure while a false positive wastes component life",
         "A model drifting in production without monitoring, silently degrading below its validated accuracy",
         "Predictions not reaching materials planning in time to act before the predicted failure occurs",
         "Model training data quality depending on historical sensor data completeness that is not always consistent"])

P("AC-MR-EN-06",
  desc="Technical publications and maintenance manuals are revised and distributed as manufacturer updates "
       "are received, keeping the technical reference documentation current across every maintenance "
       "touchpoint.",
  trig="A manufacturer issues a technical publication revision.",
  out="Current technical publications distributed and available at every maintenance touchpoint, with "
      "superseded revisions withdrawn from use.",
  note="A technician working from a superseded manual can perform a task incorrectly relative to the "
      "current, correct procedure, which makes publication currency a direct maintenance quality control "
      "rather than a documentation administration task.",
  phases=["Revision receipt", "Content review", "Distribution and withdrawal"],
  steps=[
    S("1.1","Receive manufacturer publication revision","Technical Publications Coordinator","TRAX",
      "Manufacturer-issued revision","Received revision",
      "Received and logged within 2 business days of issuance at 100 percent","N","N",
      "Revision delivery timing and format vary by manufacturer and publication type"),
    S("2.1","Review revision for operational impact","Technical Publications Coordinator","TRAX",
      "Received revision","Reviewed impact assessment",
      "Reviewed within 5 business days of receipt at 100 percent","N","N",
      "A revision with a safety-critical change requires faster distribution than a routine editorial update"),
    S("2.2","Distribute revision to affected touchpoints","Technical Publications Coordinator","TRAX eMobility",
      "Reviewed revision","Distributed revision",
      "Distributed to 100 percent of affected touchpoints within the required timeframe","N","N",
      "Distribution has to reach every line station and base, not only the primary maintenance base"),
    S("3.1","Withdraw superseded revision from use","Technical Publications Coordinator","TRAX eMobility",
      "Distributed new revision","Withdrawn superseded revision",
      "Withdrawn within 24 hours of new revision distribution at 100 percent","N","N",
      "A technician working from a superseded manual can perform a task incorrectly relative to the current procedure"),
  ],
  kpis=["Received and logged within 2 business days of issuance at 100 percent",
        "Reviewed within 5 business days of receipt at 100 percent",
        "Distributed to 100 percent of affected touchpoints within the required timeframe",
        "Withdrawn within 24 hours of new revision distribution at 100 percent"],
  risks=["A technician working from a superseded manual performing a task incorrectly relative to the current procedure",
         "Distribution not reaching every line station and base, not only the primary maintenance base",
         "A safety-critical revision not being distributed faster than a routine editorial update would be",
         "Revision delivery timing and format varying by manufacturer, complicating a uniform intake process"])

# ── QA: Airworthiness, Records and Quality ──────────────────────────────────
P("AC-MR-QA-01",
  desc="Aircraft technical records, including the full maintenance history, are maintained and kept "
       "current, forming the permanent airworthiness record that follows the aircraft through its life and "
       "any eventual sale.",
  trig="A maintenance action is performed and requires entry into the permanent technical record.",
  out="A complete, accurate, current technical record for every aircraft in the fleet, correctly reflecting "
      "its full maintenance history.",
  note="Technical records are a permanent legal record with value extending to the aircraft's eventual sale "
      "or lease return, which makes record completeness a long-horizon asset protection question, not just "
      "a compliance administrative task.",
  phases=["Record capture", "Verification", "Permanent archival"],
  steps=[
    S("1.1","Capture maintenance action for the technical record","Technical Records Coordinator","TRAX",
      "Completed maintenance action","Captured record entry",
      "Captured within 24 hours of the maintenance action at 100 percent","N","N",
      "A record not captured promptly risks being missed entirely as work volume accumulates"),
    S("2.1","Verify record completeness against the work performed","Technical Records Coordinator","TRAX",
      "Captured entry and work order","Verified complete record",
      "Verified for 100 percent of entries before archival at 100 percent","Y","N",
      "Verification has to catch a gap between what was actually done and what was recorded"),
    S("3.1","Archive record permanently","Technical Records Coordinator","TRAX",
      "Verified entry","Permanently archived record",
      "Archived within 5 business days of verification at 100 percent","N","N",
      "A record gap discovered years later, at an aircraft sale for instance, can be effectively unrecoverable"),
    S("3.2","Confirm record availability for regulatory and sale review","Technical Records Coordinator","TRAX",
      "Archived record","Confirmed retrievable record",
      "100 percent of archived records retrievable on request within the required timeframe","N","N",
      "A record that is archived but not readily retrievable is functionally as unavailable as a missing one"),
  ],
  kpis=["Captured within 24 hours of the maintenance action at 100 percent",
        "Verified for 100 percent of entries before archival at 100 percent",
        "Archived within 5 business days of verification at 100 percent",
        "Technical record completeness audit findings below target"],
  risks=["A record gap discovered years later, at an aircraft sale for instance, being effectively unrecoverable",
         "A record not captured promptly risking being missed entirely as work volume accumulates",
         "Verification failing to catch a gap between what was actually done and what was recorded",
         "Technical records carrying long-horizon asset value extending to the aircraft's eventual sale"])

P("AC-MR-QA-02",
  desc="Continuing airworthiness compliance is reviewed on a recurring cycle, confirming every aircraft in "
       "the fleet remains in full compliance with its approved maintenance programme.",
  trig="The recurring continuing airworthiness review cycle runs.",
  out="Confirmed continuing airworthiness compliance for every aircraft, with any gap identified and "
      "remediated before it becomes a regulatory finding.",
  note="This review is the systematic check that everything else in maintenance, checks, directives, "
      "deferrals and records, has actually come together correctly for every individual aircraft, rather "
      "than assuming it has because each individual process worked.",
  phases=["Compliance data compilation", "Gap identification", "Remediation"],
  steps=[
    S("1.1","Compile compliance status by aircraft","Quality Assurance Coordinator","TRAX",
      "Check, directive and deferral status across the fleet","Compiled compliance status",
      "Compiled for 100 percent of the fleet each review cycle at 100 percent","N","N",
      "Compliance status spans several distinct maintenance processes that need consistent joining"),
    S("2.1","Identify compliance gaps","Quality Assurance Coordinator","TRAX",
      "Compiled status","Identified gaps by aircraft",
      "Identified for 100 percent of the fleet each review cycle at 100 percent","N","N",
      "A gap in one process, such as a records entry, can be invisible without cross-checking against the others"),
    S("3.1","Remediate identified gaps","Quality Assurance Coordinator","TRAX",
      "Identified gap","Remediated compliance",
      "Remediated within the defined timeframe for 95 percent of identified gaps","N","Y",
      "A gap not remediated before the next review cycle compounds into a more serious finding"),
    S("3.2","Report fleet-wide compliance status","Quality Assurance Coordinator","TRAX",
      "Remediated status","Compliance status report",
      "Reported to safety and engineering leadership each review cycle at 100 percent","N","N",
      "Without a consolidated report, an individual aircraft's compliance status is visible but a fleet-wide pattern is not"),
  ],
  kpis=["Compiled for 100 percent of the fleet each review cycle at 100 percent",
        "Identified for 100 percent of the fleet each review cycle at 100 percent",
        "Remediated within the defined timeframe for 95 percent of identified gaps",
        "Zero unremediated gaps carried into a regulatory audit"],
  risks=["A gap in one process being invisible without systematic cross-checking against the others",
         "A gap not remediated before the next review cycle compounding into a more serious finding",
         "Compliance status spanning several distinct maintenance processes that need consistent joining",
         "Assuming compliance because each individual process worked, without the systematic cross-check"])

P("AC-MR-QA-03",
  desc="Parts and inventory are provisioned and planned against forecast consumption, balancing spares "
       "availability against inventory carrying cost.",
  trig="The recurring parts provisioning planning cycle runs, or an inventory level crosses a reorder "
       "threshold.",
  out="Parts inventory positioned to meet forecast maintenance demand, balancing availability against "
      "carrying cost across the network.",
  note="Provisioning has the same fundamental trade-off as reserve crew sizing in AC-CM-CP-03: insufficient "
      "spares cause AOG delay, excessive spares tie up working capital in inventory that may never be used.",
  phases=["Demand forecasting", "Provisioning calculation", "Network positioning"],
  steps=[
    S("1.1","Forecast part demand from maintenance schedule","Materials Planner","TRAX",
      "Scheduled maintenance and historical consumption","Forecast demand by part",
      "Forecast for 100 percent of active part numbers each cycle","N","N",
      "Unscheduled AOG demand is inherently less predictable than scheduled maintenance demand"),
    S("2.1","Calculate provisioning level against service target","Materials Planner","TRAX",
      "Forecast demand and target service level","Calculated provisioning level",
      "Calculated for 100 percent of active part numbers each cycle","N","N",
      "The availability-versus-carrying-cost trade-off has no single objectively correct answer"),
    S("2.2","Position inventory across the station network","Materials Planner","TRAX",
      "Calculated provisioning level","Positioned inventory by station",
      "Positioned to meet forecast demand at each station at 90 percent","N","N",
      "A part positioned at the wrong station is effectively unavailable for an AOG event elsewhere"),
    S("3.1","Monitor stockout and excess inventory","Materials Planner","SAP Analytics Cloud",
      "Actual consumption against positioned inventory","Stockout and excess report",
      "Reviewed each planning cycle for 100 percent of part categories","N","N",
      "A stockout event and an excess inventory finding both indicate the same underlying forecasting weakness"),
  ],
  kpis=["Forecast for 100 percent of active part numbers each cycle",
        "Positioned to meet forecast demand at each station at 90 percent",
        "AOG delay attributable to parts unavailability below target",
        "Inventory carrying cost against target tracked each cycle"],
  risks=["Insufficient spares causing AOG delay, or excessive spares tying up working capital unnecessarily",
         "A part positioned at the wrong station being effectively unavailable for an AOG event elsewhere",
         "Unscheduled AOG demand being inherently less predictable than scheduled maintenance demand",
         "A stockout and an excess inventory finding both indicating the same underlying forecasting weakness"])

P("AC-MR-QA-04",
  desc="Suppliers of parts and materials are qualified and ordering is executed against Spec 2000 industry "
       "standards, confirming supplier quality before parts enter the serviceable inventory.",
  trig="A new supplier requires qualification, or a routine order is placed against a qualified supplier.",
  out="Parts sourced only from qualified suppliers, ordered against Spec 2000 standards, with quality "
      "confirmed before entering serviceable stock.",
  note="A part that enters serviceable inventory from an unqualified or compromised source is a direct "
      "airworthiness risk, which makes supplier qualification a safety control rather than a purely "
      "commercial procurement discipline.",
  phases=["Supplier qualification", "Spec 2000 order execution", "Receiving quality confirmation"],
  steps=[
    S("1.1","Qualify new supplier against quality standards","Materials Planner","Aeroxchange",
      "Candidate supplier and quality requirements","Qualified or declined supplier",
      "Qualification assessed against defined standards for 100 percent of new suppliers","Y","N",
      "Qualification depends on documentation and audit evidence the supplier itself provides"),
    S("2.1","Execute order against Spec 2000 standards","Materials Planner","Aeroxchange",
      "Part requirement and qualified supplier","Placed Spec 2000 order",
      "Ordered against the standard for 100 percent of qualified supplier orders at 100 percent","N","N",
      "Spec 2000 messaging standardises the transaction but does not itself guarantee part quality"),
    S("2.2","Confirm receiving quality on delivery","Materials Planner","TRAX",
      "Delivered part","Confirmed quality and documentation",
      "Confirmed before entry into serviceable stock for 100 percent of receipts at 100 percent","N","N",
      "A part received without complete traceability documentation cannot legally enter serviceable stock"),
    S("3.1","Enter part into serviceable inventory","Materials Planner","TRAX",
      "Confirmed quality","Entered serviceable inventory",
      "Entered within 24 hours of confirmed quality at 100 percent","N","N",
      "A part entered into inventory without complete quality confirmation is a direct airworthiness risk"),
  ],
  kpis=["Qualification assessed against defined standards for 100 percent of new suppliers",
        "Ordered against the standard for 100 percent of qualified supplier orders at 100 percent",
        "Confirmed before entry into serviceable stock for 100 percent of receipts at 100 percent",
        "Zero parts entering serviceable inventory without complete traceability documentation"],
  risks=["A part entering serviceable inventory from an unqualified or compromised source, a direct airworthiness risk",
         "Qualification depending on documentation and audit evidence the supplier itself provides",
         "A part received without complete traceability documentation being unable to legally enter serviceable stock",
         "Spec 2000 messaging standardising the transaction without itself guaranteeing part quality"])

P("AC-MR-QA-05",
  desc="A maintenance audit finding, whether from an internal audit or a Transport Canada inspection, is "
       "investigated and closed with a documented corrective action.",
  trig="An audit finding is raised by an internal quality audit or a Transport Canada inspection.",
  out="A finding investigated to root cause, with a corrective action implemented and closed within the "
      "required timeframe.",
  note="A finding closed superficially, addressing the immediate symptom without the underlying root cause, "
      "tends to recur at the next audit, which is why root cause discipline matters more here than closure "
      "speed alone.",
  phases=["Finding intake", "Root cause investigation", "Corrective action and closure"],
  steps=[
    S("1.1","Receive and register the audit finding","Quality Assurance Coordinator","TRAX",
      "Audit finding notification","Registered finding with required response deadline",
      "Registered within 2 business days of receipt at 100 percent","N","N",
      "Transport Canada findings carry a specific regulatory response deadline distinct from internal audit findings"),
    S("2.1","Investigate root cause","Quality Assurance Coordinator","TRAX",
      "Registered finding","Root cause determination",
      "Investigated within the defined response window at 100 percent","N","N",
      "A finding closed on the immediate symptom rather than the root cause tends to recur at the next audit"),
    S("2.2","Develop corrective action plan","Quality Assurance Coordinator","TRAX",
      "Root cause determination","Corrective action plan",
      "Developed before the required response deadline at 100 percent","Y","N",
      "A corrective action addressing only the specific instance, not the systemic cause, has limited durability"),
    S("3.1","Implement and close the corrective action","Quality Assurance Coordinator","TRAX",
      "Approved plan","Closed finding with verified corrective action",
      "Closed within the required timeframe for 90 percent of findings","N","N",
      "Closure verification has to confirm the corrective action actually took effect, not just that it was implemented"),
  ],
  kpis=["Registered within 2 business days of receipt at 100 percent",
        "Investigated within the defined response window at 100 percent",
        "Closed within the required timeframe for 90 percent of findings",
        "Repeat finding rate on the same underlying issue below target"],
  risks=["A finding closed on the immediate symptom rather than root cause tending to recur at the next audit",
         "Closure verification not confirming the corrective action actually took effect",
         "A corrective action addressing only the specific instance rather than the systemic cause",
         "Transport Canada findings carrying a specific regulatory response deadline distinct from internal audits"])

P("AC-MR-QA-06",
  desc="Certification and approval status with Transport Canada is maintained current, covering the air "
       "operator certificate and maintenance organisation approval that underpin Air Canada's authority to "
       "operate and maintain its fleet.",
  trig="A certification renewal comes due, or a change to Air Canada's operation requires an amended "
      "approval.",
  out="Current, valid certification and approval status maintained with Transport Canada, with any renewal "
      "or amendment completed before expiry.",
  note="These are the foundational regulatory approvals everything else in flight and maintenance "
      "operations depends on, which makes their currency a board-level compliance concern rather than a "
      "routine administrative renewal.",
  phases=["Renewal and amendment tracking", "Application preparation", "Approval confirmation"],
  steps=[
    S("1.1","Track certification and approval renewal dates","Regulatory Affairs Analyst","Transport Canada CAWIS",
      "Current certification and approval status","Tracked renewal calendar",
      "Tracked continuously with no lapse for 100 percent of approvals","N","N",
      "Multiple distinct certifications and approvals carry different renewal cycles that need independent tracking"),
    S("2.1","Prepare renewal or amendment application","Regulatory Affairs Analyst","Transport Canada CAWIS",
      "Approaching renewal or operational change","Prepared application",
      "Prepared within the required lead time before expiry at 100 percent","N","N",
      "An amendment triggered by an operational change has to be identified proactively, not only at routine renewal"),
    S("2.2","Submit application to Transport Canada","Regulatory Affairs Analyst","Transport Canada CAWIS",
      "Prepared application","Submitted application",
      "Submitted within the required lead time before expiry at 100 percent","N","N",
      "Regulatory processing time is outside Air Canada's own control and has to be planned for"),
    S("3.1","Confirm renewed or amended approval","Regulatory Affairs Analyst","Transport Canada CAWIS",
      "Regulatory decision","Confirmed current approval",
      "Confirmed before the prior approval's expiry at 100 percent","N","N",
      "A lapsed certification or approval would halt the affected operation entirely"),
  ],
  kpis=["Tracked continuously with no lapse for 100 percent of approvals",
        "Prepared within the required lead time before expiry at 100 percent",
        "Submitted within the required lead time before expiry at 100 percent",
        "Confirmed before the prior approval's expiry at 100 percent"],
  risks=["A lapsed certification or approval halting the affected operation entirely",
         "Regulatory processing time being outside Air Canada's own control and needing to be planned for",
         "An operational change requiring an amendment not being proactively identified outside routine renewal",
         "Multiple distinct certifications carrying different renewal cycles that need independent tracking"])
