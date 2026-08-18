# -*- coding: utf-8 -*-
"""AC-FO-OC (5 remaining, OC-05 already in a_pilot) and AC-FO-SR — Safety & Occurrence Reporting (6)."""
from content_lib import P, S

# ── OC: Ops Control and IRROP Recovery ──────────────────────────────────────
P("AC-FO-OC-01",
  desc="Flight watch monitors every active flight through its day of operation, from off-block to on-block, "
       "tracking status against plan and identifying irregularities as early as possible.",
  trig="A flight is off-block and in active flight watch monitoring.",
  out="Continuous, current status awareness of every active flight, with an irregularity detected and "
      "escalated as soon as it emerges.",
  note="Flight watch is the baseline situational awareness function everything else in operations control "
      "depends on; a monitoring gap here delays every downstream recovery decision by exactly as long as the "
      "gap lasted.",
  phases=["Status monitoring", "Irregularity detection", "Escalation"],
  steps=[
    S("1.1","Monitor flight status against plan","Operations Control Analyst","NetLine/Ops",
      "Active flight datalink and ATC position reports","Current status against planned progress",
      "Monitored continuously for 100 percent of active flights","N","N",
      "Datalink coverage gaps over oceanic and remote airspace create monitoring blind spots"),
    S("2.1","Detect deviation from plan","Operations Control Analyst","NetLine/Ops",
      "Current status and planned progress","Detected deviation flag",
      "Material deviations detected within 5 minutes at 95 percent","N","N",
      "A gradual deviation is harder to detect promptly than a sudden, discrete event"),
    S("2.2","Assess deviation severity","Operations Control Analyst","NetLine/Ops",
      "Detected deviation","Severity classification",
      "Classified within 5 minutes of detection at 100 percent","Y","N",
      "Severity classification under uncertainty tends toward caution, which can over-trigger escalation"),
    S("3.1","Escalate to duty manager where required","Operations Control Analyst","Jeppesen OCC",
      "Classified deviation","Escalated case to the duty manager",
      "Escalated within 10 minutes of classification at 100 percent","N","N",
      "Escalation volume during a widespread event can exceed what duty management can individually review"),
  ],
  kpis=["Monitored continuously for 100 percent of active flights",
        "Material deviations detected within 5 minutes at 95 percent",
        "Escalated within 10 minutes of classification at 100 percent",
        "Datalink coverage gap duration tracked and minimised"],
  risks=["Datalink coverage gaps over oceanic and remote airspace creating monitoring blind spots",
         "A gradual deviation being detected later than a sudden, discrete event",
         "Escalation volume during a widespread event exceeding what duty management can individually review",
         "Severity classification under uncertainty defaulting to caution and over-triggering escalation"])

P("AC-FO-OC-02",
  desc="An irregular operations event is formally declared and a recovery plan is developed, mobilising the "
       "cross-functional response across crew, airport and customer teams.",
  trig="A flight watch or station event crosses the threshold for a formal irregular operations declaration.",
  out="A declared IRROP event with an assigned recovery lead and an initial recovery plan communicated "
      "across affected functions.",
  note="A formal IRROP declaration is what mobilises the cross-functional machine; declaring too late means "
      "every affected function starts its own recovery work later than it needed to.",
  phases=["Event declaration", "Recovery plan development", "Cross-functional mobilisation"],
  steps=[
    S("1.1","Assess event against declaration threshold","Operations Control Duty Manager","NetLine/Ops",
      "Event details and scope","Declaration decision",
      "Decision made within 15 minutes of the triggering event at 100 percent","Y","N",
      "A threshold applied too conservatively delays mobilisation of the wider response"),
    S("1.2","Declare the IRROP event","Operations Control Duty Manager","Jeppesen OCC",
      "Declaration decision","Formal IRROP declaration",
      "Declared and communicated within 5 minutes of the decision at 100 percent","N","N",
      "Declaration communication has to reach every affected function simultaneously, not sequentially"),
    S("2.1","Develop initial recovery plan","Operations Control Duty Manager","NetLine/Ops",
      "Declared event and available resources","Initial recovery plan",
      "Initial plan developed within 30 minutes of declaration at 90 percent","N","N",
      "An initial plan developed under time pressure is a working hypothesis, not a final answer"),
    S("3.1","Mobilise cross-functional response","Operations Control Duty Manager","Jeppesen OCC",
      "Recovery plan","Mobilised crew, airport and customer response teams",
      "Mobilised within 15 minutes of plan development at 95 percent","N","N",
      "Mobilisation speed depends on functions that are not all staffed to the same response readiness level"),
  ],
  kpis=["Decision made within 15 minutes of the triggering event at 100 percent",
        "Declared and communicated within 5 minutes of the decision at 100 percent",
        "Initial plan developed within 30 minutes of declaration at 90 percent",
        "Mobilised within 15 minutes of plan development at 95 percent"],
  risks=["A declaration threshold applied too conservatively delaying mobilisation of the wider response",
         "Declaration communication reaching affected functions sequentially rather than simultaneously",
         "An initial recovery plan developed under time pressure being treated as final rather than a working hypothesis",
         "Cross-functional mobilisation speed being limited by functions not staffed to the same readiness level"])

