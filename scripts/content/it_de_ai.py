# -*- coding: utf-8 -*-
"""AC-IT-DE — Data Engineering and Integration (5) and AC-IT-AI (4 remaining, AI-03 already in a_pilot)."""
from content_lib import P, S

# ── DE: Data Engineering and Integration ────────────────────────────────────
P("AC-IT-DE-01",
  desc="Data from a source system, such as Amadeus Altea or TRAX, is ingested into the Databricks "
       "lakehouse, the same pipeline discipline referenced across the operational domains this wiki covers.",
  trig="A scheduled data ingestion pipeline runs, or a new source system is onboarded requiring a new "
       "pipeline.",
  out="Current, validated source data available in the lakehouse for downstream analytics and AI model use "
      "across every function that depends on it.",
  note="This is the same pipeline discipline described specifically for revenue management data in "
      "AC-RM-YM-06, applied at the enterprise level across every source system feeding the lakehouse, since "
      "the underlying quality and validation principles do not change by function.",
  phases=["Pipeline execution", "Data quality validation", "Availability confirmation"],
  steps=[
    S("1.1","Execute scheduled ingestion pipeline","Data Engineer","Databricks Lakehouse",
      "Source system data","Ingested raw data in the lakehouse",
      "Pipelines complete within the scheduled window at 99 percent","N","N",
      "A source system schema change can silently break a downstream pipeline transformation"),
    S("2.1","Validate data quality against defined rules","Data Engineer","Databricks Lakehouse",
      "Ingested data","Quality validation report",
      "Validated for 100 percent of scheduled runs","N","N",
      "Quality rules cover known failure modes but cannot anticipate every new class of data issue"),
    S("2.2","Remediate quality failures","Data Engineer","Unity Catalog",
      "Quality validation failure","Remediated data or documented known issue",
      "Remediated within 1 business day of detection at 90 percent","N","Y",
      "Remediation sometimes requires a source system fix outside the data team's direct control"),
    S("3.1","Confirm availability to downstream consumers","Data Engineer","Databricks Lakehouse",
      "Validated data","Confirmed availability",
      "Confirmed within the scheduled window at 100 percent","N","N",
      "Downstream model and dashboard consumers are not always notified when availability is delayed"),
  ],
  kpis=["Pipelines complete within the scheduled window at 99 percent",
        "Validated for 100 percent of scheduled runs",
        "Remediated within 1 business day of detection at 90 percent",
        "Confirmed within the scheduled window at 100 percent"],
  risks=["A source system schema change silently breaking a downstream pipeline transformation",
         "Quality rules missing an entirely new class of data issue not anticipated in the rule set",
         "Remediation depending on a source system fix outside the data team's direct control",
         "Downstream consumers not being notified when data availability is delayed"])

P("AC-IT-DE-02",
  desc="An interface or API is designed, built and versioned across its lifecycle, governing how internal "
       "systems and external partners exchange data with Air Canada's platforms.",
  trig="A new interface requirement is identified, or an existing interface requires a version change.",
  out="A documented, versioned interface meeting the consuming system's requirements, deployed with "
      "appropriate backward compatibility.",
  note="Interface design decisions have a much longer lifespan than the project that originally created "
      "them, since other systems build dependencies on the interface's specific behaviour that persist long "
      "after the original requirement is forgotten.",
  phases=["Interface design", "Build and versioning", "Deployment and lifecycle management"],
  steps=[
    S("1.1","Design the interface specification","Integration Analyst","ITSM Platform",
      "Consumer requirement","Designed interface specification",
      "Designed with documented versioning approach for 100 percent of new interfaces","N","N",
      "A design decision here has a much longer lifespan than the project that originally created it"),
    S("2.1","Build and test the interface","Integration Analyst","ITSM Platform",
      "Design specification","Built and tested interface",
      "Tested against 100 percent of documented consumer scenarios before release","N","N",
      "Test coverage rarely spans every consumer's actual usage pattern, only the documented ones"),
    S("2.2","Version and document the interface","Integration Analyst","ITSM Platform",
      "Built interface","Versioned and documented interface",
      "Documented for 100 percent of released interfaces at 100 percent","N","N",
      "Undocumented interface behaviour becomes tribal knowledge that is lost when the original team moves on"),
    S("3.1","Deploy with backward compatibility management","Integration Analyst","ITSM Platform",
      "Versioned interface","Deployed interface with compatibility plan",
      "Deployed without breaking an existing consumer at 100 percent","N","N",
      "Breaking a consumer that depends on old interface behaviour is a common cause of an unexpected downstream failure"),
  ],
  kpis=["Designed with documented versioning approach for 100 percent of new interfaces",
        "Tested against 100 percent of documented consumer scenarios before release",
        "Documented for 100 percent of released interfaces at 100 percent",
        "Deployed without breaking an existing consumer at 100 percent"],
  risks=["A design decision having a much longer lifespan than the project that originally created it",
         "Test coverage spanning only documented consumer scenarios, not every actual usage pattern",
         "Undocumented interface behaviour becoming tribal knowledge lost when the original team moves on",
         "Breaking an existing consumer that depends on old behaviour causing an unexpected downstream failure"])

