from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Drop collections directly using Djongo's connection
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        for collection in ['activity', 'user', 'workout', 'leaderboard', 'team']:
            db[collection].drop()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', universe='Marvel')
        dc = Team.objects.create(name='DC', universe='DC')

        # Create Users (Superheroes)
        tony = User.objects.create(email='tony@stark.com', username='IronMan', team=marvel)
        steve = User.objects.create(email='steve@rogers.com', username='CaptainAmerica', team=marvel)
        bruce = User.objects.create(email='bruce@wayne.com', username='Batman', team=dc)
        clark = User.objects.create(email='clark@kent.com', username='Superman', team=dc)

        # Create Workouts
        strength = Workout.objects.create(name='Super Strength', description='Heavy lifting and power moves')
        agility = Workout.objects.create(name='Agility Training', description='Speed and flexibility drills')
        strength.suggested_for.add(marvel, dc)
        agility.suggested_for.add(marvel, dc)

        # Create Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='Martial Arts', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, type='Flying', duration=120, date=timezone.now().date())

        # Create Leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=200)

        self.stdout.write(self.style.SUCCESS('Test data successfully populated in octofit_db!'))