P("AC-FO-OC-03",
  desc="An aircraft swap or rotation recovery plan is executed when the originally planned tail cannot "
       "operate its scheduled rotation, reassigning capacity while protecting maintenance and crew "
       "feasibility.",
  trig="An aircraft becomes unavailable for its scheduled rotation due to a technical, weather or other "
       "operational cause.",
  out="A feasible recovery rotation with an alternate aircraft assigned, protecting downstream flights as "
      "far as possible.",
  note="An aircraft swap decision made quickly to protect the immediate flight can create a cascading "
      "problem several flights downstream in the original rotation, so the recovery has to think several "
      "moves ahead, not just the next one.",
  phases=["Unavailability assessment", "Swap option evaluation", "Recovery execution"],
  steps=[
    S("1.1","Assess aircraft unavailability and cause","Operations Control Duty Manager","TRAX",
      "Reported unavailability","Assessed cause and expected duration",
      "Assessed within 15 minutes of the report at 100 percent","N","N",
      "Expected duration for a technical issue is often uncertain at the point recovery planning must begin"),
    S("2.1","Identify candidate swap aircraft","Operations Control Duty Manager","NetLine/Ops",
      "Unavailable aircraft and fleet position","Candidate swap aircraft list",
      "Candidates identified within 20 minutes of assessment at 90 percent","N","N",
      "A candidate aircraft's own downstream rotation has to be checked before it can be safely swapped"),
    S("2.2","Assess cascading impact on downstream rotation","Operations Control Duty Manager","NetLine/Ops",
      "Candidate swap","Cascading impact assessment",
      "Assessed for 100 percent of candidate swaps before execution","Y","N",
      "A swap that resolves the immediate flight can create a new problem several flights downstream"),
    S("3.1","Execute the swap and notify affected functions","Operations Control Duty Manager","Jeppesen OCC",
      "Selected swap option","Executed swap with cross-functional notification",
      "Notified within 10 minutes of the swap decision at 100 percent","N","N",
      "Crew, maintenance and customer functions all need the swap information simultaneously to act on it"),
  ],
  kpis=["Assessed within 15 minutes of the report at 100 percent",
        "Candidates identified within 20 minutes of assessment at 90 percent",
        "Assessed for 100 percent of candidate swaps before execution",
        "Notified within 10 minutes of the swap decision at 100 percent"],
  risks=["A swap that resolves the immediate flight creating a new cascading problem downstream in the rotation",
         "A candidate aircraft's own downstream rotation not being checked before it is swapped in",
         "Expected duration for a technical issue being genuinely uncertain at the point recovery must begin",
         "Crew, maintenance and customer functions not receiving swap information simultaneously"])

