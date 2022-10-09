from csv import excel
import requests
from bs4 import BeautifulSoup
import openpyxl

excel = openpyxl.Workbook()

sheet = excel.active
sheet.title = 'MU Faculty Data'

sheet.append(['URL','Name', 'Profession', 'Department', 'Emil-Id And Phone Number','experience', 'publications', 'research'])


def emptyCheck(data):
    if len(data.strip()) == 0:
        print('No data available.')


all_url = [
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=0",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=1",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=2",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=3",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=4",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=5",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=6",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=7",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=8",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=9",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=10",
"https://www.mahindrauniversity.edu.in/faculty?field_profile_target_id=All&title=&page=11"
]


#url = "https://www.mahindrauniversity.edu.in/faculty/chitra-gurnani"

#urls = ['https://www.mahindrauniversity.edu.in/faculty/dr-ram-m-vemuri', 'https://www.mahindrauniversity.edu.in/faculty/anish-hirwe', 'https://www.mahindrauniversity.edu.in/faculty/dr-keerthi-katam', 'https://www.mahindrauniversity.edu.in/faculty/abhinav-chaturvedi', 'https://www.mahindrauniversity.edu.in/faculty/vandna-gokhroo', 'https://www.mahindrauniversity.edu.in/faculty/kamna-pande', 'https://www.mahindrauniversity.edu.in/faculty/catherine-xavier', 'https://www.mahindrauniversity.edu.in/faculty/neha-khurana', 'https://www.mahindrauniversity.edu.in/faculty/alok-verma', 'https://www.mahindrauniversity.edu.in/faculty/meher-pramod-mantravadi', 'https://www.mahindrauniversity.edu.in/faculty/nidhi-gupta', 'https://www.mahindrauniversity.edu.in/faculty/dr-vivek-sehrawat', 'https://www.mahindrauniversity.edu.in/faculty/yerramadha-jyothi-basu', 'https://www.mahindrauniversity.edu.in/faculty/dr-sonal-hukampal-singh', 'https://www.mahindrauniversity.edu.in/faculty/v-janardhan', 'https://www.mahindrauniversity.edu.in/faculty/bandari-balaji-prashanth', 'https://www.mahindrauniversity.edu.in/faculty/ani-thomas', 'https://www.mahindrauniversity.edu.in/faculty/dr-vinay-sharma', 'https://www.mahindrauniversity.edu.in/faculty/dr-samyukta-bhupatiraju', 'https://www.mahindrauniversity.edu.in/faculty/darshna-gupta', 'https://www.mahindrauniversity.edu.in/faculty/sanjay-singh', 'https://www.mahindrauniversity.edu.in/faculty/mona-pattanaik', 'https://www.mahindrauniversity.edu.in/faculty/aparna-singh', 'https://www.mahindrauniversity.edu.in/faculty/tatheer-fatima', 'https://www.mahindrauniversity.edu.in/faculty/sehar-khwaja', 'https://www.mahindrauniversity.edu.in/faculty/ankesh-shreyansh', 'https://www.mahindrauniversity.edu.in/faculty/anindita-chakrabarty', 'https://www.mahindrauniversity.edu.in/faculty/mandeep-kaur', 'https://www.mahindrauniversity.edu.in/faculty/rishi-raj-bhardwaj', 'https://www.mahindrauniversity.edu.in/faculty/nisha-mary-mathew', 'https://www.mahindrauniversity.edu.in/faculty/dr-nmythili', 'https://www.mahindrauniversity.edu.in/faculty/anjali-bhatnagar', 'https://www.mahindrauniversity.edu.in/faculty/vanita-malewar', 'https://www.mahindrauniversity.edu.in/faculty/ayushi-tandon', 'https://www.mahindrauniversity.edu.in/faculty/amogh-kumbargeri', 'https://www.mahindrauniversity.edu.in/faculty/sowmini-devi-veeramachaneni', 'https://www.mahindrauniversity.edu.in/faculty/simon-see', 'https://www.mahindrauniversity.edu.in/faculty/sherlin-suresh', 'https://www.mahindrauniversity.edu.in/faculty/shampa-raghunathan', 'https://www.mahindrauniversity.edu.in/faculty/ravibabu-mashetti', 'https://www.mahindrauniversity.edu.in/faculty/pradeep-kumar-rai', 'https://www.mahindrauniversity.edu.in/faculty/pankaj-narke', 'https://www.mahindrauniversity.edu.in/faculty/monali-sahu-pathange', 'https://www.mahindrauniversity.edu.in/faculty/greeshma-mohan', 'https://www.mahindrauniversity.edu.in/faculty/dr-faiz-iqbal', 'https://www.mahindrauniversity.edu.in/faculty/dipti-mishra', 'https://www.mahindrauniversity.edu.in/faculty/bhuvaneswari-gurumoorthy', 'https://www.mahindrauniversity.edu.in/faculty/anil-annadi', 'https://www.mahindrauniversity.edu.in/faculty/paromita-das', 'https://www.mahindrauniversity.edu.in/faculty/vivek-nd', 'https://www.mahindrauniversity.edu.in/faculty/shruti-kakkar', 'https://www.mahindrauniversity.edu.in/faculty/muneer-shaik', 'https://www.mahindrauniversity.edu.in/faculty/rakesh-prasad-badoni', 'https://www.mahindrauniversity.edu.in/faculty/sri-kalyana-rama-j', 'https://www.mahindrauniversity.edu.in/faculty/george-varghese', 'https://www.mahindrauniversity.edu.in/faculty/biswarup-biswas', 'https://www.mahindrauniversity.edu.in/faculty/meraj-alam', 'https://www.mahindrauniversity.edu.in/faculty/nilanjan-banik', 'https://www.mahindrauniversity.edu.in/faculty/prashanth-podili', 'https://www.mahindrauniversity.edu.in/faculty/manish-gupta', 'https://www.mahindrauniversity.edu.in/faculty/pranjal-chandrakar', 'https://www.mahindrauniversity.edu.in/faculty/shreeja-ganta', 'https://www.mahindrauniversity.edu.in/faculty/manjula-mallepalli', 'https://www.mahindrauniversity.edu.in/faculty/shivdasini-singh-amin-0', 'https://www.mahindrauniversity.edu.in/faculty/sridhar-acharyulu', 'https://www.mahindrauniversity.edu.in/faculty/pradeep-racherla', 'https://www.mahindrauniversity.edu.in/faculty/ramakrishna-velamuri', 'https://www.mahindrauniversity.edu.in/faculty/vegitha-reddy', 'https://www.mahindrauniversity.edu.in/faculty/tamal-kanti-paul', 'https://www.mahindrauniversity.edu.in/faculty/sayoni-laha', 'https://www.mahindrauniversity.edu.in/faculty/salome-benhur', 'https://www.mahindrauniversity.edu.in/faculty/ranjith-shankaran', 'https://www.mahindrauniversity.edu.in/faculty/rajkumar-phatate-0', 'https://www.mahindrauniversity.edu.in/faculty/raj-narayanan', 'https://www.mahindrauniversity.edu.in/faculty/paromita-bose', 'https://www.mahindrauniversity.edu.in/faculty/kumudham-balasubramanian', 'https://www.mahindrauniversity.edu.in/faculty/visalakshi-talakokula', 'https://www.mahindrauniversity.edu.in/faculty/venkata-dilip-kumar-pasupuleti', 'https://www.mahindrauniversity.edu.in/faculty/saladi-sv-subbarao', 'https://www.mahindrauniversity.edu.in/faculty/jayapraksh-vemuri', 'https://www.mahindrauniversity.edu.in/faculty/hari-prasad', 'https://www.mahindrauniversity.edu.in/faculty/yayati-gupta', 'https://www.mahindraunivers/www.mahindrauniversity.edu.in/faculty/subbarao-boddu', 'https://www.mahindrauniversity.edu.in/faculty/sreedhar-madichetty', 'https://www.mahindrauniversity.edu.in/faculty/sayantan-hazra', 'https://www.mahindrauniversity.edu.in/faculty/pooran-singh', 'https://www.mahindrauniversity.edu.in/faculty/kr-sarma', 'https://www.mahindrauniversity.edu.in/faculty/jl-bhattacharya', 'https://www.mahindrauniversity.edu.in/faculty/gopinath-g-r', 'https://www.mahindrauniversity.edu.in/faculty/senbagaraman-sudarsanam', 'https://www.mahindrauniversity.edu.in/faculty/sebastian-uppapalli', 'https://www.mahindrauniversity.edu.in/faculty/ravikiran-bompelly', 'https://www.mahindrauniversity.edu.in/faculty/ranjith-kunnath', 'https://www.mahindrauniversity.edu.in/faculty/prasad-pokkunuri', 'https://www.mahindrauniversity.edu.in/faculty/palash-roy-chowdhury', 'https://www.mahindrauniversity.edu.in/faculty/manish-kumar-agrawal', 'https://www.mahindrauniversity.edu.in/faculty/kondaiah-p', 'https://www.mahindrauniversity.edu.in/faculty/jagan-mohan-padbidri', 'https://www.mahindrauniversity.edu.in/faculty/harshavardhan-kalathur', 'https://www.mahindrauniversity.edu.in/faculty/deep-seth', 'https://www.mahindrauniversity.edu.in/faculty/gomathi-anandhanatarajan', 'https://www.mahindrauniversity.edu.in/faculty/chitra-gurnani', 'https://www.mahindrauniversity.edu.in/faculty/dr-sanjukta-das', 'https://www.mahindrauniversity.edu.in/faculty/rakhee-basu', 'https://www.mahindrauniversity.edu.in/faculty/manoj-kumar-yadav', 'https://www.mahindrauniversity.edu.in/faculty/mahipal-j', 'https://www.mahindrauniversity.edu.in/faculty/jai-prakash', 'https://www.mahindrauniversity.edu.in/faculty/naga-deepthi-kuchibhatla', 'https://www.mahindrauniversity.edu.in/faculty/murtaza-bohra', 'https://www.mahindrauniversity.edu.in/faculty/jayasri-d', 'https://www.mahindrauniversity.edu.in/faculty/dibakar-roy-chowdhury', 'https://www.mahindrauniversity.edu.in/faculty/bishnu-p-pal', 'https://www.mahindrauniversity.edu.in/faculty/bhanukiran-perabathini', 'https://www.mahindrauniversity.edu.in/faculty/dr-avirneni-deepti', 'https://www.mahindrauniversity.edu.in/faculty/dr-mohd-ataullah-khan', 'https://www.mahindrauniversity.edu.in/faculty/arun-kumar-pujari', 'https://www.mahindrauniversity.edu.in/faculty/dr-ankita-jain', 'https://www.mahindrauniversity.edu.in/faculty/dr-aditya-abburi', 'https://www.mahindrauniversity.edu.in/faculty/tabitha-chekuri', 'https://www.mahindrauniversity.edu.in/faculty/arya-kumar-bhattacharya', 'https://www.mahindrauniversity.edu.in/faculty/bharghava-rajaram', 'https://www.mahindrauniversity.edu.in/faculty/bhaskar-tamma', 'https://www.mahindrauniversity.edu.in/faculty/chirala-satyanarayana', 'https://www.mahindrauniversity.edu.in/faculty/ganesh-babu-kodeboyina', 'https://www.mahindrauniversity.edu.in/faculty/neha-bharill', 'https://www.mahindrauniversity.edu.in/faculty/venkataraman-n-v', 'https://www.mahindrauniversity.edu.in/faculty/prabhakar-singh', 'https://www.mahindrauniversity.edu.in/faculty/abhijit-bhattacharyya']