P("AC-IT-DE-03",
  desc="IATA Type-B and EDIFACT airline messaging is operated and monitored, the legacy but still "
       "load-bearing messaging layer underneath schedule, PNL, ADL and interline communication across the "
       "estate.",
  trig="The Type-B and EDIFACT messaging gateway processes a continuous stream of industry airline "
       "messages.",
  out="Continuous, reliable operation of the messaging gateway, with any interruption detected and resolved "
      "before it disrupts a dependent operational process.",
  note="This messaging standard predates almost every other integration pattern in the estate but still "
      "carries genuinely load-bearing traffic, schedule change, PNL and ADL, which means an outage here has "
      "consequences that reach all the way back to network planning and departure control.",
  phases=["Message flow monitoring", "Issue detection and resolution", "Reliability reporting"],
  steps=[
    S("1.1","Monitor message flow through the gateway","Integration Analyst","IATA Type-B Messaging",
      "Continuous message traffic","Monitored flow status",
      "Monitored continuously with 100 percent coverage","N","N",
      "Message volume and format variety across the whole industry make comprehensive monitoring genuinely complex"),
    S("2.1","Detect message delivery failure or delay","Integration Analyst","IATA Type-B Messaging",
      "Monitored flow","Detected failure or delay",
      "Detected within 5 minutes of a material delay at 100 percent","N","N",
      "A delayed schedule or PNL message has downstream consequences that reach back into network planning and departure control"),
    S("2.2","Resolve the delivery issue","Integration Analyst","ITSM Platform",
      "Detected issue","Resolved delivery",
      "Resolved within the defined service level at 90 percent","N","Y",
      "Resolution can depend on a third-party message routing provider outside Air Canada's direct control"),
    S("3.1","Report gateway reliability performance","Integration Analyst","ITSM Platform",
      "Resolved and ongoing issues","Reliability performance report",
      "Reported each reporting cycle at 100 percent","N","N",
      "This messaging layer is old enough that its reliability is sometimes assumed rather than actively measured"),
  ],
  kpis=["Monitored continuously with 100 percent coverage",
        "Detected within 5 minutes of a material delay at 100 percent",
        "Resolved within the defined service level at 90 percent",
        "Gateway uptime meeting target each reporting cycle"],
  risks=["A delayed schedule or PNL message having downstream consequences reaching back into network planning",
         "Resolution depending on a third-party message routing provider outside Air Canada's direct control",
         "This legacy messaging layer's reliability being assumed rather than actively measured given its age",
         "Message volume and format variety across the whole industry making comprehensive monitoring genuinely complex"])

P("AC-IT-DE-04",
  desc="Data quality across the lakehouse is monitored on a standing basis, independent of any individual "
       "pipeline's own validation, catching a data quality issue that crosses multiple source systems.",
  trig="The recurring cross-system data quality monitoring cycle runs.",
  out="A data quality report identifying issues that individual pipeline validation alone would not catch, "
      "routed to the appropriate data owner for remediation.",
  note="An individual pipeline's own quality check, as in AC-IT-DE-01, cannot catch an inconsistency that "
      "only becomes visible when data from two different source systems is compared, which is what this "
      "standing monitoring layer exists to find.",
  phases=["Cross-system quality screening", "Issue investigation", "Remediation routing"],
  steps=[
    S("1.1","Screen for cross-system data inconsistency","Data Engineer","Databricks Lakehouse",
      "Data from multiple ingested source systems","Screened inconsistency findings",
      "Screened for 100 percent of defined cross-system checks each cycle","N","N",
      "A cross-system check depends on both source systems' data being genuinely comparable in the first place"),
    S("2.1","Investigate flagged inconsistencies","Data Engineer","Unity Catalog",
      "Screening findings","Investigated root cause",
      "Investigated within 5 business days of flagging at 90 percent","N","N",
      "Root cause can sit in either source system or in the transformation logic joining them, complicating diagnosis"),
    S("3.1","Route remediation to the responsible data owner","Data Engineer","ITSM Platform",
      "Investigated finding","Routed remediation with an owner",
      "Routed within 2 business days of investigation at 100 percent","N","N",
      "A finding routed without a clear owner defaults to being unresolved across data quality review cycles"),
    S("3.2","Track remediation to closure","Data Engineer","ITSM Platform",
      "Routed remediation","Closed remediation record",
      "Closed within the defined timeframe for 90 percent of routed findings","N","N",
      "A remediation not tracked to closure can recur in the next standing screening cycle unresolved"),
  ],
  kpis=["Screened for 100 percent of defined cross-system checks each cycle",
        "Investigated within 5 business days of flagging at 90 percent",
        "Routed within 2 business days of investigation at 100 percent",
        "Cross-system data quality issues resolved within one review cycle at target rate"],
  risks=["A finding routed without a clear owner defaulting to being unresolved across data quality review cycles",
         "Root cause sitting in either source system or the transformation logic joining them, complicating diagnosis",
         "A cross-system check depending on both source systems' data being genuinely comparable in the first place",
         "An inconsistency only becoming visible when compared across systems, invisible to any single pipeline check"])

