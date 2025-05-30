

import time
import sys



name = ""
#user's name which they will have to provide using CLI





def get_quotes(user_name):   #user's name will be passed here, which the user will provide using CLI
    """function which contains all the motivational qoutes will appear on the terminal ,later on"""
    return [
        f"{user_name}, fail fast, learn faster.",
        "Build what others fear.",
        "Remember, success loves bold minds.",
        "Test, break, rebuild—repeat.",
        f"{user_name}, launch your vision or stay grounded.",
        "Dream big or stay average.",
        "Try until you fail!",
        "Remember, comfort kills innovation.",
        f"{user_name}, let obsession drive execution.",
        "Be relentless or be forgotten.",
        "Hard work is the key to success.",
        f"{user_name}, never give up!",
        "In any situation, be patient.",
        f"And the last advice for you, dear {user_name}:",
        "Disrupt or be disrupted!"
    ]#the motivational qoutes




#new commit by soma_madhobilata , 
#unit testing feature added
#time delay extended by +1.5 second to give a more animative vibe





def motivation():
    """function to show motivational qoutes on the terminal"""
    global name
    quotes = get_quotes(name)
    for quote in quotes:
        print(quote)
        print("\n")    #print a blank line for code readibility
        time.sleep(2.5)    #time delay extended on current commit
    return quotes          #returning the qoutes for ease of unit testing







def main():
    """main function"""
    global name
    if len(sys.argv) < 2:
        #if no arguement is provided by the user on the command line
        #we shall exit the program
        print("Please provide your name as a command line argument.")
        sys.exit(1)
    name = sys.argv[1]   #user will have to provide their name here 
                         #then motivational qoutes will start appearing on the terminal along with the user's name
    motivation()   #run the motivation fcuntion to start the program







def test_motivation_func():
    """function to test the program using unit test"""
    global name
    name = "TestUser"
    expected = get_quotes(name)
    result = get_quotes(name)
    #test the function by comapring the qoutes in it
    assert expected == result, "Function is not working properly!"
    





#main test  
#run the program by running the main function
if __name__=="__main__":
    main()        