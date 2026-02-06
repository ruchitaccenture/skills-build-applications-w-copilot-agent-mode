from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', universe='Marvel')
        self.user = User.objects.create(email='tony@stark.com', username='IronMan', team=self.team)
        self.workout = Workout.objects.create(name='Super Strength', description='Heavy lifting')
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2024-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Marvel')

    def test_user_str(self):
        self.assertEqual(str(self.user), 'IronMan')

    def test_activity_str(self):
        self.assertIn('IronMan', str(self.activity))

    def test_workout_str(self):
        self.assertEqual(str(self.workout), 'Super Strength')

    def test_leaderboard_str(self):
        self.assertIn('Marvel', str(self.leaderboard))
