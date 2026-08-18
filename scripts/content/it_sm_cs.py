# -*- coding: utf-8 -*-
"""AC-IT-SM — Service Management and User Support (5) and AC-IT-CS — Cybersecurity and Identity (5)."""
from content_lib import P, S

# ── SM: Service Management and User Support ─────────────────────────────────
P("AC-IT-SM-01",
  desc="An IT incident is detected, triaged and resolved, with a major incident command structure "
       "mobilised for anything materially affecting operations, drawing on the same discipline the June "
       "2023 outage exposed as underdeveloped.",
  trig="A monitoring alert or user report indicates an IT service disruption.",
  out="A resolved incident with service restored, and for a major incident, a command structure that "
      "coordinated the response and a documented post-incident review.",
  note="This process is the same discipline referenced across the operational domains, AC-CX-DC-06 and "
      "AC-FO-OC-06, applied at the enterprise IT level; the difference is scale and the specific systems "
      "involved rather than the underlying incident management principle.",
  phases=["Detection and triage", "Major incident mobilisation", "Resolution and review"],
  steps=[
    S("1.1","Detect and log the incident","IT Service Desk Analyst","ITSM Platform",
      "Monitoring alert or user report","Logged incident with initial severity",
      "Logged within 5 minutes of detection at 100 percent","N","N",
      "Initial severity classification under uncertainty tends toward caution, which can over-trigger major incident process"),
    S("1.2","Triage and assign the incident","IT Service Desk Analyst","ITSM Platform",
      "Logged incident","Triaged incident with assigned owner",
      "Triaged within 15 minutes of logging at 95 percent","N","N",
      "An incident affecting a shared platform can be misassigned to a single team when it is actually cross-functional"),
    S("2.1","Mobilise major incident command for severity 1","Incident Commander","ITSM Platform",
      "Severity 1 classification","Mobilised incident command",
      "Mobilised within 10 minutes of severity 1 classification at 100 percent","Y","N",
      "Effective incident command depends on rehearsed procedure, not just a role being assigned in the moment"),
    S("3.1","Resolve the incident","IT Service Desk Analyst","ITSM Platform",
      "Diagnosed cause","Applied fix with confirmed resolution",
      "Resolved within the defined service level for the severity at 90 percent","N","N",
      "A fix that resolves the symptom without addressing root cause risks recurrence"),
    S("3.2","Conduct post-incident review for major incidents","Incident Commander","ITSM Platform",
      "Resolved severity 1 incident","Documented review with root cause and actions",
      "Conducted within 5 business days of resolution at 100 percent","N","N",
      "Follow-up actions from a review are not always tracked through to actual completion"),
  ],
  kpis=["Logged within 5 minutes of detection at 100 percent",
        "Mobilised within 10 minutes of severity 1 classification at 100 percent",
        "Resolved within the defined service level for the severity at 90 percent",
        "Conducted within 5 business days of resolution at 100 percent"],
  risks=["Effective incident command depending on rehearsed procedure, not just a role assigned in the moment",
         "A fix that resolves the symptom without addressing root cause risking recurrence",
         "An incident affecting a shared platform being misassigned to a single team when it is cross-functional",
         "Follow-up actions from a post-incident review not being tracked through to actual completion"])

