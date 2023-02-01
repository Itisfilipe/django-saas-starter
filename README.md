## Django SaaS Starter Kit
### ⚠️ Work in Progres ⚠️
I am tired of having to write the same boilerplates when starting a new project. So I decided to create a starter kit for Django SaaS projects. This is a work in progress and I will be adding more features as I go along. If you have any suggestions, please feel free to open an issue or a pull request.

### Features
- [ ] Core Technologies
  - [x] Django with Tailwind CSS and Alpine.js
  - [x] Docker
  - [x] Database with PostgreSQL
  - [x] Dependencies management with Pipenv
  - [x] Celery with Celery Beat and Flower
  - [x] Redis for Celery and Cache
  - [ ] Sentry for error tracking
  - [x] Django Debug Toolbar for development
  - [ ] Django Storage for S3
  - [ ] Django Environ for environment variables
  - [x] Mailhog for email testing
- [ ] Authentication
  - [ ] Email/Username authentication
  - [ ] Social authentication
  - [ ] Two-factor authentication
  - [ ] Passwordless authentication
- [ ] Authorization
  - [ ] Role-based access control
  - [ ] Permission-based access control
- [ ] User management
  - [ ] User profile
  - [ ] User subscription and billing
  - [ ] User notifications
  - [ ] Organization/Teams management
  - [ ] User roles and permissions
- [ ] Misc
  - [ ] Feature flags
  - [ ] Integration with Oauth2 providers (Google, Microsoft, Zoom, etc.)

## Development

#### Servers
- Monitor celery with flower http://localhost:8888/
- Intercept e-mails with mailhog http://localhost:8025/
- Manage the database with PGAdmin http://localhost:5050/
  - You are going to need to create a new server with the following credentials:
    - Host: db
    - Port: 5432
    - Username: postgres
    - Password: postgres
    - Database: db_local
- Access the web app http://localhost:8000/
