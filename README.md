# Camunda External Taks Client Python

## Installing

## Usage
1. Make sure you have [Camunda](https://camunda.com/download/) running.
2. Create a simple bpmn process model with an [External Service Task](https://docs.camunda.org/manual/latest/user-guide/ext-client/) and define the topic as 'topicName'.
3. Deploy the process to the Camunda BPM engine.
4. In your Python code:


```python
import cam

# create a Client instance
camundaTask = cam.client(url = "http://localhost:8080/engine-rest" ) 
"""
arguments for the client:
- 'url': url to the Workflow Engine
- 'workerId': unique Name for the external Task client, optional argument. If not set it provides a default value
"""

# susbscribe to the topic: 'topicName'
camundaTask.subscribe(topic = "topicName") 
"""
Arguments for subscribe: 
- 'topic': The client queries the topic and locks the task, if a task with the topic is available, if not it keeps polling 
- 'lockDuration': defines the time a task is locked by a worker. If not set, it is set to a default value of 1000
- 'longPolling': defines the time a request is suspended by the server if no external tasks are available. If not set, it is set to a default value of 5000
"""

#add your business logic here. 

#The complete, fail and error call can take variables as argument to provide those variables back to Camunda. Store the variables in a dictonary:
variables =	{
  "aVariable": "IAmAString",
  "anotherVariable": True,
  "aNumericVariable": 1964
}

#If the business logic was successful
camundaTask.complete(**variables)

#If the business logic failed ther
camundaTask.error(bpmn_error = "xxx")
"""
Arguments for error: 
- 'bpmn_error':
- 'error_message':
- '**kwargs': variables 
"""

#fail
camundaTask.fail()
"""
Arguments for fail:
- 'error_message':
- 'retries':
- 'retry_timeout': 

```

## Features 
This python module features the following: 
-Extend the lock duration of External Tasks
-Report BPMN errors and failures
-Share variables with the Workflow Engine

###Fetch and Lock 

###Complete

###Handle Failure

###Handle BPMN Error

###Extend duration













