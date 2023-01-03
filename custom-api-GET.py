import requests
import json

while True:
    
    #will try to make a connection with the user supplied url
    #error message if that connection string fails with a chance to restart from the beginning
    try:
        user_url = input("What is the URL of the API your accessing? https://jsonplaceholder.typicode.com/todos/1 = an example.\n")
        get_url = requests.get(user_url)
        
    except:
        null_ask_var = input("Unable to get that json URL. https://jsonplaceholder.typicode.com/todos/1 = an example. please press enter to restart or type 'exit' to exit\n")
        if null_ask_var == 'exit':
            break
        else:
            continue
        
    #will try to pull the data and convert into json format
    #error message if that fails with a chance to restart from the beginning
    try:
        pull_data = get_url.text
        json_parse = json.loads(pull_data)
        
    except:
        null_json = input("Failed to pull the data and convert into json format. please press enter to restart or type 'exit' to exit\n")
        if null_json == 'exit':
            break
        else:
            continue
    
    #Asks user how many nested variables there are and will ask what they are called.
    try:
        user_json1 = input("How many nested variables are there? (1-2)\n")
        if user_json1 == '1':
            user_json1_input = input("What is the variable you are looking for? 12 = an example\n")
            print(json_parse[user_json1_input])
        
        elif user_json1 == '2':
            user_json1_input = input("What is the first variable you are looking for? 12 = an example\n")
            user_json2_input = input("What is the second nested variable your looking for? name = an example\n")
            print(json_parse[user_json1_input][user_json2_input])
        else:
            not1to2 = input("Please only type the numbers 1 or 2. Press enter to restart or type 'exit' to exit\n")
            if not1to2 == 'exit':
                break
            else:
                continue
            
        restart_var = input("Press enter to quit or type the word 'restart' to start over\n")
        if restart_var == 'restart': 
            continue
        else : 
            break
        
    #if the above try fails then it will give an error message with a chance to restart from the beginning.
    except:
        null_json = input("Failed to print the json variable. Please check that the id your using is correct. please press enter to restart or type 'exit' to exit\n")
        if null_json == 'exit':
            break
        else:
            continue