P("AC-FO-OC-04",
  desc="A flight diversion is managed from the decision point through ground handling at the unplanned "
       "airport, coordinating a station that was not expecting to receive the flight.",
  trig="A flight crew declares or operations control identifies the need for a diversion.",
  out="A safely completed diversion with ground handling, passenger care and onward recovery coordinated at "
      "the diversion airport.",
  note="A diversion airport frequently has none of the standard Air Canada ground infrastructure a normal "
      "station has, which means almost everything after the safe landing has to be improvised against a "
      "station relationship that did not previously exist for this flight.",
  phases=["Diversion coordination", "Ground handling arrangement", "Onward recovery"],
  steps=[
    S("1.1","Confirm diversion airport and coordinate with the crew","Operations Control Duty Manager","Jeppesen OCC",
      "Diversion decision","Confirmed diversion airport",
      "Confirmed within 10 minutes of the diversion decision at 100 percent","N","N",
      "The diversion airport may not have been part of the original flight plan's alternate selection"),
    S("2.1","Arrange ground handling at the diversion airport","Operations Control Duty Manager","Amadeus Altea DCS",
      "Confirmed diversion airport","Arranged ground handling agreement",
      "Arranged before or immediately upon arrival at 90 percent","N","N",
      "A station with no existing Air Canada handling relationship requires arrangement from scratch under time pressure"),
    S("2.2","Coordinate passenger care at the diversion airport","Operations Control Duty Manager","Amadeus Passenger Recovery",
      "Diverted passenger complement","Arranged passenger care",
      "Care arranged within regulatory timeframes for 100 percent of diversions","Y","N",
      "Passenger care standards at an unplanned station are harder to guarantee than at a normal operating station"),
    S("3.1","Plan onward recovery from the diversion airport","Operations Control Duty Manager","NetLine/Ops",
      "Diverted aircraft and passengers","Onward recovery plan",
      "Recovery plan developed within 60 minutes of arrival at 85 percent","N","N",
      "Onward recovery competes with continuing the aircraft's original rotation from a station not designed to support either"),
  ],
  kpis=["Confirmed within 10 minutes of the diversion decision at 100 percent",
        "Arranged before or immediately upon arrival at 90 percent",
        "Care arranged within regulatory timeframes for 100 percent of diversions",
        "Recovery plan developed within 60 minutes of arrival at 85 percent"],
  risks=["A diversion airport having none of the standard ground infrastructure a normal station provides",
         "Passenger care standards being harder to guarantee at a station not designed to support this flight",
         "Ground handling arrangement having to be built from scratch under time pressure at an unfamiliar station",
         "Onward recovery competing with the aircraft's original rotation for a resolution the station cannot easily support"])

P("AC-FO-OC-06",
  desc="Operations control coordinates a fallback operating mode when a ground stop or system outage "
       "prevents normal operational tools from functioning, using manual procedures to keep the network "
       "safely moving.",
  trig="A ground stop is declared or a core operational system, such as the departure control or "
       "communicator platform, becomes unavailable.",
  out="Continued safe operation under manual fallback procedures until normal system function is restored.",
  note="The June 2023 communicator outage, which delayed or cancelled the large majority of a day's "
       "flights, is the direct reference point for why a rehearsed fallback procedure matters more than a "
       "hope that the primary system simply does not fail.",
  phases=["Outage detection and fallback activation", "Manual procedure execution", "Restoration transition"],
  steps=[
    S("1.1","Detect system outage or declared ground stop","Operations Control Duty Manager","ITSM Platform",
      "System monitoring or external ground stop notification","Detected outage or ground stop",
      "Detected within 5 minutes of onset at 100 percent","N","N",
      "A gradual system degradation is harder to detect promptly than a sudden hard outage"),
    S("1.2","Activate manual fallback procedure","Operations Control Duty Manager","Jeppesen OCC",
      "Detected outage","Activated fallback procedure",
      "Activated within 10 minutes of detection at 90 percent","N","N",
      "Fallback procedures are used rarely enough that staff familiarity cannot be assumed"),
    S("2.1","Execute manual flight tracking and coordination","Operations Control Analyst","Jeppesen OCC",
      "Activated fallback","Manually tracked flight status",
      "Manual tracking sustained for 100 percent of active flights during the outage","N","N",
      "Manual tracking throughput is materially lower than the automated system it replaces"),
    S("2.2","Coordinate manual communication with stations and crew","Operations Control Analyst","ACARS Datalink",
      "Manual tracking status","Manual station and crew communication",
      "Communication maintained for 100 percent of affected flights during the outage","N","Y",
      "Communication channels not dependent on the failed system have to be identified and used correctly"),
    S("3.1","Transition back to normal system operation","Operations Control Duty Manager","ITSM Platform",
      "Restored system","Confirmed transition with reconciled operational data",
      "Transition completed with full data reconciliation at 100 percent","N","N",
      "Data captured manually during the outage has to be reconciled back into the restored system accurately"),
  ],
  kpis=["Detected within 5 minutes of onset at 100 percent",
        "Activated within 10 minutes of detection at 90 percent",
        "Manual tracking sustained for 100 percent of active flights during the outage",
        "Transition completed with full data reconciliation at 100 percent"],
  risks=["Fallback procedures being used rarely enough that staff familiarity cannot be assumed in a real event",
         "Manual tracking throughput being materially lower than the automated system it temporarily replaces",
         "Data captured manually during the outage not reconciling accurately back into the restored system",
         "A gradual system degradation being detected later than a sudden, unambiguous hard outage"])

