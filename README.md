# Camunda External Taks Client Python

## Features 
This python module features the following: 
-Extend the lock duration of External Tasks
-Unlock External Tasks
-Report BPMN errors and failures
-Share variables with the Workflow Engine



## Installing





## Usage
1. Make sure you have [Camunda](https://camunda.com/download/) running.
2. Create a simple bpmn process model with an [External Service Task](https://docs.camunda.org/manual/latest/user-guide/ext-client/) and define the topic as 'topicName'.
3. Deploy the process to the Camunda BPM engine.
4. In your Python code:


´´´

import cam

camundaTask = cam.client(url = "http://localhost:8080/engine-rest" ) #to connect your external Task client with Camunda, define the REST endpoint of the Camunda Engine, addionally you can provide the lockduration and longPolling as arguments. If not provided those will be set to a default value

camundaTask.subscribe(topic = "topicName") # addionally you can provide the workerId as argument. If not provided those will be set to a default value

#add your business logic here

#The complete, fail and error call can take variables as argument to provide those variables back to Camunda. Store the variables in a dictonary

variables =	{
  "aVariable": "IAmAString",
  "anotherVariable": True,
  "aNumericVariable": 1964
}

camundaTask.complete(**variables)

´´´














