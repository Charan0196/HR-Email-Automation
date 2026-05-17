"""
HR Email Automation - Clean Version for GitHub
Author: Charan Kandimalla
Email: charan0912k@gmail.com
GitHub: https://github.com/Charan0196
LinkedIn: https://www.linkedin.com/in/charan-kandimalla-20a6923a6

Send personalized job application emails to HR professionals
"""

import json
import logging
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class HREmailSender:
    """
    Automated email sender for job applications
    
    Author: Charan Kandimalla
    Email: charan0912k@gmail.com
    GitHub: https://github.com/Charan0196
    LinkedIn: https://www.linkedin.com/in/charan-kandimalla-20a6923a6
    """
    
    def __init__(self, config_file='email_config.json'):
        """Initialize email sender with configuration"""
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        
        self.email_settings = self.config['email_settings']
        self.candidate_info = self.config['candidate_info']
        self.resume_path = self.config['resume_path']
        self.sent_emails = self.load_sent_emails()
    
    def load_sent_emails(self):
        """Load already sent emails to prevent duplicates"""
        try:
            with open('sent_emails.json', 'r') as f:
                data = json.load(f)
                return set(data.get('sent_to', []))
        except FileNotFoundError:
            return set()
    
    def save_sent_email(self, email):
        """Track sent email"""
        self.sent_emails.add(email)
        with open('sent_emails.json', 'w') as f:
            json.dump({
                'sent_to': list(self.sent_emails),
                'last_updated': datetime.now().isoformat()
            }, f, indent=2)
    
    def generate_email_body(self, hr_name, hr_title, company_name):
        """
        Generate personalized email for HR person
        
        Customize this template with your own:
        - Skills and experience
        - Projects and achievements
        - Education background
        - Career goals
        """
        info = self.candidate_info
        first_name = hr_name.split()[0]
        
        email_body = f"""Dear {first_name},

I hope this email finds you well. I came across your profile as the {hr_title} at {company_name}, and I wanted to reach out regarding opportunities for freshers in AI/ML and software engineering.

I am {info['name']}, a recent graduate with a {info['degree']} from {info['university']} (Class of {info['graduation_year']}). I am actively seeking entry-level opportunities where I can apply my skills in artificial intelligence, machine learning, and software development.

**Why I'm Reaching Out:**

I'm particularly interested in {company_name} because of its reputation for innovation and excellence in technology. As a recent graduate, I believe my combination of technical skills and fresh perspective would be a great fit for your team.

**What I Bring:**

🎯 **Technical Skills:**
• Programming: Python, Java, JavaScript, C++
• AI/ML: TensorFlow, PyTorch, Scikit-learn
• Web Development: React, Node.js, REST APIs
• Tools: Git, Linux, Docker, VS Code

🚀 **Key Projects:**
• [Describe your main project]
• [Describe another project]
• [Describe third project]

🌟 **What Makes Me Stand Out:**
• Strong problem-solving and analytical skills
• Quick learner with passion for new technologies
• Team player with excellent communication
• Eager to contribute and grow with {company_name}

I have attached my resume for your review. I would be grateful for the opportunity to discuss how my skills can contribute to {company_name}'s team.

**Contact Information:**
• Email: {info['email']}
• Phone: {info['phone']}
• LinkedIn: {info['linkedin']}
• GitHub: {info['github']}

Thank you for taking the time to read my email, {first_name}. I look forward to the possibility of starting my career with {company_name}.

Best regards,
{info['name']}
Recent Graduate - {info['degree']}
{info['university']} - Class of {info['graduation_year']}
{info['phone']} | {info['email']}

---
GitHub: https://github.com/Charan0196
LinkedIn: https://www.linkedin.com/in/charan-kandimalla-20a6923a6
"""
        
        return email_body
    
    def send_email(self, hr_contact):
        """Send email to HR person"""
        email = hr_contact['email']
        
        # Skip if already sent
        if email in self.sent_emails:
            logger.info(f"Already sent to {hr_contact['name']}, skipping...")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = f"{self.email_settings['sender_name']} <{self.email_settings['sender_email']}>"
            msg['To'] = email
            msg['Subject'] = f"Application for Software Engineer Position - {self.candidate_info['name']}"
            
            # Generate personalized body
            body = self.generate_email_body(
                hr_contact['name'],
                hr_contact['title'],
                hr_contact['company']
            )
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach resume
            if os.path.exists(self.resume_path):
                with open(self.resume_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                
                encoders.encode_base64(part)
                filename = os.path.basename(self.resume_path)
                part.add_header('Content-Disposition', f'attachment; filename= {filename}')
                msg.attach(part)
            
            # Send email
            server = smtplib.SMTP(self.email_settings['smtp_server'], self.email_settings['smtp_port'])
            server.starttls()
            server.login(self.email_settings['sender_email'], self.email_settings['sender_password'])
            
            text = msg.as_string()
            server.sendmail(self.email_settings['sender_email'], email, text)
            server.quit()
            
            # Track sent email
            self.save_sent_email(email)
            
            logger.info(f"✅ Email sent to {hr_contact['name']} ({hr_contact['company']})")
            return True
        
        except Exception as e:
            logger.error(f"❌ Failed to send to {hr_contact['name']}: {e}")
            return False
    
    def send_bulk(self, hr_contacts, delay=10):
        """Send emails to multiple HR people with rate limiting"""
        stats = {'total': len(hr_contacts), 'sent': 0, 'failed': 0, 'skipped': 0}
        
        logger.info("=" * 60)
        logger.info(f"Starting email campaign")
        logger.info(f"Total contacts: {stats['total']}")
        logger.info("=" * 60)
        
        for i, contact in enumerate(hr_contacts, 1):
            logger.info(f"\n[{i}/{len(hr_contacts)}] Sending to {contact['name']} at {contact['company']}...")
            
            if contact['email'] in self.sent_emails:
                stats['skipped'] += 1
                continue
            
            success = self.send_email(contact)
            
            if success:
                stats['sent'] += 1
            else:
                stats['failed'] += 1
            
            # Rate limiting
            if i < len(hr_contacts):
                logger.info(f"Waiting {delay} seconds...")
                time.sleep(delay)
        
        # Summary
        logger.info("\n" + "=" * 60)
        logger.info("CAMPAIGN SUMMARY")
        logger.info("=" * 60)
        logger.info(f"Total: {stats['total']}")
        logger.info(f"Sent: {stats['sent']}")
        logger.info(f"Failed: {stats['failed']}")
        logger.info(f"Skipped: {stats['skipped']}")
        logger.info("=" * 60)
        
        return stats


def load_hr_contacts(filename='real_hr_people.json'):
    """Load HR contacts from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"{filename} not found!")
        return []


def main():
    """
    Main function to run email campaign
    
    Author: Charan Kandimalla
    Email: charan0912k@gmail.com
    GitHub: https://github.com/Charan0196
    LinkedIn: https://www.linkedin.com/in/charan-kandimalla-20a6923a6
    """
    print("\n" + "=" * 70)
    print("HR EMAIL AUTOMATION")
    print("Author: Charan Kandimalla")
    print("GitHub: https://github.com/Charan0196")
    print("=" * 70)
    
    # Load HR contacts
    hr_contacts = load_hr_contacts()
    
    if not hr_contacts:
        print("\n❌ No HR contacts found!")
        print("Add contacts to real_hr_people.json")
        return
    
    print(f"\n✅ Loaded {len(hr_contacts)} HR contacts")
    
    # Initialize sender
    sender = HREmailSender()
    
    # Check how many already sent
    already_sent = sum(1 for c in hr_contacts if c['email'] in sender.sent_emails)
    new_contacts = [c for c in hr_contacts if c['email'] not in sender.sent_emails]
    
    print(f"\n📊 STATISTICS:")
    print(f"   Total HR contacts: {len(hr_contacts)}")
    print(f"   Already sent: {already_sent}")
    print(f"   NEW to send: {len(new_contacts)}")
    print("=" * 70)
    
    if not new_contacts:
        print("\n✅ All HR people already contacted!")
        return
    
    # Show sample
    print(f"\n📧 Sample contacts:")
    for i, contact in enumerate(new_contacts[:5], 1):
        print(f"{i}. {contact['name']:30} | {contact['company']}")
    
    if len(new_contacts) > 5:
        print(f"... and {len(new_contacts) - 5} more")
    
    # Confirm
    choice = input(f"\nSend to {len(new_contacts)} NEW contacts? (yes/no): ")
    
    if choice.lower() == 'yes':
        print("\n🚀 Starting campaign...")
        stats = sender.send_bulk(new_contacts)
        print(f"\n✅ Campaign complete!")
        print(f"   Sent: {stats['sent']}")
        print(f"   Failed: {stats['failed']}")
    else:
        print("❌ Cancelled")


if __name__ == "__main__":
    main()
