def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1161239/fields/1.json?api_key='
    KEY='AYGBIK6A2NOW250Y'
    HEADER='&results=2'
    NEW_URL= URL+KEY+HEADER
    print(NEW_URL)
    
    get_data= requests.get(NEW_URL).json()
    print(get_data)
    channel_id=get_data['channel']['id']
    
    field_1=get_data['feeds']
    print(field_1)
    
    t=[]
    for x in field_1:
        t.append(x['field1'])
        
if __name__ == '__main__':
    read_data_thingspeak()