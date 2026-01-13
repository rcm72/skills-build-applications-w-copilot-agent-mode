from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from djongo import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample users (superheroes)
        users = [
            {"name": "Clark Kent", "email": "superman@dc.com", "team": "DC"},
            {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "DC"},
            {"name": "Diana Prince", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Steve Rogers", "email": "captainamerica@marvel.com", "team": "Marvel"},
            {"name": "Peter Parker", "email": "spiderman@marvel.com", "team": "Marvel"},
        ]
        db.users.insert_many(users)

        # Teams
        teams = [
            {"name": "Marvel", "members": ["Tony Stark", "Steve Rogers", "Peter Parker"]},
            {"name": "DC", "members": ["Clark Kent", "Bruce Wayne", "Diana Prince"]},
        ]
        db.teams.insert_many(teams)

        # Activities
        activities = [
            {"user": "Clark Kent", "activity": "Flight", "duration": 60},
            {"user": "Bruce Wayne", "activity": "Martial Arts", "duration": 45},
            {"user": "Diana Prince", "activity": "Strength Training", "duration": 50},
            {"user": "Tony Stark", "activity": "Engineering", "duration": 40},
            {"user": "Steve Rogers", "activity": "Running", "duration": 30},
            {"user": "Peter Parker", "activity": "Wall Climbing", "duration": 35},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"user": "Clark Kent", "points": 100},
            {"user": "Tony Stark", "points": 95},
            {"user": "Diana Prince", "points": 90},
            {"user": "Steve Rogers", "points": 85},
            {"user": "Bruce Wayne", "points": 80},
            {"user": "Peter Parker", "points": 75},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"name": "Super Strength", "description": "Heavy lifting and resistance training."},
            {"name": "Agility Training", "description": "Speed and flexibility drills."},
            {"name": "Endurance Run", "description": "Long-distance running."},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