# ── SR: Safety and Occurrence Reporting ─────────────────────────────────────
P("AC-FO-SR-01",
  desc="A safety occurrence is captured and reported by any employee who observes it, feeding the safety "
       "management system's hazard register and risk assessment process.",
  trig="An employee observes or is involved in a safety-relevant occurrence during operations.",
  out="A captured, complete occurrence report entered into the safety management system for triage and "
      "follow-up.",
  note="A just culture reporting environment depends on the reporting process itself being genuinely "
      "non-punitive and low-friction; a process that feels risky or burdensome to use suppresses exactly the "
      "reports the safety system most needs.",
  phases=["Occurrence observation", "Report capture", "System entry"],
  steps=[
    S("1.1","Observe and identify a reportable occurrence","Safety Reporting Employee","ITSM Platform",
      "Direct observation or involvement","Identified reportable occurrence",
      "Reportable occurrences identified consistently across employee groups","N","N",
      "What counts as reportable is not always intuitively clear to every employee group"),
    S("2.1","Capture the occurrence report","Safety Reporting Employee","ITSM Platform",
      "Identified occurrence","Captured report with factual detail",
      "Captured within 24 hours of the occurrence at 90 percent","N","N",
      "Report quality depends on the employee's confidence that the process is genuinely non-punitive"),
    S("3.1","Enter report into the safety management system","Safety Management Coordinator","ITSM Platform",
      "Captured report","Entered report in the SMS hazard register",
      "Entered within 48 hours of capture at 100 percent","N","N",
      "A delay between capture and system entry delays every downstream risk assessment"),
    S("3.2","Acknowledge receipt to the reporting employee","Safety Management Coordinator","ITSM Platform",
      "Entered report","Acknowledgement sent to the reporter",
      "Acknowledgement sent within 5 business days at 95 percent","N","N",
      "A reporter who never hears back has less incentive to submit the next report"),
  ],
  kpis=["Captured within 24 hours of the occurrence at 90 percent",
        "Entered within 48 hours of capture at 100 percent",
        "Reporting volume per flight hour tracked as a leading indicator of reporting culture health",
        "Report quality sufficient for triage without follow-up clarification above 80 percent"],
  risks=["A reporting process that feels punitive or burdensome suppressing exactly the reports the system needs most",
         "Inconsistent understanding across employee groups of what actually constitutes a reportable occurrence",
         "A delay between capture and system entry delaying every downstream risk assessment",
         "Report quality varying enough to require follow-up clarification before triage can proceed"])

