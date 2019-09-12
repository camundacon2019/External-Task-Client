import requests
import json
import time
import uuid


class client:
    def __init__(self, url, workerid = "defaultid"):  
        self.url = url
        self.workerid = workerid
        
    
    def subscribe(self, topic, lockDuration = 1000, longPolling = 5000):
        # Define the endpoint for fetch and lock
        endpoint = str(self.url) +"/external-task/fetchAndLock"
        # Define unique ID for the worker
    
        #global uid
        #uid = uuid.uuid1()
        #uid = str(uid)

        workerid = str(self.workerid)
    
        #Define the Json for the Request
        task= {"workerId": workerid,
               "maxTasks":1,
               "usePriority":"true",
               "asyncResponseTimeout": longPolling,
               "topics":
               [{"topicName": topic,
                 "lockDuration": lockDuration
                }]
              }
 
    
        #Make the request
        global engine
        engine = True
    
        try:
            fetch_and_lock = requests.post(endpoint, json=task)
            print(fetch_and_lock.status_code)
            global body
            body = fetch_and_lock.text
               
        except:
            engine = False
            print("Engine is down")
        
        if(engine == True):
            while body == '[]':
                print("polling")
                fetch_and_lock = requests.post(endpoint, json=task)
                body = fetch_and_lock.text
                time.sleep(5)
            
                if body != '[]':
                    break
                
                
    #Complete Call
    def complete(self, **kwargs): 
        response_body = json.loads(body)
        taskid = response_body[0]['id']
        taskid = str(taskid)
        
        endpoint = str(self.url) + "/external-task/" + taskid + "/complete"
    
        #get workerid
        workerid = response_body[0]['workerId']
        workerid = str(workerid)
    
    
    
    
        #puts the variables from the dictonary into the nested format for the json response
        variables_for_response = {}
        for key, val in kwargs.items():
            variable_new = {key:{"value": val}}
            variables_for_response.update(variable_new)  

         
    
        response= {"workerId": workerid,
                  "variables": variables_for_response
                  }
    
       
        try:
            complete = requests.post(endpoint, json =response)
            body_complete = complete.text
            print(body_complete)
            print(complete.status_code)
        
        except:
            print('fail')
            
    
    #BPMN Error
    
    def error(self, bpmn_error, error_message = "not defined", **kwargs):
        
        response_body = json.loads(body)
        taskid = response_body[0]['id']
        taskid = str(taskid)
    
      
        endpoint = str(self.url) + "/external-task/"+ taskid + "/bpmnError"
    
    
        workerid = response_body[0]['workerId']
        workerid = str(workerid)
    
    
        variables_for_response = {}
        for key, val in kwargs.items():
            variable_new = {key:{"value": val}}
            variables_for_response.update(variable_new)  

    
        response =  {
          "workerId": workerid,
          "errorCode": bpmn_error,
          "errorMessage": error_message,
            "variables": variables_for_response
           }
       
    
        try:
            error = requests.post(endpoint, json = response)
            print(error.status_code)
        
        except:
            print('fail')
            
            
#Create an incident
            

    def fail(self, error_message, retries = 0, retry_timeout= 0):
        response_body = json.loads(body)
        taskid = response_body[0]['id']
        taskid = str(taskid)   

    
        endpoint = str(self.url) + "/external-task/"+ taskid + "/failure"
    
        workerid = response_body[0]['workerId']
        workerid = str(workerid)
    
    
        response = {
            "workerId": workerid,
            "errorMessage": error_message,
            "retries": retries, 
            "retryTimeout": retry_timeout}
                   
        try:
            fail = requests.post(endpoint, json = response)
            print(fail.status_code)        
        
        except:
            print('fail')
            
 # New Lockduration           
    
    def new_lockduration(self, new_duration):
        
        response_body = json.loads(body)
        taskid = response_body[0]['id']
        taskid = str(taskid)
        
        endpoint = str(self.url) + "/external-task/"+ taskid + "/extendLock"
        
        workerid = response_body[0]['workerId']
        workerid = str(workerid)
        
        response = {
            "workerId": workerid,
            "newDuration": new_duration
        }
        
        try:
            newDuration = requests.post(endpoint, json = response)
            print(newDuration.status_code)
            print(workerid)
        except:
            print('fail')


