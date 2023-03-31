from bs4 import BeautifulSoup
import requests


v_company_names = [] # initialize a vector which will be filled with the names of the companies

with open('emo_test_linkedin.html', 'r') as html_file: #open an html file and give it a name "html_file"
    content = html_file.read() # read the file

    soup = BeautifulSoup(content, 'lxml')  #scan the file

    profile_name = soup.find('h1') #find the first "h1" tag and assign it to "profile name" (This is the name of the profile account) 
    company_box = soup.find_all('div', class_ = 'pvs-entity pvs-entity--padded pvs-list__item--no-padding-in-columns') #These are the boxes under profile Experience
    for x in company_box: #iterate over each box
        company_names = x.find_all('span', class_='t-14 t-normal') #find the names of each company using the span tag
        for name in company_names: # This is the format of each name " SwooshedOut Â· Full-timeSwooshedOut Â· Full-time "
            word = 'Â·' # We use the following python properties to clean the string and get only the text before the first "A" symbol
            if word not in name.text: # This excludes some strings that do not contain names of companies
                continue
            string = name.text.split(' ') 
            index = string.index(word)
            final_company_name = ''
            for words in name.text.split()[0:index]: #Now we combine back the filtered strings into one string
                final_company_name += f'{words} ' # ['Bocconi', 'AI', '&', 'Neuroscience', 'Student', 'Association'] --> Bocconi AI & Neuroscience Student Association
            v_company_names.append(final_company_name) #append the final names to the vector
            print(f"{profile_name.text} has worked for {final_company_name}") # print each company the user has worked for
