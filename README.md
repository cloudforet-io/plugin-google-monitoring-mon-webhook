# plugin-google-monitoring-mon-webhook
webhook for Google Monitoring (Operation Suites)

# Data Model

## Google Monitoring Raw Data

Webhook notification: 

~~~

 {
    "version": "test",
    "incident": {
      "incident_id": "12345",
      "scoping_project_id": "12345",
      "scoping_project_number": 12345,
      "url": "http://www.example.com",
      "started_at": 0,
      "ended_at": 0,
      "state": "OPEN",
      "summary": "Test Incident",
      "apigee_url": "http://www.example.com",
      "observed_value": "1.0",
      "resource": {
        "type": "example_resource",
        "labels": {
          "example": "label"
        }
      },
      "resource_type_display_name": "Example Resource Type",
      "resource_id": "12345",
      "resource_display_name": "Example Resource",
      "resource_name": "projects/12345/example_resources/12345",
      "metric": {
        "type": "test.googleapis.com/metric",
        "displayName": "Test Metric",
        "labels": {
          "example": "label"
        }
      },
      "metadata": {
        "system_labels": {
          "example": "label"
        },
        "user_labels": {
          "example": "label"
        }
      },
      "policy_name": "projects/12345/alertPolicies/12345",
      "policy_user_labels": {
        "example": "label"
      },
      "documentation": "Test documentation",
      "condition": {
        "name": "projects/12345/alertPolicies/12345/conditions/12345",
        "displayName": "Example condition",
        "conditionThreshold": {
          "filter": "metric.type=\"test.googleapis.com/metric\" resource.type=\"example_resource\"",
          "comparison": "COMPARISON_GT",
          "thresholdValue": 0.5,
          "duration": "0s",
          "trigger": {
            "count": 1
          }
        }
      },
      "condition_name": "Example condition",
      "threshold_value": "0.5"
    }
  }

~~~

| Field 	| Example |
| ---   	| ---     |
| title		| Dastabase Size alert |
| message       | Database xxxxxx      |
| state  	| Alerting , ok , no_data |
| orgID		| 1			|
| ruleID	| 92			|
| dashboardID	|			|
| ruleName	| Database Size alert	|
| panelID	| 5			|
| ruleUrl	| https://grafana.stargate.cloudeco.io/d/9tvNgo77k/mongodb-database-details_copy-20210818?tab=alert&viewPanel=5&orgId=1 |
| ImageUrl	| https://grafana.stargate.cloudeco.io/d/9tvNgo77k/mongodb-database-details_copy-20210818?tab=alert&viewPanel=5&orgId=1 |
| tags		| { "a": "b" } 		|
| evalMatches	| "evalMatches": [{"value": 342.2222, "metric": "Count", "tags": null}] |

## Event key criteria
Hash key of ```raw_data.incident.incident_id```.

## Severity matching information
|Google Monitoring  ```state```| SpaceONE Event  ```severity```|
|---|---|
|Open|ALERT|
|Closed|RECOVERY|
|Acknowledged|NONE|


## SpaceONE Event Model
| Field		| Type | Description	| Example	|
| ---      | ---     | ---           | ---           |
| event_id | str  | auto generation | event-1234556  |
| event_key | str | raw_data.incident.incident_id | 1234 |
| event_type |  str  | RECOVERY , ALERT based on raw_data.incident.state | RECOVERY	|
| title | str	| raw_data.incident.summary	| Test Incident	|
| description | str | raw_data.incident.summary	| Test Incident		|
| severity | str  | alert level based raw_data.incident.state (Open  -> ALERT, Closed -> RECOVERY, Acknowledged -> NONE | ALERT	|
| resource | dict | Not used		| N/A	|
| raw_data | dict | Google Monitoring Raw Data | {"title": "Database Size Alert", "dashboardId": 1, ... } |
| addtional_info | dict | raw_data.dashboardID, raw_data.orgID, raw_data.imageUrl, raw_data.ruleUrl, raw_data.evalMatches, raw_data.tags 	| {"org_id": "1.0", "rule_url" "https://...." } |
| occured_at | datetime | webhook received time | "2021-08-23T06:47:32.753Z" |
| alert_id | str | mapped alert_id	| alert-3243434343 |
| webhook_id | str  | webhook_id	| webhook-34324234234234 |
| project_id | str	| project_id	| project-12312323232    |
| domain_id | str	| domain_id	| domain-12121212121	|
| created_at | datetime | created time | "2021-08-23T06:47:32.753Z"	|

## cURL Requests examples
This topic provides examples of calls to the SpaceONE Grafana monitoring webhook using cURL.

Here's a cURL command that works for getting the response from webhook, you can test the following on your local machine.
```
curl -X POST https://your_spaceone_monitoring_webhook_url -d '{
  "dashboardId": xx,
  "evalMatches": [
    {
      "value": xxx,
      "metric": "xxx",
      "tags": {}
    }
  ],
  "ruleUrl": "xxx",
  "imageUrl": "xxx",
  "message": "xxx",
  "orgId": xx,
  "panelId": xx,
  "ruleId": xx,
  "ruleName": "xxx",
  "ruleUrl": "xxx",
  "state": "xxx",
  "tags": {
    "xxx": "xxx"
  },
  "title": "xxx"
}
```

Followings are examples which works for testing your own webhook.

```
curl -X POST https://{your_spaceone_monitoring_grafana_webhook_url} -d '{
  "dashboardId": 1,
  "evalMatches": [
    {
      "value": 1,
      "metric": "Count",
      "tags": {}
    }
  ],
  "ruleUrl": "https://grafana.stargate.cloudeco.io/d/6eRS6XR7k/spaceone-dev-cluster-alerts-dashboard-20210621-backup?tab=alert&viewPanel=14&orgId=1",
  "imageUrl": "https://grafana.com/assets/img/blog/mixed_styles.png",
  "message": "Notification Message",
  "orgId": 1,
  "panelId": 2,
  "ruleId": 1,
  "ruleName": "Panel Title alert",
  "ruleUrl": "http://localhost:3000/d/hZ7BuVbWz/test-dashboard?fullscreen\u0026edit\u0026tab=alert\u0026panelId=2\u0026orgId=1",
  "state": "alerting",
  "tags": {
    "tag name": "tag value"
  },
  "title": "[Alerting] Panel Title alert"
}'
```

```
curl -X POST https://monitoring-webhook.dev.spaceone.dev/monitoring/v1/webhook/webhook-1eea0a98d2aa/ed270cc6ea8bb6037313ddbc1e6ee0b3/events -d '{
  "tags": {},
  "orgId": 0.0,
  "state": "alerting",
  "message": "Someone is testing the alert notification within Grafana.",
  "ruleUrl": "https://grafana.stargate.cloudeco.io/",
  "dashboardId": 1.0,
  "title": "[Alerting] Test notification",
  "panelId": 1.0,
  "ruleId": 3.2760766009712717e+18,
  "ruleName": "Test notification",
  "evalMatches": [
      {
          "metric": "High value",
          "tags": null,
          "value": 100.0
      },
      {
          "metric": "Higher Value",
          "value": 200.0,
          "tags": null
      }
  ]
}'
```
