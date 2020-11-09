# Camunda External Taks Client Python
Implement your [BPMN Service Task](https://docs.camunda.org/manual/latest/user-guide/process-engine/external-tasks/) in Python by using the cam.py module. 
The module cam.py is written in Python3. To use the module Python 3.7 is requiered. 
This python module was used for the [tutorial](https://www.youtube.com/watch?v=XNZDEw33udU) about external task clients at Camundacon 2019. 

*Note: This module is a sample and not supported in any way.* 


## Installing
1. Download the cam.py module from this repo
2. Put the cam.py module in the same directory, where you want to create your python worker 
3. Create a new python file for the python worker
3. Import the cam.py module in your python worker python file by using the import statement 

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
- 'workerId': optional argument: unique Name for the external Task client. If not set it provides a default value
"""

# susbscribe to the topic: 'topicName'
camundaTask.subscribe(topic = "topicName")
#Put your business logic for the task here
#complete the task
camundaTask.complete()
```

## Features 
This python module features the following: 
-Extend the lock duration of External Tasks
-Report BPMN errors and failures
-Share variables with the Workflow Engine

###[Fetch and Lock](https://docs.camunda.org/manual/latest/reference/rest/external-task/fetch/)
- Polling tasks from the engine works by performing fetch & lock operation of tasks that have a subscription. 
- If the funcion subscribe from the external task client is used, it will try to fetch and lock task for the registered topic. 
If no task is available the external task client is polling periodically.
```python
"""
# susbscribe to the topic: 'topicName'
camundaTask.subscribe(topic = "topicName")
Optional arguments:
- 'lockDuration': defines the time the task is locked for the client. Default value: 1000
- 'longPolling' : defines the time a request is suspended if no task is available. Default value: 5000
"""
```

###[Complete](https://docs.camunda.org/manual/latest/reference/rest/external-task/post-complete/)

```python
# susbscribe to the topic: 'topicName'
camundaTask.subscribe(topic = "topicName")
#Put your business logic for the task here
#Create some variables
variables =	{
  "aVariable": "IAmAString",
  "anotherVariable": True,
  "aNumericVariable": 1964
}
#complete the task with variables
camundaTask.complete(**variables)

```

###[Handle Failure](https://docs.camunda.org/manual/latest/reference/rest/external-task/post-failure/)


```python
#Subscribe to the topic 'topicName'
camundaTask.subscribe(topic = "topicName") 
#Put your business logic for the task here
#Handle a Failure
camundaTask.fail(error_message = "some failure message", retries = 0, retryTimeout = 2000)
"""
Optional arguments:
- 'retries': A number of how often the task should be retried. If the number is 0 an incident is created. Default value: 0
- 'retry_timeout' : A timeout in milliseconds before the external task becomes available again for fetching. Default value: 0
"""
```

###[Handle BPMN Error](https://docs.camunda.org/manual/latest/reference/rest/external-task/post-bpmn-error/)

```python
#Subscribe to the topic 'topicName'
camundaTask.subscribe(topic = "topicName")
#Put your business logic for the task here
#Create some Variables
variables =	{
  "aVariable": "IAmAString",
  "anotherVariable": True,
  "aNumericVariable": 1964
}
#Handle a BPMN Failure (throw a BPMN error)
camundaTask.error(bpmn_error = "errorCode", "error message", variables)
"""
the bpmn_error code reffers to the error code, that is defined in the BPMN diagram 
Optional arguments:
- 'error_message': An error message that describes the error.
- 'variables' : must be stored in the Python code as dictonary and will be passed to Camunda
"""
```

###[Extend duration](https://docs.camunda.org/manual/latest/reference/rest/external-task/post-extend-lock/)
```python
#Subscribe to the topic 'topicName'
camundaTask.subscribe(topic = "topicName")
#Put your business logic for the task here
#Extend the lock time
camundaTask.new_lockduration(new_duration ="6000")
```