for url in all_url:
    page = requests.get(url)

    doc = BeautifulSoup(page.text,"html.parser")

    string = "https://www.mahindrauniversity.edu.in"
    for temp in  (doc.find_all("li",{ "class" : "specialisation-block col-lg-4 col-md-6 col-sm-12 col-12"})):
        link = temp.find("a")
        href = link.attrs['href']
        url = (string + href)
        #print(string + href)
        r = requests.get(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent,'html.parser')
        title = soup.title #<title>Om Prakash Patel | Mahindra University</title> # paras = soup.find_all('p') #gets all the paragraphs from the page with all the associated tags # print(soup.find('p')) prints the first paragraph/get the first element in html page #find_all gives all the paragraphs related to the tag
        # get_text(strip=True) in the get text will put everything in one single line
        description = soup.find('div', {'class': 'profile-details-block d-flex flex-column'}).get_text().strip() #name,profession,dept,email,phone
        experience = soup.find('div',{'class':'faculty-tabs-content','id':'experience'}).get_text()
        publications= soup.find('div',{'class':'faculty-tabs-content','id':'publications'}).get_text()
        research = soup.find('div',{'class':'faculty-tabs-content','id':'research'}).get_text()
        emptyCheck(description) #ensuring there is a description
        emptyCheck(experience) #ensuring there is a experience
        emptyCheck(publications) #ensuring there is a publications
        emptyCheck(research) #ensuring there is a research
        desclist = description.split('\n') #it is a list which has name, desgn, dept,email phone
        #desclist.pop(1) #removes the empty line bw name and designation
        #print(url,desclist[0],desclist[1],desclist[2],desclist[3])
        for i in desclist:
            if(len(i) == 0):
                desclist.remove(i) 
        sheet.append([url, desclist[0], desclist[1], desclist[2], desclist[3],experience,publications,research])

excel.save("MU_Chat_Faculty.xlsx")