P("AC-IT-SM-02",
  desc="An employee service request, from access provisioning to a hardware request, is submitted, "
       "fulfilled and closed through the standard service request channel.",
  trig="An employee submits a service request through the ITSM portal or the service desk.",
  out="A fulfilled service request closed within the standard service level, with the requesting employee "
      "confirmed satisfied.",
  note="Service request volume at a company of roughly 35,000 employees is high enough that fulfilment "
      "consistency, not any single request, is what actually determines whether the function is perceived as "
      "reliable.",
  phases=["Request submission and validation", "Fulfilment", "Closure confirmation"],
  steps=[
    S("1.1","Submit and validate the request","IT Service Desk Analyst","ITSM Platform",
      "Employee submitted request","Validated request with approval where required",
      "Validated within 4 business hours of submission at 95 percent","N","N",
      "Requests requiring manager approval add a dependency outside the service desk's direct control"),
    S("2.1","Fulfil the request","IT Service Desk Analyst","ITSM Platform",
      "Validated request","Fulfilled request",
      "Fulfilled within the standard service level for the request type at 90 percent","N","N",
      "Fulfilment time varies materially by request type, from a quick access change to a hardware procurement"),
    S("3.1","Confirm closure with the requester","IT Service Desk Analyst","ITSM Platform",
      "Fulfilled request","Confirmed closed request",
      "Confirmed within 1 business day of fulfilment at 90 percent","N","N",
      "A request closed without confirmation risks being marked complete when the employee's actual need was not met"),
    S("3.2","Capture satisfaction feedback","IT Service Desk Analyst","ITSM Platform",
      "Confirmed closure","Captured satisfaction rating",
      "Captured for 60 percent of closed requests","N","N",
      "Satisfaction feedback response rate is inherently voluntary and skews toward strongly positive or negative experiences"),
  ],
  kpis=["Validated within 4 business hours of submission at 95 percent",
        "Fulfilled within the standard service level for the request type at 90 percent",
        "Confirmed within 1 business day of fulfilment at 90 percent",
        "Employee satisfaction score on closed requests meeting target"],
  risks=["A request closed without confirmation risking being marked complete when the actual need was not met",
         "Requests requiring manager approval adding a dependency outside the service desk's direct control",
         "Fulfilment consistency across a very high request volume mattering more than any single request",
         "Fulfilment time varying materially by request type without a clearly communicated expectation"])

P("AC-IT-SM-03",
  desc="A production system change is planned, approved and released through the change management "
       "process, balancing delivery speed against the risk of introducing a new incident.",
  trig="A system change is ready for production release.",
  out="A released change with appropriate risk assessment and approval, either successfully deployed or "
      "rolled back cleanly if it fails.",
  note="Change management exists specifically to prevent a well-intentioned deployment from becoming the "
      "next incident, which means the discipline has genuine value only when it is proportionate to actual "
      "risk rather than a uniform bureaucratic gate on every change regardless of size.",
  phases=["Change risk assessment", "Approval", "Release and verification"],
  steps=[
    S("1.1","Assess change risk and impact","Change Manager","ITSM Platform",
      "Proposed change","Risk and impact assessment",
      "Assessed for 100 percent of proposed changes before approval at 100 percent","N","N",
      "Risk assessment applied uniformly regardless of actual change size becomes a bureaucratic gate rather than a genuine control"),
    S("2.1","Obtain change approval","Change Manager","ITSM Platform",
      "Risk assessment","Approved change",
      "Approved before the planned release window at 100 percent","Y","N",
      "Approval cadence that does not match the pace of a fast-moving development team creates pressure to bypass the process"),
    S("3.1","Release the change to production","Digital Platform Engineer","ITSM Platform",
      "Approved change","Released change",
      "Released within the approved window at 95 percent","N","N",
      "A release without a rehearsed rollback plan turns a failed deployment into an extended incident"),
    S("3.2","Verify the change and confirm no incident","Digital Platform Engineer","Dynatrace",
      "Released change","Verified stable production system",
      "Verified within 1 hour of release at 100 percent","N","N",
      "A change-caused incident that surfaces after the verification window closes is harder to attribute back to the change"),
  ],
  kpis=["Assessed for 100 percent of proposed changes before approval at 100 percent",
        "Approved before the planned release window at 100 percent",
        "Released within the approved window at 95 percent",
        "Change-caused incident rate below target"],
  risks=["A release without a rehearsed rollback plan turning a failed deployment into an extended incident",
         "Risk assessment applied uniformly regardless of change size becoming a bureaucratic gate rather than a real control",
         "Approval cadence not matching a fast-moving development team's pace, creating pressure to bypass the process",
         "A change-caused incident surfacing after the verification window closes, complicating attribution"])

