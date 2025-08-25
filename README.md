# 🎾 My Tennis Club - Django Web Application

A modern, responsive web application built with Django for managing tennis club memberships. This project features a clean Bootstrap-powered interface that allows visitors to register as club members and view the tennis community.

## ✨ Features

### 🏠 **Public Features**
- **Modern Homepage** - Welcoming landing page with tennis club information
- **Member Registration** - Self-service signup form for new members
- **Member Directory** - Browse all current club members
- **Member Profiles** - Detailed view of individual member information
- **Responsive Design** - Mobile-friendly interface that works on all devices

### ⚙️ **Admin Features**
- **Django Admin Panel** - Full administrative control
- **Member Management** - Add, edit, and delete member records
- **Search & Filter** - Find members by name, phone, or join date
- **User-Friendly Display** - Members shown by name instead of object IDs

### 🎨 **Design & UI**
- **Bootstrap 5 Integration** - Professional, modern styling
- **Tennis Theme** - Green color scheme with tennis-related icons
- **Responsive Navigation** - Mobile-friendly collapsible menu
- **Card-Based Layout** - Clean, organized presentation of information

## 🛠️ Tech Stack

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, Bootstrap 5, Bootstrap Icons
- **Database**: SQLite (default Django database)
- **Python**: 3.12+

## 📁 Project Structure

```
my_tennis_club/
├── my_tennis_club/           # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── members/                  # Main app
│   ├── models.py            # Member data model
│   ├── views.py             # Application logic
│   ├── urls.py              # URL routing
│   ├── forms.py             # Registration form
│   ├── admin.py             # Admin configuration
│   └── templates/           # HTML templates
│       ├── master.html      # Base template
│       ├── main.html        # Homepage
│       ├── all_members.html # Member listing
│       ├── details.html     # Member profile
│       ├── register.html    # Registration form
│       └── registration_success.html
├── manage.py                # Django management script
└── db.sqlite3              # Database file
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.12 or higher
- pip (Python package manager)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd DjangoPlay
```

### 2. Create Virtual Environment
```bash
python -m venv myworld
source myworld/bin/activate  # On macOS/Linux
# or
myworld\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Navigate to Project Directory
```bash
cd my_tennis_club
```

### 5. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## 📱 Application URLs

| URL | Description |
|-----|-------------|
| `/` | Homepage with club information |
| `/members/` | List of all tennis club members |
| `/members/details/<id>` | Individual member profile page |
| `/register/` | Member registration form |
| `/registration-success/` | Registration confirmation page |
| `/admin/` | Django administration panel |

## 🎯 How to Use

### For New Members:
1. Visit the homepage at http://127.0.0.1:8000/
2. Click "Join Our Club Today!"
3. Fill out the registration form with your information
4. Submit and receive confirmation
5. Your profile will immediately appear in the member directory

### For Club Administrators:
1. Access the admin panel at http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Manage members through the intuitive interface
4. Search, filter, and organize member data
5. Add members manually if needed

## 🔧 Database Model

### Member Model
```python
class Member(models.Model):
    first_name = CharField(max_length=255)      # Required
    last_name = CharField(max_length=255)       # Required  
    phone = CharField(max_length=15)            # Optional
    joined_date = DateField()                   # Optional
```

## 🎨 Customization

The application uses a tennis-themed design with:
- **Primary Color**: Green (#28a745) - representing tennis courts
- **Bootstrap Icons**: Tennis, trophy, and user-related icons
- **Responsive Grid**: Mobile-first design approach
- **Professional Cards**: Clean, modern presentation

## 🚧 Future Enhancements

Potential features for expansion:
- **Court Booking System** - Reserve tennis courts online
- **Tournament Management** - Organize and track competitions  
- **Payment Integration** - Handle membership fees
- **Email Notifications** - Welcome emails and updates
- **Member Photos** - Profile picture uploads
- **Skill Level Tracking** - Beginner, Intermediate, Advanced
- **Match History** - Record game results

## 🐛 Troubleshooting

### Common Issues:

**Server won't start:**
- Ensure you're in the virtual environment (`source myworld/bin/activate`)
- Check that Django is installed (`pip install django`)
- Verify you're in the correct directory (`my_tennis_club/`)

**Admin login issues:**
- Create a superuser account (`python manage.py createsuperuser`)
- Check credentials and try again

**Template not found:**
- Ensure all template files exist in `members/templates/`
- Check template inheritance is correct

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a Django learning project for tennis club management.

---

🎾 **Ready to serve up some great tennis club management!** 🎾
