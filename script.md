# CS50 Final Project Presentation Script - PingPost

## Video Duration: Under 3 minutes

---

## **Opening (0:00 - 0:20)**
*[Show PingPost homepage with posts]*

"Hi, I'm Ravi Ranjan. This is PingPost - my CS50 final project. It's a micro-blogging platform where users share short messages with optional photos, like Twitter but simpler and more visual."

*[Quick scroll through timeline]*

"Built with Django and Python, featuring a modern dark theme with responsive card-based design."

---

## **Live Demo (0:20 - 1:40)**

### **Core Features (0:20 - 1:00)**
*[Demo user registration/login]*

"Users register with secure authentication. Django handles password validation and CSRF protection."

*[Create a new post with photo]*

"Creating posts is simple - write up to 250 characters, optionally add a photo, and publish. The interface is clean and intuitive."

### **Post Management (1:00 - 1:25)**
*[Show edit/delete on own posts]*

"Users can only edit or delete their own posts - I implemented ownership validation. When updating photos, old files are automatically cleaned up to prevent storage bloat."

### **Responsive Design (1:25 - 1:40)**
*[Show mobile/desktop views]*

"Fully responsive using Bootstrap 5 and some CSS. Desktop shows a multi-column grid, mobile stacks vertically for optimal viewing."

---

## **Technical Implementation (1:40 - 2:30)**
*[Show code structure briefly]*

"The architecture follows Django's MVC pattern:
- **Model**: Single Tweet model with user foreign key, text field, image upload, and timestamps
- **Views**: Function-based views handling CRUD operations with proper authentication
- **Templates**: Bootstrap 5 with custom CSS for the dark theme"

*[Show models.py quickly]*

"Key technical challenges I solved: automatic file cleanup on post updates, secure user authentication, and responsive image handling. The database uses SQLite for development but scales easily to PostgreSQL."

---

## **Closing (2:30 - 2:50)**
*[Show final timeline]*

"PingPost demonstrates full-stack web development - from database design to user authentication to responsive frontend. It's a complete social media platform showcasing Django best practices, security implementation, and modern web design."

"Thanks for watching!"

---

## **Quick Reference:**
- **0:00-0:20**: Project intro + visual overview
- **0:20-1:40**: Live feature demonstration
- **1:40-2:30**: Technical architecture explanation
- **2:30-2:50**: Wrap-up and conclusion

## **Key Points to Hit:**
- Django framework mastery
- Security (authentication, CSRF, ownership validation)
- File management and cleanup
- Responsive design
- Database relationships
- Clean code architecture
