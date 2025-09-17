from django.shortcuts import render

def resume_view(request):
    data = {
        # ==== HEADER ====
        "name": "Aditya Kolluru",
        "role": "Software / Data — Analytics Focus",
        "contact": {
            "email": "kan9336@nyu.edu",
            "phone": "(+1) 943 238-1803",
            "linkedin": "https://linkedin.com/in/nikhil-boddupalli-504257129/",  # replace if needed
        },

        # ==== EDUCATION ====
        "education": [
            {
                "school": "New York University",
                "location": "New York, NY",
                "degree": "M.S. in Computer Science — Specialization: Data Science & Analytics",
                "dates": "Aug 2024 – May 2026",
            },
            {
                "school": "National University of Singapore (NUS)",
                "location": "Singapore",
                "degree": "Exchange Student — Business Analytics",
                "dates": "Aug 2022 – May 2023",
            },
            {
                "school": "SRM Institute of Science & Technology",
                "location": "Chennai, India",
                "degree": "B.E. in Computer Science Engineering — GPA 9.4/10",
                "dates": "Aug 2020 – May 2024",
            },
        ],

        # ==== EXPERIENCE ====
        "experience": [
            {
                "company": "KPMG",
                "title": "Summer Associate",
                "location": "",
                "dates": "May 2025 – Aug 2025",
                "bullets": [
                    "Partnered with Lloyds Bank UK on analytics for EU FIDA compliance; built Python/SQL models for fraud/risk detection.",
                    "Automated validation processes (~40% review time reduction).",
                    "Prototyped GenAI ideas to streamline compliance reporting.",
                ],
            },
            {
                "company": "Walmart (via Sagarsoft)",
                "title": "Data/Analytics Intern",
                "location": "",
                "dates": "2023 – 2024",
                "bullets": [
                    "Built analytical pipelines & dashboards that improved visibility into key KPIs and anomaly trends.",
                    "Worked with large data extracts; helped connect anomalies to operational metrics and ratios.",
                ],
            },
            {
                "company": "Lupin Pharma",
                "title": "Analytics / Pharmacovigilance (project exposure)",
                "location": "",
                "dates": "2023",
                "bullets": [
                    "Contributed to analytics used in regulatory submission contexts.",
                    "Developed interpretable model outputs to aid compliance decisions; reached ~92% accuracy on test data.",
                ],
            },
        ],

        # ==== PROJECTS (from your resume) ====
        "projects": [
            {
                "name": "BiLSTM-GAN for Transaction Anomaly Detection",
                "dates": "Dec 2022 – Mar 2023",
                "bullets": [
                    "Architected a hybrid BiLSTM–GAN model for sequential financial transaction anomaly detection.",
                    "Improved detection accuracy by ~12% over baseline methods, enabling better fraud/risk pattern monitoring.",
                ],
            },
        ],

        # ==== SKILLS ====
        "skills": {
            "languages": "Python (Pandas, NumPy, Matplotlib, Scikit-learn, NLTK, BeautifulSoup, Selenium), SQL, R",
            "tools": "Power BI, Tableau, AWS Cloud Operations, Azure, Alteryx, (exposure) Gurobi, Gen AI, Microsoft Copilot, Microsoft Excel",
        },

        # ==== CERTIFICATIONS ====
        "certifications": [
            "AWS Academy Graduate — AWS Academy Cloud Operations",
            "Stanford — Introduction to Statistics",
            "Microsoft Power BI Data Analyst Professional Certificate",
        ],

        # ==== ACHIEVEMENTS ====
        "achievements": [
            "NYU Academic Scholarship — awarded for outstanding academic performance and potential.",
            "Presidential Honor — recognized by the President of India (Dept. of Science & Technology) for national-level scientific contribution.",
        ],
    }
    return render(request, "resume.html", {"data": data})
