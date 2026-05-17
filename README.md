# 📧 Automated HR Email Sender for Job Applications

**Author:** Charan Kandimalla  
**Email:** charan0912k@gmail.com  
**GitHub:** [Charan0196](https://github.com/Charan0196)  
**LinkedIn:** [charan-kandimalla](https://www.linkedin.com/in/charan-kandimalla-20a6923a6)

---

## 🎯 Overview

Automated email system to send personalized job applications to HR professionals at tech companies and startups. Built for fresh graduates seeking AI/ML and software engineering roles.

## ✨ Features

- ✅ **Personalized Emails** - Customized for each HR person and company
- ✅ **Resume Attachment** - Automatically attaches your resume
- ✅ **Duplicate Prevention** - Tracks sent emails to avoid duplicates
- ✅ **Gmail SMTP** - Uses Gmail's secure SMTP server
- ✅ **Rate Limiting** - 10-second delay between emails
- ✅ **Real HR Contacts** - Send to actual HR people, not generic emails

## 📋 Prerequisites

- Python 3.7+
- Gmail account with App Password enabled
- Your resume in PDF format

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/Charan0196/hr-email-automation.git
cd hr-email-automation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Email Settings

Edit `email_config.json`:

```json
{
  "email_settings": {
    "sender_email": "your-email@gmail.com",
    "sender_password": "your-app-password",
    "sender_name": "Your Name",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587
  },
  "resume_path": "/path/to/your/resume.pdf",
  "candidate_info": {
    "name": "Your Name",
    "email": "your-email@gmail.com",
    "phone": "+91 XXXXXXXXXX",
    "linkedin": "https://www.linkedin.com/in/your-profile",
    "github": "https://github.com/your-username",
    "university": "Your University",
    "degree": "Your Degree",
    "graduation_year": "2026"
  }
}
```

### 4. Add HR Contacts

Edit `real_hr_people.json` with real HR contacts:

```json
[
  {
    "name": "HR Person Name",
    "title": "Talent Acquisition Lead",
    "company": "Company Name",
    "email": "hr.person@company.com",
    "linkedin": "https://www.linkedin.com/in/hr-person",
    "source": "LinkedIn",
    "actively_hiring": true,
    "hiring_freshers": true
  }
]
```

### 5. Run Email Campaign

```bash
python send_to_real_hr.py
```

## 📁 Project Structure

```
hr-email-automation/
├── send_to_real_hr.py          # Main email sender script
├── email_config.json            # Email configuration
├── real_hr_people.json          # HR contacts database
├── sent_emails.json             # Tracking sent emails
├── requirements.txt             # Python dependencies
├── README.md                    # This file
└── your-resume.pdf              # Your resume
```

## 🔐 Gmail App Password Setup

1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Enable 2-Step Verification
3. Go to [App Passwords](https://myaccount.google.com/apppasswords)
4. Generate new app password for "Mail"
5. Copy the 16-character password
6. Use it in `email_config.json`

## 📧 Email Template

The script sends personalized emails with:
- Recipient's name and title
- Company-specific messaging
- Your skills and projects
- Contact information
- Resume attachment

## 🎓 Perfect For

- Recent graduates seeking tech jobs
- AI/ML engineering roles
- Software engineering positions
- Fresher-friendly companies
- Startup opportunities

## ⚠️ Important Notes

- **Rate Limiting:** 10-second delay between emails (recommended)
- **Daily Limit:** Gmail allows ~500 emails/day
- **Duplicate Prevention:** Automatically skips already-contacted HRs
- **Real Emails Only:** Use verified HR contacts, not generic careers@ emails

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

## 📝 License

MIT License - feel free to use and modify

## 👤 Author

**Charan Kandimalla**
- 🎓 B.Tech in Computer Science Engineering (AI & ML)
- 🏫 JNTUH University College of Engineering Wanaparthy
- 📧 charan0912k@gmail.com
- 💼 [LinkedIn](https://www.linkedin.com/in/charan-kandimalla-20a6923a6)
- 💻 [GitHub](https://github.com/Charan0196)

## 🙏 Acknowledgments

Built to help fresh graduates automate their job search and reach real HR professionals at tech companies.

---

**⭐ If this helped you, please star the repository!**