P("AC-FO-SR-02",
  desc="Hazards identified through occurrence reports, audits or proactive observation are assessed for "
       "risk and entered into the hazard register with a defined mitigation and review cycle.",
  trig="A hazard is identified through an occurrence report, audit finding or proactive safety observation.",
  out="An assessed hazard entered into the register with a documented risk rating and an assigned "
      "mitigation owner.",
  note="The hazard register is the safety management system's living memory; a hazard assessed once and "
      "then never revisited is functionally the same as a hazard never assessed at all.",
  phases=["Hazard identification", "Risk assessment", "Register entry and ownership"],
  steps=[
    S("1.1","Identify the hazard from source material","Safety Management Coordinator","ITSM Platform",
      "Occurrence report, audit finding or observation","Identified hazard",
      "Identified within the standard triage cycle at 100 percent","N","N",
      "A hazard pattern spanning multiple individually minor occurrence reports can be missed if reports are reviewed in isolation"),
    S("2.1","Assess likelihood and severity","Safety Management Coordinator","ITSM Platform",
      "Identified hazard","Risk rating by likelihood and severity",
      "Rated using the standard risk matrix at 100 percent","Y","N",
      "Likelihood and severity assessment involves genuine judgement, particularly for a novel hazard type"),
    S("2.2","Assign mitigation owner and target","Safety Management Coordinator","ITSM Platform",
      "Risk rating","Assigned owner with mitigation target date",
      "100 percent of material hazards assigned an owner and target","N","N",
      "A hazard without a named owner and target date tends to remain unmitigated indefinitely"),
    S("3.1","Enter hazard into the register with review cycle","Safety Management Coordinator","ITSM Platform",
      "Assigned mitigation","Registered hazard with defined review cycle",
      "Entered within 5 business days of assessment at 100 percent","N","N",
      "A hazard entered without a defined review cycle can be assessed once and then never revisited"),
  ],
  kpis=["Rated using the standard risk matrix at 100 percent",
        "100 percent of material hazards assigned an owner and target",
        "Entered within 5 business days of assessment at 100 percent",
        "Hazard mitigation closure rate against target dates tracked"],
  risks=["A hazard pattern spanning multiple individually minor reports being missed if reports are reviewed in isolation",
         "A hazard without a named owner and target date remaining unmitigated indefinitely",
         "A hazard entered without a defined review cycle being assessed once and never revisited",
         "Likelihood and severity assessment involving genuine judgement, particularly for a novel hazard type"])

P("AC-FO-SR-03",
  desc="A safety occurrence meeting mandatory reporting criteria is reported to Transport Canada within the "
       "regulated timeframe, distinct from internal occurrence capture in AC-FO-SR-01.",
  trig="An occurrence is identified as meeting Transport Canada's mandatory reporting criteria under the "
       "Canadian Aviation Regulations.",
  out="A complete, accurate mandatory occurrence report filed with Transport Canada within the regulated "
      "timeframe.",
  note="Mandatory reporting criteria are specific and regulatory, distinct from the broader voluntary "
      "internal reporting culture; correctly identifying which occurrences actually trigger the mandatory "
      "threshold is itself a compliance-critical judgement.",
  phases=["Mandatory criteria assessment", "Report preparation", "Regulatory filing"],
  steps=[
    S("1.1","Assess occurrence against mandatory reporting criteria","Safety Management Coordinator","Transport Canada CAWIS",
      "Occurrence detail","Mandatory reporting determination",
      "Determined within the regulatory assessment window at 100 percent","Y","N",
      "Mandatory criteria interpretation for a borderline occurrence requires careful regulatory judgement"),
    S("2.1","Prepare the mandatory occurrence report","Safety Management Coordinator","ITSM Platform",
      "Determined mandatory occurrence","Prepared report with required regulatory fields",
      "Prepared within the required lead time before the filing deadline at 100 percent","N","N",
      "Regulatory report fields do not always map directly to the internal occurrence report structure"),
    S("3.1","File with Transport Canada","Safety Management Coordinator","Transport Canada CAWIS",
      "Prepared report","Filed regulatory report",
      "Filed within the mandatory reporting deadline at 100 percent","N","N",
      "A missed mandatory reporting deadline is itself a regulatory compliance failure"),
    S("3.2","Retain filing confirmation for audit evidence","Safety Management Coordinator","ITSM Platform",
      "Filed report","Retained confirmation record",
      "100 percent of mandatory filings retained with confirmation for the required period","N","N",
      "Filing confirmation retention feeds directly into the IOSA audit evidence base in AC-FO-SR-06"),
  ],
  kpis=["Determined within the regulatory assessment window at 100 percent",
        "Prepared within the required lead time before the filing deadline at 100 percent",
        "Filed within the mandatory reporting deadline at 100 percent",
        "Zero missed mandatory reporting deadlines"],
  risks=["Mandatory criteria interpretation for a borderline occurrence requiring careful regulatory judgement",
         "A missed mandatory reporting deadline constituting a regulatory compliance failure in itself",
         "Regulatory report fields not mapping directly to the internal occurrence report structure",
         "An occurrence incorrectly assessed as non-mandatory when it actually met the reporting threshold"])

