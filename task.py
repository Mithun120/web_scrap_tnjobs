from bs4 import BeautifulSoup
import requests
import re
import csv


# Fetch HTML content
html_content = requests.get("https://www.tnprivatejobs.tn.gov.in/Home/Jobs").text

# Parse HTML
soup = BeautifulSoup(html_content, "html.parser")
extract_list = soup.find('div', class_="col-md-12")

# Write HTML content to a file
with open('list.html', 'w') as html_file:
    for i in extract_list:
        html_file.write(i.text)
for i in range(0,351,10):
# # Find company names using regex
    company_names = re.findall(r'<a\s+style="color:\s*#(?:[0-9a-fA-F]{3}){1,2};?"\s+href="https:\/\/www\.tnprivatejobs\.tn\.gov\.in\/candidate\/Home\/ca_jobfair_single\/\d+">\s*(.*?)\s*<\/a>', html_content)

# # Print company names
# print('company names',company_names)

    management_names=re.findall('<a\s+style="color:\s*#\w{6};?"\s+href="https:\/\/www\.tnprivatejobs\.tn\.gov\.in\/Home\/jobsdetails_page\/company\/\d+">\s*(.*?)\s*<\/a>',html_content)
# #print management names
# print('management names',management_names)

    work=re.findall('<span\s+style="color:\s*#\w{6};line-height:\s*\d+px;">\s*<i\s+class="fa\s+fa-cogs"\s+aria-hidden="true"\s+style="color:\s*#\w{6};"><\/i>\s*(.*?)\s*<\/span>',html_content)
# print('work',work)

# looping

# Determine the length of the lists (assuming they have the same length)
    num_entries = len(company_names)

# Write the data to a CSV file
    with open('extracted_data.csv', 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Company Name', 'Management Name', 'Work'])  # Write header row
        for i in range(num_entries):
            writer.writerow([company_names[i], management_names[i], work[i]])

print("CSV file created successfully.")



###

# jobs=[] for i in range(0,351,10): page_url='https://www.tnprivatejobs.tn.gov.in/Home/jobs/'+str(i) res=requests.get(page_url) soup=BeautifulSoup(res.text,'html.parser') divtag=soup.find_all('li') for li_tag in divtag: h4tag = li_tag.find_all('h4') for h4 in h4tag: jobs.append(h4.text.strip()) print(jobs)
###

# import requests
# from bs4 import BeautifulSoup
# import csv

# # Fetch HTML content
# html_content = requests.get("https://www.tnprivatejobs.tn.gov.in/Home/Jobs").text

# # Parse HTML
# soup = BeautifulSoup(html_content, "html.parser")

# # Find container for job listings
# extract_list = soup.find('div', class_="col-md-12")

# # Open CSV file for writing
# with open('jobs.csv', 'w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file)
    
#     # Write header row
#     writer.writerow(['Name', 'Posted Date', 'Open Until', 'Location', 'Salary', 'Work'])
    
#     # Extract and process each job listing
#     for job in extract_list.find_all('div', class_='job-listing'):
#         name = job.find('h5').text.strip()
#         details = job.find('p').text.strip().split('|')
#         posted_date = None
#         open_until = None
#         salary = None
#         location = None
#         work = None

#         for detail in details:
#             detail = detail.strip()
#             if detail.startswith("Posted Date"):
#                 posted_date = detail.split(':')[1].strip()
#             elif detail.startswith("Open Until"):
#                 open_until = detail.split(':')[1].strip()
#             else:
#                 parts = detail.split(' ')
#                 if len(parts) > 1:
#                     if parts[0].isdigit() and '-' in parts[1]:
#                         salary = detail.strip()
#                     else:
#                         location = detail.strip()
#                 else:
#                     work = detail.strip()

#         # Write row to CSV
#         writer.writerow([name, posted_date, open_until, location, salary, work])

# print("CSV file created successfully.")
