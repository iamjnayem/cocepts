from copy import deepcopy
me = {
    "name": "Nayem",
    "info": {
        "company": "deshi",
        "stack": "laravel",
        "os": "ubuntu",
        "role": "intern",
        "seat": "window-seat"
    }
}
print(me)

# now tipu bro comes

tipu = me.copy()
tipu["name"] = "Tipu The Yo Boy"
tipu["info"]["role"] = "Software Engineer"
tipu["info"]["seat"] = "right side of Nayem"
print(tipu)

#Now I wish I would change my seat location in new office
#At new office

me["info"]["seat"] ="new office new seat near window"
print(me)

print(tipu)

me = deepcopy(tipu)
me["name"] = "Nayem"
me["info"]["seat"] = "Meeting room"
print(me)
print(tipu)
