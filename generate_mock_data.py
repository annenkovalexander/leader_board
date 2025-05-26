import random
from faker import Faker
from results.models import Result

fake = Faker()

competitions = ['SpringCup2025', 'AutumnChallenge', 'WinterBlast', 'SummerShowdown']
scenarios = ['scenarioA', 'scenarioB', 'scenarioC']
commands = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo']

def generate_mock_results(n=100):
    for _ in range(n):
        competition = random.choice(competitions)
        room_id = fake.bothify(text='Room-###')
        command_name = random.choice(commands)
        user_name = fake.user_name()
        scenario = random.choice(scenarios)
        flight_time = round(random.uniform(10.0, 300.0), 2)
        false_start = random.choices([False, True], weights=[0.9, 0.1])[0]

        Result.objects.get_or_create(
            competition=competition,
            room_id=room_id,
            command_name=command_name,
            user_name=user_name,
            scenario=scenario,
            defaults={
                'flight_time': flight_time,
                'false_start': false_start,
            }
        )

    print(f"Created {n} mock Result records.")

# generate_mock_results(100)