P("AC-IT-DE-05",
  desc="Legacy Cloudera workloads are migrated to the Databricks lakehouse, retiring the legacy platform "
       "while maintaining continuity for every dependent analytics and reporting process during the "
       "transition.",
  trig="A Cloudera-hosted workload is scheduled for its migration wave to Databricks.",
  out="The workload migrated with validated output parity, running on Databricks with the legacy Cloudera "
      "version retired once parity is confirmed.",
  note="This migration mirrors the same interim double-entry risk pattern seen in the Cargospot cutover in "
      "AC-CG-CP-04: a workload that runs on both platforms during transition creates a reconciliation burden "
      "and a window where the two outputs can diverge.",
  phases=["Migration readiness", "Parallel run and validation", "Legacy retirement"],
  steps=[
    S("1.1","Assess migration readiness for the workload","Data Engineer","Cloudera",
      "Candidate Cloudera workload","Readiness assessment",
      "Assessed before migration wave begins for 100 percent of scheduled workloads","N","N",
      "Some legacy transformations carry undocumented business logic that is not fully understood before migration begins"),
    S("2.1","Migrate and run in parallel on Databricks","Data Engineer","Databricks Lakehouse",
      "Assessed workload","Parallel-running workload on both platforms",
      "Parallel run maintained for the defined validation period at 100 percent","N","N",
      "Running on both platforms during transition creates a reconciliation burden and a divergence risk"),
    S("2.2","Validate output parity between platforms","Data Engineer","Databricks Lakehouse",
      "Parallel outputs","Validated parity or identified discrepancy",
      "Parity validated before legacy retirement for 100 percent of migrated workloads","Y","N",
      "A discrepancy discovered late in the parallel run period compresses the time available to resolve it before retirement"),
    S("3.1","Retire legacy Cloudera workload","Data Engineer","Cloudera",
      "Confirmed parity","Retired legacy workload",
      "Retired within 10 business days of confirmed parity at 100 percent","N","N",
      "A legacy workload retired before parity is genuinely confirmed risks a silent downstream reporting error"),
  ],
  kpis=["Assessed before migration wave begins for 100 percent of scheduled workloads",
        "Parallel run maintained for the defined validation period at 100 percent",
        "Parity validated before legacy retirement for 100 percent of migrated workloads",
        "Retired within 10 business days of confirmed parity at 100 percent"],
  risks=["Undocumented business logic in a legacy transformation not being fully understood before migration",
         "A discrepancy discovered late in the parallel run compressing the time available to resolve it",
         "A legacy workload retired before parity is genuinely confirmed risking a silent downstream reporting error",
         "Running on both platforms during transition creating a reconciliation burden and divergence risk"])

