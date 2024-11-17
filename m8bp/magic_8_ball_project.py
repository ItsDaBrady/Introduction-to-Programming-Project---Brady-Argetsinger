import random
import requests

def read_responses(file_path):
    """Read responses from a specified text file."""
    with open(file_path, 'r') as f:
        return f.read().splitlines()

def pick_response(responses_list):
    """Select a random response from the list."""
    return random.choice(responses_list)

def main():
    response_file = 'responses.txt'
    responses = read_responses(response_file)

    while True:
        user_question = input("What would you like to ask? (type 'exit' to leave): ")
        if user_question.lower() == 'exit':
            print("Goodbye!")
            break
        
        if responses:
            response = pick_response(responses)
            print(f"The Magic 8 Ball says: {response}")
            responses.remove(response)  # Remove the response once used
        else:
            print("No responses left! Fetching a new answer from an external source...")
            api_response = requests.get("https://api.some-random-response.com/get")
            if api_response.ok:
                random_answer = api_response.json().get("answer", "Try asking again.")
                print(f"The Magic 8 Ball says: {random_answer}")
            else:
                print("Unable to retrieve a response right now.")

if __name__ == "__main__":
    main()