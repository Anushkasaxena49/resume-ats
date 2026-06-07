resume = open("resume.txt").read().lower()
job = open("job.txt").read().lower()

resume_words = resume.split()
job_words = job.split()

match = 0
           
for word in job_words:
    if word in resume_words:
        match += 1
        
score = (match / len(job_words))*100
print("ATS Score:", round(score, 2), "%")       
               