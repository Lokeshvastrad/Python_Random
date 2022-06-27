def eventsAlerts(events,criteria):
    l=[]
    d={}
    for event in events:
        if event['type'] == 'refund' and event['value'] < criteria['threshold']:
            l.append(event)
    
    return l



events = [
    {'type':'Purchase', 'value':'1'},
    {'type':'refund','value' : '2'},
    {'type':'refund', 'value': '3'}
    ]

criteria = { 'op':'lesser','threshold': '4'}


print(eventsAlerts(events,criteria))