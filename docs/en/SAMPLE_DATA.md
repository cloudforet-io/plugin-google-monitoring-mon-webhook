# Alert Fromat Version 1.2

~~~
{
    "incident": {
      "condition": {
        "conditionThreshold": {
          "aggregations": [
            {
              "alignmentPeriod": "300s",
              "perSeriesAligner": "ALIGN_MEAN"
            },
            {
              "alignmentPeriod": "60s",
              "crossSeriesReducer": "REDUCE_MEAN",
              "perSeriesAligner": "ALIGN_MEAN"
            }
          ],
          "comparison": "COMPARISON_GT",
          "duration": "0s",
          "filter": "resource.type = \"gce_instance\" AND metric.type = \"compute.googleapis.com/instance/cpu/utilization\" AND metric.labels.instance_name = \"choonho-test\"",
          "thresholdValue": 0.5,
          "trigger": {
            "count": 1
          }
        },
        "displayName": "VM Instance - CPU utilization",
        "name": "projects/<My Project ID>/alertPolicies/10988491472291860640/conditions/10988491472291860713"
      },
      "condition_name": "VM Instance - CPU utilization",
      "documentation": {
        "content": "Server High CPU Usage",
        "mime_type": "text/markdown"
      },
      "ended_at": null,
      "incident_id": "0.mtdi83m6w8ao",
      "metadata": {
        "system_labels": {},
        "user_labels": {}
      },
      "metric": {
        "displayName": "CPU utilization",
        "labels": {},
        "type": "compute.googleapis.com/instance/cpu/utilization"
      },
      "observed_value": "0.790",
      "policy_name": "choonho-server-cpu-alert-policy-test",
      "resource": {
        "labels": {
          "project_id": "xxxxxxxxxxxxxxxxxxxxxxxx"
        },
        "type": "gce_instance"
      },
      "resource_id": "",
      "resource_name": "xxxxxxxxxxxxxxxxxxxxxxxx VM Instance labels {project_id=xxxxxxxxxxxxxxxxxxxxxxxx}",
      "resource_type_display_name": "VM Instance",
      "scoping_project_id": "xxxxxxxxxxxxxxxxxxxxxxxx",
      "scoping_project_number": 286919713412,
      "started_at": 1675315787,
      "state": "open",
      "summary": "CPU utilization for xxxxxxxxxxxxxxxxxxxxxxxx VM Instance labels {project_id=xxxxxxxxxxxxxxxxxxxxxxxx} is above the threshold of 0.500 with a value of 0.790.",
      "threshold_value": "0.5",
      "url": "https://console.cloud.google.com/monitoring/alerting/incidents/0.mtdi83m6w8ao?project=xxxxxxxxxxxxxxxxxxxxxxxx"
    },
    "version": "1.2"
  }
~~~