P("AC-FO-SR-04",
  desc="Flight data from the aircraft's recorders is monitored and analysed to identify operational trends "
       "and exceedances, feeding proactive safety management independent of any specific reported occurrence.",
  trig="The recurring flight data monitoring analysis cycle runs on downloaded flight data.",
  out="Identified operational trends and exceedances feeding both individual crew debriefing where "
      "appropriate and systemic safety management findings.",
  note="Flight data monitoring finds patterns that no individual occurrence report would ever surface, "
      "because it looks at the aggregate of thousands of flights rather than at the events crew or ground "
      "staff happened to notice and report.",
  phases=["Data download and processing", "Trend and exceedance analysis", "Findings distribution"],
  steps=[
    S("1.1","Download and process flight data","Flight Data Analyst","NetLine/Ops",
      "Aircraft recorder data","Processed flight data set",
      "Processed for 100 percent of flights within the standard cycle","N","N",
      "Data download opportunity depends on aircraft connectivity and ground time"),
    S("2.1","Screen for defined exceedance events","Flight Data Analyst","Databricks Lakehouse",
      "Processed flight data","Identified exceedance events",
      "Screened for 100 percent of processed flights each cycle","N","N",
      "Exceedance thresholds require periodic recalibration as fleet and operating patterns change"),
    S("2.2","Analyse fleet-wide operational trends","Flight Data Analyst","Databricks Lakehouse",
      "Aggregated flight data history","Identified trend findings",
      "Trends analysed each reporting cycle for 100 percent of fleet types","N","N",
      "A genuine trend can be masked by normal flight-to-flight variance if the analysis window is too short"),
    S("3.1","Distribute findings to safety management and training","Flight Data Analyst","ITSM Platform",
      "Exceedance and trend findings","Distributed findings report",
      "Distributed within 10 business days of the analysis cycle at 100 percent","N","N",
      "Findings distributed without a clear owner for follow-up action risk going unactioned"),
  ],
  kpis=["Processed for 100 percent of flights within the standard cycle",
        "Screened for 100 percent of processed flights each cycle",
        "Distributed within 10 business days of the analysis cycle at 100 percent",
        "Identified trends closed to a mitigation action within one reporting cycle at target rate"],
  risks=["A genuine trend being masked by normal flight-to-flight variance if the analysis window is too short",
         "Exceedance thresholds going stale as fleet and operating patterns change without recalibration",
         "Findings distributed without a clear owner for follow-up action, risking they go unactioned",
         "Data download opportunity being constrained by aircraft connectivity and available ground time"])

