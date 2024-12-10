import json

# Let's look at dictionaries in a more hand-on way.
# JSON files are very common place for storing lots of data.
# The most challenging aspect of these files is being able to 
# get access to the data we are interested in but with a bit
# of practice and going step-by-step we can extract the data
# we want.


people_string = '''
{
    "student":[
        {
            "name": "John Smith",
            "phone": "555-555-5456",
            "emails": ["john.smith@du.edu", "jsmith@gmail.com"],
            "undergrad": false
        },
        {
            "name": "Jane Doe",
            "phone": "888-888-4563",
            "emails": null,
            "undergrad": true
        },
        {
            "name": "Thomas Hoffman",
            "phone": "999-777-4563",
            "emails": ["thomas.hoffman@realemail.com"],
            "undergrad": true
        }
    ],
    "professors":[
        {
            "name": "Professor McProfessorFace",
            "phone": "111-111-1111",
            "office_number": "217",
            "department": "Computer Science",
            "tenure": true,
            "courses": ["Intro to Python", "Data Science Tools 1"],
            "advising": ["Jane Doe", "Thomas Hoffman"],
            "responsibilities": {"manage":"COMP3006", "grade":"COMP4448"}
        },
        {
            "name": "Teacher McTeacherFace",
            "phone": "222-222-2222",
            "office_number": "517",
            "department": "Computer Science",
            "tenure": false,
            "courses": ["Parallel & Distributed Computing", "Machine Learning"],
            "advising": null
        }
    ]
}
'''

#Sanity check:
# print("This is a string:", people_string.upper())


#Load data (json string) so we can search within the JSON data structure:
# data = json.loads(people_string)
# print(data)
# print(type(data)) #dict


#Let's access the "student" list:
# print(data['student']) #list of dictionaries
# print(type(data['student']))
# print(data['student'][0]) #dictionary


#Let's check the data types:
# print(data['student'][0]['emails']) #list of emails
# print(type(data['student'][0]['emails'])) #list
# print(data['student'][0]['emails'][1])


#We can access the data just like we would in a dictionary:
# print(data["student"])


#We can go deeper in the data structure to get exactly what we want. Let's get John Smith's second email:



#Let's iterate over the students and print out some information:
# for student in data['student']:
#     print("\n",student['name'])
#     try:
#         for email in student['emails']:
#             print(email)
#     except TypeError:
#         print("This student doesn't have an email:", \
#               student["name"],f"\nText them instead at: {student['phone']}")





#We can store whatever values we're interested in in variables:
# studentDictList = data['student'] #List of dictionaries
# studentDict0 = studentDictList[0] #Dictionary with student info
# studentEmailList = studentDict0['emails'] #Get emails list
# studentSecondEmail = studentEmailList[1] #Get student's second email
# print(studentSecondEmail) #Expected output: jsmith@gmail.com






#Let's loop over the people in our list and print out their information:
# for student in data['student']:
#     print(student['emails'])


#Let's loop over the people in our list and print out their name only:
# for student in data['student']:
#     print(student['name'])


# for student in data['student']:
#         print(student)
#         del student['phone']
#         print(student)

#Let's now delete the phone for each student:
# def delete_phone():
#     for student in data['student']:
#         # print(student)
#         del student['phone']
#         # print(student)


# print(data['student'])
# delete_phone()
# print("\n\n",data['student'])





#Write the data out to a json string:
# new_json_string = json.dumps(data)
# print(new_json_string)
# print(type(new_json_string))


#Our last json string was hard to read, so we can change the formatting:
# new_json_string = json.dumps(data, indent=2)
# print(new_json_string)


#It's also possible to sort the keys in a json string :
# new_json_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_json_string)







#--------------Reading JSON files---------------------


#Read in data from a json file:
# with open('json_files/westworld.json', 'r') as f:
#     data = json.load(f)

#Let's peak in the data to find where the data we're interested in is located:
# for dat in data.items():
#     print(dat, "\n\n")

#Sanity check that we can get the summary for the show:
# print(data['summary'])

# print(json.dumps(data, indent=2))

# for episode in data['_embedded']['episodes']:
#     print(episode, "\n\n")


#Let's extract the following fields from each episode and put them in 
#a JSON string with indentation so it's easier to read:
#Episode's title
#(Season, episode number)
#Airdate
#Run time
#Rating
#Summary
    
# for episode in data['_embedded']['episodes']:
#     print(episode["name"])
#     print(episode["season"], episode["number"])
#     print(episode["airdate"])
#     print(episode['runtime'])
#     print(episode['rating'])
#     print(episode["summary"], end="\n\n")







# episodes = []

# for episode in data['_embedded']['episodes']:
#     episodeDict = {}
#     episodeDict['title'] = episode['name']
#     episodeDict['se'] = (episode['season'], episode['number'])
#     episodeDict['airdate'] = episode['airdate']
#     episodeDict['runtime'] = episode['runtime']
#     episodeDict['rating'] = episode['rating']
#     episodeDict['summary'] = episode['summary'].lstrip("<p>").rstrip("</p>")
#     episodes.append(episodeDict)
    
#Our data is all here... it's just hard to read:
# print(episodes)
# for episode in episodes:
#     print(episode)


#We can have json dump our data into a json string :
# episodes_json = json.dumps(episodes, indent=2)
# print(episodes_json[:700])

#List of dictionaries
# episodes

#Get a given episode:
# print(episodes[0])

#Extract ratings for an episode:
# print(episodes[0]['rating']['average'])

#Compute the averge rating for the show:
# counter = 0
# ratingTotal = 0

# for episode in episodes:
#     episodeRating = episode['rating']
    
#     #Increase episode counter:
#     counter +=1 

#     #Count up the ratings total:
#     ratingTotal += episodeRating['average']

# print("The serie's average rating:", ratingTotal/counter)


#Exercise: Compute the averge rating for the each season.






# Exercise solution:
# counter = 0
# ratingTotal = 0
# seasonDict = {}
# for episode in episodes:
#     #Extract rating:
#     episodeRating = episode['rating']['average']
#     #Extract season:
#     episodeSeason = episode['se'][0]

#     if episodeSeason not in seasonDict:
#         seasonDict[episodeSeason] = [episodeRating, 1]
#         # seasonDict['counter' + str(episodeSeason)] = 1
#     else:
#         seasonDict[episodeSeason][0] = seasonDict[episodeSeason][0] + episodeRating 
#         seasonDict[episodeSeason][1] += 1
#         # seasonDict['counter' + str(episodeSeason)] += 1

# print(seasonDict)

# for key, value in seasonDict.items():
#     print(f"Season {key} average rating is: {value[0]/value[1]}")