# ── AI: AI and ML Platform (remaining 4) ────────────────────────────────────
P("AC-IT-AI-01",
  desc="A proposed AI use case is assessed for business value and feasibility before it enters the "
       "development pipeline, distinct from the governance and control design process in AC-IT-AI-03.",
  trig="A business function proposes an AI use case.",
  out="A use case either approved to enter development with a defined value case, or declined with "
      "documented reasoning.",
  note="Value assessment happens before governance design specifically because a use case that is not "
      "commercially or operationally worthwhile does not merit the governance investment described in "
      "AC-IT-AI-03; the two processes are sequential, not parallel.",
  phases=["Use case intake", "Value and feasibility assessment", "Development decision"],
  steps=[
    S("1.1","Receive and register the proposed use case","AI Product Manager","ITSM Platform",
      "Business function proposal","Registered use case",
      "Registered within 5 business days of proposal at 100 percent","N","N",
      "Proposals arrive with varying levels of business case detail depending on the proposing function's own maturity"),
    S("2.1","Assess business value and feasibility","AI Product Manager","Databricks Lakehouse",
      "Registered proposal","Value and feasibility assessment",
      "Assessed within the standard intake cycle at 100 percent","N","N",
      "Value estimation for a novel AI use case is inherently more speculative than for a conventional IT project"),
    S("2.2","Screen against available data and technical feasibility","AI Product Manager","Databricks Lakehouse",
      "Value assessment","Technical feasibility screening",
      "Screened for 100 percent of value-approved use cases at 100 percent","Y","N",
      "A use case that is commercially attractive can still be technically infeasible given actual data availability"),
    S("3.1","Approve or decline entry to development","AI Product Manager","ITSM Platform",
      "Feasibility screening","Development decision with documented rationale",
      "Decided within the standard intake cycle at 100 percent","N","N",
      "A declined use case without documented rationale can be re-proposed repeatedly without addressing the original reason"),
  ],
  kpis=["Registered within 5 business days of proposal at 100 percent",
        "Assessed within the standard intake cycle at 100 percent",
        "Screened for 100 percent of value-approved use cases at 100 percent",
        "Decided within the standard intake cycle at 100 percent"],
  risks=["Value estimation for a novel AI use case being inherently more speculative than a conventional IT project",
         "A use case that is commercially attractive still being technically infeasible given actual data availability",
         "A declined use case without documented rationale being re-proposed repeatedly without resolution",
         "Proposals arriving with varying business case detail depending on the proposing function's own maturity"])

P("AC-IT-AI-02",
  desc="An approved AI use case is developed, with features engineered from the Databricks lakehouse and "
       "the model trained against a defined performance target.",
  trig="A use case is approved for development following the assessment in AC-IT-AI-01.",
  out="A trained model meeting its defined performance target, ready for the governance and control design "
      "process before production deployment.",
  note="Model development on Air Canada's data is only as good as the lakehouse feeding it, which makes "
      "development quality directly dependent on the data engineering discipline in AC-IT-DE-01 rather than "
      "a self-contained activity.",
  phases=["Feature engineering", "Model training", "Performance validation"],
  steps=[
    S("1.1","Engineer features from lakehouse data","ML Engineer","Databricks Lakehouse",
      "Approved use case and available data","Engineered feature set",
      "Engineered within the project timeline at 90 percent","N","N",
      "Feature engineering quality is directly dependent on the underlying data quality established in AC-IT-DE-01"),
    S("2.1","Train the model against the feature set","ML Engineer","Databricks Lakehouse",
      "Engineered features","Trained model",
      "Trained within the project timeline at 90 percent","N","N",
      "Training data representativeness determines whether the model generalises to real production conditions"),
    S("2.2","Validate model performance against target","ML Engineer","Databricks Lakehouse",
      "Trained model","Validated performance",
      "Validated against the defined target before handoff at 100 percent","Y","N",
      "A model meeting an aggregate performance target can still underperform badly on a specific important subgroup"),
    S("3.1","Hand off to governance for control design","ML Engineer","ITSM Platform",
      "Validated model","Handed off model with performance documentation",
      "Handed off within 5 business days of validation at 100 percent","N","N",
      "A model handed off without complete performance documentation slows the governance process in AC-IT-AI-03"),
  ],
  kpis=["Engineered within the project timeline at 90 percent",
        "Trained within the project timeline at 90 percent",
        "Validated against the defined target before handoff at 100 percent",
        "Handed off within 5 business days of validation at 100 percent"],
  risks=["Feature engineering quality being directly dependent on the underlying data engineering discipline",
         "A model meeting an aggregate performance target while still underperforming badly on an important subgroup",
         "Training data representativeness determining whether the model generalises to real production conditions",
         "A model handed off without complete performance documentation slowing the governance process"])

