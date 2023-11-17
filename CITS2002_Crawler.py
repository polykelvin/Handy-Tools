import requests
from bs4 import BeautifulSoup
import os
from termcolor import colored

def download_pdf(url, filename):
    """
    Download a PDF file from a given URL and save it with the given filename.
    """
    # Check if the file already exists
    if not os.path.exists(filename):
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(colored(f"Downloaded: {filename}", 'green'))
        else:
            print(colored(f"Failed to download {filename}", 'red'))
    else:
        print(f"File already exists: {filename}")

def download_page(url, filepath):
    """
    Download an HTML page and save it to a specified filepath.
    """
    # Check if the file already exists
    if not os.path.exists(filepath):
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(colored(f"Downloaded: {filepath}", 'green'))
        else:
            print(colored(f"Failed to download {url}", 'red'))
    else:
        print(f"File already exists: {filepath}")

def extract_links(url):
    """
    Download the schedule page and extract labsheet URLs.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        labsheet_links = []
        project_links = []
        for link in links:
            href = link.get('href')
            if href and 'labsheet' in href:  # This checks if 'labsheet' is in the URL
                labsheet_links.append(href)
            if href and 'projects' in href and 'multi' not in href:  # This checks if 'projects' is in the URL
                project_links.append(href)
            if href and 'project' in href and 'multi' not in href:
                project_links.append(href)
        return set(labsheet_links),set(project_links)
    else:
        print(f"Failed to download {url}")
        return []

def main():
    base_url = "https://teaching.csse.uwa.edu.au/units/CITS2002/lectures/"
    schedule_url = "https://teaching.csse.uwa.edu.au/units/CITS2002/schedule.php"
    os.makedirs("CITS2002/lectures", exist_ok=True)

    for i in range(1, 23):  # Assuming there are 22 lectures
        lecture_url = f"{base_url}lecture{i:02}/lecture{i:02}.pdf"
        download_pdf(lecture_url, f"CITS2002/lectures/lecture{i:02}.pdf")

    print("\n")

    os.makedirs("CITS2002/downloaded_pages", exist_ok=True)
    base_url = "https://teaching.csse.uwa.edu.au/units/CITS2002/"
    pages = ["index.php", "schedule.php", "faq.php", "os-books.php", "c-books.php", "past-projects", "workeffectively.php","examinations.php"]
    for page in pages:
        download_page(base_url + page, "CITS2002/downloaded_pages/" + page)

    print("\n")

    # Extract labsheet links
    labsheet_links,project_links = extract_links(schedule_url)

    if labsheet_links == []:
        print("No links found")
        exit()
    os.makedirs("CITS2002/labsheets", exist_ok=True)

    for link in labsheet_links:
        full_url = base_url + link
        filename = link.split('/')[-1]
        download_page(full_url, "CITS2002/labsheets/" + filename)

    os.makedirs("CITS2002/projects", exist_ok=True)
    for link in project_links:
        filename = link.split('/')[-1]
        download_page(link, "CITS2002/projects/" + filename)
        
    os.makedirs("CITS2002/projects/projects_description", exist_ok=True)

    for link in project_links:
        _,new_project_links = extract_links(link)
        for newlink in new_project_links:
            filename = newlink.split('/')[-1]
            full_url = base_url+"projects/" + newlink
            download_page(full_url, "CITS2002/projects/projects_description/" + filename)



if __name__ == "__main__":
    main()
