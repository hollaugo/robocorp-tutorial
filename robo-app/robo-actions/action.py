"""
A simple AI Action template for comparing timezones

Please checkout the base guidance on AI Actions in our main repository readme:
https://github.com/robocorp/robocorp/blob/master/README.md

"""
import os
import json
from dotenv import load_dotenv
from robocorp.actions import action
from datetime import datetime
import pytz
from tavily import TavilyClient
from simple_salesforce import Salesforce


load_dotenv()

#Get environment variables
TAVILY_API_KEY = os.environ["TAVILY_API_KEY"]
SALESFORCE_USERNAME = os.environ["SALESFORCE_USERNAME"]
SALESFORCE_PASSWORD = os.environ["SALESFORCE_PASSWORD"]
SALESFORCE_SECURITY_TOKEN = os.environ["SALESFORCE_SECURITY_TOKEN"]


# Create a Tavily client
tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

# Create a Salesforce client
sf = Salesforce(instance='can80.salesforce.com', session_id='')
sf = Salesforce(username=SALESFORCE_USERNAME, password=SALESFORCE_PASSWORD, security_token=SALESFORCE_SECURITY_TOKEN)



@action
def compare_time_zones(user_timezone: str, compare_to_timezones: str) -> str:
    """
    Compares user timezone time difference to given timezones

    Args:
        user_timezone (str): User timezone in tz database format. Example: "Europe/Helsinki"
        compare_to_timezones (str): Comma seperated timezones in tz database format. Example: "America/New_York, Asia/Kolkata"

    Returns:
        str: List of requested timezones, their current time and the user time difference in hours
    """
    output: list[str] = []

    try:
        user_tz = pytz.timezone(user_timezone)
        user_now = datetime.now(user_tz)
    except pytz.InvalidTimeError:
        return f"Timezone '{user_timezone}' could not be found. Use tz database format."
    
    output.append(f"- Current time in {user_timezone} is {user_now.strftime('%I:%M %p')}")

    target_timezones = [s.strip() for s in compare_to_timezones.split(',')]
    for timezone in target_timezones:
        try:
            target_tz = pytz.timezone(timezone)
            target_now = datetime.now(target_tz)
            time_diff = (int(user_now.strftime('%z')) - int(target_now.strftime('%z'))) / 100

            output.append(f"- Current time in {timezone} is {target_now.strftime('%I:%M %p')}, the difference with {user_timezone} is {time_diff} hours")
        except pytz.InvalidTimeError:
            output.append(f"- Timezone '{timezone}' could not be found. Use tz database format.")

    # Pretty print for log
    print("\n".join(output))
    
    return "\n".join(output)

@action
def search_topics(topic: str) -> str:
    """
    Searches for topics in Tavily

    Args:
        topic (str): Topic to search for

    Returns:
        str: List of results found
    """
    response = tavily.search(query=topic)

    # Convert the response to a JSON string
    response_str = json.dumps(response)

    return response_str

@action
def query_accounts() -> str:
    """
    Queries Salesforce for accounts

    Returns:
        str: Result of the query.
    """
    response = sf.query("SELECT Id, Name FROM Account")
    result = json.dumps(response)
    return result

#Search for an account's related cases plus their information including their status based on a name
@action
def query_cases(account_name: str) -> str:
    """
    Queries Salesforce for cases related to an account

    Args:
        account_name (str): Name of the account to search for

    Returns:
        str: Result of the query.
    """
    response = sf.query(f"SELECT Id, CaseNumber, Subject, Description, Status FROM Case WHERE Account.Name = '{account_name}'")
    result = json.dumps(response)
    return result