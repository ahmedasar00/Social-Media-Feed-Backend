# Social Media Feed Backend - ProDev BE

## Real-World Application

This project prepares backend engineers for building scalable and interactive systems like social media platforms. Key takeaways include:

- Using GraphQL for flexible data fetching
- Designing schemas for high-traffic applications
- Managing complex user interactions efficiently

---

## Overview

This case study involves developing a backend to manage posts and user interactions for a social media feed. The project emphasizes GraphQL API development, real-time interactions, and scalable backend solutions.

---

## Project Goals

- **Post Management**: Design APIs for creating, fetching, and managing posts
- **Flexible Querying**: Implement GraphQL for advanced querying capabilities
- **Scalability**: Optimize database schema for high-volume user interactions

---

## Technologies Used

| Technology             | Purpose                              |
| ---------------------- | ------------------------------------ |
| **Django**             | For backend development              |
| **PostgreSQL**         | To store relational data efficiently |
| **GraphQL (Graphene)** | For flexible data queries            |
| **GraphQL Playground** | For testing APIs                     |

---

## Key Features

### 1. GraphQL APIs

- Enable flexible querying of posts and interactions
- Provide resolvers for creating, fetching, and managing posts and interactions

### 2. Interaction Management

- Allow users to like, comment, and share posts
- Track interactions for analytics and feedback

### 3. API Testing

- Publish a hosted GraphQL Playground for easy testing

---

## Implementation Process

### Git Commit Workflow

The project follows a structured development approach with clear commit messages:

- `feat: set up Django project with PostgreSQL`
- `feat: create models for posts, comments, and interactions`
- `feat: implement GraphQL API for querying posts and interactions`
- `feat: integrate and publish GraphQL Playground`
- `perf: optimize database queries for interactions`
- `docs: update README with API usage`

---

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip and virtualenv

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd social-media-feed-backend2
   ```

2. **Create and activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   ```bash
   # Copy .env.example to .env and configure your database settings
   cp .env.example .env
   ```

5. **Set up the database**

   ```bash
   # Create PostgreSQL database
   createdb social_media_db

   # Run migrations
   python manage.py migrate

   # Create superuser (optional)
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

### Access Points

| Service                | URL                           | Description                  |
| ---------------------- | ----------------------------- | ---------------------------- |
| **GraphQL Playground** | http://localhost:8000/graphql | Interactive API explorer     |
| **GraphQL Endpoint**   | http://localhost:8000/graphql | API endpoint for client apps |
| **Admin Panel**        | http://localhost:8000/admin   | Django admin interface       |

---

## Submission Details

### API Deployment

- Host API with GraphQL Playground for testing
- Ensure GraphQL Playground is publicly accessible for evaluation
- Provide deployment URL and credentials (if required)

---

## Evaluation Criteria

### 1. Functionality

- ✅ Fully functional GraphQL APIs for posts and interactions
- ✅ High-performing queries for large datasets

### 2. Code Quality

- ✅ Clean and modular code
- ✅ Efficient database schema design

### 3. User Experience

- ✅ GraphQL Playground is intuitive and easy to use

### 4. Version Control

- ✅ Frequent and clear commits
- ✅ Organized project repository

---

## Project Structure

```
social-media-feed-backend2/
│
├── docs/                                    # 📚 Comprehensive documentation
│   ├── 00_PROJECT_OVERVIEW.md
│   ├── 01_REQUIREMENTS.md
│   ├── 02_ARCHITECTURE.md
│   ├── 03_DEPLOYMENTS.md
│   ├── 04_UNIT_TEST.md
│   └── database/
│       ├── 01_ER_DIAGRAM.md
│       ├── 02_SCHEMA.md
│       ├── 03_INDEXING_STRATEGY.md
│       └── 04_SEEDING_AND_MIGRATIONS.md
│
├── social_media_feed_backend/               # 🐍 Django project configuration
│   ├── settings.py                         # Environment-based settings
│   ├── urls.py                             # URL routing
│   └── wsgi.py                             # WSGI config for production
│
├── social_media_feed_app/                   # 📦 Main application logic
│   ├── models.py                           # Database models
│   ├── schema/                             # GraphQL implementation
│   │   ├── queries.py                      # GraphQL queries
│   │   ├── mutations.py                    # GraphQL mutations
│   │   └── types.py                        # GraphQL types
│   └── migrations/                         # Database migrations
│
├── requirements.txt                         # Python dependencies
├── manage.py                               # Django management
└── README.md                               # This file
```

---

## Testing

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test social_media_feed_app

# Run with verbose output
python manage.py test --verbosity=2
```

For detailed testing documentation, see [docs/04_UNIT_TEST.md](docs/04_UNIT_TEST.md).

---

## Development Workflow

### Database Migrations

```bash
# Create migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Seeding Sample Data

```bash
# Seed database with sample data (if command available)
python manage.py seed
```

---

## Documentation

Comprehensive documentation is available in the `docs/` directory:

- **[Project Overview](docs/00_PROJECT_OVERVIEW.md)** - Project introduction and overview
- **[Requirements](docs/01_REQUIREMENTS.md)** - Detailed requirements and specifications
- **[Architecture](docs/02_ARCHITECTURE.md)** - System architecture and design
- **[Deployments](docs/03_DEPLOYMENTS.md)** - Deployment guides and configurations
- **[Unit Testing](docs/04_UNIT_TEST.md)** - Testing documentation and guidelines
- **[Database Documentation](docs/database/)** - Database schema, ER diagrams, and indexing strategies

---

## Learning Outcomes

By completing this project, you will gain hands-on experience with:

1. **GraphQL API Design**: Creating flexible and efficient GraphQL schemas
2. **Database Optimization**: Designing schemas for high-traffic applications
3. **Django Best Practices**: Structuring Django projects for scalability
4. **API Testing**: Using GraphQL Playground for interactive API testing
5. **Real-world Backend Development**: Managing complex user interactions and data relationships

---

## License

This project is part of a professional development curriculum and is intended for educational purposes.

---

## Contact & Support

For questions or support regarding this project, please refer to the documentation in the `docs/` directory or contact your course instructor.
