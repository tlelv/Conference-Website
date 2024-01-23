import csv


# Program which populates a form with nametags for data from an outside file

line_list = []
collective_list = []
data_content = ""
counter = 0

try:
    with open ('data/registrant_data.csv', 'r') as myFile:
        next(myFile)
        for line in myFile:
            line_list = line.strip().split(sep=',') #strip removes the new line
            newDict = {
                'registration_date': line_list[0],
                'title': line_list[1],
                'firstname': line_list[2],
                'lastname': line_list[3],
                'address1': line_list[4],
                'address2': line_list[5],
                'city': line_list[6],
                'state': line_list[7],
                'zipcode': line_list[8],
                'telephone': line_list[9],
                'email': line_list[10],
                'web': line_list[11],
                'position': line_list[12],
                'company': line_list[13],
            }
            if counter % 2 == 0:
                curr = ("<div class=\"row\"><div class=\"left\"><h1><span class=\"firstname\""
                        ">" + newDict['firstname'] + " </span><span class=\"lastname\">" + newDict['lastname'] + "</span>"
                        "</h1><h2 class=\"position\">" + newDict['position'] + "</h2><p class=\"company\">" +
                        newDict['company'] + "</p><p><span class=\"state\">" + newDict['state'] + "</span>, "
                        "<span class=\"city\">" + newDict['city'] + "</span></p></div>")
            else:
                curr = ("<div class=\"right\"><h1><span class=\"firstname\""
                        ">" + newDict['firstname'] + " </span><span class=\"lastname\">" + newDict['lastname'] + "</span>"
                        "</h1><h2 class=\"position\">" + newDict['position'] + "</h2><p class=\"company\">" +
                        newDict['company'] + "</p><p><span class=\"state\">" + newDict['state'] + "</span>, "
                        "<span class=\"city\">" + newDict['city'] + "</span></p></div></div>")
            counter += 1
            data_content += curr
            collective_list.append(newDict)

        with open('nametags10gen.html', 'w+') as outFile:
            top_content = ("<!DOCTYPE html> !-- Name: Treyson Le Assignment: CS336 Assignment #7 Created: 10/29/2023 "
                           "Description: Nametag page of the conference site --> <html lang=\"en\"><head><meta charset=\"UTF-8\">"
                           "<title>Nametags</title><link rel=\"stylesheet\" href=\"css/avery.css\" type=\"text/css\"></head><body>"
                           "<div class=\"main\"><p></p>")
            bottom_content = "</div></body></html>"
            outFile.write(top_content + data_content + bottom_content)

except FileNotFoundError:
    print("Error: File not found!")