P("AC-FO-SR-05",
  desc="Crew fatigue reports are reviewed against fatigue risk management standards, assessing whether a "
       "specific pairing or roster pattern is contributing to a fatigue risk trend.",
  trig="A crew member submits a fatigue report, or the recurring fatigue risk management review cycle runs.",
  out="A reviewed fatigue report with any contributing pairing or roster pattern identified and fed back "
      "into crew planning.",
  note="A fatigue report submitted by an individual crew member is most valuable when it is reviewed "
      "against the pattern across the whole crew base, not evaluated purely as a single, isolated incident.",
  phases=["Fatigue report intake", "Pattern analysis", "Feedback to crew planning"],
  steps=[
    S("1.1","Receive and register the fatigue report","Fatigue Risk Management Coordinator","ITSM Platform",
      "Crew-submitted fatigue report","Registered report",
      "Registered within 24 hours of submission at 100 percent","N","N",
      "Fatigue reports arrive without a standardised structure that makes cross-report comparison easy"),
    S("2.1","Assess the individual report against fatigue standards","Fatigue Risk Management Coordinator","Jeppesen Crew",
      "Registered report and pairing detail","Assessed report against fatigue risk criteria",
      "Assessed within 5 business days of registration at 100 percent","Y","N",
      "Individual fatigue experience is genuinely subjective and hard to assess against an objective standard alone"),
    S("2.2","Screen for a contributing pairing or roster pattern","Fatigue Risk Management Coordinator","Databricks Lakehouse",
      "Assessed report and historical fatigue report data","Identified pattern or isolated case",
      "Screened against the historical pattern for 100 percent of material reports","N","N",
      "A pattern across multiple crew members on the same pairing type can be missed if each report is assessed in isolation"),
    S("3.1","Feed pattern findings back to crew planning","Fatigue Risk Management Coordinator","Jeppesen Crew",
      "Identified pattern","Feedback to the crew planning process",
      "Fed back within one planning cycle of confirmation at 100 percent","N","N",
      "The feedback loop from finding to an actual pairing design change can take a full planning cycle to close"),
  ],
  kpis=["Registered within 24 hours of submission at 100 percent",
        "Assessed within 5 business days of registration at 100 percent",
        "Screened against the historical pattern for 100 percent of material reports",
        "Fed back within one planning cycle of confirmation at 100 percent"],
  risks=["A pattern across multiple crew members on the same pairing type being missed if reports are assessed in isolation",
         "Individual fatigue experience being genuinely subjective and hard to assess against an objective standard",
         "The feedback loop from finding to an actual pairing design change taking a full planning cycle to close",
         "Fatigue reports arriving without a standardised structure that makes cross-report comparison difficult"])

P("AC-FO-SR-06",
  desc="Records and evidence are assembled and maintained to support Air Canada's IOSA operational safety "
       "audit, demonstrating ongoing compliance with the Star Alliance membership safety standard.",
  trig="The recurring IOSA audit cycle approaches, or a continuous evidence maintenance requirement applies "
       "between audit cycles.",
  out="Complete, current audit evidence available for IOSA review, demonstrating sustained safety management "
      "compliance rather than a point-in-time preparation exercise.",
  note="IOSA is not merely an internal safety exercise, it is a condition of Star Alliance membership, which "
      "means an audit finding has commercial and alliance-relationship consequences beyond the safety "
      "domain itself.",
  phases=["Evidence identification", "Continuous maintenance", "Audit preparation"],
  steps=[
    S("1.1","Identify required evidence against IOSA standards","Safety Management Coordinator","ITSM Platform",
      "Current IOSA standard set","Mapped evidence requirement by standard",
      "Mapped for 100 percent of applicable standards each audit cycle","N","N",
      "IOSA standards are periodically revised, and evidence mapping has to stay current with the latest version"),
    S("2.1","Maintain evidence continuously between audits","Safety Management Coordinator","ITSM Platform",
      "Ongoing safety management activity","Continuously updated evidence record",
      "Evidence updated on a rolling basis rather than only before an audit at 100 percent","N","N",
      "Evidence assembled only in the weeks before an audit is a weaker demonstration of sustained compliance"),
    S("2.2","Conduct internal readiness review","Safety Management Coordinator","ITSM Platform",
      "Maintained evidence","Readiness review findings",
      "Conducted at least 90 days before the scheduled audit at 100 percent","Y","N",
      "A readiness review finding a gap close to the audit date leaves little time for genuine remediation"),
    S("3.1","Present evidence to the IOSA audit team","Safety Management Coordinator","ITSM Platform",
      "Reviewed and complete evidence","Presented audit evidence",
      "Presented complete and organised for 100 percent of requested standards","N","N",
      "Evidence organisation quality directly affects how efficiently the audit team can complete their review"),
  ],
  kpis=["Mapped for 100 percent of applicable standards each audit cycle",
        "Evidence updated on a rolling basis rather than only before an audit at 100 percent",
        "Conducted at least 90 days before the scheduled audit at 100 percent",
        "IOSA audit findings closed within the required remediation timeframe at 100 percent"],
  risks=["Evidence assembled only in the weeks before an audit being a weaker demonstration of sustained compliance",
         "A readiness review finding a gap close to the audit date leaving little time for genuine remediation",
         "IOSA standards being periodically revised, requiring evidence mapping to stay current",
         "An audit finding carrying commercial and Star Alliance membership consequences beyond the safety domain"])
