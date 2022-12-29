from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


def parse_page():
    main_page = requests.get("https://www.studentski-servis.com/studenti/prosta-dela").text
    soup_page = BeautifulSoup(main_page, "lxml")
    num_of_pages = soup_page.find_all("a", "page-link")[-2].text

    job_list = []
    for number in range(int(num_of_pages)):
        print(f"Scraping page {number + 1} of {num_of_pages} ...")
        page = requests.get(f"https://www.studentski-servis.com/studenti/prosta-dela?page={number}").text
        soup_page = BeautifulSoup(page, "lxml")
        jobs = parse_jobs(soup_page)
        job_list.append(jobs)

    flat_list = [item for sublist in job_list for item in sublist]
    save_to_csv(flat_list)


def parse_jobs(page: BeautifulSoup):
    job_list = page.find_all("article", class_="job-item")
    jobs = []

    for job in job_list:
        title = job.find("h5").text
        salary = job.find("li", class_="job-payment").text.strip()
        digits = re.search(r"(\d+\.\d+) €/h", salary)
        net_salary = 0
        if digits:
            net_salary = digits.group(1)

        location = job.find_all("p")[1].get_text(strip=True)
        description = job.find_all("p")[2].get_text(strip=True)

        jobs.append({
            "title": title,
            "salary": f"{net_salary} €/h",
            "location": location,
            "description": description
        })

    return jobs


def save_to_csv(jobs: []):
    df = pd.DataFrame(jobs)
    df.to_csv("jobs.csv", sep=',', encoding='utf-8')


if __name__ == '__main__':
    parse_page()