P("AC-IT-SM-04",
  desc="The configuration management database is maintained as the authoritative record of IT assets and "
       "their relationships, kept current as systems are deployed, changed and retired.",
  trig="A system or asset is deployed, materially changed or retired, requiring a CMDB update.",
  out="An accurate, current CMDB reflecting the actual state of IT assets and their interdependencies.",
  note="A CMDB that has drifted from reality is worse than no CMDB at all, since incident responders and "
      "change planners make decisions trusting it, and a wrong assumption sourced from a stale record can "
      "actively mislead a response under pressure.",
  phases=["Asset lifecycle tracking", "Relationship mapping", "Currency assurance"],
  steps=[
    S("1.1","Update CMDB on asset deployment or change","IT Asset Coordinator","ITSM Platform",
      "Deployed or changed asset","Updated CMDB entry",
      "Updated within 5 business days of the change at 90 percent","N","N",
      "Updates depend on teams remembering to report a change, which is not always the first priority during a deployment"),
    S("2.1","Map asset relationships and dependencies","IT Asset Coordinator","ITSM Platform",
      "Updated asset entry","Mapped relationship and dependency data",
      "Mapped for 100 percent of material assets at 90 percent","N","N",
      "Dependency mapping for a complex integration is genuinely difficult to capture completely and accurately"),
    S("2.2","Retire asset records on decommission","IT Asset Coordinator","ITSM Platform",
      "Decommissioned asset","Retired CMDB entry",
      "Retired within 5 business days of decommission at 90 percent","N","N",
      "A retired system left active in the CMDB misleads future incident and change decisions"),
    S("3.1","Audit CMDB accuracy against actual state","IT Asset Coordinator","ITSM Platform",
      "CMDB records and actual infrastructure state","Audit findings with corrections",
      "Audited on a recurring cycle for 100 percent of critical systems at 100 percent","N","N",
      "A CMDB drifted from reality is worse than no CMDB, since responders make decisions trusting a wrong record"),
  ],
  kpis=["Updated within 5 business days of the change at 90 percent",
        "Mapped for 100 percent of material assets at 90 percent",
        "Retired within 5 business days of decommission at 90 percent",
        "Audited on a recurring cycle for 100 percent of critical systems at 100 percent"],
  risks=["A CMDB drifted from reality being worse than no CMDB, since responders trust a wrong record under pressure",
         "Updates depending on teams remembering to report a change, not always a priority during a deployment",
         "A retired system left active in the CMDB misleading future incident and change decisions",
         "Dependency mapping for a complex integration being genuinely difficult to capture completely"])

P("AC-IT-SM-05",
  desc="Vendor and managed service provider performance is governed against contracted service levels, "
       "covering the specific unconfirmed but assumed application management and infrastructure vendor "
       "relationships this wiki exists to help win.",
  trig="The recurring vendor governance review cycle runs, or a service level breach is identified.",
  out="Vendor performance assessed against contracted service levels, with underperformance addressed "
      "through the contract's defined governance mechanism.",
  note="This is the exact process an application management and user support engagement would be measured "
      "against, which makes it the most self-referential process in the wiki: the discipline described here "
      "is the discipline this sales artifact is arguing Air Canada should trust a new vendor to deliver.",
  phases=["Performance data compilation", "Service level assessment", "Governance action"],
  steps=[
    S("1.1","Compile vendor performance data","Vendor Governance Manager","ITSM Platform",
      "Service delivery data against contract terms","Compiled performance data",
      "Compiled within 5 business days of period close at 100 percent","N","N",
      "Performance data quality depends partly on the vendor's own reporting, which is not independently verified in every instance"),
    S("2.1","Assess against contracted service levels","Vendor Governance Manager","ITSM Platform",
      "Compiled data and contract terms","Service level assessment",
      "Assessed for 100 percent of governed vendors each cycle at 100 percent","N","N",
      "Service levels negotiated years earlier may no longer reflect the operational priorities that matter most today"),
    S("2.2","Identify underperformance requiring escalation","Vendor Governance Manager","SAP Analytics Cloud",
      "Assessment results","Identified underperformance pattern",
      "Identified within 10 business days of assessment at 100 percent","N","N",
      "A single service level breach is different from a persistent pattern and needs a different response"),
    S("3.1","Escalate per the governance framework","Vendor Governance Manager","SAP Ariba",
      "Identified pattern","Escalated case with contractual remedy",
      "Escalated within the contract's defined timeframe at 100 percent","N","Y",
      "Vendor performance is entirely dependent on governance mechanisms working as designed, since direct operational authority does not exist"),
  ],
  kpis=["Compiled within 5 business days of period close at 100 percent",
        "Assessed for 100 percent of governed vendors each cycle at 100 percent",
        "Identified within 10 business days of assessment at 100 percent",
        "Escalated within the contract's defined timeframe at 100 percent"],
  risks=["Performance data quality depending partly on the vendor's own reporting, not independently verified in every instance",
         "Service levels negotiated years earlier no longer reflecting today's actual operational priorities",
         "Vendor performance being entirely dependent on governance mechanisms working as designed",
         "A single breach being treated the same as a persistent underperformance pattern"])

