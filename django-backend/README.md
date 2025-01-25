#References


# Awareness Sessions Management System

This project is a Django-based application designed to manage awareness sessions, track attendance, manage digital resources, handle interactive assignments, implement gamification, and provide notifications and reports. The application aims to enhance student engagement and facilitate effective learning experiences.

## Features

1. **Session Scheduling**
   - Admin can create awareness sessions with details like title, description, date, time, venue, and resources.
   - Sessions can be categorized for better organization.
   - Unique session codes are generated for student access.

2. **Attendance Tracking**
   - QR codes are generated for each session to mark attendance.
   - Real-time validation ensures only registered students can mark attendance.
   - Attendance data can be exported as CSV or PDF.

3. **Digital Resource Management**
   - Admin can upload session materials and assign them to specific sessions.
   - Students can access downloadable resources via the mobile app.

4. **Interactive Assignments**
   - Admin can create assignments linked to sessions with various submission types.
   - Students can submit assignments and receive feedback.

5. **Gamification**
   - Points and badges are awarded for participation and achievements.
   - A leaderboard displays top-performing students.

6. **Push Notifications**
   - Students receive notifications about new sessions, resource uploads, and assignment deadlines.
   - Scheduled reminders are implemented for important updates.

7. **Multi-Language Support**
   - Users can select their preferred language.
   - Admin can upload resources in multiple languages.

8. **Reports and Analytics**
   - Admin dashboard provides insights into attendance trends and student engagement.
   - Reports can be exported for further analysis.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-backend
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```
   python manage.py migrate
   ```

4. Create a superuser for the admin panel:
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin` to manage sessions, attendance, resources, assignments, and notifications.
- Use the mobile app to browse sessions, submit assignments, and track progress.

## Future Enhancements

- AI-powered personalized session recommendations.
- Integration with video conferencing tools for remote sessions.
- Offline functionality for resource access.