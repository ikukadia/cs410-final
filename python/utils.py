import io
import json

# returns all messages of given user
# returns a list of message objects
def get_messages(data, user):
    participants = list(map(lambda x: x["name"], data["participants"]))
    if user not in participants:
        return []
    messages = list(filter(lambda x: x["sender_name"] == user, data["messages"]))
    print(messages)
    return messages

def write_all_messages(data, user):
    
    f = open("%s.txt" %user, "w+")
    
    for message in get_messages(data, user):
        if "content" in message.keys():
            f.write(message["content"])
    
    f.close()

# returns a list of participants in given JSON
# returns a list of strings
def get_participants(data):
    return list(map(lambda x: x["name"], data["participants"]))

def format_dict(dict):
    # {"Omar Mbarki": 5, "Suhirtha Raj": 7, "Elaine Raj": 7}
    # [{"name": Omar Mbarki, "amount": 5}, {"name": "Suhirtha Raj", "amount": 4}, {"name: Elaine Wang", "amount": 7}]
    list = []

    for key, value in dict.items():
        data = {}
        data["category"] = key
        data["amount"] = value
        list.append(data)
    
    json_array = json.dumps(list)
    return json_array

def main():
    with open('dont_commit.json') as f:
        data = json.load(f)
    write_all_messages(data, "Suhirtha Raj")

if __name__ == '__main__':
    main()