# ── CS: Cybersecurity and Identity ──────────────────────────────────────────
P("AC-IT-CS-01",
  desc="An employee's access is provisioned, modified and deprovisioned through the identity and access "
       "lifecycle, matching system access to the employee's current role and employment status.",
  trig="An employee joins, changes role, or leaves Air Canada, triggering an access lifecycle event.",
  out="Access correctly provisioned for a new or changed role, and promptly revoked on departure, with no "
      "orphaned access remaining.",
  note="Deprovisioning speed at departure is the highest-consequence part of this process: access that "
      "should have been revoked at termination but was not is a live security exposure for exactly as long "
      "as it takes to notice.",
  phases=["Access request and approval", "Provisioning", "Deprovisioning on departure"],
  steps=[
    S("1.1","Request access against role requirement","IT Access Coordinator","Workforce Identity",
      "New hire, role change or system need","Registered access request",
      "Registered within 1 business day of the triggering event at 100 percent","N","N",
      "Access requirements are not always fully specified for a genuinely new role"),
    S("2.1","Approve access against least privilege","IT Access Coordinator","Workforce Identity",
      "Registered request","Approved or declined access",
      "Approved within the defined service level at 90 percent","Y","N",
      "Approval under time pressure to unblock a new employee can favour broader access than the role strictly requires"),
    S("2.2","Provision approved access","IT Access Coordinator","Workforce Identity",
      "Approved access request","Provisioned access",
      "Provisioned within 1 business day of approval at 95 percent","N","N",
      "A provisioning delay for a new employee's first day generates avoidable friction and support volume"),
    S("3.1","Deprovision access on departure","IT Access Coordinator","Workforce Identity",
      "Departure notification","Revoked access across all systems",
      "Revoked within 4 hours of the departure effective time at 100 percent","N","N",
      "Access not revoked at termination is a live security exposure for exactly as long as it takes to notice"),
  ],
  kpis=["Registered within 1 business day of the triggering event at 100 percent",
        "Provisioned within 1 business day of approval at 95 percent",
        "Revoked within 4 hours of the departure effective time at 100 percent",
        "Zero orphaned access accounts found in a periodic access review"],
  risks=["Access not revoked at termination being a live security exposure for as long as it takes to notice",
         "Approval under time pressure favouring broader access than the role strictly requires",
         "Access requirements not being fully specified for a genuinely new role",
         "A provisioning delay on a new employee's first day generating avoidable friction and support volume"])

P("AC-IT-CS-02",
  desc="Privileged access to sensitive systems is granted, time-bounded and monitored, requiring a higher "
       "standard of control than standard employee access given the elevated risk of misuse.",
  trig="An administrator or engineer requires privileged access to perform a specific task.",
  out="Privileged access granted for the minimum necessary duration, monitored during use, and "
      "automatically expired.",
  note="Privileged access is the highest-value target for both external attackers and insider risk, which "
      "is why the standard here, time-bounded and monitored rather than standing, is deliberately stricter "
      "than the standard employee access lifecycle.",
  phases=["Privileged access request", "Time-bounded grant", "Monitoring and expiry"],
  steps=[
    S("1.1","Request privileged access for a specific task","Security Operations Analyst","CyberArk",
      "Specific administrative task requiring elevated access","Registered privileged access request",
      "Registered with a documented business justification for 100 percent of requests","N","N",
      "A justification too vague to evaluate can still be approved under operational time pressure"),
    S("2.1","Grant time-bounded privileged access","Security Operations Analyst","CyberArk",
      "Justified request","Granted access with defined expiry",
      "100 percent of privileged grants carry an explicit expiry, none standing indefinitely","Y","N",
      "Standing privileged access, rather than time-bounded, is the single highest-risk configuration in the identity estate"),
    S("2.2","Monitor privileged session activity","Security Operations Analyst","CyberArk",
      "Active privileged session","Monitored session activity",
      "100 percent of privileged sessions logged and monitored","N","N",
      "Monitoring without active review is a record after the fact, not a real-time control"),
    S("3.1","Expire access and confirm revocation","Security Operations Analyst","CyberArk",
      "Expiry reached","Confirmed revoked access",
      "Zero privileged grants remaining active past their expiry at 100 percent","N","N",
      "An expiry that is not system-enforced depends entirely on manual follow-through to actually take effect"),
  ],
  kpis=["100 percent of privileged grants carry an explicit expiry, none standing indefinitely",
        "100 percent of privileged sessions logged and monitored",
        "Zero privileged grants remaining active past their expiry at 100 percent",
        "Privileged access requests with a documented business justification at 100 percent"],
  risks=["Standing privileged access, rather than time-bounded, being the single highest-risk identity configuration",
         "A justification too vague to genuinely evaluate still being approved under operational time pressure",
         "Monitoring without active review being a record after the fact rather than a real-time control",
         "An expiry not system-enforced depending entirely on manual follow-through to actually take effect"])

