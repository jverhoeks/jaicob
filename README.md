# Jaicob

Replacing myself with ai.

There are a lot of communication channels, useful but also distracting.
I want to see how far i can come by automatic myself using ai agents/bots. 
For example somebody asks a PR review, 

## Data Channels


### Text Interaction

* Slack
* Whatsapp
* Teams Chat

Optional

* Signal

### Email

* Gmail
* Office365

### Video (audio)

This might be harder.

* Teams
* Slack
* Zoom
* Whatsapp

### News gathering

* hacker news
* rss
* slack channels


## How ?

This is a great project to start with LLM agents running on Python.
I'm a aws cloud architect, so some aws, cloudflare an what more.

Let's start with [Slack](./slack/)

First test works, i can write message as me. So now i need to get all the messages from all channels and 
then build some logic to decide when to ask

```python
    response = client.chat_postMessage(
            channel="xxxxxx",  # Replace with the channel ID
            text="Hello from the bot acting as me!",
            as_user=True  
        )
```

## Next steps

* Build public callback infra
* save messages into rag?
* cheap llm or regex to analyse the message and see when needs to act
* write some "agents" to do my tasks
* * Pr Review
* * general questions.
* * * Need rag/cag with documentation and code (how to keep that up2date)


## Design

```mermaid
graph TD
  %% Sources
  A[Source: Slack] --> B[Analyzer]
  A2[Source: WhatsApp] --> B
  A3[Source: Teams] --> B
  A4[Source: Outlook] --> B

  B["Receiver"] --> C[Storage: All Messages]
  C --> D[Analysis with Cheap LLM]
  D --> E{Action Required?}

  %% Action Required decision
  E -- Yes --> F[Agent Router]
  E
  C

  %% Agent Router sends to specialized agents
  F --> PR[PR Reviewer: GitHub PR Check]
  F --> Doc[Documentation Lookup]
  F --> Social[Social Media Response]
  F --> Email[Check Incoming Emails]

  %% Email handling process
  Email --> D2[Cheap LLM Email Processing]
  D2 --> E2{Action Required?}
  E2 -- Yes --> Agt[Select Agent]
  E2
  Archive[Archive Email]

  %% Select agent and perform actions
  Agt -->|Response| Resp[Send Response]
  Agt -->|Delete| Delete[Delete Email]
  Agt -->|Alert| SlackAlert[Alert via Slack if Important]
  Agt --> Archive[Archive Email]

  %% PR Review Process
  PR --> n2["Get PR data"]
  n2 --> n3["LLM: Analyze code and text"]
  n3 --> n4["Approve PR with comment"]
  n3 --> n5["Reject PR with comment"]
  n3 --> n6@{ shape: "stadium", label: "Ignore" }
  n4 --> n7["Respond in Slack"]
  n5 --> n7
  n6
  n7

  %% Documentation Lookup Process
  Doc --> n8["LLM: Analyze question"]
  n8 --> n9["Respond in Slack"]
  n8 --> n10@{ shape: "stadium", label: "Ignore" }

  %% Optional alert back to Slack when important
  SlackAlert
  A[Source: Slack]

  %% Daily Report generation
  ResumeAgent[Resume Agent] --> Report[Generate Daily Report of Interactions]

  %% Optional interactions flow
  Resp
  C
  Archive
  C
  Delete
  C
  SlackAlert
  C

  %% Event Logging
  C --> ResumeAgent["Overview Agent"]
  %% Storage connections
  style D2 fill:#FF3131, color:#000000
  style D fill:#FF3131
  style ResumeAgent fill:#FF5757
  style C fill:#7ED957
	E ---|"No"| n11@{ shape: "stadium", label: "Ignore" }
	E2 ---|"No"| n12@{ shape: "stadium", label: "Ignore" }
	style n6 fill:#FFBD59
	style n12 fill:#FFDE59
	style n10 fill:#FFDE59
	style n11 fill:#FFDE59
	n5 --- n13
```