P("AC-IT-AI-04",
  desc="A deployed AI model is monitored in production for drift and performance degradation, with the "
       "model retrained or withdrawn when it no longer meets its validated performance standard.",
  trig="A model is deployed to production following governance approval in AC-IT-AI-03.",
  out="Continuous production monitoring with drift detected early, and the model retrained or withdrawn "
      "before its degraded performance causes material harm.",
  note="Production monitoring is what keeps the governance approval in AC-IT-AI-03 meaningful over time, "
      "since a model approved once under specific validated conditions can silently drift away from those "
      "conditions without ever being explicitly re-approved.",
  phases=["Production performance tracking", "Drift detection", "Retraining or withdrawal decision"],
  steps=[
    S("1.1","Track production performance against validated baseline","ML Engineer","Databricks Lakehouse",
      "Live production predictions and outcomes","Tracked performance",
      "Tracked continuously for 100 percent of deployed models","N","N",
      "Ground truth outcomes for comparison are not always available in real time for every model type"),
    S("2.1","Detect performance drift against threshold","ML Engineer","Databricks Lakehouse",
      "Tracked performance","Detected drift or confirmed stability",
      "Detected within one monitoring cycle of drift beginning at 90 percent","Y","N",
      "A model approved once under specific conditions can silently drift away from them without ever being re-approved"),
    S("2.2","Investigate drift root cause","ML Engineer","Databricks Lakehouse",
      "Detected drift","Root cause hypothesis",
      "Investigated within 5 business days of detection at 100 percent","N","N",
      "Drift root cause can be a genuine change in underlying conditions rather than a model defect"),
    S("3.1","Retrain, constrain or withdraw the model","ML Engineer","ITSM Platform",
      "Investigated drift","Retrained, constrained or withdrawn model",
      "Action taken within 10 business days of confirmed drift at 100 percent","N","Y",
      "A withdrawal decision has to route back through governance if the model is customer-facing, per AC-IT-AI-03"),
  ],
  kpis=["Tracked continuously for 100 percent of deployed models",
        "Detected within one monitoring cycle of drift beginning at 90 percent",
        "Investigated within 5 business days of detection at 100 percent",
        "Action taken within 10 business days of confirmed drift at 100 percent"],
  risks=["A model approved once under specific conditions silently drifting away from them without re-approval",
         "Ground truth outcomes for comparison not being available in real time for every model type",
         "Drift root cause being a genuine change in underlying conditions rather than a model defect",
         "A withdrawal decision for a customer-facing model needing to route back through governance"])

P("AC-IT-AI-05",
  desc="A customer-facing AI assistant's grounding content is maintained current against the source policy "
       "it references, keeping the assistant's allow-listed knowledge base synchronised with actual, "
       "current Air Canada policy.",
  trig="A source policy referenced by the virtual assistant's grounding content changes.",
  out="The assistant's grounding content updated to reflect current policy, with the change validated "
      "before it affects live customer-facing responses.",
  note="This is the ongoing maintenance discipline that keeps the governance control designed in AC-IT-AI-03 "
      "actually meaningful day to day; a governance framework that approves grounding sources once and never "
      "revisits their currency is not really governing anything in an ongoing sense.",
  phases=["Policy change detection", "Grounding content update", "Validation before live effect"],
  steps=[
    S("1.1","Detect a source policy change","AI Governance Lead","Air Canada Virtual Assistant",
      "Updated policy content in an allow-listed source","Detected policy change",
      "Detected within 24 hours of the policy update at 90 percent","N","N",
      "Detection depends on the policy owner correctly notifying the AI governance function of a change"),
    S("2.1","Update the assistant's grounding content","AI Governance Lead","Air Canada Virtual Assistant",
      "Detected change","Updated grounding content",
      "Updated within 2 business days of detection at 95 percent","N","N",
      "An update applied incorrectly can introduce a new inconsistency rather than resolving the original one"),
    S("2.2","Validate updated content against current policy","AI Governance Lead","Air Canada Virtual Assistant",
      "Updated grounding content","Validated content",
      "Validated before it affects live responses for 100 percent of updates at 100 percent","Y","N",
      "A grounding update not validated before going live risks stating an incorrect version of the new policy"),
    S("3.1","Confirm live effect and monitor for residual inconsistency","AI Governance Lead","Air Canada Virtual Assistant",
      "Validated update","Confirmed live effect",
      "Confirmed within 24 hours of validation at 100 percent","N","N",
      "A governance framework that approves grounding sources once and never revisits currency is not really governing"),
  ],
  kpis=["Detected within 24 hours of the policy update at 90 percent",
        "Updated within 2 business days of detection at 95 percent",
        "Validated before it affects live responses for 100 percent of updates at 100 percent",
        "Confirmed within 24 hours of validation at 100 percent"],
  risks=["A governance framework approving grounding sources once and never revisiting their currency",
         "Detection depending on the policy owner correctly notifying the AI governance function of a change",
         "An update applied incorrectly introducing a new inconsistency rather than resolving the original one",
         "A grounding update not validated before going live risking an incorrect statement of the new policy"])
