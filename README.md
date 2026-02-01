# TaskFight

TaskFight is a productivity application that combines a todo list, focus timer, and gamification elements to help users boost their productivity.

## Features

- **Todo List**: Create and manage tasks with name, priority, tag, and timer
- **Focus Timer**: Start, pause, stop, and complete timers for tasks
- **Gamification**: Track progress with HP bars showing task completion percentage
- **Statistics Dashboard**: Visualize time spent and completed tasks by tag and priority
- **Filtering**: Filter tasks by tag and view in-progress tasks

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- AsyncPG

### Frontend
- HTML/CSS
- TailwindCSS
- AlpineJS
- Vite

## Installation

### Docker Deployment (Recommended)

1. Make sure you have Docker and Docker Compose installed
2. From the project root directory, run:
```bash
docker-compose up -d
```
3. The application will be available at:
   - Backend API: http://localhost:8000
   - Frontend: http://localhost:5173
   - Database: localhost:5432 (for external connections)

To rebuild the containers:
```bash
docker-compose up -d --build
```

To stop and remove containers:
```bash
docker-compose down
```


### Manual Setup

#### Backend Setup

1. Install Python dependencies:
```bash
pip install -r server/requirements.txt
```

2. Set up your PostgreSQL database and update the connection string in `server/config.py`

3. Run the application:
```bash
cd server
uvicorn main:app --reload
```

#### Frontend Setup

1. Install Node.js dependencies:
```bash
cd client
npm install
```

2. Start the development server:
```bash
npm run dev
```

## Usage

1. Access the application at `http://localhost:5173` (Vite default port)
2. Create tasks with name, priority, tag, and timer duration
3. Start tasks to begin the focus timer
4. Use the timer screen to manage your focus session
5. View statistics on the dashboard page

## API Endpoints

### Tasks
- `GET /tasks` - Get all tasks
- `GET /tasks/{task_id}` - Get a specific task
- `POST /tasks` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task
- `POST /tasks/{task_id}/start-timer` - Start the timer for a task
- `POST /tasks/{task_id}/pause-timer` - Pause the timer for a task
- `POST /tasks/{task_id}/stop-timer` - Stop the timer for a task
- `POST /tasks/{task_id}/complete` - Complete a task

### Statistics
- `GET /statistics/time-by-tag` - Get time spent by tag
- `GET /statistics/completed-tasks-by-tag-priority` - Get completed tasks by tag and priority
- `GET /statistics/total-time-spent` - Get total time spent
- `GET /statistics/completed-tasks-count` - Get completed tasks count

## Project Structure

```
taskfight/
├── client/                 # Frontend files
│   ├── public/             # Public assets
│   │   ├── index.html      # Main application page
│   │   └── timer.html      # Timer screen
│   ├── src/
│   │   ├── style.css       # Tailwind CSS styles
│   │   └── main.js         # JavaScript modules
│   ├── package.json        # Frontend dependencies
│   └── tailwind.config.js  # Tailwind configuration
├── server/                 # Backend files
│   ├── api/                # API route definitions
│   ├── database/           # Database configuration
│   ├── models/             # Database models
│   ├── repositories/       # Database operations
│   ├── schemes/            # Pydantic schemas
│   ├── services/           # Business logic
│   ├── config.py           # Configuration settings
│   ├── main.py             # Application entry point
│   └── requirements.txt    # Python dependencies
├── todo.md                 # Development progress tracker
└── README.md               # This file
```

## Architecture

The application follows a clean architecture pattern with separation of concerns:

- **Models**: Define database entities using SQLAlchemy
- **Schemas**: Define API request/response models using Pydantic
- **Repositories**: Handle database operations
- **Services**: Implement business logic
- **API**: Define API routes and handle HTTP requests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.