P("AC-IT-CS-03",
  desc="Security monitoring detects and triages a potential threat across the IT estate, distinguishing a "
       "genuine security event from noise before it reaches full incident response.",
  trig="A security monitoring alert is generated from any monitored system or network segment.",
  out="A triaged security alert either dismissed as a false positive with documented reasoning, or "
      "escalated into the security incident response process.",
  note="Alert volume at enterprise scale is high enough that triage quality, not detection coverage alone, "
      "determines whether a genuine threat gets timely attention or is lost in noise the monitoring system "
      "generates by design.",
  phases=["Alert generation and initial triage", "Threat assessment", "Escalation or dismissal"],
  steps=[
    S("1.1","Generate and receive security alert","Security Operations Analyst","Crowdstrike Falcon",
      "Monitored system or network activity","Generated alert",
      "Received by the security operations function within 1 minute of generation at 100 percent","N","N",
      "Alert volume at enterprise scale is high enough that individual review depth is inherently constrained"),
    S("2.1","Perform initial triage against known patterns","Security Operations Analyst","Splunk",
      "Generated alert","Initial triage classification",
      "Triaged within 15 minutes of receipt at 90 percent","N","N",
      "Triage quality, not detection coverage alone, determines whether a genuine threat gets timely attention"),
    S("2.2","Assess genuine threat indicators","Security Operations Analyst","Splunk",
      "Triaged alert requiring deeper review","Threat assessment",
      "Assessed within 1 hour of triage for elevated-priority alerts at 90 percent","Y","N",
      "A genuine threat assessed too slowly gives an attacker additional time inside the environment"),
    S("3.1","Escalate to incident response or dismiss with documentation","Security Operations Analyst","ITSM Platform",
      "Threat assessment","Escalated incident or documented dismissal",
      "100 percent of assessed alerts closed with a documented outcome","N","Y",
      "An undocumented dismissal cannot be reviewed later if the same pattern recurs and turns out to be genuine"),
  ],
  kpis=["Received by the security operations function within 1 minute of generation at 100 percent",
        "Triaged within 15 minutes of receipt at 90 percent",
        "Assessed within 1 hour of triage for elevated-priority alerts at 90 percent",
        "100 percent of assessed alerts closed with a documented outcome"],
  risks=["Triage quality, not detection coverage alone, determining whether a genuine threat gets timely attention",
         "A genuine threat assessed too slowly giving an attacker additional time inside the environment",
         "Alert volume at enterprise scale inherently constraining the depth of individual review",
         "An undocumented dismissal being unreviewable later if the same pattern recurs and proves genuine"])

