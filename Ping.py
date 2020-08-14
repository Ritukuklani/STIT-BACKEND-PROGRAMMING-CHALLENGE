import json
import boto3
import random as r

def lambda_handler(event, context):
    # dynamo_resource = boto3.resource('dynamodb')

    # dynamo_visitors_table = dynamo_resource.Table("visitors")
    # dynamo_passcodes_table = dynamo_resource.Table("passcodes")
    resource = boto3.resource('dynamodb')
    table = resource.Table('UserTable')
    usertable = resource.Table('Users')
    reservationtable = resource.Table('ReservationTable')
    
    if (event["context"]["resource-path"]) == "/login/setfavourite":
        input = {'Username':'Ritukuklani', "FavouriteRestaurant": [event["body-json"]["FavouriteRestaurant"]]}
        print(input)
        response = table.put_item(Item=input)
        print(response)
    if (event["context"]["resource-path"]) == "/login/unsetfavourite":
        
        print(event["body-json"]["UnsetFavouriteRestaurant"])
        response = table.get_item(Key={"Username":"Ritukuklani"})
        print(response)
        new_list = response['Item']['FavouriteRestaurant'][0]
        print(new_list)
        for item in response['Item']['FavouriteRestaurant'][0]:
            if item == event["body-json"]["UnsetFavouriteRestaurant"]:
                new_list.remove(item)
        print(new_list)
        input = {'Username':'Ritukuklani', "FavouriteRestaurant":new_list}
        response = table.put_item(Item=input)
    
    if (event["context"]["resource-path"]) == "/login/reserve":
        reservationID=""
        for i in range(4):
            reservationID+=str(r.randint(1,9))
        # print(event["params"]["header"]["Authorization"])
        # response = table.get_item(Key={"UserID":event["params"]["header"]["Authorization"]})
        # print(response)
        input1 = {'Username':"Ritukuklani", "BusinessID": [event["body-json"]["BusinessID"]], "status":r.choice(["SUCCESS", "FAILURE", "PENDING"]), "ReservationID":reservationID}
        print(input1)
        response = reservationtable.put_item(Item=input1)
        print(response)
        input = {"Username":"Ritukuklani",'BusinessID':event["body-json"]["BusinessID"], "ReservationID": [reservationID]}
        print(input)
        response = table.put_item(Item=input)
        print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
