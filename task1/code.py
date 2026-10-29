def evaluate_and_allocate(applicants, available_slots):
  eligible = []
  for app in applicants:
    if (
        app['aggregate'] >= 75
        and app['attendance'] >= 85
        and app['income'] <= 50000
        and all(m >= 60 for m in app['subjects'])
    ):
      score = (app['aggregate'] * 0.6) + (app['attendance'] * 0.4)
      app['score'] = score
      eligible.append(app)

  eligible.sort(
      key=lambda x: (x['score'], x['aggregate'], x['attendance'], -x['income']),
      reverse=True,
  )

  allocated = eligible[:available_slots]
  return allocated


applicants_data = [
    {
        'id': 1,
        'name': 'Alice',
        'aggregate': 88,
        'subjects': [70, 85, 90],
        'attendance': 90,
        'income': 40000,
    },
    {
        'id': 2,
        'name': 'Bob',
        'aggregate': 92,
        'subjects': [80, 85, 95],
        'attendance': 95,
        'income': 45000,
    },
    {
        'id': 3,
        'name': 'Charlie',
        'aggregate': 88,
        'subjects': [75, 80, 85],
        'attendance': 92,
        'income': 35000,
    },
    {
        'id': 4,
        'name': 'Diana',
        'aggregate': 70,
        'subjects': [65, 70, 60],
        'attendance': 80,
        'income': 30000,
    },
]

result = evaluate_and_allocate(applicants_data, 2)
for r in result:
  print(f"ID: {r['id']}, Name: {r['name']}, Score: {r['score']:.2f}")