P("AC-IT-CS-04",
  desc="Known vulnerabilities across the IT estate are identified, prioritised and remediated through "
       "patch management, closing the window between a vulnerability's disclosure and its exploitation "
       "risk.",
  trig="A vulnerability is disclosed affecting a system in Air Canada's IT estate.",
  out="The vulnerability assessed for applicability and risk, and patched within a timeframe proportionate "
      "to its severity.",
  note="The gap between vulnerability disclosure and patch deployment is a known, actively exploited window "
      "in the industry, which makes remediation speed proportionate to severity the actual control, not "
      "patching everything eventually.",
  phases=["Vulnerability identification and scoring", "Prioritisation", "Patch deployment"],
  steps=[
    S("1.1","Identify vulnerability applicability to the estate","Security Operations Analyst","Crowdstrike Falcon",
      "Disclosed vulnerability","Assessed applicability across affected systems",
      "Assessed within 24 hours of disclosure for critical vulnerabilities at 100 percent","N","N",
      "Applicability assessment depends on an accurate asset inventory, which connects back to CMDB currency in AC-IT-SM-04"),
    S("2.1","Score vulnerability severity and exploitability","Security Operations Analyst","Crowdstrike Falcon",
      "Applicable vulnerability","Scored severity",
      "Scored using a documented methodology for 100 percent of applicable vulnerabilities","Y","N",
      "A published severity score does not always reflect the actual exploitability risk to Air Canada's specific environment"),
    S("2.2","Prioritise remediation against risk","Security Operations Analyst","ITSM Platform",
      "Scored vulnerability","Prioritised remediation queue",
      "Prioritised for 100 percent of vulnerabilities each cycle at 100 percent","N","N",
      "Prioritisation has to balance patch urgency against the operational risk of an untested change to a production system"),
    S("3.1","Deploy patch within the target timeframe","Digital Platform Engineer","ITSM Platform",
      "Prioritised remediation","Deployed patch",
      "Deployed within the target timeframe for the severity at 90 percent","N","N",
      "The gap between disclosure and patch deployment is an actively exploited window in the industry"),
  ],
  kpis=["Assessed within 24 hours of disclosure for critical vulnerabilities at 100 percent",
        "Scored using a documented methodology for 100 percent of applicable vulnerabilities",
        "Deployed within the target timeframe for the severity at 90 percent",
        "Critical vulnerability mean time to remediate meeting industry benchmark"],
  risks=["The gap between vulnerability disclosure and patch deployment being an actively exploited window",
         "A published severity score not always reflecting actual exploitability risk to Air Canada's specific environment",
         "Applicability assessment depending on an accurate asset inventory tied to CMDB currency",
         "Patch urgency having to be balanced against the operational risk of an untested production change"])

P("AC-IT-CS-05",
  desc="A confirmed security incident is contained, investigated and remediated, with forensic evidence "
       "preserved for potential regulatory or legal follow-up.",
  trig="A security alert is escalated from triage in AC-IT-CS-03 into a confirmed security incident.",
  out="The incident contained, root cause identified, systems remediated, and evidence preserved for any "
      "required follow-up.",
  note="Speed and evidence preservation are frequently in tension during incident response, since the "
      "fastest path to containment can destroy forensic evidence a later investigation or regulatory "
      "inquiry would need.",
  phases=["Containment", "Investigation and forensics", "Remediation and closure"],
  steps=[
    S("1.1","Contain the confirmed incident","Security Operations Analyst","Crowdstrike Falcon",
      "Confirmed security incident","Contained incident",
      "Contained within the target response time for the severity at 90 percent","N","N",
      "Containment speed and evidence preservation are frequently in tension during active response"),
    S("2.1","Preserve forensic evidence","Security Operations Analyst","Splunk",
      "Active or contained incident","Preserved evidence",
      "Preserved before any remediation action that could alter evidence at 100 percent","Y","N",
      "The fastest path to containment can destroy forensic evidence a later investigation would need"),
    S("2.2","Investigate root cause and scope","Security Operations Analyst","Splunk",
      "Preserved evidence","Root cause and scope determination",
      "Investigated within the defined timeframe for the severity at 100 percent","N","N",
      "Scope determination has to account for lateral movement, not just the initially detected point of entry"),
    S("3.1","Remediate and confirm closure","Security Operations Analyst","ITSM Platform",
      "Investigated incident","Remediated systems with confirmed closure",
      "Closed within the defined timeframe with confirmed remediation at 90 percent","N","N",
      "Closure without confirming full remediation risks the same vulnerability being exploited again"),
  ],
  kpis=["Contained within the target response time for the severity at 90 percent",
        "Preserved before any remediation action that could alter evidence at 100 percent",
        "Investigated within the defined timeframe for the severity at 100 percent",
        "Closed within the defined timeframe with confirmed remediation at 90 percent"],
  risks=["Containment speed and evidence preservation being frequently in tension during active response",
         "The fastest path to containment potentially destroying forensic evidence a later investigation would need",
         "Scope determination needing to account for lateral movement beyond the initially detected point of entry",
         "Closure without confirming full remediation risking the same vulnerability being exploited again"])
